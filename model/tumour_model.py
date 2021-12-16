from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from tumour_agent import Tumour_agent, Chemo_agent
from math import sin, cos
import random
from mesa.datacollection import DataCollector

# Compute number of cells present
def compute_total_cells(model):
    return len([cell for cell in model.schedule.agents])
# Compute number of stem_cells
def compute_stem_cells(model):
    return len([cell for cell in model.schedule.agents if cell.status == "stem_cell"])
# Compute number of transitional dividing cells
def compute_transitional_div(model):
    return len([cell for cell in model.schedule.agents if cell.status == "transitional_div"]) 
# Compute number of transitional non-dividing cells
def compute_transitional_nondiv(model):
    return len([cell for cell in model.schedule.agents if cell.status == "transitional_nondiv"]) 


class Tumour_model (Model):
    """A model with a tumour consisting of cell agents with radius r and a concentration of chemo agents."""
    def __init__(self, radius, concentration, width, height):
        self.r = radius
        self.concentration = concentration
        self.grid = MultiGrid(width, height, True)
        self.schedule_chemo = RandomActivation(self)
        self.schedule= RandomActivation(self)
        self.running = True
        self.id = 0
        self.cells = []

        # Create tumour agents in circle
        y = int(self.grid.height/2)
        x = int(self.grid.width/2)
        RAD = 3.1415926535 / 180
        
        # Ensure the inner cells are stem_cells, middle are transitional_div and outer are transitional_nondiv
        for j in range(self.r):
            if j > (self.r / 3 * 2):
                type_agent = "transitional_nondiv"
            elif j > (self.r / 3):
                type_agent = "transitional_div"
            else:
                type_agent = "stem_cell"

            for i in range(360):
                x1 = int(j * cos(i * RAD))
                y1 = int(j * sin(i * RAD))
                if len(self.grid[x+x1][y+y1]) == 0:
                    a = Tumour_agent(self.id, self, type_agent)
                    self.grid.place_agent(a, (x+x1, y+y1))
                    self.id += 1
                    self.cells.append(a)
                    self.schedule.add(a)

        # Place chemo
        for i in range(self.concentration):
            a = Chemo_agent(self.id, self)
            self.schedule_chemo.add(a)
            # Add the agent to a random grid cell
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if len(self.grid.get_cell_list_contents((x,y))) == 0:
                    self.grid.place_agent(a, (x, y))
                    self.id += 1
                    break
        
        # Collect data on number of cells
        self.datacollector = DataCollector(
            model_reporters={"Total_cells": compute_total_cells, "Stem_cells": compute_stem_cells, 
                             "Transitional_div": compute_transitional_div, "Transitional_nondiv": compute_transitional_nondiv})


    def duplicate(self, agent_duplicate):
        # Duplicating the cell
        if (agent_duplicate.status == "stem_cell" or agent_duplicate.status == "transitional_div"):
            
            if agent_duplicate.status == "stem_cell":
                status = random.choices(["stem_cell", "transitional_div"], weights=[0.1, 0.9], k=1)[0]
            elif agent_duplicate.status == "transitional_div":
                status = random.choices(["transitional_div", "transitional_nondiv"], weights=[0.1, 0.9], k=1)[0]
            
            # Creating new tumour agent
            expanded_cell = Tumour_agent(self.id, self, status)
            self.grid.place_agent(expanded_cell, agent_duplicate.pos)
            self.id += 1 
            self.schedule.add(expanded_cell)
            if status != "transitional_nondiv":
                self.cells.append(expanded_cell)
            
            
            # Deciding which side the new cell is pushed to
            x_plus, y_plus = agent_duplicate.choice_direction(expanded_cell)
            agent_duplicate.expand(expanded_cell, x_plus, y_plus)


    def step(self):
        # Deciding which dividing cell wil divide
        agent_step = self.random.choices(self.cells, k = int(len(self.cells)* 0.1))
        for i in range(len(agent_step)):
            self.duplicate(agent_step[i])
        
        # Step tumour agents
        self.schedule.step()

        # Step Chemo agents
        self.schedule_chemo.step()

        # Data collection
        self.datacollector.collect(self)

        



