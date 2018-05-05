data = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 9),
    (2, 3),
    (2, 5),
    (2, 6),
    (2, 7),
    (3, 7),
    (3, 8),
    (3, 9),
    (4, 5),
    (4, 9),
    (4, 10),
    (4, 11),
    (4, 15),
    (5, 6),
    (5, 11),
    (6, 7),
    (6, 11),
    (6, 12),
    (6, 13),
    (7, 8),
    (7, 14),
    (8, 9),
    (8, 13),
    (8, 14),
    (8, 15),
    (9, 15),
    (10, 11),
    (10, 15),
    (10, 16),
    (10, 18),
    (11, 12),
    (11, 16),
    (12, 13),
    (12, 16),
    (12, 17),
    (13, 14),
    (13, 17),
    (14, 15),
    (14, 17),
    (14, 18),
    (15, 18),
    (16, 17),
    (16, 18),
    (16, 19),
    (17, 18),
    (17, 19),
    (18, 19),
    ]
#NA
#import csv
#with open('data.csv') as f:
#    next(f) # Skip header
#    data = [map(int, row) for row in csv.reader(f)]
#    # Python 3.x: map(int, row) -> tuple(map(int, row))

n = max(max(user, item) for user, item in data) + 1 # Get size of matrix

matrix = [[0] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = 1

for user, item in data:
    matrix[user][item] = 1
    matrix[item][user] = 1

for row in matrix:
    print('{}'.format(row))
