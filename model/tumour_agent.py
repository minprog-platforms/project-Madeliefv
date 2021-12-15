from mesa import Agent
import random


class Tumour_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, type_agent):
        super().__init__(unique_id, model)
        self.status = type_agent
        self.eaten = True
        self.time_eaten = 0
        self.age = 0
        
    
    def duplicate(self):
        # duplicating the cell
         if (self.status == "stem_cell" or self.status == "transitional_div"):
            self.model.id = self.model.id + 1
            
            if self.status == "stem_cell":
                status = random.choice(["stem_cell", "transitional_div"])
            elif self.status == "transitional_div":
                status = random.choice(["transitional_div", "transitional_nondiv"])
            
            # creating new agent
            expanded_cell = Tumour_agent(self.model.id, self.model, status)
            self.model.grid.place_agent(expanded_cell, self.pos)
            self.model.cells.append(expanded_cell)
            
            # deciding which side the new cell is pushed to
            x_plus, y_plus = self.choice_direction(expanded_cell)
            self.expand(expanded_cell, x_plus, y_plus)


    def expand(self, agent_to_place, x_plus, y_plus):
        #check the direction in which a particular agent expands (will impact x,y coordinates used)
        x,y = agent_to_place.pos

        # Look around if there is any free space 
        neighborhood = self.model.grid.get_neighborhood(agent_to_place.pos , True)
        possible_moves = [neighbor for neighbor in neighborhood 
                          if self.model.grid.is_cell_empty(neighbor) or isinstance(neighbor, Chemo_agent)]

        if len(possible_moves) > 0:
            pos = random.choice(possible_moves)
            self.model.grid.place_agent(agent_to_place, pos)
        

        # If there is no free space to move, put cell on place of direction and replace the cell on that place
        elif y + y_plus < self.model.grid.height and y + y_plus >= 0 and x + x_plus < self.model.grid.width and x + x_plus >= 0:
            # Remember the cell that was in there before expansion               
            cell_contents = self.model.grid.get_cell_list_contents((x + x_plus, y + y_plus))
            old_cell = cell_contents[0]

            # Place the cell needed to be placed
            self.model.grid.place_agent(agent_to_place, (x + x_plus, y + y_plus))
            x_plus, y_plus = self.choice_direction(old_cell)
            
            # Relocate the old cell
            self.expand(old_cell, x_plus, y_plus)
        
        else:
            # If the direction is not possible (end of )
            self.model.grid.place_agent(agent_to_place, (x, y))


    def choice_direction(self, agent_to_direct):
        # Decide on the direction the other cells will be moved to 
        x,y = agent_to_direct.pos
        x_plus = 0
        y_plus = 0

        # Decide which side of the grid it will move based on current postion
        if x > self.model.grid.width/2:
            x_plus = 1
        elif x < self.model.grid.width/2:
            x_plus = -1

        if y > self.model.grid.height/2:
            y_plus = 1
        elif y < self.model.grid.height/2:
            y_plus = -1

        # By 60% chance chage either x or y to 0
        if random.randint(0,9) < 6:
            zero = random.choice(["y", "x"])
            if zero == "y":
                y_plus = 0
            else:
                x_plus = 0

        return x_plus, y_plus
    

    def death(self):
        if self.status == "transitional_nondiv" and self.age > 6:
            self.model.grid._remove_agent(self.pos, self)
        if self.status == "transitional_div" and self.age > 12:
            self.model.grid._remove_agent(self.pos, self)
        
        neighborhood = self.model.grid.get_neighborhood(self.pos , True)
        neighbors = [neighbor for neighbor in neighborhood if not self.model.grid.is_cell_empty(neighbor)]
        if len(neighbors) < 2:
            self.model.grid._remove_agent(self.pos, self)
        
        

    def step(self):
        self.duplicate()
        self.death()
        self.age += 1


class Chemo_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, ):
        super().__init__(unique_id, model)
        self.status = "chemo"
        self.age = 0 

    def move(self):
        # Move the chemocells
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        
    
    def kill(self):
         # If there is a tumour cell present killl
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        cancer_cell = [obj for obj in this_cell if obj.status == "stem_cell" or obj.status == "transitional_div" ]
        for i in range(len(cancer_cell)):
            cell_to_kill = cancer_cell[i]

            # Kill the cells
            self.model.grid._remove_agent(self.pos, cell_to_kill)
    
    def step(self):
        self.move()
        self.kill()
        