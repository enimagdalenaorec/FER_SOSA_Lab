import hashlib
import os

# ISPRAVAK 1: Credentials se čitaju iz environment varijabli
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# Rjecnik koji simulira bazu podataka korisnika
users = {}
def add_user(username, password):
    # ISPRAVAK 2: SHA-256 hashiranje umjesto MD5
    hashed = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed
    print(f"Korisnik {username} uspješno dodan.")

def check_password(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed:
        print("Lozinka točna.")
    else:
        print("Pogrešna lozinka.")

def main():
    print("Upiši administratorsko korisničko ime: ", end="")
    username = input()
    print("Upiši administratorsku lozinku: ", end="")
    password = input()
    if username != DB_USER or password != DB_PASSWORD:
        print("Pogrešni administratorski podaci. Izlaz.")
        return
    while True:
        print("\nDobrodošli u DataVault sustav upravljanja korisnicima")
        print("1. Dodaj korisnika")
        print("2. Provjeri lozinku")
        print("3. Izlaz")
        print("Odaberi opciju: ", end="")
        opcija = input()
        if opcija == "1":
            print("Upiši korisničko ime: ", end="")
            u = input()
            print("Upiši lozinku: ", end="")
            p = input()
            add_user(u, p)
        elif opcija == "2":
            print("Upiši korisničko ime: ", end="")
            u = input()
            print("Upiši lozinku: ", end="")
            p = input()
            check_password(u, p)
        elif opcija == "3":
            break
        else:
            print("Nepoznata opcija.")

if __name__ == "__main__":
    main()
