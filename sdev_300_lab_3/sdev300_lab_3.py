"""
Allow the user to Alphabetically Display all US States.
Search for a state and display information about it.
Provide a bar graph of the top 5 populated states.
Update the population for a specific state.
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# create dictionary
state_info = [
    {"State": "Alabama", "Capital": "Montgomery", "State Flower": "Camellia", "Population": 4887680},
    {"State": "Alaska", "Capital": "Juneau", "State Flower": "Forget Me Not", "Population": 735139},
    {"State": "Arizona", "Capital": "Phoenix", "State Flower": "Saguaro Cactus Blossom", "Population": 7158020},
    {"State": "Arkansas", "Capital": "Little Rock", "State Flower": "Apple Blossom", "Population": 3009730},
    {"State": "California", "Capital": "Sacramento", "State Flower": "California Poppy", "Population": 39461600},
    {"State": "Colorado", "Capital": "Denver", "State Flower": "White and Lavender Columbine", "Population": 5691290},
    {"State": "Connecticut", "Capital": "Hartford", "State Flower": "Mountain Laurel", "Population": 3571520},
    {"State": "Delaware", "Capital": "Dover", "State Flower": "Peach Blossom", "Population": 965479},
    {"State": "Florida", "Capital": "Tallahassee", "State Flower": "Orange Blossom", "Population": 21244300},
    {"State": "Georgia", "Capital": "Atlanta", "State Flower": "Cherokee Rose", "Population": 10511100},
    {"State": "Hawaii", "Capital": "Honolulu", "State Flower": "Hibiscus", "Population": 1420590},
    {"State": "Idaho", "Capital": "Boise", "State Flower": "Syringa", "Population": 1750540},
    {"State": "Illinois", "Capital": "Springfield", "State Flower": "Purple Violet", "Population": 12723100},
    {"State": "Indiana", "Capital": "Indianapolis", "State Flower": "Peony", "Population": 6695500},
    {"State": "Iowa", "Capital": "Des Moines", "State Flower": "Wild Prairie Rose", "Population": 3148620},
    {"State": "Kansas", "Capital": "Topeka", "State Flower": "Sunflower", "Population": 2911360},
    {"State": "Kentucky", "Capital": "Frankfort", "State Flower": "Goldenrod", "Population": 4461150},
    {"State": "Louisiana", "Capital": "Baton Rouge", "State Flower": "Magnolia", "Population": 4659690},
    {"State": "Maine", "Capital": "Augusta", "State Flower": "White Pine Cone and Tassel", "Population": 1339060},
    {"State": "Maryland", "Capital": "Annapolis", "State Flower": "Black-Eyed Susan", "Population": 6035800},
    {"State": "Massachusetts", "Capital": "Boston", "State Flower": "Mayflower", "Population": 6882640},
    {"State": "Michigan", "Capital": "Lansing", "State Flower": "Apple Blossom", "Population": 9984070},
    {"State": "Minnesota", "Capital": "Saint Paul", "State Flower": "Pink and White Lady Slipper",
     "Population": 5606250},
    {"State": "Mississippi", "Capital": "Jackson", "State Flower": "Magnolia", "Population": 2981020},
    {"State": "Missouri", "Capital": "Jefferson City", "State Flower": "White Hawthorn Blossom", "Population": 6121620},
    {"State": "Montana", "Capital": "Helena", "State Flower": "Bitterroot", "Population": 1060660},
    {"State": "Nebraska", "Capital": "Lincoln", "State Flower": "Goldenrod", "Population": 1925610},
    {"State": "Nevada", "Capital": "Carson City", "State Flower": "Sagebrush", "Population": 3027340},
    {"State": "New Hampshire", "Capital": "Concord", "State Flower": "Purple Lilac", "Population": 1353460},
    {"State": "New Jersey", "Capital": "Trenton", "State Flower": "Violet", "Population": 8886020},
    {"State": "New Mexico", "Capital": "Santa Fe", "State Flower": "Yucca Flower", "Population": 2092740},
    {"State": "New York", "Capital": "Albany", "State Flower": "Rose", "Population": 19530400},
    {"State": "North Carolina", "Capital": "Raleigh", "State Flower": "Dogwood", "Population": 10381600},
    {"State": "North Dakota", "Capital": "Bismarck", "State Flower": "Wild Prairie Rose", "Population": 758080},
    {"State": "Ohio", "Capital": "Columbus", "State Flower": "Red Carnation", "Population": 11676300},
    {"State": "Oklahoma", "Capital": "Oklahoma City", "State Flower": "Mistletoe", "Population": 3940240},
    {"State": "Oregon", "Capital": "Salem", "State Flower": "Oregon Grape", "Population": 4181890},
    {"State": "Pennsylvania", "Capital": "Harrisburg", "State Flower": "Mountain Laurel", "Population": 12800900},
    {"State": "Rhode Island", "Capital": "Providence", "State Flower": "Violet", "Population": 1058290},
    {"State": "South Carolina", "Capital": "Columbia", "State Flower": "Yellow Jessamine", "Population": 5084160},
    {"State": "South Dakota", "Capital": "Pierre", "State Flower": "Pasque Flower", "Population": 878698},
    {"State": "Tennessee", "Capital": "Nashville", "State Flower": "Iris", "Population": 6771630},
    {"State": "Texas", "Capital": "Austin", "State Flower": "Bluebonnet", "Population": 28628700},
    {"State": "Utah", "Capital": "Salt Lake City", "State Flower": "Sego Lily", "Population": 3153550},
    {"State": "Vermont", "Capital": "Montpelier", "State Flower": "Red Clover", "Population": 624358},
    {"State": "Virginia", "Capital": "Richmond", "State Flower": "Dogwood", "Population": 8501290},
    {"State": "Washington", "Capital": "Olympia", "State Flower": "Pink Rhododendron", "Population": 7523870},
    {"State": "West Virginia", "Capital": "Charleston", "State Flower": "Rhododendron", "Population": 1804290},
    {"State": "Wisconsin", "Capital": "Madison", "State Flower": "Wood Violet", "Population": 5807410},
    {"State": "Wyoming", "Capital": "Cheyenne", "State Flower": "Indian Paintbrush", "Population": 577601}
]


def menu():
    """Function to print out the user menu"""
    print("Please enter a number, 1 through 5.")
    print("1: Display all U.S. States in Alphabetical order along"
          " with the Capital, State Population, and Flower")
    print("2: Search for a specific state and display the appropriate Capital "
          "name, State Population, and an image of the associated State Flower.")
    print("3: Display a Bar graph of the top 5 populated States showing their overall population.")
    print("4: Update the overall state population for a specific state.")
    print("5: Exit the program")


def display_state_info():
    """Display all info about the states (name, capital, flower, and population"""
    # use for loop to loop through dictionary values
    for state in state_info:
        for i in state:
            print(i + ":", state[i])
        # split each state with a line
        print("---------------------------------------")


def search_state():
    """Search for a state, output the information, and display
     a picture of the state flower"""
    state_searched = input("Please enter the state you would like to search?"
                           " Please enter the full state name:").lower()
    continue_loop = 1  # marker for when to end loop
    while continue_loop == 1:
        # use for loop to loop through dictionary values
        for state in state_info:
            # print out specific state searched
            if state["State"].lower() == state_searched:
                for i in state:
                    print(i + ":", state[i])
                print()

                # Find the file "flower pictures" and print pic for specific state
                picture = mpimg.imread(f'flower pictures\\{state_searched}.jpg')
                plt.suptitle("State Flower of " + state_searched)
                plt.imshow(picture)
                plt.show()
                continue_loop = 2  # end while loop
                break
        else:
            # Re-run if user does not enter a valid state
            state_searched = input("Please try again. You must type "
                                   "the full state name.").lower()


def bar_graph():
    """Function to print a bar graph showing the top 5 most populated states"""
    sort_states = sorted(state_info, key=lambda i: i['Population'], reverse=True)

    sorted_states = []  # list for the top 5 states
    sorted_populations = []  # list for the top 5 populations

    for state in sort_states[:5]:
        sorted_states.append(state["State"])
        sorted_populations.append(state["Population"])

    # Plot the graph and create labels
    plt.bar(sorted_states, sorted_populations)
    plt.title('Top 5 Populated States in US')
    plt.xlabel('States')
    plt.ylabel('Population')

    # Add number lables above bars on the graph
    for index, value in enumerate(sorted_populations):
        plt.text(index - .4, value, str(value))

    plt.show()


def update_population():
    """Function to as the user what the new population
     size of a specific state is and update it"""

    update_state_pop = input("Please enter the state you would like to update"
                             " the population for:").lower()
    continue_loop = 1  # marker for when to end loop
    while continue_loop == 1:
        for state in state_info:
            # If the user entered state is found, end the loop
            if state["State"].lower() == update_state_pop:
                continue_loop = 2  # End while loop
                break
        else:
            # Re-run if user does not enter a valid state
            update_state_pop = input("Please try again. You must type"
                                     " the full state name.").lower()

    population = input("Please enter the new population amount:")

    while True:
        # Check if user entered population is an integer
        if population.isdigit():
            population = int(population)
            break
        else:
            # If user entry is not an integer, re-run
            population = input("Please try again. The population size must be an integer.")

    # Update population based on user entered state
    for state in state_info:
        if state["State"].lower() == update_state_pop:
            state["Population"] = population
            break


while True:
    menu()
    choice = input(">>> ")

    if choice == "1":
        display_state_info()

    elif choice == "2":
        search_state()

    elif choice == "3":
        bar_graph()

    elif choice == "4":
        update_population()

    elif choice == "5":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice. Please try again.\n")
