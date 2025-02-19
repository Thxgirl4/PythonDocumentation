# x = int(input("please enter an integer: " ))
#    if x < 0:
#     x = 0
#     print('Negative changed to zero')
#    elif x == 0:
#     print('Zero')
#    elif x == 1:
#     print('Single')
#    else:
#     print('More than one digit')



# users = {'Hans' : 'active', 'Eleonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


# for num in range(2, 10):
#          if num % 2 == 0:
#              print(f"Found an even number: {num}")
#              continue
#          print(f"Found an odd number: {num}")

# match statements
#def http_error(status):
#   match status:
#       case 400:
#           return "Bad Request"
#       case 404:
#           return "Not Found"
#       case 418:
#           return "I'm a teapot"
#       case _:
#           return "Something went wrong"


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# def where_is(point):
#     match point:
#      case Point(x=0, y=0):
#          print('Origin')
#      case Point(x=0, y=y):
#          print(f"Y={y}")
#      case Point(x=x, y=0):
#          print(f"X={x}")
#      case Point():
#          print("somewhere else")
#      case _:
#          raise ValueError("Not a valid point")


            


