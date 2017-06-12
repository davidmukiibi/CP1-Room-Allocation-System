class Person(object):
    """Person class blueprint for the staff and fellow classes.
    It lays the foundation for the fellow and staff classes and the eventually for the
    their objects."""
    def __init__(self, first_name, second_name, person_type):
        self.first_name = first_name
        self.second_name = second_name
        self.person_name = '{} {}'.format(self.first_name, self.second_name)
        self.person_type = person_type
        self.lspace_option = 'N'
        self.allocated_office = None
        self.allocated_living_space = None

class Staff(Person):
    """new staff blueprint but also inherits from the Person class"""

    def __init__(self, first_name, second_name, person_type='STAFF'):
        super(Staff, self).__init__(first_name, second_name, person_type)


class Fellow(Person):
    """New fellow blueprint but also inherits from the Person class."""

    def __init__(self, first_name, second_name, person_type='FELLOW'):
        super(Fellow, self).__init__(first_name, second_name, person_type)
