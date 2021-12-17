from mesa import Agent
import random


class Tumour_agent(Agent):
    """ An agent with a type and age which can duplicate (in model) """
    def __init__(self, unique_id, model, type_agent):
        super().__init__(unique_id, model)
        self.status = type_agent
        self.age = 0
        

    def expand(self, agent_to_place, x_plus, y_plus):
        #check the direction in which a particular agent expands (will impact x,y coordinates used)
        x,y = agent_to_place.pos

        # Look around if there is any free space 
        neighborhood = self.model.grid.get_neighborhood(agent_to_place.pos , True)
        possible_moves = [neighbor for neighbor in neighborhood 
                          if self.model.grid.is_cell_empty(neighbor) or isinstance(neighbor, Chemo_agent)]
        if len(possible_moves) > 0:
            pos = random.choice(possible_moves)
            self.model.grid.move_agent(agent_to_place, pos)
        

        # If there is no free space to move, put cell on place of direction and replace the cell on that place
        elif y + y_plus < self.model.grid.height and y + y_plus >= 0 and x + x_plus < self.model.grid.width and x + x_plus >= 0:
            # Remember the cell that was in there before expansion               
            cell_contents = self.model.grid.get_cell_list_contents((x + x_plus, y + y_plus))
            old_cell = cell_contents[0]
            self.model.grid.move_agent(agent_to_place, (x + x_plus, y + y_plus))
            
            # Relocate the old cell
            self.expand(old_cell, x_plus, y_plus)
        
        else:
            # If the direction is not possible (end of grid) remove agent
            # self.model.grid._remove_agent(agent_to_place.pos, agent_to_place)
            # self.model.schedule.remove(agent_to_place)
            self.model.stop_status = "Fail"
            self.model.running = False


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

        # By 80% chance chage either x or y to 0 -> for a equal distribution
        if random.randint(0,10) < 9:
            zero = random.choice(["y", "x"])
            if zero == "y":
                y_plus = 0
            else:
                x_plus = 0
        return x_plus, y_plus
    

    def death(self):
        # Checks if a cell dies 
        neighborhood = self.model.grid.get_neighborhood(self.pos , True)
        neighbors = [neighbor for neighbor in neighborhood if not self.model.grid.is_cell_empty(neighbor)]
        # A dividing cell dies when it has less then 2 neighbors (this is a non stable envirnment for the cell)
        if len(neighbors) < 3 and (self.status == "stem_cell" or self.status == "transit_amplifying"):
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            self.model.cells.remove(self)

        # Cell dies when of a certain age
        elif self.status == "differentiated" and self.age > random.randint(25, 100):
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
        elif self.status == "transit_amplifying" and self.age > random.randint(50, 500):
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            self.model.cells.remove(self)

    def step(self):
        self.death()
        self.age += 1


class Chemo_agent(Agent):
    """ An agent which can kill the tumour cell agents."""
    def __init__(self, unique_id, model, ):
        super().__init__(unique_id, model)
        self.status = "chemo"
        self.age = 0 
        self.cells_killed = 0

    def move(self):
        # Move the chemo molecules
        x, y = self.pos
        if x < self.model.grid.width/2:
            x_new = x + 1
        elif x > self.model.grid.width/2:
            x_new = x - 1

        if y < self.model.grid.height/2:
           y_new = y + 1
        elif y > self.model.grid.height/2:
            y_new = y - 1

        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        other_position = random.choices(possible_steps)
        new_position = random.choices([other_position, [(x_new,y_new)]], weights=[1- self.model.vascularisation /10, self.model.vascularisation /10], k=1)[0]
        self.model.grid.move_agent(self, new_position[0])
        
    
    def kill(self):
         # If there is a dividing tumour cell present kill it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        cancer_cell = [obj for obj in this_cell if (obj.status == "stem_cell" or obj.status == "transit_amplifying")]
        if len(cancer_cell) > 0:
            cell_to_kill = cancer_cell[0]
            self.model.grid._remove_agent(cell_to_kill.pos, cell_to_kill)
            self.model.schedule.remove(cell_to_kill)
            self.model.cells.remove(cell_to_kill)
            self.cells_killed += 1
    
    def worked_out(self):
        if self.age > random.randint(10, 100) or self.cells_killed > random.randint(5, 10):
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule_chemo.remove(self)
    
        
    def step(self):
        self.move()
        self.kill()
        self.worked_out()
        self.age += 1
        