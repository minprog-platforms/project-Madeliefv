from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from tumour_agent import Tumour_agent, Chemo_agent
from math import sin, cos
import random

class Tumour_model (Model):
    """A model with some number of agents."""
    def __init__(self, radius, concentration, width, height):
        self.r = radius
        self.concentration = concentration
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.id = 0
        self.cells = []

        # Create tumour agents
        y = int(self.grid.height/2)
        x = int(self.grid.width/2)
        RAD = 3.1415926535 / 180
        
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
                a = Tumour_agent(self.id, self, type_agent)
                self.grid.place_agent(a, (x+x1, y+y1))
                self.id += 1
                self.cells.append(a)

        # Place chemo
        for i in range(self.concentration):
            a = Chemo_agent(self.id, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if len(self.grid.get_cell_list_contents((x,y))) ==  0:
                    self.grid.place_agent(a, (x, y))
                    self.id += 1
                    break

    def step(self):
        agent_step =self.random.choices(self.cells, k = int(len(self.cells)* 0.001))
        for i in range(len(agent_step)):
            agent_step[i].step()
        self.schedule.step()

