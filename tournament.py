import tkinter as tk
from tkinter import simpledialog, messagebox

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Organizer")
        self.individuals = []  # To store individual names
        self.events = []  # To store event details
        self.teams = {}
        self.scores_by_team = {}  # To store scores by team
        self.scores_by_individual = {}  # To store scores by individual
        self.setup_ui()
    
    def setup_ui(self):
        # Initial UI setup, buttons for starting the setup process
        self.setup_btn = tk.Button(self.root, text="Setup Tournament", command=self.setup_tournament)
        self.setup_btn.pack(pady=20)
        self.score_btn = tk.Button(self.root, text="Start Scoring", command=self.start_scoring)
        self.score_btn.pack(pady=20)
        self.score_btn = tk.Button(self.root, text="Display Results", command=self.display_results)
        self.score_btn.pack(pady=20)

    def setup_tournament(self):
      # Gather the number of individuals
      num_individuals = simpledialog.askinteger("Input", "How many individuals are entering the tournament?", parent=self.root, minvalue=1)
      for i in range(num_individuals):
          name = simpledialog.askstring("Input", f"Enter the individual's name {i + 1}:", parent=self.root)
          if name:  # Check if the name is not None or empty
              self.individuals.append(name)
      
      # Gather the number of teams
      num_teams = simpledialog.askinteger("Input", "How many teams are participating in the tournament?", parent=self.root, minvalue=1)
      for i in range(num_teams):
          team_name = simpledialog.askstring("Input", f"Enter the team's name {i + 1}:", parent=self.root)
          self.teams[team_name] = []  # Initialise the team with an empty list of members
          
          # Prompt for the individuals in this team
          team_members = simpledialog.askstring("Input", f"Enter the names of individuals in {team_name} separated by commas:", parent=self.root)
          if team_members:  # Check if the input is not None or empty
              # Split the string by commas and strip whitespace, then add to the team's list
              self.teams[team_name] = [member.strip() for member in team_members.split(',')]

          #TODO: There may be an individual without a Team, possibly tell Organizer to ensure each Individual is recorded or add further functionality to handle this

      # Gather the number of events 
      #TODO;print checkmate when you win chess do this for all the academic games
      num_events = simpledialog.askinteger("Input", "How many events are in the tournament?", parent=self.root, minvalue=1)
      for i in range(num_events):
          event_title = simpledialog.askstring("Input", f"Enter the event's title {i + 1}:", parent=self.root)
          event_type = simpledialog.askstring("Input", "Enter the event's type (Sports/Academic):", parent=self.root)
          # Validate event type
          while event_type not in ['Sports', 'Academic']:
              messagebox.showwarning("Warning", "Type must be either 'Sports' or 'Academic'.")
              event_type = simpledialog.askstring("Input", "Enter the event's type (Sports/Academic):", parent=self.root)
          
          # Ask for the team assigned to this event  
          teams_assigned = simpledialog.askstring("Input", f"Which teams are assigned to the event '{event_title}'? Separate each team with a comma.", parent=self.root)
          teams_check = False
          while teams_assigned and not teams_check:
              proposed_teams = [team.strip() for team in teams_assigned.split(',')]
              for i in range(len(proposed_teams)):
                while proposed_teams[i] not in self.teams:
                    messagebox.showwarning("Warning", f"Team {proposed_teams[i]} does not exist. Please enter a valid team name.")
                    teams_assigned = simpledialog.askstring("Input", f"Which team is assigned to the event '{event_title}'?", parent=self.root)
                    break
                if i is (len(proposed_teams) - 1):
                    teams_check = True
              teams_assigned = proposed_teams

          self.events.append({"title": event_title, "type": event_type, "teams": teams_assigned})

    def start_scoring(self):
        for event in self.events:
            event_title = event['title']
            teams = event['teams']
            self.prompt_for_scores(event_title, teams)

    def prompt_for_scores(self, event_title, teams):
        # Prompt for the total score for the team in this event
        for team in teams:
          total_score = simpledialog.askinteger("Input", f"Enter total score for team {team} in event '{event_title}':", parent=self.root, minvalue=0)
          self.scores_by_team[team] = self.scores_by_team.get(team, 0) + total_score

          # Ask if a breakdown by individuals is necessary 
          breakdown = messagebox.askyesno("Question", "Do you want to break down the score by individuals?")
          if breakdown:
              team_list = self.teams[team]
              for individual in team_list:
                  score = simpledialog.askinteger("Input", f"Enter score for {individual} in team {team}:", parent=self.root, minvalue=0)
                  self.scores_by_individual[individual] = score

    def display_results(self):
        # Sort teams by their scores
        sorted_teams = sorted(self.scores_by_team.items(), key=lambda item: item[1], reverse=True)
        team_results = "Teams Rankings:\n" + "\n".join([f"{team}: {score}" for team, score in sorted_teams])
        
        # Ensure individual scores include team score if not individually specified
        for individual in self.individuals:
            if individual not in self.scores_by_individual:
                for team in self.teams:
                    if individual in self.teams[team]:
                      self.scores_by_individual[individual] = self.scores_by_individual.get(individual, 0) + self.scores_by_team[team]
                      break
                        

        # Sort individuals by their scores
        sorted_individuals = sorted(self.scores_by_individual.items(), key=lambda item: item[1], reverse=True)
        individual_results = "Individual Rankings:\n" + "\n".join([f"{individual}: {score}" for individual, score in sorted_individuals])

        # Display the results
        messagebox.showinfo("Results", f"{team_results}\n\n{individual_results}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()
