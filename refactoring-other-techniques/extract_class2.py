class Actor:
    def __init__(self, first_name, last_name, birth_year, email, movies=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


for i, value in enumerate(emails):
    actor = Actor(first_names[i], last_names[i], birth_year[i], emails[i], movies[i])
    print('Added ', actor.first_name)
    if actor.birth_year > 1985:
        print('Movies Played: ', end='')
        for m in actor.movies:
            print(m, end=', ')

        actor.send_hiring_email()
