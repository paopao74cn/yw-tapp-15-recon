import os

next_resource_id = 1

def resource_facts(file):
    global next_resource_id
    if os.path.isfile(file):
        print 'resource({0}, "{1}").'.format(next_resource_id, file)
        next_resource_id += 1
    elif os.path.isdir(file):
        dir = file
        subdirs = []
        for item in sorted(os.listdir(dir)):
            path = os.path.join(dir, item)
            if (os.path.isfile(path)):
                resource_facts(path)
            else:
                subdirs.append(path)
        for subdir in subdirs:
           resource_facts(subdir)

def resource_channel_fact(file_id, channel_id):
    print "resource_channel({0}, {1}).".format(file_id, channel_id)

def resource_channel_facts(file_id_first, file_id_last, channel_id):
    for file_id in range(file_id_first, file_id_last + 1):
        resource_channel_fact(file_id, channel_id);

def variable_value_fact(resource_id, variable_id, variable_value):
    print 'uri_variable_value({0}, {1}, "{2}").'.format(resource_id, variable_id, variable_value)

def variable_value_facts(resource_id_first, resource_id_last, variable_id, variable_value):
    for resource_id in range(resource_id_first, resource_id_last + 1):
        variable_value_fact(resource_id, variable_id, variable_value)

def variable_incrementing_values_facts(resource_id_first, resource_id_last, variable_id, variable_value_first):
    variable_value = variable_value_first;
    for resource_id in range(resource_id_first, resource_id_last + 1):
        variable_value_fact(resource_id, variable_id, variable_value)
        variable_value += 1

if __name__ == '__main__':

    print '\n% FACT: resource(resource_id, resource_uri).'
    resource_facts('./calibration.img')
    resource_facts('./cassette_q55_spreadsheet.csv')
    resource_facts('./run')

    print '\n% FACT: resource_channel(resource_id, channel_id).'
    resource_channel_fact(1, 23)
    resource_channel_fact(2, 9)
    resource_channel_fact(3, 3)
    resource_channel_fact(4, 4)
    resource_channel_fact(5, 2)
    resource_channel_facts(6, 139, 1)
    resource_channel_facts(140, 273, 22)

    print '\n% FACT: uri_variable_value(resource_id, variable_id, variable_value).'

    # values for raw image sample_id uri variables
    variable_value_facts(140, 213, 3, 'DRT240')  
    variable_value_facts(214, 273, 3, 'DRT322')

    # values for raw image frame_number uri variables
    variable_incrementing_values_facts(140, 176, 4, 1)
    variable_incrementing_values_facts(177, 213, 4, 1)    
    variable_incrementing_values_facts(214, 243, 4, 1)    
    variable_incrementing_values_facts(244, 273, 4, 1)    

    # values for raw image cassette_id uri variables
    variable_value_facts(140, 273, 5, 'q55')

    # values for raw image energy uri variables
    variable_value_facts(140, 176, 6, '10000')
    variable_value_facts(177, 213, 6, '11000')
    variable_value_facts(214, 243, 6, '10000')
    variable_value_facts(244, 273, 6, '11000')



    # values for corrected image sample_id uri variables
    variable_value_facts(6, 79, 7, 'DRT240')  
    variable_value_facts(80, 139, 7, 'DRT322')
    
    # values for corrected image frame_number uri variables
    variable_incrementing_values_facts(6, 42, 8, 1)
    variable_incrementing_values_facts(43, 79, 8, 1)
    variable_incrementing_values_facts(80, 109, 8, 1)
    variable_incrementing_values_facts(110, 138, 8, 1)   # changed from 139 for Q4 to output a result

    # values for corrected image energy uri variables
    variable_value_facts(6, 42, 9, '10000')
    variable_value_facts(43, 79, 9, '11000')
    variable_value_facts(80, 109, 9, '10000')
    variable_value_facts(110, 139, 9, '11000')

    
    # values for sample spreadsheet cassette_id 
    variable_value_fact(2, 2, "q55")

