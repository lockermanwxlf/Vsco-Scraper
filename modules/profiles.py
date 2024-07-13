import csv

class Profiles:
    def __iter__(self):
        self.profiles = csv.reader(open('profiles.csv', 'r'))
        next(self.profiles)
        return self.profiles
