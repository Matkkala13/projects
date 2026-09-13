def numeroDeIslas(mapa):
   # Tu código aquí 👇

    def island_counter(mapa):
        y_len_map = len(mapa)
        x_len_map = len(mapa[0])

        def check(i, j):  
            if i < 0 or i > y_len_map - 1:
                return False
            if j < 0 or j > x_len_map - 1:
                return False
            
            if mapa[i][j] == "1":
                mapa[i][j] = "0"
                checks = [
                    check(i, j + 1), #right
                    check(i, j - 1), #left
                    check(i - 1, j), #up
                    check(i + 1, j)  #down
                    ]
    
                for x in checks:
                    if not x:
                        
                        return True
                    else:
                        pass
                     
            else:
                return False

        islands = 0
        for i in range(y_len_map):
            for j in range(x_len_map):
                if check(i,j):
                    islands +=1
                     
        return islands

    mapa = island_counter(mapa) 
    return mapa

mapa = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"],
]
response = numeroDeIslas(mapa)
print(response)

mapa = [
["1","1","0","0","1"],
["1","1","1","0","1"],
["0","0","1","0","1"],
["0","0","0","0","1"],
["0","0","0","0","1"],
]
response = numeroDeIslas(mapa)
print(response)

mapa = [
["1","1","0","0","1"],
["1","1","1","0","1"],
["0","0","1","0","1"],
["0","0","0","0","1"],
["1","1","0","0","1"],
["1","0","1","0","1"],
["0","0","1","1","1"],
["1","0","0","1","1"],
]
response = numeroDeIslas(mapa)
print(response)