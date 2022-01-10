import requests
import json

url = 'https://ct-mock-tech-assessment.herokuapp.com/'


class Partners:
    def __init__(self, firstName=None, lastName=None, availableDates=None, email=None, country=None):
        self.firstName = firstName
        self.lastName = lastName
        if availableDates is None:
            self.availableDates = []
        if email is None:
            self.email = []
        if self.country is None:
            self.country = []

    def from_dict(self, data):
        field = []
        for i in field in ['firstName', 'lastName', 'availableDates', 'email', 'country']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return f'<partner>: {self.firstName}'


class conference:
    pass

    class Partners:

    def instructions(cls):
        print("""Welcome
        Type 'view" to view list'
        Type 'end' to end.""")

    @classmethod
    def add(cls, availableDates):

        if cls._list:
            for p in cls._list:
                if availableDates == p.availableDates:
                    input('Not available, please try again.')
        try:

            print('Checking')
            r = requests.get(
                f'https: // ct-mock-tech-assessment.herokuapp.com /Partners/{availableDates}')
        except:
            input("Error, please try again.")

        pass
        p = Partners()
        data_dict = {
            'firstName'r['firstName']: ,
            'lastName'r['lastName']: ,
            'availableDates': [a[""] for i in r['availableDates']],
            'email'r['email']: ,
            'country'r['country']: ,
        }
        p.from_dict(data_dict)
        cls._list.append(p)

    def run(cls):
        done = False

        while not done:

            cls.instructions()

            conference_choice = input(
                " Type 'view' to view or type 'end'")
            if conference_choice == 'view':
                cls.view()
            elif conference_choice == 'end':
                done = True
                input("Type 'ENTER' to continue")
            else:
                cls.add(conference_choice)
