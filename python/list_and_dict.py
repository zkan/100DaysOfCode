us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

states_list = ['Oklahoma',
               'Kansas',
               'North Carolina',
               'Georgia',
               'Oregon',
               'Mississippi',
               'Minnesota',
               'Colorado',
               'Alabama',
               'Massachusetts',
               'Arizona',
               'Connecticut',
               'Montana',
               'West Virginia',
               'Nebraska',
               'New York',
               'Nevada',
               'Idaho',
               'New Jersey',
               'Missouri',
               'South Carolina',
               'Pennsylvania',
               'Rhode Island',
               'New Mexico',
               'Alaska',
               'New Hampshire',
               'Tennessee',
               'Washington',
               'Indiana',
               'Hawaii',
               'Kentucky',
               'Virginia',
               'Ohio',
               'Wisconsin',
               'Maryland',
               'Florida',
               'Utah',
               'Maine',
               'California',
               'Vermont',
               'Arkansas',
               'Wyoming',
               'Louisiana',
               'North Dakota',
               'South Dakota',
               'Texas',
               'Illinois',
               'Iowa',
               'Michigan',
               'Delaware']


for index, each in enumerate(us_state_abbrev, 1):
    if index == 10:
        print(each, us_state_abbrev[each])

print('-' * 10)

for index, each in enumerate(states_list, 1):
    if index == 10:
        print(each)

print('-' * 10)

for index, each in enumerate(us_state_abbrev, 1):
    if index == 45:
        print(each)

print('-' * 10)

for index, each in enumerate(us_state_abbrev, 1):
    if index == 27:
        print(us_state_abbrev[each])
