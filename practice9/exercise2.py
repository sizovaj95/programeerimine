array_ = [[5,6,7],
          [8,9,10]]


for i in range(2):
    row = array_[i]
    print(f"row {i}:", end=' ')
    for el in row:
        print(el, end=' ')
    print('\n')

print('\n')

for i in range(3):
    print(f"col {i}:", end=' ')
    for j in range(2):
        row = array_[j]
        print(row[i], end=' ')
    print('\n')

