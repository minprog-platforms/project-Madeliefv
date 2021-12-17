from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from tumour_model import Tumour_model, compute_stop_status, compute_steps
from mesa.visualization.UserParam import UserSettableParameter
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt

def run_surfer():
    def agent_portrayal(agent):
        portrayal = {"Shape": "circle",
                    "Filled": "true",
                    "r": 1}

        if agent.status == "stem_cell":
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 0
        elif agent.status == "transit_amplifying":
            portrayal["Color"] = "red"
            portrayal["Layer"] = 0
        elif agent.status == "differentiated":
            portrayal["Color"] = "pink"
            portrayal["Layer"] = 0
        elif agent.status == "chemo":
            portrayal["Color"] = "green"
            portrayal["Layer"] = 0
        return portrayal


    concentration_slider = UserSettableParameter('slider', "concentration", 200, 0, 500, 10)
    radius_slider = UserSettableParameter('slider', "radius", 10, 0, 35, 1)
    chemo_repetition_slider = UserSettableParameter('slider', "chemo repitition", 3, 0, 10, 1)
    vascularisation_slider = UserSettableParameter('slider', "vascularisation", 3, 0, 10, 1)
    grid = CanvasGrid(agent_portrayal, 75, 75, 600, 600)
    chart = ChartModule([{"Label": "Total_cells", "Color": "Black"}, 
                        {"Label": "Stem_cells", "Color": "Blue"},
                        {"Label": "Transit_amplifying", "Color": "Red"},
                        {"Label": "Differentiated", "Color": "pink"}], 
                        data_collector_name='datacollector')
    server = ModularServer(Tumour_model,
                        [grid, chart],
                        "Tumour model",
                        {"radius": radius_slider, "concentration":concentration_slider, 
                            "chemo_repetition" : chemo_repetition_slider, "vascularisation": vascularisation_slider,
                            "width":75, "height":75})
    server.port = 8521 # The default                
    server.launch()


def run_batch_con_r():
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition" : 3,
                    "vascularisation": 3}
    variable_params = {"radius": range(0, 30, 5),
                       "concentration":range(100, 1000, 100)}


    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status" : compute_stop_status})
    batch_run.run_all() 

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()
    color_dict = { 'Succes':'green', 'Fail':'red', 'not_stopped':'yellow'}
    plt.scatter(run_data.radius, run_data.concentration, s = 200, c= [color_dict[i] for i in run_data.stop_status])
    plt.show()


def run_batch_con_r_time():
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition" : 3,
                    "vascularisation": 3}
    variable_params = {"radius": range(0, 30, 5),
                       "concentration":range(100, 1000, 100)}


    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status" : compute_stop_status, "steps": compute_steps})
    batch_run.run_all() 

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()
    color_dict = { 'Succes':'green', 'Fail':'red', 'not_stopped':'yellow'}
    plt.scatter(run_data.steps, run_data.concentration, s = run_data.radius, c= [color_dict[i] for i in run_data.stop_status])
    plt.show()



def run_batch_repition_con():
    fixed_params = {"width": 75,
                    "height": 75,
                    "radius" : 10,
                    "vascularisation": 3}
    variable_params = {"chemo_repetition": range( 10, 1),
                       "concentration":range(100, 1000, 100)}


    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status" : compute_stop_status, "steps": compute_steps})
    batch_run.run_all() 

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()
    color_dict = { 'Succes':'green', 'Fail':'red', 'not_stopped':'yellow'}
    plt.scatter(run_data.chemo_repetition, run_data.concentration, s = 200, c= [color_dict[i] for i in run_data.stop_status])
    plt.show()



def run_batch_vasc_radius():
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition" : 3,
                    "concentration": 300}
    variable_params = {"radius": range(0, 30, 5),
                       "vascularisation":range(1, 10, 1)}


    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status" : compute_stop_status})
    batch_run.run_all() 

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()
    color_dict = { 'Succes':'green', 'Fail':'red', 'not_stopped':'yellow'}
    plt.scatter(run_data.radius, run_data.concentration, s = 200, c= [color_dict[i] for i in run_data.stop_status])
    plt.show()

run_batch_repition_con()


