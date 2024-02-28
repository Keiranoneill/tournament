import tkinter as tk               ## I feel bad 
from tkinter import messagebox

# Dictionary to store team participants for each game
individuals_games = {}
teams_games = {}

def join_tournament():
    individual = var.get()
    name = entry_name.get()
    game_name = game_selector.get()

    if individual == 1:
        if game_name:
            individuals_game = individuals_games.setdefault(game_name, [])
            individuals_game.append(name)
            remove_individual(game_name, name)
        else:
            messagebox.showerror("Error", "Please select a game.")
    else:
        if game_name:
            teams_game = teams_games.setdefault(game_name, [])
            teams_game.append(name)
            add_team(game_name)
        else:
            messagebox.showerror("Error", "Please select a game.")

def remove_individual(game_name, name):
    individuals_game = individuals_games.get(game_name, [])
    if name in individuals_game:
        individuals_game.remove(name)
        update_individual_list(game_name)
        messagebox.showinfo("Success", f"You, {name}, have been removed from the individual game {game_name}.")
    else:
        messagebox.showerror("Error", f"{name} not found in the individual game {game_name}.")

def add_team(game_name):
    team_name = entry_name.get()
    teams_game = teams_games.get(game_name, [])
    teams_game.append(team_name)
    update_team_list(game_name)
    messagebox.showinfo("Success", f"Team {team_name} has been added to the team game {game_name}.")

def update_individual_list(game_name):
    individuals_game = individuals_games.get(game_name, [])
    individuals_list.set(f"Remaining individuals in {game_name}: " + ", ".join(individuals_game))

def update_team_list(game_name):
    teams_game = teams_games.get(game_name, [])
    team_list.set(f"Remaining teams in {game_name}: " + ", ".join(teams_game))

def start_game():
    # Add your logic to start the game here
    messagebox.showinfo("Game Started", "The tournament has started!")

# Tkinter GUI
root = tk.Tk()
root.title("Tournament Scoring System")

var = tk.IntVar()

label = tk.Label(root, text="Hello Participants, welcome to the competition")
label.pack()

radio_individual = tk.Radiobutton(root, text="Join as an individual", variable=var, value=1)
radio_individual.pack()

radio_team = tk.Radiobutton(root, text="Join as a team", variable=var, value=0)
radio_team.pack()

label_name = tk.Label(root, text="Enter your name:")
label_name.pack()

# Dropdown menu to select the game for participants
game_selector = tk.StringVar()
game_selector.set("Game 1")  # Set the default game
game_menu = tk.OptionMenu(root, game_selector, "Game 1", "Game 2", "Game 3", "Game 4" "Game 5 ")  # Add more games as needed
game_menu.pack()

entry_name = tk.Entry(root) 
entry_name.pack()

button_join = tk.Button(root, text="Join Tournament", command=join_tournament)
button_join.pack()

individuals_list = tk.StringVar()
label_individuals = tk.Label(root, textvariable=individuals_list)
label_individuals.pack()

team_list = tk.StringVar()
label_teams = tk.Label(root, textvariable=team_list)
label_teams.pack()

# Button to start the game
button_start_game = tk.Button(root, text="Start Game", command=start_game)
button_start_game.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Dictionary to store team participants for each game
individuals_games = {}
teams_games = {}

def join_tournament():
    individual = var.get()
    name = entry_name.get()
    game_name = game_selector.get()

    if individual == 1:
        if game_name:
            individuals_game = individuals_games.setdefault(game_name, [])
            individuals_game.append(name)
            remove_individual(game_name, name)
            print(f"Individual participant {name} joined {game_name}")
        else:
            messagebox.showerror("Error", "Please select a game.")
    else:
        if game_name:
            teams_game = teams_games.setdefault(game_name, [])
            teams_game.append(name)
            add_team(game_name)
            print(f"Team {name} joined {game_name}")
        else:
            messagebox.showerror("Error", "Please select a game.")

def remove_individual(game_name, name):
    individuals_game = individuals_games.get(game_name, [])
    if name in individuals_game:
        individuals_game.remove(name)
        update_individual_list(game_name)
        messagebox.showinfo("Success", f"You, {name}, have been removed from the individual game {game_name}.")
    else:
        messagebox.showerror("Error", f"{name} not found in the individual game {game_name}.")

def add_team(game_name):
    team_name = entry_name.get()
    teams_game = teams_games.get(game_name, [])
    teams_game.append(team_name)
    update_team_list(game_name)
    messagebox.showinfo("Success", f"Team {team_name} has been added to the team game {game_name}.")

def update_individual_list(game_name):
    individuals_game = individuals_games.get(game_name, [])
    individuals_list.set(f"Remaining individuals in {game_name}: " + ", ".join(individuals_game))

def update_team_list(game_name):
    teams_game = teams_games.get(game_name, [])
    team_list.set(f"Remaining teams in {game_name}: " + ", ".join(teams_game))

def start_game():
    # Add your logic to start the game here
    print("Game Started!")
    print("Individuals:")
    for game_name, participants in individuals_games.items():
        print(f"{game_name}: {', '.join(participants)}")
    
    print("\nTeams:")
    for game_name, teams in teams_games.items():
        print(f"{game_name}: {', '.join(teams)}")
    messagebox.showinfo("Game Started", "The tournament has started!")

# Tkinter GUI
root = tk.Tk()
root.title("Tournament Scoring System")

var = tk.IntVar()

label = tk.Label(root, text="Hello Participants, welcome to the competition")
label.pack()

radio_individual = tk.Radiobutton(root, text="Join as an individual", variable=var, value=1)
radio_individual.pack()

radio_team = tk.Radiobutton(root, text="Join as a team", variable=var, value=0)
radio_team.pack()

label_name = tk.Label(root, text="Enter your name:")
label_name.pack()

# Dropdown menu to select the game for participants
game_selector = tk.StringVar()
game_selector.set("Game 1")  # Set the default game
game_menu = tk.OptionMenu(root, game_selector, "Game 1", "Game 2", "Game 3", "Game 4" "Game 5")  # Add more games as needed
game_menu.pack()

entry_name = tk.Entry(root) 
entry_name.pack()

button_join = tk.Button(root, text="Join Tournament", command=join_tournament)
button_join.pack()

individuals_list = tk.StringVar()
label_individuals = tk.Label(root, textvariable=individuals_list)
label_individuals.pack()

team_list = tk.StringVar()
label_teams = tk.Label(root, textvariable=team_list)
label_teams.pack()

# Button to start the game
button_start_game = tk.Button(root, text="Start Game", command=start_game)
button_start_game.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Dictionary to store team participants for each game
individuals_games = {}
teams_games = {}

def join_tournament():
    individual = var.get()
    name = entry_name.get()
    game_name = game_selector.get()

    if individual == 1:
        if game_name:
            individuals_game = individuals_games.setdefault(game_name, [])
            individuals_game.append(name)
            remove_individual(game_name, name)
            print(f"Individual participant {name} joined {game_name}")
        else:
            messagebox.showerror("Error", "Please select a game.")
    else:
        if game_name:
            teams_game = teams_games.setdefault(game_name, [])
            teams_game.append(name)
            add_team(game_name)
            print(f"Team {name} joined {game_name}")
        else:
            messagebox.showerror("Error", "Please select a game.")

def remove_individual(game_name, name):
    individuals_game = individuals_games.get(game_name, [])
    if name in individuals_game:
        individuals_game.remove(name)
        update_individual_list(game_name)
        messagebox.showinfo("Success", f"You, {name}, have been removed from the individual game {game_name}.")
    else:
        messagebox.showerror("Error", f"{name} not found in the individual game {game_name}.")

import tkinter as tk
from tkinter import messagebox

# Dictionary to store team participants for each game
individuals_games = {}
teams_games = {}

def join_tournament():
    individual = var.get()
    name = entry_name.get()
    game_name = game_selector.get()

    if individual == 1:
        if game_name:
            individuals_game = individuals_games.setdefault(game_name, [])
            individuals_game.append(name)
            remove_individual(game_name, name)
        else:
            messagebox.showerror("Error", "Please select a game.")
    else:
        if game_name:
            teams_game = teams_games.setdefault(game_name, [])
            teams_game.append(name)
            add_team(game_name)
        else:
            messagebox.showerror("Error", "Please select a game.")

def remove_individual(game_name, name):
    individuals_game = individuals_games.get(game_name, [])
    if name in individuals_game:
        individuals_game.remove(name)
        update_individual_list(game_name)
        messagebox.showinfo("Success", f"You, {name}, have been removed from the individual game {game_name}.")
    else:
        messagebox.showerror("Error", f"{name} not found in the individual game {game_name}.")

def add_team(game_name):
    team_name = entry_name.get()
    teams_game = teams_games.get(game_name, [])
    teams_game.append(team_name)
    update_team_list(game_name)
    messagebox.showinfo("Success", f"Team {team_name} has been added to the team game {game_name}.")

def update_individual_list(game_name):
    individuals_game = individuals_games.get(game_name, [])
    individuals_list.set(f"Remaining individuals in {game_name}: " + ", ".join(individuals_game))

def update_team_list(game_name):
    teams_game = teams_games.get(game_name, [])
    team_list.set(f"Remaining teams in {game_name}: " + ", ".join(teams_game))

def start_game():
    # Add your logic to start the game here
    print("Game Started!")
    
    print("\nIndividuals:")
    for game_name, participants in individuals_games.items():
        print(f"{game_name}: {', '.join(participants)}")
    
    print("\nTeams:")
    for game_name, teams in teams_games.items():
        print(f"{game_name}: {', '.join(teams)}")

    messagebox.showinfo("Game Started", "The tournament has started!")

# Tkinter GUI
root = tk.Tk()
root.title("Tournament Scoring System")

var = tk.IntVar()

label = tk.Label(root, text="Hello Participants, welcome to the competition")
label.pack()

radio_individual = tk.Radiobutton(root, text="Join as an individual", variable=var, value=1)
radio_individual.pack()

radio_team = tk.Radiobutton(root, text="Join as a team", variable=var, value=0)
radio_team.pack()

label_name = tk.Label(root, text="Enter your name:")
label_name.pack()

# Dropdown menu to select the game for participants
game_selector = tk.StringVar()
game_selector.set("Game 1")  # Set the default game
game_menu = tk.OptionMenu(root, game_selector, "Game 1", "Game 2", "Game 3", "Game 4",  "Game 5",)
  # Add more games as needed
game_menu.pack()

entry_name = tk.Entry(root) 
entry_name.pack()

button_join = tk.Button(root, text="Join Tournament", command=join_tournament)
button_join.pack()

individuals_list = tk.StringVar()
label_individuals = tk.Label(root, textvariable=individuals_list)
label_individuals.pack()

team_list = tk.StringVar()
label_teams = tk.Label(root, textvariable=team_list)
label_teams.pack()

# Button to start the game
button_start_game = tk.Button(root, text="Start Game", command=start_game)
button_start_game.pack()

root.mainloop()

