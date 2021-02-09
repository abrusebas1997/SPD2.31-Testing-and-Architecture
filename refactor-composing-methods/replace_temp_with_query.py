
class Employer:
    def __init__(self, name):
        self.name = name
        self.top = []

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students, employers) -> None:
        self.students = students
        self.recruiters = employers

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passing = self.get_passing_students()

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passing:
            print(s.name)
            s.send_congrat_email()
        print('****************************')

        top_ten = self.get_top_10(passing)

        self.send_referral(self.recruiters, top_ten)

    def get_passing_students(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students

    def get_top_10(self, passing):
         # Find the top 10% of them and send their contact to the top employers
        passing.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passing))
        return passing[index:]

    def send_referral(self, employers, referrals):
        for e in employers:
            e.send(referrals)

top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students, top_employers)
school.process_graduation()
