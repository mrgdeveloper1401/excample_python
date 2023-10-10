# while True:
#     try:
#         number = int(input('Enter a number: '))
#         break
#     except ValueError:
#         print(f'invalid number')
#         print('Please enter a number. try again.')
# ---------------------------------------------------------------------------

# import socket

# addr = '127.0.0.1108'

# try:
#     socket.inet_aton(addr)
#     print('validip address')
# except socket.error as e:
#     print(e)