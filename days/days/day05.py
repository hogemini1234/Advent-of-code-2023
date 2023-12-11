input_file = open("input/day05.txt", 'r')
input = input_file.read().strip().split('\n')
input_file.close()

seeds = [int(x) for x in input[0].split(':')[-1].strip().split()]
maps = []

input = [x for x in input if x != '']

i = 1

while i < len(input):
    if not input[i][0].isdigit():
        i += 1
    mapp = []
    while i < len(input) and input[i][0].isdigit():
        mapp.append([int(x) for x in input[i].split()])
        i += 1
    maps.append(mapp)

    
def mapper(mappings, input):
    for mapp in mappings:
        start_range, start_domain, span = mapp
        if input <= start_domain + span and input >= start_domain: return start_range + (input - start_domain)

    return input

mapped_seeds = seeds.copy()

for mapping in maps:
    mapped_seeds = [mapper(mapping,input) for input in mapped_seeds]

print(mapped_seeds, min(mapped_seeds))