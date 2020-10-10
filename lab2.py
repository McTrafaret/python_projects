from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import groupby
from itertools import product
from csv import reader

#1
def count_colors_labels(colors_labels):
    d = defaultdict(int)
    for tup in set(colors_labels):
        d[tup[0]] += 1
    return d


# format: list of tuples: (color, label)
elems = [('yellow', 3), ('green', 4), ('green', 4), ('red', 2), ('green', 7), ('yellow', 4)]

# check
true_answer = {'yellow': 2, 'green': 2, 'red': 1}

assert count_colors_labels(elems) == true_answer

#2
def tail(filename, n=10):
    d = deque()
    s = ''
    with open(filename, 'r') as f:
        while(True):
            s = f.readline()
            if(not s): break
            d.append(s)
        close(f)
    for i in range(n, 1, -1):
        s += d[-i]
    return s

# # check with your file

# filename = ''
# last_lines = ''

# n = 10
# assert tail(filename, n) == last_lines

#3
def get_least_common(iterable_obj, n=3):
    c = Counter(iterable_obj).most_common()[::-1]
    return [tup[0] for tup in c[:n]]

#4
def read_employees(filename):
    with open(filename) as f:
        csvreader = reader(f)
        return [row[1] for row in csvreader]

print(read_employees('hype.csv'))

elems = [1,4,3,1,1,8,9,2,8,8,9,9]
assert get_least_common(elems) == [2, 3, 4]

#5
def get_permutations(s, n):
    res = []
    for tup in permutations(s, n):
        res.append("".join(tup))
    return sorted(res)

assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]

#6
def get_combinations(s, n):
    res = []
    for i in range(1, n+1):
        subres = []
        for tup in combinations(s, i):
            subres.append("".join(sorted(tup)))
        res += sorted(subres)
    return res

assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]

#7
def get_combinations_with_r(s, n):
    res = []
    for tup in combinations_with_replacement(s, n):
        res.append("".join(sorted(tup)))
    return sorted(res)

assert get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"]

#8
def compress_string(s):
    res = []
    for key, group in groupby(s, lambda x: x[0]):
        res.append((sum(1 for anything in group), int(key)))
    return res

assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]

#9
def maximize(lists, m):
    results = []
    combos = product(*lists)
    for combo in combos:
        results.append(sum(map(lambda x: x**2, combo)) % m)
    return max(results)

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
assert maximize(lists, m=1000) == 206

#10
def split(lists):
    return list(map(int, lists.split(',')))

str_list = "1, 2, 45, 555,5,5,23,4234"
assert split(str_list) == [1, 2, 45, 555, 5, 5, 23, 4234]
