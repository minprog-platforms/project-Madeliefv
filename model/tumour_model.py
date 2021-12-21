# Name: Madelief Verburg
# Student number: 14125331
"""
tumour_model.py
* Contains tumour model
"""
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from tumour_agent import Tumour_agent, Chemo_agent
from compute_tumour import compute_stem_cells, compute_differentiated, compute_total_cells, compute_transit_amplifying, compute_stop_status
from math import sin, cos
from mesa.datacollection import DataCollector


class Tumour_model (Model):
    def __init__(self, radius, concentration, chemo_repetition, vascularisation, width, height):
        """A model with a tumour consisting of cell agents with radius r and a concentration of chemo agents."""
        self.r = radius
        self.concentration = concentration
        self.chemo_repetition = chemo_repetition
        self.vascularisation = vascularisation
        self.grid = MultiGrid(width, height, False)
        self.schedule_chemo = RandomActivation(self)
        self.schedule = RandomActivation(self)
        self.running = True
        self.id = 0
        self.dividing_cells = []
        self.steps = 0
        self.stop_status = "not_stopped"

        # Create tumour agents in circle
        y = int(self.grid.height / 2)
        x = int(self.grid.width / 2)
        RAD = 3.1415926535 / 180

        # Ensure the inner cells are stem_cells, middle are transit_amplifying and outer are differentiated
        for j in range(self.r):
            if j > (self.r / 3 * 2):
                type_agent = "differentiated"
            elif j > (self.r / 3):
                type_agent = "transit_amplifying"
            else:
                type_agent = "stem_cell"

            for i in range(360):
                x1 = int(j * cos(i * RAD))
                y1 = int(j * sin(i * RAD))
                if len(self.grid[x + x1][y + y1]) == 0:
                    a = Tumour_agent(self.id, self, type_agent)
                    self.grid.place_agent(a, (x + x1, y + y1))
                    self.id += 1
                    self.dividing_cells.append(a)
                    self.schedule.add(a)

        self.new_chemo()

        # Collect data on number of cells and stop status
        self.datacollector = DataCollector(
            model_reporters={"Total_cells": compute_total_cells, "Stem_cells": compute_stem_cells,
                             "Transit_amplifying": compute_transit_amplifying, "Differentiated": compute_differentiated,
                             "stop_status": compute_stop_status})

    def divide(self, agent_divide):
        """Dividing the cell"""
        if (agent_divide.status == "stem_cell" or agent_divide.status == "transit_amplifying"):

            # Determining the status of the new cell based on the surounding cells
            neighbors = self.grid.get_neighbors(agent_divide.pos, True)
            if agent_divide.status == "stem_cell":
                if len([neighbor for neighbor in neighbors
                        if (neighbor.status == "transit_amplifying" or neighbor.status == "differentiated")]) > 1:
                    status_new = "transit_amplifying"
                else:
                    status_new = "stem_cell"
            elif agent_divide.status == "transit_amplifying":
                if len([neighbor for neighbor in neighbors if neighbor.status == "stem_cell"]) > 1:
                    status_new = "transit_amplifying"
                elif len([neighbor for neighbor in neighbors if neighbor.status == "transit_amplifying"]) > 1:
                    status_new = "differentiated"
                else:
                    status_new = "transit_amplifying"

            # Creating new tumour agent
            expanded_cell = Tumour_agent(self.id, self, status_new)
            self.grid.place_agent(expanded_cell, agent_divide.pos)
            self.id += 1
            self.schedule.add(expanded_cell)
            if status_new != "differentiated":
                self.dividing_cells.append(expanded_cell)

            # Deciding which side the new cell is pushed to
            x_plus, y_plus = agent_divide.choice_direction(expanded_cell)
            agent_divide.expand(expanded_cell, x_plus, y_plus)

    def new_chemo(self):
        """Adds new dose of chemo to model"""
        for _ in range(self.concentration):
            a = Chemo_agent(self.id, self)
            self.schedule_chemo.add(a)
            # Add the agent to a random grid cell
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if len(self.grid.get_cell_list_contents((x, y))) == 0:
                    self.grid.place_agent(a, (x, y))
                    self.id += 1
                    break

    def step(self):
        """"Run one step of the tumour model"""
        # Deciding which dividing cell wil divide
        agent_step = self.random.choices(self.dividing_cells, k=int(len(self.dividing_cells) * 0.1))
        for i in range(len(agent_step)):
            self.divide(agent_step[i])

        if self.steps % int(100 / self.chemo_repetition) == 0 and self.steps != 0:
            self.new_chemo()

        # Step tumour agents
        self.schedule.step()

        # Step Chemo agents
        self.schedule_chemo.step()

        # Data collection
        self.datacollector.collect(self)

        if len([cell for cell in self.schedule.agents if cell.status == "stem_cell"]) < 1:
            self.stop_status = "Succes"
            self.running = False

        self.steps += 1