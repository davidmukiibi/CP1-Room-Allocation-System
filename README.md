# CP1-Room-Allocation-System
[![DAVID MUKIIBI](https://img.shields.io/badge/DAVID%20MUKIIBI-Room%20Allocation%20System-green.svg)]()
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/d42abc6c229a4094b8db899d43c75b49/badge.svg)](https://www.quantifiedcode.com/app/project/d42abc6c229a4094b8db899d43c75b49)
[![Build Status](https://travis-ci.org/davidmukiibi/CP1-Room-Allocation-System.svg?branch=develop)](https://travis-ci.org/davidmukiibi/CP1-Room-Allocation-System)
[![Coverage Status](https://coveralls.io/repos/github/davidmukiibi/CP1-Room-Allocation-System/badge.svg?branch=master)](https://coveralls.io/github/davidmukiibi/CP1-Room-Allocation-System?branch=develop)

>Amity Room Allocation System.

    The application built here is one that assigns rooms to people in Amity.
    The people can be either Fellows or Staff.
    The rooms can either be living spaces or offices.

#1. Commands.

Command	| Argument | Example
--- | --- | ---
create_room	| l or o | create_room narnia o
add_person	| (first_name) (last_name) (person_type) (living_space_option)	| add_person david mukiibi FELLOW Y
display_people_in | (room_name) | display_people_in narnia
display_people_in_ls | | display_people_in_ls
display_people_in_offices | | display_people_in_offices
display_all_rooms | | display_all_rooms
print_allocations | [--o=filename] | print_allocations --o=allocated
print_unallocated | | print_unallocated
empty_rooms | | empty_rooms
load_people_from | (filename) | load_people_from sample_people_input.txt
load_rooms_from	| (filename) | load_rooms_from sample_rooms_input.txt
save_state | [--db=sqlite_database] | save_state --db=nairobi
load_state_from | (database_name) | load_state_from nairobi
delete_person | (person_name) | delete_person david
delete_room | (room_name) | delete_room narnia

#2. Installation and set up.

First, clone this repository to your computer. copy this link `git clone https://github.com/davidmukiibi/CP1-Amity-Room-Allocation-System.git` and paste it into your computer's command prompt or terminal.

Create a virtual environment or virtualenv on your machine and install the dependencies via `pip install -r requirements.txt` and activate it,
all this should be done in the terminal or command prompt of your computer.

Follow the link below to set up your virtual environment, activate it and install the application dependencies.
`http://sourabhbajaj.com/mac-setup/Python/virtualenv.html`

Traverse your way into the folder that you cloned the application into until you reach the folder that has `amityApp.py` file while in your terminal and run the command `python amityApp.py -i`.

#5. Usage

[![asciicast](https://asciinema.org/a/4pfe9vfo3lwzroah28r1o6083.png)](https://asciinema.org/a/4pfe9vfo3lwzroah28r1o6083)

Create rooms using the `create_room` command as shown above.
Then create and add a person or people using the `add_person` command as shown above one person at a time.
There after you can play around with other commands as shown above as you wish.

Credits

`David Mukiibi` in specific.

and

`Andela` at large.
