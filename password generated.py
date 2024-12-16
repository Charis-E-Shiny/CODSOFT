import random
import string

def generate_password(length):
    
    if length < 4:
        raise ValueError("Password length should be at least 4 to ensure complexity.")

    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation


    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

   
    all_characters = letters + digits + special_characters
    password += random.choices(all_characters, k=length - len(password))

    
    random.shuffle(password)

    return ''.join(password)


while True:
    try:
        length = int(input("Enter the desired length of your password (minimum 4): "))
        password = generate_password(length)
        print("\nYour generated password is:", password)
        flag=int(input("do you want to continue? (1/0): \n"))
        if flag==0:
            break
        elif flag==1:
            continue
        
        
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


