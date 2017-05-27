class Amity(object):
    """the Amity class is the "command center" for my whole application, in other words,
    its where i have put all the methods"""

    def __init__(self):
        self.rooms = {'offices':{}, 'living_spaces':{}, 'unallocated':{'office': [],\
                                                                    'living_space': [],},}
