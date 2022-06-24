def solution(picture):
    rows = len(picture)
    columns = len(picture[0])
    returnMatrix = [["*" for j in range(columns+2)] for i in range(rows+2)]


    print(rows)
    print(columns)

    for i in range(rows+2):
        for j in range(columns+2):
            returnMatrix[i+1][j+1] = picture[i][j]



    return returnMatrix

example_matrix = ["abc","ded"]

print(solution(example_matrix))