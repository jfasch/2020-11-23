f = open('/etc/passwd')


# read file into list of records
# ------------------------------
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

# do something with it
# --------------------
for user in users:
    print(f"name: {user['name']}, uid: {user['uid']}")
