input_file = open("input/day04.txt", 'r')
input = input_file.read().strip().split('\n')
input_file.close()

from collections import deque
from functools import cache
winning_nums, owned_nums = [],[] 

for row in input:
    temp = row.split("|")
    winning_nums.append(temp[0].strip().split())
    owned_nums.append(temp[1].strip().split())

@cache
def process(card):
    w,o  = cards[card]
    wins = len(set(w) & set(o))
    
    return list(range(card+1,card+wins+1,1))
    
cards = list(zip(winning_nums, owned_nums))
total_cards = 0
queue = deque()

for i in range(len(cards)):
    queue.append(i)

while queue:
    card = queue.popleft()
    total_cards += 1
    need_to_be_processed = process(card)
    queue.extend(need_to_be_processed)

print(total_cards)