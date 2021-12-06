from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from tumour_model import Tumour_model

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 3}

    if agent.status == "stem_cell":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
    elif agent.status == "transitional_div":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    elif agent.status == "transitional_nondiv":
        portrayal["Color"] = "pink"
        portrayal["Layer"] = 0
    elif agent.status == "chemo":
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0

grid = CanvasGrid(agent_portrayal, 75, 75, 600, 600)
server = ModularServer(Tumour_model,
                       [grid],
                       "Tumour model",
                       {"N":100, "width":800, "height":800})
server.launch()