import math

class Stat:
    def __init__(self, grades = []):
        self.grade_list = []

        for grade in grades:
            self.grade_list.append(grade)

    def input_grades(self):
        """Prompts user to input grades"""
        numStuds = int(input('Enter total number of students: '))
        for _ in range(0, numStuds):
            grade = int(input('Enter numeric grade: '))
            self.grade_list.append(grade)
        return self.print_stats()

    def mean(self):
        """Calculates mean of grades in grade_list."""
        grade_total = 0
        for grade in self.grade_list:
            grade_total += grade
        # calculate the mean
        return grade_total / len(self.grade_list)

    def standard_dev(self, mean):
        """Calculates standard deviation of grades"""
        sum_of_sqrs = 0
        for grade in self.grade_list:
            sum_of_sqrs += (grade - mean) ** 2
        return math.sqrt(sum_of_sqrs / len(self.grade_list))

    def print_stats(self):
        """Prints out results of mean and standard deviation"""
        mean = self.mean()
        sd = self.standard_dev(mean)
        print('\n****** Grade Statistics ******')
        print("The grades's mean is:", mean)
        print('The population standard deviation of grades is: ', round(sd, 3))
        print('****** END ******')

Stat().input_grades()
