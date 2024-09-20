## Topic: Command Line Interface Project

## About
This project involves a Hotel Management system which performs operations like making reservations for guests by saving their details and assigning them rooms along with assigning inventory items to guests as well as assigning tasks to the hotel staff.

## Environment set-up
1. Create a local repository called Serena-Hotel-Management-system
2. Create a remote repository for Serena
3. Create the necessary files for this project(cli.py,database.py,hotel.db,main.py,models.py)
4. Install the necessary dependencies for this project by running pipenv install
5. Enter into the virtual environment by running pipenv shell

## Folder structure
1. cli.py: this file is responsible for giving functionality to the models of this project

2. database.py: this file is responsible for all the necessary configurations for this porject

3. hotel.db: this is the database for the project where all the hotel data is stored

This database has various tables in which data is going to be stored. They include:
1. guests: for storing personal details of guests
2. inventory: for storing details of inventory items
3. reservations: for storing reservation details
4. rooms: for storing room details
5. staff: for storing staff details
6. task: for storing task details

4. main.py: this file is responsible for running the program on the terminal

5. models.py: this file holds all the models for this project and creates tables for each model as well as establishes the relationships between the models.

6. Pipfile
7. Pipfile.lock
8. README.md


## Procedure
In this project various features are implemented: 

First you will start by putting the functionality for making a reservation where guests can reserve available rooms according to the room type and data is updated in the guests and reservations tables. 

Secondly you will put the functionality for listing available guests who have made a reservation. 

Thirdly, you will put a functionality for assigning inventory items to the current guests and list the current inventories and to whom they have each been assigned to. 

Another feature to be implemented is assigning tasks to the hotel staff and finally add a function to check out guests from the hotel which will remove their personal details and their reservation from the database.


## Running the program
Open up the terminal and run python main.py to activate the program thereby displaying the choices of what activity you want to conduct in the program. You should follow the loop involving the various prompts brought about by the choices you choose unless you want to exit which will terminate the program.

Follow this link to the video with detailed explanations of the codes and running the program on the terminal below:

https://screenapp.io/app/#/shared/h-dIifK5eL




## Conclusion
After finishing the project, exit the virtual environment by simply running the command exit and that's pretty much it.

