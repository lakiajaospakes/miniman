input_list = ['sas', 'sa', 's a', 'se', 'b v', 'as', 'sl', 'srl', 'spa', 'oy', 'sdn bhd', 'sae', 'bvba', 'ltda', 'aps']

# Strings to be preserved
preserved_strings = ['ag bio']

# Filter out strings while preserving 'ag bio'
filtered_list = [s for s in input_list if s in preserved_strings or ' ' not in s]

print(filtered_list)
