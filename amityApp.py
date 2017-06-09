"""
Usage:
    Amity create_room <room_type> <room_names>...
    Amity add_person <first_name> <second_name> <person_type> <living_space_option>
    Amity print_unallocated
    Amity display_all_rooms
    Amity display_people_in_offices
    Amity display_people_in_ls
    Amity display_people_in <room_name>
    Amity load_people_from <filename>
    Amity load_rooms_from <filename>
    Amity delete_person <person_name>
    Amity delete_room <room_name>
    Amity load_state_from <database_name>
    Amity empty_rooms
    Amity (-i | --interactive)
    Amity (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
from docopt import docopt, DocoptExit
import cmd
import os
import sys
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init
from classes.amity import Amity
amity = Amity()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():

    print(__doc__)


class AmityRoomAllocation(cmd.Cmd):

    os.system("clear")

    init()

    font = Figlet(font = 'lean')

    print (Fore.GREEN + font.renderText('AMITY #TIA'))
    prompt = 'AmityRoomAllocation: '

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_names>..."""
        room_names = arg["<room_names>"]
        for name in room_names:
            r_type = arg["<room_type>"]
            print amity.create_room(name, r_type)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <second_name> <person_type> <living_space_option>"""
        first_name = arg["<first_name>"]
        second_name = arg["<second_name>"]
        person_type = arg["<person_type>"]
        lspace_option = arg["<living_space_option>"]
        print amity.add_person(first_name, second_name, person_type, lspace_option)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated"""
        print amity.print_unallocated_people()

    @docopt_cmd
    def do_display_all_rooms(self, arg):
        """Usage: display_all_rooms"""
        print amity.all_the_rooms_in_amity()

    @docopt_cmd
    def do_display_people_in_offices(self, arg):
        """Usage: display_people_in_offices"""
        print amity.all_the_people_in_all_offices()

    @docopt_cmd
    def do_display_people_in_ls(self, arg):
        """Usage: display_people_in_ls"""
        print amity.all_people_in_all_living_spaces()

    @docopt_cmd
    def do_display_people_in(self, arg):
        """Usage: display_people_in <room_name>"""
        room_name = arg["<room_name>"]
        print amity.display_people_in_room(room_name)

    @docopt_cmd
    def do_load_people_from(self, arg):
        """Usage: load_people_from <filename>"""
        filename = arg["<filename>"]
        print amity.load_people(filename)

    @docopt_cmd
    def do_load_rooms_from(self, arg):
        """Usage: load_rooms_from <filename>"""
        filename = arg["<filename>"]
        print amity.load_rooms(filename)

    @docopt_cmd
    def do_delete_person(self, arg):
        """Usage: delete_person <first_name> <second_name>"""
        first_name = arg["<first_name>"]
        second_name = arg["<second_name>"]
        person_name = '{} {}'.format(first_name, second_name)
        print amity.remove_person(person_name)

    @docopt_cmd
    def do_delete_room(self, arg):
        """Usage: delete_room <room_name>"""
        room_name = arg["<room_name>"]
        print amity.remove_room(room_name)

    @docopt_cmd
    def do_load_state_from(self, arg):
        """Usage: load_state_from <database_name>"""
        database_name = arg["<database_name>"]
        print amity.load_state(database_name)

    @docopt_cmd
    def do_empty_rooms(self, arg):
        """Usage: empty_rooms"""
        print amity.empty_rooms()

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename]"""
        filename = arg["--o"]
        if filename:
            print amity.print_allocations(filename)
        else:
            print amity.print_allocations()

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--o=database_name] """
        database_name = arg["--o"]
        if database_name:
            print amity.save_state(database_name)
        else:
            print amity.save_state()

    @docopt_cmd
    def do_reallocate(self, arg):
        """Usage: reallocate <first_name> <second_name> <new_room_name> """
        first_name = arg['<first_name>']
        second_name = arg['<second_name>']
        persons_name = '{} {}'.format(first_name, second_name)
        new_room_name = arg["<new_room_name>"]
        print amity.reallocate(first_name, second_name, new_room_name)

    def do_quit(self, arg):

        """Usage: quit
        
        """
    
        os.system('clear')
        print ('Bye Bye ===== Application Exiting')
        exit()




opt = docopt(__doc__,sys.argv[1:])
if opt["--interactive"]:
    AmityRoomAllocation().cmdloop()
    print(opt)    
