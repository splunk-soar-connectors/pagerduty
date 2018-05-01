# --
# File: pagerduty_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2016-2018
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

# Phantom App imports
import phantom.app as phantom

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# Imports local to this App
from pagerduty_consts import *

import json
import requests
from bs4 import BeautifulSoup


class RetVal4(tuple):
    def __new__(cls, val1, val2, val3, val4):
        return tuple.__new__(RetVal4, (val1, val2, val3, val4))


class RetVal2(tuple):
    def __new__(cls, val1, val2):
        return tuple.__new__(RetVal2, (val1, val2))


# Define the App Class
class PagerDutyConnector(BaseConnector):

    ACTION_ID_LIST_USERS = "list_users"
    ACTION_ID_LIST_TEAMS = "list_teams"
    ACTION_ID_GET_ONCALL = "get_pd_oncall"
    ACTION_ID_LIST_ONCALLS = "list_oncalls"
    ACTION_ID_LIST_SERVICES = "list_services"
    ACTION_ID_CREATE_INCIDENT = "create_incident"
    ACTION_ID_LIST_ESCALATIONS = "list_escalations"

    def __init__(self):

        # Call the BaseConnectors init first
        super(PagerDutyConnector, self).__init__()

        self._headers = None

    def initialize(self):

        config = self.get_config()

        api_key = config[PAGERDUTY_API_KEY]

        self._headers = {
            'Authorization': 'Token token={0}'.format(api_key),
            'Content-Type': 'application/json'}

        self._rest_url = "{0}{1}".format(config[PAGERDUTY_JSON_BASEURL].rstrip('/'), PAGERDUTY_API_URI)

        return phantom.APP_SUCCESS

    def _normalize_text(self, text):
        return text.replace('}', '}}').replace('{', '{{')

    def _parse_response(self, result, r):

        content_type = r.headers.get('content-type')

        resp_type = content_type

        status_code = r.status_code

        resp_data = None

        # It's ok if r.text is None, dump that, if the result object supports recording it
        if hasattr(result, 'add_debug_data'):
            result.add_debug_data({'r_text': r.text if r else 'r is None'})

        if 'json' in content_type:
            # Try a json parse
            try:
                resp_data = r.json()
            except:
                result.set_status(phantom.APP_ERROR, "Unable to parse response as a JSON status_code: {0}, data: {1}".format(r.status_code, self._normalize_text(r.text)))
        elif 'html' in content_type:
            try:
                soup = BeautifulSoup(r.text, "html.parser")
                resp_data = soup.text
            except Exception as e:
                self.debug_print("Handled exception", e)
                result.set_status(phantom.APP_ERROR, "Unable to parse response as a HTML status_code: {0}, data: {1}".format(r.status_code, self._normalize_text(r.text)))
        else:
            resp_data = r.text

        # Look for errors
        if 'json' in content_type:
            error = resp_data.get('error')
            if (error):
                error_message = "message: {0}, code: {1}, details: {2}".format(
                        error.get('message', 'None'),
                        error.get('code', 'None'),
                        '\n'.join(error.get('errors', [])))
                return RetVal4(result.set_status(phantom.APP_ERROR, "Error detected, status_code: {0}, data: {1}".format(r.status_code, error_message)), None, None, None)

        if not ( 200 <= r.status_code < 300):
            return RetVal4(result.set_status(phantom.APP_ERROR, "Call returned error, status_code: {0}, data: {1}"
                    .format(r.status_code, self._normalize_text(r.text))), None, None, None)

        return RetVal4(phantom.APP_SUCCESS, status_code, resp_type, resp_data)

    def _make_rest_call(self, endpoint, result, params={}, headers={}, data=None, method="get"):

        url = "{0}{1}".format(self._rest_url, endpoint)

        headers.update(self._headers)

        request_func = getattr(requests, method)

        if not request_func:
            return RetVal2(result.set_status(phantom.APP_ERROR, "Invalid method call: {0} for requests module".format(method)), None)

        if data is not None:
            data = json.dumps(data)

        try:
            r = request_func(url, headers=headers, params=params, data=data)
        except Exception as e:
            return RetVal2(result.set_status(phantom.APP_ERROR, "REST Api to server failed", e), None)

        ret_val, status_code, resp_type, resp_data = self._parse_response(result, r)

        # Any http or parsing error is handled by the _parse_response function
        if phantom.is_fail(ret_val):
            return RetVal2(result.get_status(), resp_data)

        return RetVal2(phantom.APP_SUCCESS, resp_data)

    def _test_connectivity(self, param):

        self.save_progress('Querying a single incident, to verify API key')

        params = { "limit": 1 }
        ret_val, resp_data = self._make_rest_call('/incidents', self, params)

        if phantom.is_fail(ret_val):
            self.append_to_message('Test connectivity failed')
            return self.get_status()

        return self.set_status_save_progress(phantom.APP_SUCCESS, "Test connectivity passed")

    def _handle_get_oncall(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        params = { "query": param['team'] }
        ret_val, resp_data = self._make_rest_call('/escalation_policies/on_call', action_result, params)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        policies = resp_data.get('escalation_policies')

        if not policies:
            return action_result.set_status(phantom.APP_ERROR, 'No Escalation policies configured')

        wanted_keys = ['id', 'name', 'on_call']

        policies = [{k: x[k] for k in wanted_keys} for x in policies]

        for policy in policies:
            action_result.add_data(policy)

        action_result.update_summary({'total_policies': len(policies)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_oncalls(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val, resp_data = self._make_rest_call('/oncalls', action_result)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        oncalls = resp_data.get('oncalls')

        for oncall in oncalls:
            action_result.add_data(oncall)

        action_result.update_summary({'num_oncalls': len(oncalls)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_teams(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val, resp_data = self._make_rest_call('/teams', action_result)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        teams = resp_data.get('teams')

        if not teams:
            return action_result.set_status(phantom.APP_ERROR, 'No teams configured')

        for team in teams:
            action_result.add_data(team)

        action_result.update_summary({'total_teams': len(teams)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_services(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        params = {}

        if 'team_ids' in param:
            params['team_ids[]'] = param['team_ids']

        ret_val, resp_data = self._make_rest_call('/services', action_result, params=params)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        services = resp_data.get('services', [])

        for service in services:
            action_result.add_data(service)

        action_result.update_summary({'num_services': len(services)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_users(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        params = {}

        if 'team_ids' in param:
            params['team_ids[]'] = param['team_ids']

        ret_val, resp_data = self._make_rest_call('/users', action_result, params=params)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        users = resp_data.get('users', [])

        for user in users:
            action_result.add_data(user)

        action_result.update_summary({'num_users': len(users)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_escalations(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        params = {}

        if 'user_ids' in param:
            params['user_ids[]'] = param['user_ids']
        if 'team_ids' in param:
            params['team_ids[]'] = param['team_ids']

        ret_val, resp_data = self._make_rest_call('/escalation_policies', action_result, params=params)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        esc_pols = resp_data.get('escalation_policies', [])

        for esc_pol in esc_pols:
            action_result.add_data(esc_pol)

        action_result.update_summary({'num_policies': len(esc_pols)})

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_incident(self, param):

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        body = {
                    "incident": {
                        "type": "incident",
                        "title": param["title"],
                        "service": {
                            "id": param["service_id"],
                            "type": "service"
                        },
                        "body": {
                            "type": "incident_body",
                            "details": param["description"]
                        }
                    }
               }

        if 'escalation_id' in param:
            body["escalation_policy"] = {"id": param["escalation_id"], "type": "escalation_policy"}
        elif 'assignee_id' in param:
            body["assignments"] = [{"assignee": {"id": "assignee_id", "type": "user"}}]

        ret_val, resp_data = self._make_rest_call('/incidents', action_result, data=body, method='post')

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        action_result.update_summary({'incident_key': resp_data.get('incident', {}).get('incident_key', "Unknown")})

        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == self.ACTION_ID_GET_ONCALL:
            ret_val = self._handle_get_oncall(param)
        elif action_id == self.ACTION_ID_LIST_TEAMS:
            ret_val = self._handle_list_teams(param)
        elif action_id == self.ACTION_ID_LIST_USERS:
            ret_val = self._handle_list_users(param)
        elif action_id == self.ACTION_ID_LIST_ONCALLS:
            ret_val = self._handle_list_oncalls(param)
        elif action_id == self.ACTION_ID_LIST_SERVICES:
            ret_val = self._handle_list_services(param)
        elif action_id == self.ACTION_ID_CREATE_INCIDENT:
            ret_val = self._handle_create_incident(param)
        elif action_id == self.ACTION_ID_LIST_ESCALATIONS:
            ret_val = self._handle_list_escalations(param)
        elif action_id == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY:
            ret_val = self._test_connectivity(param)

        return ret_val


if __name__ == '__main__':

    import sys
    import pudb
    pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = PagerDutyConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
