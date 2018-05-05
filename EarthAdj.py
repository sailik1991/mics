data = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 6),
    (1, 7),
    (1, 2),
    (1, 5),
    (1, 15),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 3),
    (3, 9),
    (3, 10),
    (3, 11),
    (3, 4),
    (4, 11),
    (4, 12),
    (4, 13),
    (4, 5),
    (5, 13),
    (5, 14),
    (5, 15),
    (6, 15),
    (6, 16),
    (6, 17),
    (6, 7),
    (6, 25),
    (7, 17),
    (7, 8),
    (8, 17),
    (8, 18),
    (8, 19),
    (8, 9),
    (9, 19),
    (9, 10),
    (10, 19),
    (10, 20),
    (10, 21),
    (10, 11),
    (11, 21),
    (11, 12),
    (12, 21),
    (12, 22),
    (12, 23),
    (12, 13),
    (13, 23),
    (13, 14),
    (14, 23),
    (14, 24),
    (14, 25),
    (14, 15),
    (15, 25),
    (16, 26),
    (16, 30),
    (16, 17),
    (16, 25),
    (17, 26),
    (17, 18),
    (18, 26),
    (18, 27),
    (18, 19),
    (19, 27),
    (19, 20),
    (20, 27),
    (20, 28),
    (20, 21),
    (21, 28),
    (21, 22),
    (22, 28),
    (22, 29),
    (22, 23),
    (23, 29),
    (23, 24),
    (24, 29),
    (24, 30),
    (24, 25),
    (25, 30),
    (26, 31),
    (26, 27),
    (26, 30),
    (27, 31),
    (27, 28),
    (28, 31),
    (28, 29),
    (29, 31),
    (29, 30),
    (30, 31),
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
    print('{}'.format(row,sum(row)))
