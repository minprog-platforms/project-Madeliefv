from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class Tumour_model (Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        
        # Create agents
        for i in range(self.num_agents):
            self.type_agent = self.random.choices(["prey", "predator"], weights = [0.8, 0.2], k = 1)[0]
            a = Prey_pred_Agent(i, self, self.type_agent)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()

