from mesa import Agent
import random


class Tumour_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, type_agent):
        super().__init__(unique_id, model)
        self.status = type_agent
        self.eaten = True
        self.time_eaten = 0
        
    
    def duplicate(self):
        # duplicating the cell
         if (self.status == "stem_cell" or self.status == "transitional_div"):
            self.model.id = self.model.id + 1
            
            # creating new agent
            expanded_cell = Tumour_agent(self.model.id, self, self.status)
            self.model.grid.place_agent(expanded_cell, self.pos)
            self.model.cells.append(expanded_cell)
            
            # deciding which side the new cell is pushed to
            x_plus, y_plus = self.choice_direction(expanded_cell)
            self.expand(expanded_cell, x_plus, y_plus)


    def expand(self, agent_to_place, x_plus, y_plus):
        #check the direction in which a particular agent expands (will impact x,y coordinates used)
        x,y = agent_to_place.pos
        
        if y + y_plus < self.model.grid.height and y + y_plus >= 0 and x + x_plus < self.model.grid.width and x + x_plus >= 0:
            #remember the cell that was in there before expansion (assuming that there is only one object, it is on pos 0)                
            cell_contents = self.model.grid.get_cell_list_contents((x + x_plus, y + y_plus))
            
            if len(cell_contents) > 0 and isinstance(cell_contents[0], Tumour_agent) :
                old_cell = cell_contents[0]
                self.model.grid.place_agent(agent_to_place, (x + x_plus, y + y_plus))
                # self.model.grid._remove_agent(self.pos, agent_to_place)
                # direction_next =self.random.choices(["N", "S", "E", "W", "NE", "SE", "NW", "SW"], k = 1)[0]
                x_plus, y_plus = self.choice_direction(old_cell)
                self.expand(old_cell, x_plus, y_plus)
            elif len(cell_contents)== 0 or isinstance(cell_contents[0], Chemo_agent):
                self.model.grid.place_agent(agent_to_place, (x + x_plus, y + y_plus))
        else:
            self.model.grid.place_agent(agent_to_place, (x, y))
        
    def choice_direction(self, agent_to_direct):
        x,y = agent_to_direct.pos
        x_plus = 0
        y_plus = 0
        if x > self.model.grid.width/2:
            x_plus = 1
        elif x < self.model.grid.width/2:
            x_plus = -1
        if random.randint(0,9) < 8:
            x_plus = 0
        
        if y > self.model.grid.height/2:
            y_plus = 1
        elif y < self.model.grid.height/2:
            y_plus = -1
        if random.randint(0,9) < 8:
            y_plus = 0
        return x_plus, y_plus

    

    def step(self):
        self.duplicate()



class Chemo_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, ):
        super().__init__(unique_id, model)
        self.status = "chemo"
        self.age = 0 

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        
    
    def kill(self):
         # If there is a tumour cell present killl
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        cancer_cell = [obj for obj in this_cell if isinstance(obj, Tumour_agent)]
        for i in range(len(cancer_cell)):
            cell_to_kill = cancer_cell[i]

            # Kill the cells
            self.model.grid._remove_agent(self.pos, cell_to_kill)
            # self.model.schedule.remove(cell_to_kill)
    
    def step(self):
        self.move()
        self.kill()
        