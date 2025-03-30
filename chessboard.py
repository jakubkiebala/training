def chessboard(n=8):
    for i in range(1, n+1):
        if i%2 != 0:
            row = []
            for i in range(1, n+1):
                if i%2 != 0:
                    row.append('#')
                else:
                    row.append(' ')
            row = "".join(row)
            print(row)
        elif i%2 == 0:
            second_row = []
            for i in range(1, n+1):
                if i%2 !=0:
                    second_row.append(' ')
                else:
                    second_row.append('#')
            second_row = ''.join(second_row)            
            print(second_row)                


    print((n/2))
    

chessboard(9)

