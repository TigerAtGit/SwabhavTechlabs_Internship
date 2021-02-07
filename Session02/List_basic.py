import random as rd
#EX 01
list_r = [rd.randrange(5) for x in range(10)]
print(list_r)

#EX 02
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
results = [num for sublist in list_of_lists 
                for num in sublist]
print(results)