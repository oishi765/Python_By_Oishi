print("Welcome to Login & Roll System")

users = {
    "admin": {"pass": "1234", "role": "admin"},
    "rahim": {"pass": "1111", "role": "user"}
}

u = input("Username: ")
p = input("Password: ")

if u in users and users[u]["pass"] == p:
    print("Login success")
    print("Role:", users[u]["role"])
else:
    print("Invalid login")
