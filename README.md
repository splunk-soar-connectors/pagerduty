[comment]: # "Auto-generated SOAR connector documentation"
# PagerDuty

Publisher: Splunk  
Connector Version: 2\.0\.3  
Product Vendor: PagerDuty  
Product Name: PagerDuty  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with PagerDuty to implement investigative and ticketing actions

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2016-2020 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
This app will only work with API v2 on PagerDuty. It will not function with API v1.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a PagerDuty asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | PagerDuty base url e\.g\. https\://api\.pagerduty\.com/
**api\_token** |  required  | password | API Key

### Supported Actions  
[test connectivity](#action-test-connectivity) - Test connection to PagerDuty to validate supplied API key  
[list teams](#action-list-teams) - Get list of teams configured on PagerDuty  
[list oncalls](#action-list-oncalls) - Get list of oncalls on PagerDuty  
[list services](#action-list-services) - Get list of available services on PagerDuty  
[list users](#action-list-users) - Get list of users on PagerDuty  
[list policies](#action-list-policies) - Get list of escalation policies on PagerDuty  
[create incident](#action-create-incident) - Create an incident on PagerDuty  
[get oncall user](#action-get-oncall-user) - Get list of users for a specific escalation policy  
[get user info](#action-get-user-info) - Get information on a particular user  

## action: 'test connectivity'
Test connection to PagerDuty to validate supplied API key

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'list teams'
Get list of teams configured on PagerDuty

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.id | string |  `pagerduty team id` 
action\_result\.data\.\*\.name | string |  `pagerduty team` 
action\_result\.summary\.total\_teams | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.parent | string | 
action\_result\.data\.\*\.default\_role | string | 
action\_result\.data\.\*\.self | string |  `url` 
action\_result\.data\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.summary | string | 
action\_result\.data\.\*\.privilege | string | 
action\_result\.data\.\*\.type | string |   

## action: 'list oncalls'
Get list of oncalls on PagerDuty

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.end | string | 
action\_result\.data\.\*\.escalation\_level | numeric | 
action\_result\.data\.\*\.escalation\_policy\.html\_url | string |  `url` 
action\_result\.data\.\*\.escalation\_policy\.id | string |  `pagerduty escalation id` 
action\_result\.data\.\*\.escalation\_policy\.self | string |  `url` 
action\_result\.data\.\*\.escalation\_policy\.summary | string | 
action\_result\.data\.\*\.escalation\_policy\.type | string | 
action\_result\.data\.\*\.schedule | string | 
action\_result\.data\.\*\.start | string | 
action\_result\.data\.\*\.user\.html\_url | string |  `url` 
action\_result\.data\.\*\.user\.id | string |  `pagerduty user id` 
action\_result\.data\.\*\.user\.self | string |  `url` 
action\_result\.data\.\*\.user\.summary | string | 
action\_result\.data\.\*\.user\.type | string | 
action\_result\.summary\.num\_oncalls | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.schedule\.self | string |  `url` 
action\_result\.data\.\*\.schedule\.summary | string | 
action\_result\.data\.\*\.schedule\.type | string | 
action\_result\.data\.\*\.schedule\.id | string | 
action\_result\.data\.\*\.schedule\.html\_url | string |  `url`   

## action: 'list services'
Get list of available services on PagerDuty

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**team\_ids** |  optional  | Comma\-separated list of team IDs | string |  `pagerduty team id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.team\_ids | string |  `pagerduty team id` 
action\_result\.data\.\*\.acknowledgement\_timeout | numeric | 
action\_result\.data\.\*\.auto\_resolve\_timeout | numeric | 
action\_result\.data\.\*\.created\_at | string | 
action\_result\.data\.\*\.deleted\_at | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.email\_filter\_mode | string | 
action\_result\.data\.\*\.email\_incident\_creation | string | 
action\_result\.data\.\*\.id | string |  `pagerduty service id` 
action\_result\.data\.\*\.incident\_urgency\_rule\.type | string | 
action\_result\.data\.\*\.incident\_urgency\_rule\.urgency | string | 
action\_result\.data\.\*\.last\_incident\_timestamp | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.scheduled\_actions | string | 
action\_result\.data\.\*\.service\_key | string |  `md5` 
action\_result\.data\.\*\.service\_url | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.support\_hours | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.summary\.num\_services | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.alert\_creation | string | 
action\_result\.data\.\*\.integrations\.\*\.self | string |  `url` 
action\_result\.data\.\*\.integrations\.\*\.summary | string | 
action\_result\.data\.\*\.integrations\.\*\.type | string | 
action\_result\.data\.\*\.integrations\.\*\.id | string | 
action\_result\.data\.\*\.integrations\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.summary | string | 
action\_result\.data\.\*\.alert\_grouping | string | 
action\_result\.data\.\*\.alert\_grouping\_timeout | string | 
action\_result\.data\.\*\.escalation\_policy\.self | string |  `url` 
action\_result\.data\.\*\.escalation\_policy\.summary | string | 
action\_result\.data\.\*\.escalation\_policy\.type | string | 
action\_result\.data\.\*\.escalation\_policy\.id | string | 
action\_result\.data\.\*\.escalation\_policy\.html\_url | string |  `url` 
action\_result\.data\.\*\.self | string |  `url` 
action\_result\.data\.\*\.response\_play | string | 
action\_result\.data\.\*\.privilege | string | 
action\_result\.data\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.teams\.\*\.type | string | 
action\_result\.data\.\*\.teams\.\*\.id | string | 
action\_result\.data\.\*\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.addons | string | 
action\_result\.data\.\*\.updated\_at | string |   

## action: 'list users'
Get list of users on PagerDuty

Type: **investigate**  
Read only: **True**

To get a list of users in a certain team \(or teams\) add a comma\-separated list of team IDs to the <b>team\_ids</b> parameter\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**team\_ids** |  optional  | Comma\-separated list of team IDs | string |  `pagerduty team id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.team\_ids | string |  `pagerduty team id` 
action\_result\.data\.\*\.avatar\_url | string |  `url` 
action\_result\.data\.\*\.billed | boolean | 
action\_result\.data\.\*\.color | string | 
action\_result\.data\.\*\.email | string |  `email` 
action\_result\.data\.\*\.id | string |  `pagerduty user id` 
action\_result\.data\.\*\.invitation\_sent | boolean | 
action\_result\.data\.\*\.job\_title | string | 
action\_result\.data\.\*\.marketing\_opt\_out | boolean | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.role | string | 
action\_result\.data\.\*\.time\_zone | string | 
action\_result\.data\.\*\.user\_url | string | 
action\_result\.summary\.num\_users | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.teams\.\*\.type | string | 
action\_result\.data\.\*\.teams\.\*\.id | string | 
action\_result\.data\.\*\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.summary | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.self | string |  `url` 
action\_result\.data\.\*\.contact\_methods\.\*\.summary | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.type | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.id | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.html\_url | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.self | string |  `url` 
action\_result\.data\.\*\.notification\_rules\.\*\.summary | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.type | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.id | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.html\_url | string | 
action\_result\.data\.\*\.type | string |   

## action: 'list policies'
Get list of escalation policies on PagerDuty

Type: **investigate**  
Read only: **True**

Results can be filtered based in user IDs and team IDs<br><br>To filter on user IDs, add a comma\-separated list to the <b>user\_ids</b> parameter\. The results will include all escalation policies that apply to any user in the list\.<br><br>To filter on team IDs, add a comma\-separated list to the <b>team\_ids</b> parameter\. The results will include all escalation policies that apply to any team in the list\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user\_ids** |  optional  | Comma\-separated list of user IDs | string |  `pagerduty user id` 
**team\_ids** |  optional  | Comma\-separated list of team IDs | string |  `pagerduty team id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.team\_ids | string |  `pagerduty team id` 
action\_result\.parameter\.user\_ids | string |  `pagerduty user id` 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.escalation\_delay\_in\_minutes | numeric | 
action\_result\.data\.\*\.escalation\_rules\.\*\.id | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.color | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.email | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.id | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.name | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.time\_zone | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.rule\_object\.type | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.color | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.email | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.id | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.name | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.time\_zone | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.type | string | 
action\_result\.data\.\*\.id | string |  `pagerduty escalation id` 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.num\_loops | numeric | 
action\_result\.data\.\*\.services | string | 
action\_result\.data\.\*\.services\.\*\.acknowledgement\_timeout | numeric | 
action\_result\.data\.\*\.services\.\*\.auto\_resolve\_timeout | numeric | 
action\_result\.data\.\*\.services\.\*\.created\_at | string | 
action\_result\.data\.\*\.services\.\*\.deleted\_at | string | 
action\_result\.data\.\*\.services\.\*\.description | string | 
action\_result\.data\.\*\.services\.\*\.email\_filter\_mode | string | 
action\_result\.data\.\*\.services\.\*\.email\_incident\_creation | string | 
action\_result\.data\.\*\.services\.\*\.id | string | 
action\_result\.data\.\*\.services\.\*\.incident\_counts | string | 
action\_result\.data\.\*\.services\.\*\.incident\_urgency\_rule\.type | string | 
action\_result\.data\.\*\.services\.\*\.incident\_urgency\_rule\.urgency | string | 
action\_result\.data\.\*\.services\.\*\.last\_incident\_timestamp | string | 
action\_result\.data\.\*\.services\.\*\.name | string | 
action\_result\.data\.\*\.services\.\*\.scheduled\_actions | string | 
action\_result\.data\.\*\.services\.\*\.service\_key | string |  `md5` 
action\_result\.data\.\*\.services\.\*\.service\_url | string | 
action\_result\.data\.\*\.services\.\*\.status | string | 
action\_result\.data\.\*\.services\.\*\.support\_hours | string | 
action\_result\.data\.\*\.services\.\*\.type | string | 
action\_result\.summary\.num\_policies | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.self | string |  `url` 
action\_result\.data\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.teams | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.self | string |  `url` 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.summary | string | 
action\_result\.data\.\*\.escalation\_rules\.\*\.targets\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.privilege | string | 
action\_result\.data\.\*\.summary | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.teams\.\*\.type | string | 
action\_result\.data\.\*\.teams\.\*\.id | string | 
action\_result\.data\.\*\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.services\.\*\.self | string |  `url` 
action\_result\.data\.\*\.services\.\*\.summary | string | 
action\_result\.data\.\*\.services\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.on\_call\_handoff\_notifications | string |   

## action: 'create incident'
Create an incident on PagerDuty

Type: **generic**  
Read only: **False**

The <b>email</b> parameter may be required to create an incident depending on the configuration of the PagerDuty instance\.<br><br>Either the <b>escalation\_id</b> or the <b>assignee\_id</b> parameter can be used to provide notification and assignment settings to the incident\. If neither is provided, the default escalation policy on the PagerDuty system will be used\.<br><br>If both are provided, the <b>escalation\_id</b> will be used\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**title** |  required  | Title of incident | string | 
**description** |  required  | Description of incident | string | 
**service\_id** |  required  | ID of impacted service | string |  `pagerduty service id` 
**email** |  required  | Email of user creating incident | string |  `email` 
**escalation\_id** |  optional  | ID of escalation policy to use | string |  `pagerduty escalation id` 
**assignee\_id** |  optional  | ID of user to assign incident to | string |  `pagerduty user id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.assignee\_id | string |  `pagerduty user id` 
action\_result\.parameter\.description | string | 
action\_result\.parameter\.escalation\_id | string |  `pagerduty escalation id` 
action\_result\.parameter\.service\_id | string |  `pagerduty service id` 
action\_result\.parameter\.title | string | 
action\_result\.parameter\.email | string |  `email` 
action\_result\.data | string | 
action\_result\.summary\.incident\_key | string |  `md5` 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.incident\.body\.details | string | 
action\_result\.data\.\*\.incident\.assignments\.\*\.assignee\.self | string |  `url` 
action\_result\.data\.\*\.incident\.assignments\.\*\.assignee\.summary | string | 
action\_result\.data\.\*\.incident\.assignments\.\*\.assignee\.type | string | 
action\_result\.data\.\*\.incident\.assignments\.\*\.assignee\.id | string | 
action\_result\.data\.\*\.incident\.assignments\.\*\.assignee\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.assignments\.\*\.at | string | 
action\_result\.data\.\*\.incident\.basic\_alert\_grouping | string | 
action\_result\.data\.\*\.incident\.summary | string | 
action\_result\.data\.\*\.incident\.alert\_grouping | string | 
action\_result\.data\.\*\.incident\.id | string | 
action\_result\.data\.\*\.incident\.service\.self | string |  `url` 
action\_result\.data\.\*\.incident\.service\.summary | string | 
action\_result\.data\.\*\.incident\.service\.type | string | 
action\_result\.data\.\*\.incident\.service\.id | string |  `pagerduty service id` 
action\_result\.data\.\*\.incident\.service\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.title | string | 
action\_result\.data\.\*\.incident\.escalation\_policy\.self | string |  `url` 
action\_result\.data\.\*\.incident\.escalation\_policy\.summary | string | 
action\_result\.data\.\*\.incident\.escalation\_policy\.type | string | 
action\_result\.data\.\*\.incident\.escalation\_policy\.id | string |  `pagerduty escalation id` 
action\_result\.data\.\*\.incident\.escalation\_policy\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.self | string |  `url` 
action\_result\.data\.\*\.incident\.pending\_actions\.\*\.type | string | 
action\_result\.data\.\*\.incident\.pending\_actions\.\*\.at | string | 
action\_result\.data\.\*\.incident\.last\_status\_change\_at | string | 
action\_result\.data\.\*\.incident\.first\_trigger\_log\_entry\.self | string |  `url` 
action\_result\.data\.\*\.incident\.first\_trigger\_log\_entry\.summary | string | 
action\_result\.data\.\*\.incident\.first\_trigger\_log\_entry\.type | string | 
action\_result\.data\.\*\.incident\.first\_trigger\_log\_entry\.id | string | 
action\_result\.data\.\*\.incident\.first\_trigger\_log\_entry\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.type | string | 
action\_result\.data\.\*\.incident\.status | string | 
action\_result\.data\.\*\.incident\.description | string | 
action\_result\.data\.\*\.incident\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.created\_at | string | 
action\_result\.data\.\*\.incident\.alert\_counts\.resolved | numeric | 
action\_result\.data\.\*\.incident\.alert\_counts\.all | numeric | 
action\_result\.data\.\*\.incident\.alert\_counts\.triggered | numeric | 
action\_result\.data\.\*\.incident\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.incident\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.incident\.teams\.\*\.type | string | 
action\_result\.data\.\*\.incident\.teams\.\*\.id | string | 
action\_result\.data\.\*\.incident\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.last\_status\_change\_by\.self | string |  `url` 
action\_result\.data\.\*\.incident\.last\_status\_change\_by\.summary | string | 
action\_result\.data\.\*\.incident\.last\_status\_change\_by\.type | string | 
action\_result\.data\.\*\.incident\.last\_status\_change\_by\.id | string | 
action\_result\.data\.\*\.incident\.last\_status\_change\_by\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.incident\_key | string |  `md5` 
action\_result\.data\.\*\.incident\.impacted\_services\.\*\.self | string |  `url` 
action\_result\.data\.\*\.incident\.impacted\_services\.\*\.summary | string | 
action\_result\.data\.\*\.incident\.impacted\_services\.\*\.type | string | 
action\_result\.data\.\*\.incident\.impacted\_services\.\*\.id | string | 
action\_result\.data\.\*\.incident\.impacted\_services\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.incident\.incident\_number | numeric | 
action\_result\.data\.\*\.incident\.is\_mergeable | boolean | 
action\_result\.data\.\*\.incident\.urgency | string | 
action\_result\.data\.\*\.incident\.assigned\_via | string |   

## action: 'get oncall user'
Get list of users for a specific escalation policy

Type: **investigate**  
Read only: **True**

Finds the list of users associated with the <b>escalation\_id</b>\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**escalation\_id** |  required  | ID of escalation policy to use | string |  `pagerduty escalation id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.escalation\_id | string |  `pagerduty escalation id` 
action\_result\.data | string | 
action\_result\.data\.\*\.user\.id | string |  `pagerduty user id` 
action\_result\.data\.\*\.user\.name | string | 
action\_result\.data\.\*\.user\.email | string |  `email` 
action\_result\.summary\.num\_users | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.end | string | 
action\_result\.data\.\*\.schedule | string | 
action\_result\.data\.\*\.escalation\_policy\.self | string |  `url` 
action\_result\.data\.\*\.escalation\_policy\.summary | string | 
action\_result\.data\.\*\.escalation\_policy\.type | string | 
action\_result\.data\.\*\.escalation\_policy\.id | string | 
action\_result\.data\.\*\.escalation\_policy\.html\_url | string |  `url` 
action\_result\.data\.\*\.start | string | 
action\_result\.data\.\*\.user\.job\_title | string | 
action\_result\.data\.\*\.user\.description | string | 
action\_result\.data\.\*\.user\.color | string | 
action\_result\.data\.\*\.user\.self | string |  `url` 
action\_result\.data\.\*\.user\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.user\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.user\.teams\.\*\.type | string | 
action\_result\.data\.\*\.user\.teams\.\*\.id | string | 
action\_result\.data\.\*\.user\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.user\.html\_url | string |  `url` 
action\_result\.data\.\*\.user\.summary | string | 
action\_result\.data\.\*\.user\.contact\_methods\.\*\.self | string |  `url` 
action\_result\.data\.\*\.user\.contact\_methods\.\*\.summary | string | 
action\_result\.data\.\*\.user\.contact\_methods\.\*\.type | string | 
action\_result\.data\.\*\.user\.contact\_methods\.\*\.id | string | 
action\_result\.data\.\*\.user\.contact\_methods\.\*\.html\_url | string | 
action\_result\.data\.\*\.user\.avatar\_url | string |  `url` 
action\_result\.data\.\*\.user\.role | string | 
action\_result\.data\.\*\.user\.invitation\_sent | boolean | 
action\_result\.data\.\*\.user\.time\_zone | string | 
action\_result\.data\.\*\.user\.billed | boolean | 
action\_result\.data\.\*\.user\.notification\_rules\.\*\.self | string |  `url` 
action\_result\.data\.\*\.user\.notification\_rules\.\*\.summary | string | 
action\_result\.data\.\*\.user\.notification\_rules\.\*\.type | string | 
action\_result\.data\.\*\.user\.notification\_rules\.\*\.id | string | 
action\_result\.data\.\*\.user\.notification\_rules\.\*\.html\_url | string | 
action\_result\.data\.\*\.user\.type | string | 
action\_result\.data\.\*\.escalation\_level | numeric | 
action\_result\.data\.\*\.schedule\.self | string |  `url` 
action\_result\.data\.\*\.schedule\.summary | string | 
action\_result\.data\.\*\.schedule\.type | string | 
action\_result\.data\.\*\.schedule\.id | string | 
action\_result\.data\.\*\.schedule\.html\_url | string |  `url`   

## action: 'get user info'
Get information on a particular user

Type: **investigate**  
Read only: **True**

Finds name, email, and all other information on a given <b>user\_id</b>\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user\_id** |  required  | User ID to query | string |  `pagerduty user id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.user\_id | string |  `pagerduty user id` 
action\_result\.data | string | 
action\_result\.data\.\*\.id | string |  `pagerduty user id` 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.email | string |  `email` 
action\_result\.summary\.name | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.job\_title | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.color | string | 
action\_result\.data\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.self | string |  `url` 
action\_result\.data\.\*\.teams\.\*\.summary | string | 
action\_result\.data\.\*\.teams\.\*\.type | string | 
action\_result\.data\.\*\.teams\.\*\.id | string | 
action\_result\.data\.\*\.teams\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.html\_url | string |  `url` 
action\_result\.data\.\*\.summary | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.self | string |  `url` 
action\_result\.data\.\*\.contact\_methods\.\*\.summary | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.type | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.id | string | 
action\_result\.data\.\*\.contact\_methods\.\*\.html\_url | string | 
action\_result\.data\.\*\.avatar\_url | string |  `url` 
action\_result\.data\.\*\.role | string | 
action\_result\.data\.\*\.invitation\_sent | boolean | 
action\_result\.data\.\*\.time\_zone | string | 
action\_result\.data\.\*\.billed | boolean | 
action\_result\.data\.\*\.notification\_rules\.\*\.self | string |  `url` 
action\_result\.data\.\*\.notification\_rules\.\*\.summary | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.type | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.id | string | 
action\_result\.data\.\*\.notification\_rules\.\*\.html\_url | string | 
action\_result\.data\.\*\.type | string | 