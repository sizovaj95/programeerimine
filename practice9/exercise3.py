array1 = [[1,2],
          [3,4]]

array2 = [[5,6,7],
          [8,9,10]]


array_1_rows = len(array1)
array_1_cols = len(array1[0])
array_2_rows = len(array2)
array_2_cols = len(array2[0])

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")

if array_1_cols == array_2_rows:
    result = [[0 for _ in range(array_2_cols)] for _ in range(array_1_rows)]

    for i in range(array_1_rows):
        for j in range(array_2_cols):
            for k in range(array_1_cols):
                result[i][j] += array1[i][k] * array2[k][j]
    print(result)
else:
    print('Multiplication is not possible')
