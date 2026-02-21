# "Anish", "Anish23@gmail.com", 2004-12-2, 45000

import random
names = ["Anish", "Anisha", "Tanisha", "Anjali", "Bhavna", "Shruti", "Sushant", "Anshul", "Anant", "Abhay", "Abhishek", "Akshay", "Gaurav", "Gautam", "Yash", "Birender", "Rohit", "Rohail", "Ankit", "Abhinav",  "Rahul", "Priya", "Aman", "Sneha", "Karan", "Neha", "Vikram"]
surnames = ["Sharma", "Verma", "Kapoor", "Mehta", "Singh", "Nair", "Patil", "Gupta", "Iyer", "Reddy", "Mishra", "Malhotra", "Joshi", "Choudhary", "Bansal", "Yadav", "Thakur", "Khan", "Agarwal", "Sinha", "Tripathi", "Desai", "Chauhan", "Kulkarni", "Oberoi", "Saxena", "Pillai"]

# number of data reqiured------------
try:
    num = int(input("Enter the number of record required : "))
except Exception as error:
    print(f"There is an error present at {error}")

def data_Base():
    # for random Names----------
    name = random.choice(names)
    surname = random.choice(surnames)

    # for random Emails---------
    number = random.randint(100,999)
    email = f"{name}{surname}{number}@gmail.com"

    # for random Date of birth--------
    year = random.randint(1950, 2006)
    month = random.randint(1, 12)
    day = random.randint(1, 31) 
    date_of_birth = f"{year}-{month}-{day}"
    
    # for random Salary----------
    salary = random.randint(30000, 80000)

    # for data --------
    return f'"{name}", "{email}", {date_of_birth}, {salary}'

# insert the Data to file
data = "Datarecord.txt"
with open(data,"a") as f:
    for i in range(num):
        record = data_Base()
        f.write(record + "\n")