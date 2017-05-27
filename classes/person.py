class Person(object):
    """Person class blueprint for the staff and fellow classes.
    It lays the foundation for the fellow and staff classes and the eventually for the
    their objects.
    """
    def __init__(self, first_name, second_name, person_type, lspace_option='N'):
        self.first_name = first_name
        self.second_name = second_name
        self.person_name = '%s %s' % (self.first_name, self.second_name)
        self.person_type = person_type
        self.lspace_option = lspace_option



class Staff(Person):
    """new staff blueprint but also inherits from the Person class"""

    def __init__(self, first_name, second_name, person_type='STAFF', lspace_option='N'):
        super(Staff, self).__init__(first_name, second_name, person_type,
                                    lspace_option='N')
        # self.name1 = first_name
        # self.name2 = second_name
        # self.type = person_type
        # self.option = lspace_option


class Fellow(Person):
    """New fellow blueprint but also inherits from the Person class
    person type(f) translates to fellow and (s) to staff.
    """

    def __init__(self, first_name, second_name, person_type='FELLOW', lspace_option='N'):
        super(Fellow, self).__init__(first_name, second_name, person_type,
                                     lspace_option='N')
        # self.name1 = first_name
        # self.name2 = second_name
        # self.type = person_type
        # self.option = lspace_option

