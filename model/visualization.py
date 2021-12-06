from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

class agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 3}

    if agent.status == "prey":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
    elif agent.status == "preditor":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 0