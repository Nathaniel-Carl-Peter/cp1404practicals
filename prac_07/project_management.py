# from operator import attrgetter
from projects import Projects
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project  " \
       "\n- (U)pdate project \n- (Q)uit"


def main():
    """Main project management client program"""
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            print('Load')
            projects = load_file(FILENAME)
        elif choice == 'D':
            print('Display')
            for i, project in enumerate(projects):
                print(f'{project}')
        elif choice == 'F':
            print('Filter by date')
        elif choice == 'A':
            print('Add')
            name = input("Name: ").title()
            start_date = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            # print(f"That day is/was {date.strftime('%A')}")
            # print(date.strftime("%d/%m/%Y"))
            priority = int(input(">>> "))
            cost = float(input(">>> "))
            completion = int(input('>>> '))
            project_added = Projects(name, start_date, priority, cost, completion)
            projects.append(project_added)
        elif choice == 'U':
            print('Update')
        else:
            print('Invalid input')
        print(MENU)
        choice = input('>>> ').upper()
    print()
    print('Thank you for using custom-built project management software.')


def load_file(filename):
    """Load project txt"""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip the header line
        for line in in_file:
            parts = line.strip().rstrip()
            # print(parts)
            print(repr(parts))

    # pass


if __name__ == '__main__':
    main()
    # load_file(FILENAME)
"""
import datetime

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))
"""

"""
Welcome to Pythonic Project Management
Loaded 5 projects from projects.txt
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> d
Incomplete projects: 
  Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
  Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
  Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
  Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
Completed projects: 
  Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> u
0 Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
1 Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
2 Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
3 Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
4 Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
Project choice: 3
Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
New Percentage: 20
New Priority: 
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> a
Let's add a new project
Name: Practical 7
Start date (dd/mm/yy): 1/11/2022
Priority: 1
Cost estimate: $0
Percent complete: 32
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> f
Show projects that start after date (dd/mm/yy): 20/7/2022
Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> u
0 Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
1 Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
2 Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
3 Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
4 Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
5 Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
Project choice: 0
Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
New Percentage: 100
New Priority: 3
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> d
Incomplete projects: 
  Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
  Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
  Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
  Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
Completed projects: 
  Build Car Park, start: 12/09/2021, priority 3, estimate: $600000.00, completion: 100%
  Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> q
Would you like to save to projects.txt? no, I think not.
Thank you for using custom-built project management software.
"""

"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
