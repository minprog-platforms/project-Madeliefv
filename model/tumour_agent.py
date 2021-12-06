class Tumour_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, type_agent):
        super().__init__(unique_id, model)
        self.status = type_agent
        self.eaten = True
        self.time_eaten = 0

    def move(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if self.status == "prey":
            possible_moves = []
            best_moves = []
            for neighbor in neighborhood:
                if neighbor.model.grid.get_cell_list_contents != "preditor":
                    possible_moves += neighbor
                    if neighbor.model.grid.get_cell_list_contents == "prey":
                        best_moves += neighbor
            if len(best_moves) > 0:
                new_position = self.random.choice(best_moves)
                self.model.grid.move_agent(self, new_position)
            else: 
                new_position = self.random.choice(possible_moves)
                self.model.grid.move_agent(self, new_position)
            
        if self.status== "preditor":
            possible_moves = []
            best_moves = []
            for neighbor in neighborhood:
                if neighbor.model.grid.get_cell_list_contents == "prey":
                    best_moves += neighbor
                elif neighbor.model.grid.get_cell_list_contents == "preditor":
                    possible_moves += neighbor
            if len(best_moves) > 0:
                new_position = self.random.choice(best_moves)
                self.model.grid.move_agent(self, new_position)
            else: 
                new_position = self.random.choice(possible_moves)
                self.model.grid.move_agent(self, new_position)           
