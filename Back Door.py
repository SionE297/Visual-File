# Load user list from file
u_loaded = []
with open('C:\\Users\\minyg\\OneDrive\\Documents\\Visual\\user_list.txt', 'r') as file:
    for line in file:
        u_loaded.append(line.strip())
print('User List:')
print(u_loaded)
u = u_loaded

while True:
    print('What would you like to do?')
    print('1 - Asign New User')
    print('2 - Write Message')
    print('3 - Delete All Users')


print('Type in the user you would like to register:')
new_user = input('New User:').strip()
if new_user not in u:
    u.append(new_user)
    with open('C:\\Users\\minyg\\OneDrive\\Documents\\Visual\\user_list.txt', 'w') as file:
        for user in u:
            file.write(user + '\n')
    print(f'User {new_user} registered successfully.')
else:
    print('User already exists.')