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
