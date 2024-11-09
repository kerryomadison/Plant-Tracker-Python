# INF360 - Programming in Python
# Kerry O'Connor
# Midterm Project

import sys
#logging required for final project. copied and pasted from text. 
import logging
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG, #lowest lever, set to debug
                    format='%(asctime)s -  %(levelname)s -  %(message)s')


#import data for the plants. moved plant data to a separate file
try:
    from PlantData import *
    logging.debug("Data imported successfully!")

except:
    logging.critical("PlantData.py file not found!")
    print("PlantData.py file not found!")
    sys.exit()

"""
Plant Care Tracker

This program serves as a tool for tracking plant care. It allows users to store and manage data
for their plants, including:
- Sunlight requirements
- Watering frequency and last watering date
- Fertilization schedule
- Growth logs like height and any new leaves
- General health like  condition and any infections or root rot a plant may develop.

The user can perform various actions through a menu, such as:
1. Checking if plants need watering or fertilization.
2. Conducting health checks on their plants.
3. Updating existing plant data or adding new plants to their collection.
4. Deleting plants from the inventory when necessary.

The core functionality is built around a dictionary that holds each plant's data and associated
helper functions. The 'choose plant' function acts as a sub-menu, enabling the user to select specific
plants for care-related actions.

This program aims to help plant owners maintain their plants' health and optimize their care routines.
"""


# basic function updating the user whether or not the plant needs to be watered.
# if days since watered is greater than frequency, prompt user to water.
# Then, if the calculated amount is less than watering
# frequency, do not water.
# ask if y they want to water or n and they will do later
# did this in two functions, one checking to see if it needs to be watered,
# then another function prompting the user whether or not they would like to water the plant today.

def needs_watering(plant):
    #check if the plant needs watering based on the watering frequency
    #calculate the difference between last watered and the frequency to see if needed
    if plant["Days Since Watered"]>=plant["Watering Frequency"]:
        return True
    return False

def prompt_water_plant(plant_name):
    #prompt the user whether or not they want to water the plant today
    #maybe if it is over a certain amount of days, give a warning
    #no warning implemented at this time. just give y/n option to water. 
    while True:
        
        user_input=input(f"{plant_name} needs watering. Do you want to water that today? (y/n): ")
        if user_input.lower()=="y":
            print(f"You watered {plant_name}.")
            return True
        elif user_input.lower()=="n": #if input is n then do this 
            print(f"You will be reminded to water {plant_name} tomorrow.")
            return False
        else: # this will catch any incorrect input
            print(f"Please enter a y or n. Any other characters are not proper input.")
    

def needs_fertilization(plant):
    #check if the plant needs fertilization, works similarly to watering function.
    if plant["Last Fertilized"] >= plant["Fertilizer Frequency"]:
        return True
    return False

def prompt_fertilize_plant(plant_name):
    #prompt user to fertilize plants. might also need fertilize freq for this since
    #plant dependent. should be similar to prompt water.
    #give y/n option to fertilize
    while True:
        user_input=input(f"{plant_name} needs fertilizing. Do you want to do that today? (y/n): ")
        #check if the user input is y, if it is, then they fertilized the plant.
        if user_input.lower()=="y":
            print(f"Great job! You fertilized {plant_name}.")
            return True
        elif user_input.lower()=="n":
            print(f"You will be reminded to fertilize {plant_name} tomorrow.")
            return False
        else: # this will catch any invalid input 
            print(f"Please enter a y or n. Any other characters are not proper input.")
            


#need a function returning the plant data and updating if the user wants to
# so maybe an update if user input is yes. do while loop?

def update_water_status(plant, watered):
    #if the plant was watered, reset days since watered to 0
    if watered:
        plant["Days Since Watered"]=0 #today is day 0, since user said y to watering today
    else:
        plant["Days Since Watered"]+=1 #increment by 1 day since it hasnt been watered (user says n)

def update_fertilize_status(plant, fertilized):
    #similar to update water status except for fertilizing.
    if fertilized:
        plant["Last Fertilized"] = 0  # Reset last fertilized days
    else:
        plant["Last Fertilized"]+= 1  # Increment days if not fertilized

#maybe make a function that informs the user if it is healthy or not using
#conditional logic on condition, infected and root rot. if infected/root rot
# are true then condition is moved to not healthy.

def check_health(plant):
    #check the health status of the plant, because infected or root rot may be true and condition is healthy.
    # in plants an infection or root rot means it is no longer healthy, good to know as a plant owner so you
    # can pay more attention to your plant! 
    if plant["Infected"]=="Yes" or plant["Root Rot"]=="Yes":
        plant["Condition"]="Not Healthy"
    else:
        plant["Condition"]="Healthy"
    print(f"Health check: {plant['Condition']}")
    
def choose_plant():
    plant_names = list(plants.keys())  # Get the names of the plants
    print("Choose a plant to update:")
    
    # Create a counter to display plant names
    count = 1
    for name in plant_names:
        print(f"{count}. {name}")
        count += 1  # Increment the counter

    # Get input for plant selection
    while True:  # Loop until valid input is received
        try:
            choice = int(input("Enter the number of the plant you want to update: ")) - 1
            
            # Return the selected plant name
            if 0 <= choice < len(plant_names):
                return plant_names[choice]
            else:
                print("Invalid choice. Please enter a number corresponding to a plant.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a plant.")

def update_plant_data(plant_name):
    plant = plants.get(plant_name)
    if plant is None:
        print(f"{plant_name} not found in the plant database.")
        return False 
    
    # Display current plant data
    print("\nCurrent Plant Data:")
    print(f"Name: {plant_name}")
    print(f"  Watering Frequency: {plant['Watering Frequency']}")
    print(f"  Days Since Watered: {plant['Days Since Watered']}")
    print(f"  Humidity: {plant['Humidity']}")
    print(f"  Sunlight: {plant['Sunlight']}")
    print(f"  Last Fertilized: {plant['Last Fertilized']}")
    print(f"  Fertilizer Frequency: {plant['Fertilizer Frequency']}")
    print(f"  Height: {plant['Height']}")
    print(f"  New Leaves: {plant['New Leaves']}")
    print(f"  Condition: {plant['Condition']}")
    print(f"  Infected: {plant['Infected']}")
    print(f"  Root Rot: {plant['Root Rot']}\n")

    while True: #print a sort of menu that you can choose from, specifying the type of input as well
        print("\nWhich data would you like to update?")
        print("1. Watering Frequency (integer)")
        print("2. Days Since Watered (integer)")
        print("3. Humidity (Yes/No)")
        print("4. Sunlight (Daily/Partial/None)")
        print("5. Last Fertilized (integer)")
        print("6. Fertilizer Frequency (integer)")
        print("7. Growth Log")
        print("8. Condition (Healthy/Not Healthy)")
        print("9. Infected (Yes/No)")
        print("10. Root Rot (Yes/No)")
        print("11. Exit")  # Option to exit

        choice = input("Enter the number of the field you want to update, or 11 to exit: ") #menu choice

        if choice == "11":  # Exit
            print("Exiting update process.")
            return True
        elif choice == "1":  # Watering Frequency
            while True:
                new_value = input("Enter new value for Watering Frequency (integer): ")
                if new_value.isdigit(): #if it is a digit, then change the value of watering frequency
                    plant["Watering Frequency"] = int(new_value)
                    print(f"Watering Frequency updated to {new_value}.")
                    break
                else: #if it isnt a digit, invalid input. 
                    print("Invalid input. Please enter an integer.")

        elif choice == "2":  # Days Since Watered
            while True:
                new_value = input("Enter new value for Days Since Watered (integer): ")
                if new_value.isdigit():
                    #if it is a digit, change the value of days since watered for that plant
                    plant["Days Since Watered"] = int(new_value)
                    print(f"Days Since Watered updated to {new_value}.")
                    break
                else:
                    #if it is not, then invalid input, days since water accepts only integers. 
                    print("Invalid input. Please enter an integer.")

        elif choice == "3":  # Humidity
            while True:
                new_value = input("Enter new value for Humidity (Yes/No): ").capitalize()
                if new_value in ["Yes", "No"]:
                    #if Yes or No (after capitalize) then change the value  
                    plant["Humidity"] = new_value
                    print(f"Humidity updated to {new_value}.")
                    break
                else: #if it isnt yes or no, then not good input. 
                    print("Invalid input. Please enter 'Yes' or 'No'.")

        elif choice == "4":  # Sunlight
            while True:
                new_value = input("Enter new value for Sunlight (Daily/Partial/None): ").capitalize()
                #use capitalize so that it matches daily partial and none as below
                if new_value in ["Daily", "Partial", "None"]:
                    #check to see if the input matches Daily, Partial or None.
                    plant["Sunlight"] = new_value
                    print(f"Sunlight updated to {new_value}.")
                    break
                else:
                    #if it doesnt match, then invalid
                    print("Invalid input. Please enter 'Daily', 'Partial', or 'None'.")

        elif choice == "5":  # Last Fertilized
            while True:
                new_value = input("Enter new value for Last Fertilized (integer): ")
                if new_value.isdigit():
                    #check if it is a digit
                    plant["Last Fertilized"] = int(new_value)
                    print(f"Last Fertilized updated to {new_value}.") 
                    break
                else:
                    #if it is not a digit, then it is incorrent input. last fertilized only takes in integers. 
                    print("Invalid input. Please enter an integer.")

        elif choice == "6":  # Fertilizer Frequency
            while True:
                new_value = input("Enter new value for Fertilizer Frequency (integer): ")
                if new_value.isdigit(): 
                    #check if input is a digit. 
                    plant["Fertilizer Frequency"] = int(new_value) 
                    print(f"Fertilizer Frequency updated to {new_value}.")
                    #inform of the change to user
                    break 
                else:
                    # if it isnt a digit, it isnt correct input, fertilizer frequency is an integer
                    print("Invalid input. Please enter an integer.")

        elif choice == "7":  # Growth Log
            while True:
                #growth log is twofold, asks first for height then for new leaves. 
                try: 
                    new_height = input("Please enter a new value for Height: ")
                    #try to cast new height to an integer (to check that the input is an integer)
                    plant["Height"] = int(new_height) 
                    break
                except ValueError:
                    #if it isnt an integer, output this
                    print("Invalid input. Please enter an integer for Height.")
            while True:
                try:
                    new_leaves = input("Please enter a new value for New Leaves: ")
                    #try to cast new leaves to an integer (to check that the input is an integer)
                    plant["New Leaves"] = int(new_leaves)
                    break
                except ValueError:
                    #if it isnt an integer, output this. 
                    print("Invalid input. Please enter an integer for New Leaves.")
            #output the height and leaves that were just updated to! 
            print(f"Growth Log updated to Height: {plant['Height']}, New Leaves: {plant['New Leaves']}.")

        elif choice == "8":  # Condition
            while True:
                new_value = input("Enter new value for Condition (Healthy/Not Healthy): ").capitalize()
                #check to see if the input is healthy or not healthy, if it is then update the condition. 
                if new_value in ["Healthy", "Not Healthy"]:
                    plant["Condition"] = new_value
                    print(f"Condition updated to {new_value}.")
                    break
                else:
                    #else, not valid input. 
                    print("Invalid input. Please enter 'Healthy' or 'Not Healthy'.")

        elif choice == "9":  # Infected
            while True:
                new_value = input("Enter new value for Infected (Yes/No): ").capitalize()
                #if the input is yes or no, update the value in infected. 
                if new_value in ["Yes", "No"]:
                    plant["Infected"] = new_value
                    print(f"Infected updated to {new_value}.")
                    break
                else:
                    #else let the user know invalid input
                    print("Invalid input. Please enter 'Yes' or 'No'.")

        elif choice == "10":  # Root Rot
            while True:
                new_value = input("Enter new value for Root Rot (Yes/No): ").capitalize()
                #if the input is yes or no, change the value of root rot to the input. 
                if new_value in ["Yes", "No"]:
                    plant["Root Rot"] = new_value
                    print(f"Root Rot updated to {new_value}.")
                    break
                else:
                    #else it is invalid input. 
                    print("Invalid input. Please enter 'Yes' or 'No'.")

        else:
            #else they chose a number outside 1-11. prompt user that it is wrong input. 
            print("Invalid choice. Please try again.")


# should probably have a function to add a plant, since sometimes you buy new plants!
# I should have a delete plant function in case a plant dies.
def add_plant():
    #ask for the plant name and check if it already exists in plants dictionary
    plant_name=input("Please enter the name of your new plant!: ").strip()
    #check for the inputted name, case sensitive. we dont want duplicate plants!
    if plant_name.lower() in (name.lower() for name in plants.keys()):
        print(f"A plant named {plant_name} already exists. Choose a different name!")
        return

    #ask for the watering frequency and validate input
    while True:
        try:
            watering_freq=int(input("Enter watering frequency (days in integer, e.g. 7): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer!")
            
    #ask for days since last watered and valildate input
    while True:
        try:
            days_since_water=int(input("Please enter the days since last watered.: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    while True:
        humidity=input("Does this plant need a higher humidity? (Yes/No): ").lower()
        #check and compare to lowercase yes and no.
        if humidity in ['yes', 'no']:
            humidity=humidity.capitalize()
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
        
        
    #ask for sunlight, remove extra whitespace to compare
    sunlight=input("Enter sunlight preference(e.g., 'Daily', 'Partial', or 'None':").strip()

    #get valid input for last fertilized integer
    while True:
        try:
            last_fertilized=int(input("Enter the number of days since last fertilized: "))
            break
        except ValueError:
            print("Invalid input, please enter an integer.")
    #get input for fertilizer frequency integer
    while True:
        try:
            fertilizer_frequency=int(input("Enter the fertilizer frequency in days: "))
            break
        except ValueError:
            print("Please enter a valild integer for fertilizer frequency.")
    #get input for height integer
    while True:
        try:
            new_height=int(input("Please enter the plants height in inches: "))
            new_leaves=int(input("Please enter the number of new leaves: "))
            break
        except ValueError:
            print("Please enter an integer (number) for the height.")

    #get input for condition, healthy or not healthy only
    while True:
        condition=input("Does this plant seem to be healthy (Yes/No): ").lower()
        if condition in ['yes', 'no']:
            condition=condition.capitalize()
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            
    #get input for infection status, yes or no
    while True:
        infection=input("Does this plant have any sort of infection (bugs, mold, etc)? (Yes/No): ").lower()
        if infection in ['yes', 'no']:
            infection=infection.capitalize()
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            
    #get input for root rot, yes or no
    while True:
        root_rot=input("Does this plant have rotting roots? (Yes/No): ").lower()
        if root_rot in ['yes', 'no']:
            root_rot=root_rot.capitalize()
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    # add the new plant to the dictionary
    plants[plant_name] = {
        "Watering Frequency": watering_freq,
        "Days Since Watered": days_since_water,
        "Humidity": humidity,
        "Sunlight": sunlight,
        "Last Fertilized": last_fertilized,
        "Fertilizer Frequency": fertilizer_frequency,
        "Height": new_height,
        "New Leaves": new_leaves,
        "Condition": condition,
        "Infected": infection,
        "Root Rot": root_rot
    }

    print(f"New plant '{plant_name}' added successfully!")
# delete plant function
def delete_plant():
    plant_name = choose_plant()  # Allow user to choose a plant from the list
    if plant_name in plants:
        del plants[plant_name]
        print(f"Plant '{plant_name}' has been deleted.")
    else:
        print(f"No plant found with the name '{plant_name}'.")


              
def main():
    while True:
        # Display the menu options
        print("\nPlant Care Menu:")
        print("1. Check watering needs")
        print("2. Check fertilization needs")
        print("3. Perform a health check")
        print("4. Add a new plant")
        print("5. Update plant data")
        print("6. Delete a plant")
        print("7. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-7): ")

        # Based on the choice, call the appropriate function
        if choice == "1":
            if not plants: # check if there are any plants to check
                print("No plants available to check watering needs. Please add a plant.")
                continue
            plant_name=choose_plant()
            if plant_name:
                prompt_water_plant(plant_name)
        elif choice == "2":
            if not plants: # check if there are any plants to check
                print("No plants available to check watering needs. Please add a plant.")
                continue
            plant_name=choose_plant()
            if plant_name:
                prompt_fertilize_plant(plant_name)
        elif choice == "3":
            plant_name=choose_plant()
            #get the plant dictionary from the plants dictionary
            plant=plants.get(plant_name)
            if plant:
                check_health(plant) #pass the entire plant dictionary
            else:
                print(f"Plant '{plant_name}' not found.")
        elif choice == "4":
            add_plant()
        elif choice == "5":
            if not plants:  # Check if there are any plants to update
                print("No plants available to update. Please add a plant first.")
                continue
            plant_name = choose_plant()
            if plant_name:  # Ensure a valid plant name was returned
                update_plant_data(plant_name)
        elif choice == "6":
            delete_plant()
                
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please select a number from 1 to 7.")

# Call the main function to run the menu
main()


