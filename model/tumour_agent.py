from mesa import Agent


class Tumour_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, type_agent):
        super().__init__(unique_id, model)
        self.status = type_agent
        self.eaten = True
        self.time_eaten = 0

    def expand(self, agent, direction):
        #check the direction in which a particular agent expands (will impact x,y coordinates used)
        x,y = agent.pos
        
        if (direction == "NORTH"):
            #remember the cell that was in there before expansion (assuming that there is only one object, it is on pos 0)                
            cell_contents = self.model.grid.get_cell_list_contents((x,y+1))
            print(cell_contents)
            
            if (len(cell_contents) > 0):
                old_cell = cell_contents[0]
            
                #check the type of cell that is expanding
                if (agent.status == "stem_cell" or agent.status == "transitional_div" or agent.status == "transitional_nondiv"):
                    #create a new cell of the expanding type, with incremented id of that type
                    print(old_cell)
                    #ENSURE THAT A DIFFERENT AGENT IS CREATED FOR A DIFFERENT TYPE OF CELL
                    expanded_cell = Tumour_agent(self.model.id + 1, self, "stem_cell")
                    #place that newly created agent on the adjacent square in the direction
                    self.model.grid.place_agent(expanded_cell, (x, y + 1))
                    #recursive function if the next cell is not empty (if the content list is not null)
                    self.expand(old_cell, "NORTH")

    def step(self):
        self.expand(self, "NORTH")



class Chemo_agent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, ):
        super().__init__(unique_id, model)
        self.status = "chemo"
        self.age = 0 

    def move(self):
        # self.random_move()
        
        # If there is a tumour cell present killl
        x, y = self.pos
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        cancer_cell = [obj for obj in this_cell if isinstance(obj, Tumour_agent)]
        for i in range(len(cancer_cell)):
            cell_to_kill = cancer_cell[i]

            # Kill the cells
            self.model.grid._remove_agent(self.pos, cell_to_kill)
            self.model.schedule.remove(cell_to_kill)
    
    def step(self):
        self.move()
        