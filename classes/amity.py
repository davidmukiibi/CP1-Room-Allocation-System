from room import Office, LivingSpace
from person import Staff, Fellow
from database_tables import Base, Room, Person, DatabaseCreator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
import os

# how to override defaults arguments.
class Amity(object):
    """the Amity class is the "command center" for my whole application, in other words,
    its where i have put all the methods"""
    def __init__(self):
        self.rooms = {'offices':{}, 'living_spaces':{}, 'unallocated':{'office': [],\
                                                                    'living_space': [],},}
    
    def create_room(self, room_type, room_name):
        """this method creates a room, either an office or a living space
        and adds it to the respectives dictionary values"""
        if room_name.isalpha() and room_type.isalpha():
            if room_type.lower() == 'o':
                office = Office(room_name=room_name, room_type='o')
                self.rooms['offices'].update({office.room_name: office.occupants})
                return '{} office created successfully.'.format(office.room_name)
            elif room_type.lower() == 'l':
                lspace = LivingSpace(room_name=room_name, room_type='l')
                self.rooms['living_spaces'].update({lspace.room_name: lspace.occupants
                                                })
                return '{} living space created successfully.'.format(lspace.room_name)
            else:
                return '{} wrong room type entered.'.format(room_type)
        else:
            return 'Either {} or {} is not a string, please check and try again!'.format(room_name,
                                                                                        room_type)

    def add_person(self, first_name, second_name, person_type, lspace_option):
        """this method adds a person to the system and assigns them an office and/or
        living space if they are eligible and/or if they with to opt for it."""
        if first_name.isalpha() and second_name.isalpha() and person_type.isalpha() and lspace_option.isalpha():
            fellow = Fellow(first_name, second_name, 'FELLOW', lspace_option)
            staff = Staff(first_name, second_name, 'STAFF', lspace_option)
            chosen_room = random.choice(self.rooms['offices'].keys())
            chosen_ls = random.choice(self.rooms['living_spaces'].keys())

            if (person_type.upper() == 'STAFF') and (staff.lspace_option.upper() == 'N'):
                if self.rooms['offices']: 
                    if len(self.rooms['offices'][chosen_room]) < 6:
                        self.rooms['offices'][chosen_room].append(staff)
                        staff.allocated_office = chosen_room
                        return '{} was added successfully to office: {}.'.\
                                    format(staff.person_name, chosen_room)
                    else:
                        self.rooms['unallocated']['office'].append(staff)
                else:
                    return 'No offices avalaible at the moment, contact facilities dept!'

            elif (person_type.upper() == 'FELLOW') and (lspace_option.upper() == 'N'):
                if self.rooms['offices']:
                    
                    if len(self.rooms['offices'][chosen_room]) < 6:
                        self.rooms['offices'][chosen_room].append(fellow)
                        fellow.allocated_office = chosen_room
                        return '{} was added successfully to office: {}'.\
                                    format(fellow.person_name, chosen_room)
                    else:
                        self.rooms['unallocated']['office'].append(fellow)
                        return 'All offices are fully occupied at the moment.'
                else:
                    self.rooms['unallocated']['office'].append(fellow)
                    return 'No offices available at the time.'

            elif (person_type.upper() == 'FELLOW') and (lspace_option.upper() == 'Y'):
                if self.rooms['offices']:
                    # for an_office, occupants in self.rooms['offices'].items():
                    if len(self.rooms['offices'][chosen_room]) < 6:
                        self.rooms['offices'][chosen_room].append(fellow)
                        fellow.allocated_office = chosen_room
                        print '{} has been added successfully to office: {}'.\
                                                            format(fellow.person_name, chosen_room)
                        if self.rooms['living_spaces']:
                            if len(self.rooms['living_spaces'][chosen_ls]) < 4:
                                self.rooms['living_spaces'][chosen_ls].append(fellow)
                                fellow.allocated_living_space = chosen_ls
                                return '{} added successfully to living space: '\
                                            '{}'.format(fellow.person_name, chosen_ls)
                            else:
                                self.rooms['unallocated']['living_space'].append(fellow)
                                return 'No living spaces available right now!'
                        else:
                            return 'No living spaces at the moment'
                    else:
                        print 'No offices available at the time'
                        self.rooms['unallocated']['office'].append(fellow)
                        if self.rooms['living_spaces']:
                            if len(self.rooms['living_spaces'][chosen_ls]) < 4:
                                self.rooms['living_spaces'][chosen_ls].append(fellow)
                                fellow.allocated_living_space = chosen_ls
                                return 'Fellow has been added successfully to living space'\
                                                            '{}'.format(chosen_ls)
                            else:
                                self.rooms['unallocated']['living_space'].append(fellow)
                                return 'No living spaces available right now!'
                else:
                    self.rooms['unallocated']['office'].append(fellow)
                    print 'No offices available at the time'
                    if self.rooms['living_spaces']:
                        # for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                        #                                     items():
                        if len(self.rooms['living_spaces'][chosen_ls]) < 4:
                            self.rooms['living_spaces'][chosen_ls].append(fellow)
                            fellow.allocated_living_space = chosen_ls
                            return 'Fellow has been added successfully to living space'\
                                                        '{}'.format(chosen_ls)
                        else:
                            self.rooms['unallocated']['living_space'].append(fellow)
                            return 'No living spaces available right now!'
            else:
                return 'Either the user is not eligible for a living space or You entered some wrong value, cross check and try again!'
        else:
            return 'Please check the values you entered, all must be alphabetic letters.'

    def print_unallocated_people(self):
        """Prints all the people without rooms to the screen""" 
        all_people_without_rooms = []
        if self.rooms['unallocated']['office']:
            for person in self.rooms['unallocated']['office']:
                all_people_without_rooms.append(person)

        if self.rooms['unallocated']['living_space']:
            for person in self.rooms['unallocated']['living_space']:
                all_people_without_rooms.append(person)
        
        if not all_people_without_rooms:
            return 'No one is unallocated at the moment.'
        else:
            for numbering, people in enumerate(all_people_without_rooms, 1):
                print numbering, people.person_name

    def all_the_rooms_in_amity(self):
        """Prints all rooms there are in Amity"""
        all_rooms = []
        for office_name, office_occupants in self.rooms['offices'].items():
            all_rooms.append(str(office_name))

        for lspace_names, lspace_occupants in self.rooms['living_spaces'].items():
            all_rooms.append(str(lspace_names))

        if all_rooms:
            return 'these are the rooms we have in amity: {}'.format(all_rooms)
        else:
            return 'Amity doesnt have rooms at the moment!'

    def all_the_people_in_all_offices(self):
        """prints out al the people in offices in amity"""
        all_people_in_offices = []
        for room_name, people_objects in self.rooms['offices'].items():
            for each_person_object in people_objects:
                all_people_in_offices.append(each_person_object.person_name)

        if all_people_in_offices:
            for numbering, people in enumerate(all_people_in_offices, 1):
                print numbering, people
        else:
            return 'No people in any office!'

    def all_people_in_all_living_spaces(self):
        """prints out al the people in living spaces in amity"""
        all_people_in_living_spaces = []
        for ls_name, fellow_objects in self.rooms['living_spaces'].items():
            for each_fellow_object in fellow_objects:
                all_people_in_living_spaces.append(each_fellow_object.person_name)

        if all_people_in_living_spaces:
            for numbering, people in enumerate(all_people_in_living_spaces, 1):
                print numbering, people
        else:
            return 'No people in any living space!'

    def display_people_in_room(self, room_name):
        """This displays people in a given room (office or living space) are displayed on screen"""
        people_in_room = []
        if room_name.isalpha():
            if room_name in self.rooms['living_spaces'].keys():
                if self.rooms['living_spaces'][room_name]:
                    for person in self.rooms['living_spaces'][room_name]:
                        people_in_room.append(person.person_name)
                    return people_in_room
                else:
                    print len(self.rooms['living_spaces'][room_name])
                    return '{} is empty.'.format(room_name)

            elif room_name in self.rooms['offices'].keys():
                if self.rooms['offices'][str(room_name)]:
                    for person in self.rooms['offices'][str(room_name)]:
                        people_in_room.append(person.person_name)
                    return people_in_room
                else:
                    return '{} is empty.'.format(room_name)
            else:
                return '{} does not exist in amity!'.format(room_name)
        else:
            return '{} is not a string!'.format(room_name)

    def load_people(self, filename):
        """ This method adds people to rooms from a txt file. """
        docpath = os.path.dirname(__file__)
        filepath = os.path.join(docpath, filename + ".txt")
        if not os.path.isfile(filepath):
            return "{} does not exist!".format(filepath)

        with open(filepath, 'r') as a_file:
            for each_line in a_file:
                words_list = each_line.split()
                first_name = words_list[0]
                second_name = words_list[1]
                person_type = words_list[2]

                if len(words_list) < 4:
                    lspace_option = "N"
                else:
                    lspace_option = words_list[3]
            self.add_person(first_name, second_name, person_type, lspace_option)
        return "People were loaded successfully!"

    def load_rooms(self, filename):
        """method loads rooms from a text file"""
        docpath = os.path.dirname(__file__)
        filepath = os.path.join(docpath, filename + ".txt")
        if not os.path.isfile(filepath):
            return "{} is not a valid file path or file doesnt exist or wrong file name.".\
                                                                                format(filepath)
        with open(filepath, 'r') as f:
            for each_line in f:
                words_list = each_line.split()
                room_name = words_list[0]
                room_type = words_list[1]
                self.create_room(room_name, room_type)
        return "Rooms were loaded successfully!"

    def remove_person(self, name):
        """removes a person from amity"""                
        if isinstance(name, str):
            for room in self.rooms['offices']:
                for room_name, occupants in self.rooms['offices'].items():
                    for each_occupant in occupants:
                        if name == each_occupant.person_name:
                            self.rooms['offices'][room_name].remove(each_occupant)
                            return '{} was removed successfully from {}.'.\
                                                        format(each_occupant.person_name, room_name)
                        else:
                            return '{} does not exist in amity!'.format(name)

            for room in self.rooms['living_spaces']:
                for room_name, occupants in self.rooms['living_spaces'].items():
                    for each_occupant in occupants:
                        if name == each_occupant.person_name:
                            self.rooms['living_spaces'][room_name].remove(each_occupant)
                            return '{} was removed successfully from {}.'.\
                                                        format(each_occupant.person_name, room_name)
                        else:
                            return '{} does not exist in amity!'.format(name)
        else:
            return '{} is not an alphabetical name!'.format(name)

    def remove_room(self, room_name):
        """Method deletes a room from amity."""
        if isinstance(room_name, str):
            if room_name in self.rooms['offices'].keys():
                if self.rooms['offices'][room_name]:
                    return '{} can not be deleted because it is not empty.'.format(room_name)
                else:
                    del self.rooms['offices'][room_name]
                    return '{} was removed successfully!'.format(room_name)
            elif room_name in self.rooms['living_spaces'].keys():
                if self.rooms['living_spaces'][room_name]:
                    return '{} can not be deleted because it is not empty.'.format(room_name)
                else:
                    del self.rooms['living_spaces'][room_name]
                    return '{} was removed successfully!'.format(room_name)
            else:
                return 'You are trying to delete room: {} that doesnt exist.'.format(room_name)
        else:
            return '{} entered is not a string.'.format(room_name)

    def print_allocations(self, filename=None):
        """Prints all rooms with occupants in amity plus there occupants"""
        if not filename:
            if (self.rooms['offices'].values()) or (self.rooms['living_spaces'].values()):
                for each_room, room_occupants in self.rooms['offices'].items():
                    if room_occupants:
                        print '{}'.format(each_room)
                        for numbering, people in enumerate(room_occupants, 1):
                            print numbering, people.person_name
                        return people.person_name
                    else:
                        print '{} is empty at the moment!'.format(each_room)
                for each_room, room_occupants in self.rooms['living_spaces'].items():
                    if room_occupants:
                        print '{}'.format(each_room)
                        for numbering, people in enumerate(room_occupants, 1):
                            print numbering, people.person_name
                        return people.person_name
                    else:
                        print '{} is empty at the moment!'.format(each_room)
            else:
                return 'No one is allocated in offices at the moment.'
        else:
            # Creating the file with the given filename, writing to it and saving it.
            print "Saving output data to file..."
            output = ''
            for office, occupants in self.rooms['offices'].items():
                output += '\n'
                output += office.upper()
                output += '\n'
                output += '-' * 20
                output += '\n'
                if occupants:
                    for occupant in occupants:
                        output += occupant.person_name.upper() + "\n"
                else:
                    output += '{} is empty.'.format(office.upper())
                    output += '\n\n'
            for lspace, ls_occupants in self.rooms['living_spaces'].items():
                output += '\n'
                output += lspace.upper()
                output += '\n'
                output += '--' * 5
                output += '\n'
                if ls_occupants:
                    for ls_occupant in ls_occupants:
                        output += ls_occupant.person_name.upper() + "\n\n" 
                else:
                    output += '{} is empty.'.format(lspace.upper())
                    output += '\n\n'
            text_file = open(filename + '.txt', 'w')
            text_file.write(output)
            text_file.close()
            return '{}.txt saved successfully to the computer.'.format(filename)

    def save_state(self, database_name=None):
        """ Method that saves all the data in the application into a given database """
        all_rooms_in_amity = self.rooms['offices'].keys() + self.rooms['living_spaces'].keys()
        all_people = []

        for room in self.rooms['offices'].keys():
            if self.rooms['offices'].values():
                capacity = len(self.rooms['offices'][room])
                for person in self.rooms['offices'][room]:
                    all_people.append(person)
        
        for another_room in self.rooms['living_spaces'].keys():
            if self.rooms['living_spaces'].values():
                capacity = len(self.rooms['living_spaces'][another_room])
                for persona in self.rooms['living_spaces'][another_room]:
                    all_people.append(persona)

        for unallocated_Room in self.rooms['unallocated'].keys():
            if self.rooms['unallocated'].values():
                capacity = len(self.rooms['unallocated'][unallocated_Room])
                for person in self.rooms['unallocated'][unallocated_Room]:
                    all_people.append(person)

        if not database_name:
            database = DatabaseCreator("amity")
        else:
            database = DatabaseCreator(database_name)
        Base.metadata.bind = database.engine
        database_session = database.session()
        database_session.query(Person).delete()
        database_session.query(Room).delete()

        for a_room in all_rooms_in_amity:
            if a_room in self.rooms['offices'].keys():
                saved_room = Room(
                    r_name=a_room,
                    r_type='o',
                    capacity=len(self.rooms['offices'][a_room]))
            else:
                saved_room = Room(
                    r_name=a_room,
                    r_type='l',
                    capacity=len(self.rooms['living_spaces'][a_room]))
            database_session.add(saved_room)

        for a_person in all_people:
            saved_person = Person(
                first_name=a_person.first_name,
                second_name=a_person.second_name,
                person_type=a_person.person_type,
                office_space=a_person.allocated_office,
                living_space=a_person.allocated_living_space,
                lspace_option=a_person.lspace_option)
            database_session.add(saved_person)
        database_session.commit()
        return "State Successfully Saved!"
  
    def load_state(self, database_name):
        """ Method that loads the saved application state from the database """
        engine = create_engine("sqlite:///" + database_name + ".db")
        session = sessionmaker()
        session.configure(bind=engine)
        new_session = session()
        try:
            people = new_session.query(Person).all()
            the_rooms = new_session.query(Room).all()
            for each_room in the_rooms:
                if each_room.r_type == "o":
                    # create new office
                    office = Office(each_room.r_name, each_room.r_type)
                    # add to list of offices
                    self.rooms['offices'].update({each_room.r_name: []})
                elif each_room.r_type == 'l':
                    lspace = LivingSpace(each_room.r_name, each_room.r_type)
                    self.rooms['living_spaces'].update({each_room.r_name: []})
                else:
                    print 'Invalid room type loaded -> {}'.format(each_room.r_type)
            for each_person in people:
                if each_person.person_type == "STAFF":
                    staff = Staff(each_person.first_name, each_person.second_name, each_person.person_type,
                                each_person.lspace_option)
                    if each_person.office_space != None:
                        self.rooms['offices'][each_person.office_space].append(staff)
                    else:
                        self.rooms['unallocated']['office'].append(staff)
                else:
                    fellow = Fellow(each_person.first_name, each_person.second_name, each_person.person_type, each_person.lspace_option)
                    if each_person.office_space != None:
                        self.rooms['offices'][each_person.office_space].append(fellow)
                    else:
                        self.rooms['unallocated']['office'].append(fellow)
                    if each_person.lspace_option == 'Y':
                        self.rooms['living_spaces'][each_person.living_space].append(fellow)
                    if (each_person.living_space == None) and (each_person.lspace_option == 'Y'):
                        self.rooms['unallocated']['living_space'].append(fellow)
            return "Data loaded successfully!"
        except:
            return "Sorry! You either havent specified a Database or the Database does not exist or is empty."

    def empty_rooms(self):
        """Lists all the empty rooms in amity"""
        all_of_the_rooms = []
        for office in self.rooms['offices'].keys():
            if not self.rooms['offices'][office]:
                all_of_the_rooms.append(str(office))
        for lspace in self.rooms['living_spaces'].keys():
            if not self.rooms['living_spaces'][lspace]:
                all_of_the_rooms.append(str(lspace))
        if all_of_the_rooms:
            return all_of_the_rooms
        else:
            return 'There no empty rooms in amity!'

    def reallocate(self, first_name, second_name, new_room_name):
        """method re-allocates a person from one room to another"""
        persons_name = '{} {}'.format(first_name, second_name)
        all_people = [] # This list is populated with all people in both offices and living spaces.

        for each_value in self.rooms['offices'].values(): # populating the above people list with people in offices.
            for each_person in each_value:
                all_people.append(each_person.person_name)

        for each_value in self.rooms['living_spaces'].values(): # populating the above people list with people in living spaces.
            for each_person in each_value:
                all_people.append(each_person.person_name)

        if persons_name in all_people:
            if new_room_name in self.rooms['offices'].keys():
                # checking if room exists in amity offices.
                for room, people_list in self.rooms['offices'].items():
                    if people_list:
                        for each_person in people_list:
                            if persons_name == each_person.person_name:
                                self.rooms['offices'][room].remove(each_person)
                                self.rooms['offices'][new_room_name].append(each_person)
                                return 'added person to {}'.format(new_room_name)
                            else:
                                self.rooms['offices'][new_room_name].append(each_person)
                                return 'added person to {}'.format(new_room_name)            
                    else:
                        self.rooms['offices'][new_room_name].append(each_person)
                        return 'added person to {}'.format(new_room_name)
            elif new_room_name in self.rooms['living_spaces'].keys():
                # checking if room exists in amity living spaces.
                for room, people_list in self.rooms['living_spaces'].items():
                    if people_list:
                        for each_person in people_list:
                            if persons_name == each_person.person_name:
                                if each_person.person_type == 'FELLOW':
                                    self.rooms['living_spaces'][room].remove(each_person)
                                    print 'removed person from room'
                                    self.rooms['living_spaces'][new_room_name].append(each_person)
                                    return 'added person to {}'.format(new_room_name)        
                                else:
                                    return '{} is not a fellow hence can not be reallocated to a living space.'.format(persons_name)
                            else:
                               self.rooms['living_spaces'][new_room_name].append(each_person)
                               return 'added person to {}'.format(new_room_name)
                    else:
                        if each_person.person_type == 'FELLOW':
                            # Removing person from room they exist.
                            self.rooms['living_spaces'][room].remove(each_person)
                            print 'removed person from room'
                            # Adding the person to the new room.
                            self.rooms['living_spaces'][new_room_name].append(each_person)
                            return 'added person to {}'.format(new_room_name)
                        else:
                            return '{} is not a fellow hence can not be reallocated to a living space.'.format(persons_name)
            else:
                return '{} does not exist in amity.'.format(new_room_name)
        else:
            return '{} does not exist in amity.'.format(persons_name)

