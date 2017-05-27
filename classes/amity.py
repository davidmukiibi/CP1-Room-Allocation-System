import sys
import os
sys.path.append(os.path.abspath("/Users/davidmukiibi/Desktop/Room-allocation/classes"))
from room import Room, Office, LivingSpace
from person import Staff, Fellow


class Amity(object):
    """the Amity class is the "command center" for my whole application, in other words,
    its where i have put all the methods"""

    def __init__(self):
        self.rooms = {'offices':{}, 'living_spaces':{}, 'unallocated':{'office': [],\
                                                                    'living_space': [],},}

    def create_room(self, room_name, room_type):
          """this method creates a room, either an office or a living space
          and adds it to the respectives dictionary values"""

          if isinstance(room_name, str) and isinstance(room_type, str):
              if room_type.lower() == 'o':
                  office = Office(room_name=room_name, room_type='o')
                  self.rooms['offices'].update({office.room_name: office.office_occupants})
                  print '{} office created successfully.'.format(office.room_name)

              elif room_type.lower() == 'l':
                  lspace = LivingSpace(room_name=room_name, room_type='l')
                  self.rooms['living_spaces'].update({lspace.room_name: lspace.living_space_occupants
                                                     })
                  print '{} living space created successfully.'.format(lspace.room_name)

              else:
                  print '{} wrong room type entered.'.format(room_type)

          else:
              print 'Either {} or {} is not a string, please check and try again!'.format(room_name,
                                                                                          room_type)


    def add_person(self, first_name, second_name, person_type, lspace_option='N'):
      """this method adds a person to the system and assigns them an office and/or
      living space if they are eligible and/or if they with to opt for it."""

      if (isinstance(first_name, str) and isinstance(second_name, str)
              and isinstance(person_type, str) and isinstance(lspace_option, str)):

          fellow = Fellow(first_name=first_name, second_name=second_name, person_type='FELLOW'
                          , lspace_option='N')
          staff = Staff(first_name=first_name, second_name=second_name, person_type='STAFF'
                        , lspace_option='N')
          if person_type.upper() == 'STAFF':
              if self.rooms['offices']:
                  for an_office, occupants in self.rooms['offices'].items():
                      if len(occupants) < 5:
                          self.rooms['offices'][an_office].append(staff)
                          # import ipdb; ipdb.set_trace()
                          return '{} was added successfully to office: {}.'.\
                                      format(staff.person_name, an_office)
                      else:
                          self.rooms['unallocated']['office'].append(staff)
              else:
                  return 'No offices avalaible at the moment, contact facilities dept!'

          elif person_type.upper() == 'FELLOW' and lspace_option.upper() == 'N':
              if self.rooms['offices']:
                  for an_office, occupants in self.rooms['offices'].items():
                      if len(occupants) < 5:
                          self.rooms['offices'][an_office].append(fellow)
                          return '{} was added successfully to office: {}'.\
                                      format(fellow.person_name, an_office)
                      else:
                          self.rooms['unallocated']['office'].append(fellow)
                          return 'All offices are fully occupied at the moment.'
              else:
                  self.rooms['unallocated']['office'].append(fellow)
                  return 'No offices available at the time.'

          elif person_type.upper() == 'FELLOW' and lspace_option.upper() == 'Y':
              if self.rooms['offices']:
                  for an_office, occupants in self.rooms['offices'].items():
                      if len(occupants) < 5:
                          self.rooms['offices'][an_office].append(fellow)
                          print 'Fellow has been added successfully to office: {}'.\
                                                                      format(an_office)
                          if self.rooms['living_spaces']:
                              for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                                  items():
                                  if len(ls_occupants) < 7:
                                      self.rooms['living_spaces'][a_living_space].append(fellow)
                                      return 'Fellow added successfully to living space: '\
                                                                  '{}'.format(a_living_space)
                                  else:
                                      self.rooms['unallocated']['living_space'].append(fellow)
                                      return 'no living spaces available right now!'
                          else:
                              return 'no living spaces at the moment'
                      else:
                          print 'No offices available at the time'
                          self.rooms['unallocated']['office'].append(fellow)
                          if self.rooms['living_spaces']:
                              for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                                  items():
                                  if len(ls_occupants) < 7:
                                      self.rooms['living_spaces'][a_living_space].append(fellow)
                                      return 'Fellow has been added successfully to living space'\
                                                                  '{}'.format(a_living_space)
                                  else:
                                      self.rooms['unallocated']['living_space'].append(fellow)
                                      return 'no living spaces available right now!'
              else:
                  self.rooms['unallocated']['offices'].append(fellow)
                  print 'No offices available at the time'
                  if self.rooms['living_spaces']:
                      for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                          items():
                          if len(ls_occupants) < 7:
                              self.rooms['living_spaces'][a_living_space].append(fellow)
                              return 'Fellow has been added successfully to living space'\
                                                          '{}'.format(a_living_space)
                          else:
                              self.rooms['unallocated']['living_space'].append(fellow)
                              return 'no living spaces available right now!'

          else:
              return 'you entered some wrong value, cross check and try again!'
      else:
          return 'please check the values you entered, all must be letters.'


    def print_unallocated_people(self):
          """Prints all the people without rooms to the screen"""

          all_people_without_rooms = []
          if self.rooms['unallocated']['office']:
              for person in self.rooms['unallocated']['office']:
                  all_people_without_rooms.append(person)

          if self.rooms['unallocated']['living_space']:
              for person in self.rooms['unallocated']['living_space']:
                  all_people_without_rooms.append(person)

          for numbering, people in enumerate(all_people_without_rooms, 1):
              print numbering, people.person_name

    def all_the_rooms_in_amity(self):
          """Prints all rooms there are in Amity"""

          all_rooms = []
          for office_name, office_occupants in self.rooms['offices'].items():
              all_rooms.append(office_name)

          for lspace_names, lspace_occupants in self.rooms['living_spaces'].items():
              all_rooms.append(lspace_names)

          return 'these are the rooms we have in amity: {}'.format(all_rooms)
