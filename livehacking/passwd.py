f = open('/etc/passwd')

users = []

for line in f:
    fields = line.split(':')

    user = {
        'name': fields[0],
        'password': fields[1],
        'uid': fields[2],
        'gid': fields[3],
        'description': fields[4],
        'home': fields[5],
        'shell': fields[6],
    }

    users.append(user)

print(users)
