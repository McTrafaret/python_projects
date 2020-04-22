import sys

JOURNAL_NUMBER = 27

number_of_tasks = int(sys.argv[1])

print(JOURNAL_NUMBER % number_of_tasks + 1)
