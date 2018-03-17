class DateTime():
    day = 0
    month = 0
    year = 0
    hour = 0
    minutes = 0
    seconds = 0

    def __init__(self, day, month, year, hour, minutes, seconds):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

# def make_student(name, age, major):
#     student = Student(name, age, major)
#     return student