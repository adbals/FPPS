def zigzag(row,col,a):
    evenRow = 0
    oddRow = 1
    index = []
    while evenRow < row:
        for i in range(col):
            x = (a[evenRow][i])
            index.append(x)
        evenRow = evenRow + 2

        if oddRow < row:
            for i in range(col - 1, -1, -1):
                x = (a[oddRow][i])
                index.append(x)
        oddRow = oddRow + 2
    return (index)
r = 3
c = 5

mat = [[1, 2, 3, 4, 5], 
	[6, 7, 8, 9, 10], 
	[11, 12, 13, 14, 15]]; 

print(type(zigzag(r , c , mat)))
