def save_into_db(info):
    print("saved into database")

def user_prompts():
    username = input('Please enter your username: ')
    save_into_db(username)

    user_age = int(input('Please enter your birth year: '))
    age = 2020 - user_age
    print("You are ", age, " years old.")

user_prompts()
