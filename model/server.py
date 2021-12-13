
from abc import abstractmethod
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from tumour_model import Tumour_model


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 1}

    if agent.status == "stem_cell":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    elif agent.status == "transitional_div":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    elif agent.status == "transitional_nondiv":
        portrayal["Color"] = "pink"
        portrayal["Layer"] = 0
    elif agent.status == "chemo":
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    return portrayal

grid = CanvasGrid(agent_portrayal, 75, 75, 600, 600)
server = ModularServer(Tumour_model,
                       [grid],
                       "Tumour model",
                       {"radius":20, "concentration":30,  "width":75, "height":75})
server.port = 8521 # The default                
server.launch()


    
    
