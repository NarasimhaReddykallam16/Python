# class Duck:
#     def quack(self):
#         print('Quack,quack')

#     def fly(self):
#         print('Flap,flap')


# class Person:
#     def quack(self):
#         print("i'm Quacking like a duck")

#     def fly(self):
#         print("i'm flapping my arms")


# def quack_and_fly(thing):
#     thing.quack()
#     thing.fly()       # This is Duck Typing not caring about
# who the object is


# def quack_and_fly(thing):
#     if hasattr(thing, 'quack'):         # This is asking permission
#         if callable(thing.quack):       # before calling.
#             thing.quack()               #LBYL
#     if hasattr(thing, 'fly'):           # Look Before You Heap
#         if callable(thing.fly):
#             thing.fly()

# def quack_and_fly(thing):
#     try:
#         thing.quack()                 #EAFP
#         thing.fly()                     #It is easy to try and ask
#     except IndentationError as e:        #forgiveness
#         print(e)


# d = Duck()
# p = Person()

# quack_and_fly(p)


##        EAFP FOR DICTIONARY       ##

# person = {'name': 'jass', 'age': 20, 'job': 'IT'}
# person = {'name': 'jass', 'age': 20}

# if 'name' in person and 'age' in person and 'job' in person:
#     print(f'name is {person['name']},age is {
#           person['age']},job is {person['job']}')
# else:                                   ###   LBYL TYPE ####
#     print('Missing some Keys')

# try:
#     print(f'name is {person['name']},age is {
#           person['age']},job is {person['job']}')
# except KeyError as k:                              ### EAFP #####
#     print(f'Missing some keys :{k}')


##       EAFP FOR LIST      ##


# l = [1, 2, 3, 4, 5]
# l = [1, 2, 3, 4, 5, 6]

# if len(l) >= 6:
#     print(l[5])
# else:
#     print('That index does not exist')


# try:
#     print(l[5])
# except IndexError as i:
#     print(i)
