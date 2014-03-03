# Chap1_7 teh algorithm that if an element in an MxN matrix is 0, its entire
# row and column is set to 0.A


def main():

# This is wrong, can't multiply the rows directly like this'
    #matrix = row * [col * [1]]
    matrix = [[ 1, 2, 3, 4, 5 ], [ 6, 7, 8, 9, 10 ]]
    row, col = 2, 5
    matrix[0][0] = 0

    # Adding the row and cols that need to be 0
    row_list = list()
    col_list = list()
    for i in xrange(row):
        for j in xrange(col):
            if matrix[i][j] == 0:
                row_list.append(i)
                col_list.append(j)

    # Check on 0s and print the results
    if row_list:
        for i in row_list:
            for j in xrange(col):
                matrix[i][j] = 0
    if col_list:
        for j in col_list:
            for i in xrange(row):
                matrix[i][j] = 0
    print matrix


if __name__ == "__main__":
    main()
