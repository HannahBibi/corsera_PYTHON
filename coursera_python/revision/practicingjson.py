import json

geocoding_file = open('geocoding_data.json').read()
dictionary_geo = json.loads(geocoding_file)


address_list = dictionary_geo['results']
addr_count = len(address_list)

print('Address Count:', addr_count)

first_dictionary = address_list[0]
number_of_keys = len(first_dictionary.keys())

print('Number of Keys:', number_of_keys)

address_components = first_dictionary['address_components']
number_of_addr_components = len(address_components)

print('Number of address components:', number_of_addr_components, '\n')

for address_component in address_components:
    print('Long name:', address_component['long_name'], '\n', 'Type:', address_component['types'][0], '\n')
    #You can search for specific words in dictionaries because they are the keys!

print(first_dictionary['formatted_address'], '\n')

for formatted_addr in address_list:
    print('Formatted Address', formatted_addr['formatted_address'])