import random

print("Welcome to password ganarator")

letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o''p','q','r','s','t','u','j','k','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+','-','*','/']

x_letters = int(input("How many letters would you like in your password (Maximun = 5) : " ))
x_number = int(input("How many number would you like in your password (Maximun = 5) : " ))
x_symbols = int(input("How many symbols would you like in your password (Maximun = 5) : " ))

# ตรวจสอบว่าไม่เกิน 5

x_letters = min(x_letters, 5)
x_numbers = min(x_number, 5)
x_symbols = min(x_symbols, 5)

# สุ่มแต่ละส่วน
password_list = []
password_list += random.choices(letters, k=x_letters)
password_list += random.choices(numbers, k=x_numbers)
password_list += random.choices(symbols, k=x_symbols)

# สุ่มลำดับของรหัสผ่าน
random.shuffle(password_list)

random_letters = random.choice(letters)

# รวมเป็น string
password = ''.join(password_list)

print(f"Your password: {password}")

