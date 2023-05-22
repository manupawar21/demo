# # BFS 

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# queue = []
# visited = []

# def BFS(graph, visited, node):

#     queue.append(node)
#     visited.append(node)

#     while queue:
#         ele = queue.pop(0)
#         print(ele, " ")

#         for neighbour in graph[ele]:
#             if neighbour not in visited:
#                 queue.append(neighbour)
#                 visited.append(neighbour)


# BFS(graph, visited, 'A')

#---------------------------------------------------------------------------------------------

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# visited = set()

# def DFS(graph, visited, node):

#     if node not in visited:
#         print(node)
#         visited.add(node)

#         for neighbour in graph[node]:
#             DFS(graph, visited, neighbour)

# DFS(graph, visited, 'A')


#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

# ChatBot

def greet():
    print("Hello, I am ChatBot")
    print("Created in @2023")


def name():
    print("What is your good name ! ")
    name = input()
    print("Ohh That's Nice...", name," !")

def age():
    print()
    print("I Can Guess You Age")
    print("Enter Remainder of your age by dviding 3, 5 and 7")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = ((rem3*70) + (rem5*21)+ (rem7*15))%105
    print("Your Age Is : ",age)

def count():
    print()
    print("I Can Count Numbers For You")
    print("Please Enter Number : ")
    num = int(input())
    for i in range (num):
        print(i+1, " !")


def test():
    print("How to Define a Funtion ?")
    print("1. funtion")
    print("2. def")
    print("3. sub")
    print("4. for")

    
    test = 0

    while (test != 2):
        test = int(input())
        if(test == 2):
            print("Ohh Corret Ans")
            print("Thanks For Giving Time For Me")
            print("Have A Nice Day")
        if(test == 1, test == 3, test == 4):
            print("Sorry Try Again")










# greet()
# name()
# age()
count()
test()