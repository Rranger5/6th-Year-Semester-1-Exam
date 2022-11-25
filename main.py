# ### Question 1
# ## 1. 
# # Using CSV files allow users to import and input large amounts of data into databases, all of which can be manipulated and used for programs and tasks.

# ## 2.
# numbers = input("Please enter 5 numbers (please put a comma in between each number): ")

# ## 3.
# file = open("numList.csv", "w")
# file.write(numbers)
# file.close()

# ## 4.
# file = open("numList.csv", "r")
# dataIn = file.read()
# file.close()
# print(dataIn)

# ## 5.
# numList = dataIn.split(",")
# numList = [int(i) for i in numList]

# ## 6.
# print(numList)

# ## 7.
# numList.sort()

# ## 8.
# print(numList)

# ## 9.
# print(numList[-1])
# print(numList[0])

# ## 10.
# import statistics
# average = statistics.mean(numList)
# print(average)

# ## 11.
# names = []

# ## 12.
# pets = []

# ## 13.
# name = input("Please enter your name: ")
# numPets = int(input("Please enter the number of pets you have: "))

# ## 14.
# names.append(name)
# pets.append(numPets)

# ## 15.
# import matplotlib.pyplot as ply
# ply.bar(names, pets)
# ply.title("How many pets do you have?")
# ply.xlabel("Names")
# ply.ylabel("Pets")
# ply.show()

######################################################################

### Question 2
## a) The term abstraction means to identify patterns in a problem/task and extract what informtaion is needed to solve the problem/task, and identify which can be ignored. In the context of code, it requires a programmer to think about which parts of the problem/task is necessary to write code for in order to solve it, and which parts can be left out, as they are not instrumental to the question.

## b) Functions can be used by programmers to achieve abstraction, as to create a function, a programmer must first analyse their problem to see what they want the function to carry out and achieve, which would require using abstraction to see which parts of the problem require a function to solve. Functions are also very limited, in that they can only solve what they have been programmed to solve, and would be useless in solving something that they weren't supposed to. In order to maximise the use of their functions, a programmer would have to use abstraction to ensure that their function is as useful as possible to their code and solves the problem they need it to.

#################################################################################

### Question 3
## a) 01001010 + 10011001 = 11100011
## b) 
# 11100011 = 1(2^0) + 1(2^1) + 0(2^2) + 0(2^3) + 0(2^4) + 1(2^5) + 1(2^6) + 1(2^7)
#          = 1(1) + 1(2) + 0(4) + 0(8) + 0(16) + 1(32) + 1(64) + 1(128)
#          = 1 + 2 + 0 + 0 + 0 + 32 + 64 + 128
# 11100011 = 227

##################################################################################

### Question 4
# def is_anagram(w1, w2):
#   if sorted(w1) == sorted(w2):
#     return True
#   else:
#     return False
  
# word1 = input("Enter the first word: ")
# word2 = "SILENT"

# if (sorted(word1)) == (sorted(word2)):
#   print("YES")

##################################################

## i)
# def is_anagram(w1, w2):
#   if sorted(w1) == sorted(w2):
#     return True
#   else:
#     return False
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# if (sorted(word1)) == (sorted(word2)):
#   print("YES")

################################################

## ii)
# def is_anagram(w1, w2):
#   if sorted(w1) == sorted(w2):
#     return True
#   else:
#     return False
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# if (sorted(word1)) == (sorted(word2)):
#   print(word1, "is an anagram of", word2)

################################################

## iii)
# def is_anagram(w1, w2):
#   if sorted(w1) == sorted(w2):
#     return True
#   else:
#     return False
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# if (sorted(word1)) == (sorted(word2)):
#   print(word1, "is an anagram of", word2)
# else:
#   print(word1, "is NOT an anagram of", word2)

##################################################

## iv)
# def is_anagram(w1, w2):
#   if sorted(w1) == sorted(w2):
#     return True
#   else:
#     return False
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# word1 = word1.upper()
# word2 = word2.upper()

# if (sorted(word1)) == (sorted(word2)):
#   print(word1, "is an anagram of", word2)
# else:
#   print(word1, "is NOT an anagram of", word2)

################################################

## v)
# def is_anagram(w1, w2):
#   w1 = w1.upper()
#   w2 = w2.upper()
#   if sorted(w1) == sorted(w2):
#     print(w1, "is an anagram of", w2)
#   else:
#     print(w1, "is NOT an anagram of", w2)
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# word1 = word1.upper()
# word2 = word2.upper()

# is_anagram(word1, word2)

# if (sorted(word1)) == (sorted(word2)):
#   print(word1, "is an anagram of", word2)
# else:
#   print(word1, "is NOT an anagram of", word2)

#################################################

## vi)
# def is_anagram(w1, w2):
#   w1 = w1.upper()
#   w2 = w2.upper()
#   if sorted(w1) == sorted(w2):
#     print(w1, "is an anagram of", w2)
#   else:
#     print(w1, "is NOT an anagram of", w2)
  
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# word1 = word1.upper()
# word2 = word2.upper()

# is_anagram(word1, word2)

# if (sorted(word1)) == (sorted(word2)):
#   print(word1, "is an anagram of", word2)
# else:
#   print(word1, "is NOT an anagram of", word2)

# phrase = input("Enter a phrase: ")

# phrase = phrase.upper()
# phrase1 = phrase.replace(" ", "")
# if (sorted(word1)) == (sorted(phrase1)):
#   print(word1, "is an anagram of", phrase)
# else:
#   print(word1, "is NOT an anagram of", phrase)

# if (sorted(word2)) == (sorted(phrase1)):
#   print(word2, "is an anagram of", phrase)
# else:
#   print(word2, "is NOT an anagram of", phrase)
