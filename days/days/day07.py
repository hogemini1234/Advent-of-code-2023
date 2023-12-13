from itertools import groupby

input_file = 'input/day07.txt'

q = { 7: open(input_file).read().strip() }


groups = [x.split() for x in q[7].split('\n')]
for g in groups:
    g[0] = ['AKQJT98765432'.index(c) + 1 for c in g[0]]

def score(h):
    s = sorted(h)
    if len(set(s)) == 1:
        return 7
    elif s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

for g in groups:
    g.append(score(g[0]))

groups.sort(key=lambda x: x[2])
ranked_groups = [list(g) for _, g in groupby(groups, lambda x: x[2])]
for g in ranked_groups:
    g.sort(key=lambda x: x[0], reverse=True)

groups = []
for g in ranked_groups:
    groups += g

total = 0
for i, g in enumerate(groups):
    total += int(g[1]) * (i+1)

print('Day 07 Part 1:',total)

print('Day 07 Part 1:',(y:=[[['AKQJT98765432'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and [g.__iadd__([(s:=sorted(g[0])) and (7 if len(set(s))==1 else 6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in groupby(sorted(y,key=lambda x:x[2]), lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]))

groups = [x.split() for x in q[7].split('\n')]
for g in groups:
    g[0] = ['AKQT98765432J'.index(c) + 1 for c in g[0]]

def score(h):
    if len(set(h)) == 1 or len(set(h)) == 2 and 13 in h:
        return 7
    replace = min([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 13])])
    s = sorted([replace if c == 13 else c for c in h])
    if s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

for g in groups:
    g.append(score(g[0]))

groups.sort(key=lambda x: x[2])
ranked_groups = [list(g) for _, g in groupby(groups, lambda x: x[2])]
for g in ranked_groups:
    g.sort(key=lambda x: x[0], reverse=True)

groups = []
for g in ranked_groups:
    groups += g

total = 0
for i, g in enumerate(groups):
    total += int(g[1]) * (i+1)

print('Day 07 Part 2:',total)

print('Day 07 Part 2:',(y:=[[['AKQT98765432J'.index(c)+1 for c in g.split()[0]],g.split()[1]] for g in q[7].split('\n')]) and (score:=lambda h:(7 if len(set(h)) == 1 or len(set(h)) == 2 and 13 in h else 0) or (s:=sorted([min([c for c in h if h.count(c) == max([h.count(c) for c in h if c != 13])]) if c == 13 else c for c in h])) and (6 if s[0]==s[1]==s[2]==s[3] or s[1]==s[2]==s[3]==s[4] else 5 if s[0]==s[1]==s[2] and s[3]==s[4] or s[0]==s[1] and s[2]==s[3]==s[4] else 4 if s[0]==s[1]==s[2] or s[1]==s[2]==s[3] or s[2]==s[3]==s[4] else 3 if s[0]==s[1] and s[2]==s[3] or s[0]==s[1] and s[3]==s[4] or s[1]==s[2] and s[3]==s[4] else 2 if len(set(s))==4 else 1)) and [g.__iadd__([score(g[0])]) for g in y] and sum([int(g[1])*(i+1) for i, g in enumerate([g for g in [list(g) for _,g in groupby(sorted(y,key=lambda x:x[2]), lambda x:x[2])] for g in sorted(g,key=lambda x:x[0],reverse=True)])]))