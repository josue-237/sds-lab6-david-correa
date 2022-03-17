# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

state_capital_dict = {'Alabama': 'montgomery', 'Alaska': 'juneau', 'Arizona': 'phoenix', 'Arkansas': 'little rock', 'California': 'sacramento', 'Colorado': 'denver', 'Connecticut': 'hartford', 'Delaware': 'dover', 'Florida': 'tallahassee', 'Georgia': 'atlanta', 'Hawaii': 'honolulu', 'Idaho': 'boise', 'Illinois': 'springfield', 'Indiana': 'indianapolis', 'Iowa': 'des moines', 'Kansas': 'topeka', 
'Kentucky': 'frankfort', 'Louisiana': 'baton rouge', 'Maine': 'augusta', 'Maryland': 'annapolis', 'Massachusetts': 'boston', 'Michigan': 'lansing', 'Minnesota': 'saint paul', 'Mississippi': 'jackson', 'Missouri': 'jefferson city', 'Montana': 'helena', 'Nebraska': 'lincoln', 'Nevada': 'carson city', 'New Hampshire': 'concord', 'New Jersey': 'trenton', 'New Mexico': 'santa fe', 'New York': 'albany', 
'North Carolina': 'raleigh', 'North Dakota': 'bismarck', 'Ohio': 'colombus', 'Oklahoma': 'oklahoma city', 'Oregon': 'salem', 'Pennsylvania': 'harrisburg', 'Rhode Island': 'providence', 'South Carolina': 'columbia', 'South Dakota': 'pierre', 'Tennessee': 'nashville', 'Texas': 'austin', 'Utah': 'salt lake city', 'Vermont': 'montpelier', 'Virginia': 'richmond', 'Washington': 'olympia', 
'West Virginia': 'charleston', 'Wisconsin': 'madison', 'Wyoming': 'cheyenne'}

def user_results(response_dict):  # {state, capital}
    result_return_dict = {}
    for state in response_dict:
        if response_dict[state].lower() == state_capital_dict[state].lower():
            result_return_dict[state] = "Correct"
        else:
            result_return_dict[state] = "Incorrect"
    return result_return_dict  # {state, Correct/Incorrect}
