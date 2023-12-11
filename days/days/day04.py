input_file = open("input/day04.txt", 'r')
input = input_file.read().strip().split("\n")
input_file.close()

winning_nums, owned_nums = [],[] 

for row in input:
    temp = row.split("|")
    winning_nums.append(temp[0].strip().split())
    owned_nums.append(temp[1].strip().split())

summ = 0
for w,o in zip(winning_nums,owned_nums):
    wins = len(set(w) & set(o))
    points = 0 if not wins else 2**(wins-1)
    summ += points

print(summ)