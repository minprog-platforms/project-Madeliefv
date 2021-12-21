# Name: Madelief Verburg
# Student number: 14125331
"""
runner.py
* runs tumour model
* runs a live model server
* runs experiments:
    * run_batch_con_r
    * run_batch_con_r_9_15
    * run_batch_repition_con
    * run_batch_vasc_radius
"""

from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from tumour_model import Tumour_model, compute_stop_status
from mesa.visualization.UserParam import UserSettableParameter
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt
import sys


def run_surfer():
    """Run a visualisation of the model"""

    def agent_portrayal(agent):
        """Determine the agent portayel of the model"""
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

    # Add sliders so the variables can be changed
    concentration_slider = UserSettableParameter('slider', "concentration", 200, 0, 1000, 10)
    radius_slider = UserSettableParameter('slider', "radius", 10, 0, 35, 1)
    chemo_repetition_slider = UserSettableParameter('slider', "chemo repitition", 3, 0, 10, 1)
    vascularisation_slider = UserSettableParameter('slider', "vascularisation", 3, 0, 10, 1)

    # Creating a grid
    grid = CanvasGrid(agent_portrayal, 75, 75, 600, 600)

    # Creating a chart with the number of cells
    chart = ChartModule([{"Label": "Total_cells", "Color": "Black"},
                        {"Label": "Stem_cells", "Color": "Blue"},
                        {"Label": "Transit_amplifying", "Color": "Red"},
                        {"Label": "Differentiated", "Color": "Pink"}],
                        data_collector_name='datacollector')

    # Creating the server with model
    server = ModularServer(Tumour_model,
                           [grid, chart],
                           "Tumour model",
                           {"radius": radius_slider, "concentration": concentration_slider,
                            "chemo_repetition": chemo_repetition_slider, "vascularisation": vascularisation_slider,
                            "width": 75, "height": 75})
    server.port = 8521   # The default         
    server.launch()


def run_batch_con_r():
    """Run a batch run with concentration and radius as variables"""

    # Determine the params
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition": 3,
                    "vascularisation": 3}
    variable_params = {"radius": range(0, 31, 5),
                       "concentration": range(100, 1100, 100)}

    # Create batch run
    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status": compute_stop_status})
    batch_run.run_all()

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()

    # Visualize the batch run
    color_dict = {'Succes': 'green', 'Fail': 'red', 'not_stopped': 'yellow'}
    plt.scatter(run_data.radius, run_data.concentration, s=200, c=[color_dict[i] for i in run_data.stop_status])
    plt.xlabel("Radius tumour")
    plt.ylabel("Concentration chemo")
    plt.show()


def run_batch_con_r_9_15():
    """Run a batch run with concentration and radius as variables specifically looking at 9-15 radius"""

    # Determine the params
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition": 3,
                    "vascularisation": 3}
    variable_params = {"radius": range(9, 16, 1),
                       "concentration": range(100, 1100, 100)}

    # Create batch run
    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=10,
                            max_steps=350,
                            model_reporters={"stop_status": compute_stop_status})
    batch_run.run_all()

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()

    # Visualize the batch run
    color_dict = {'Succes': 'green', 'Fail': 'red', 'not_stopped': 'yellow'}
    plt.scatter(run_data.radius, run_data.concentration, s=200, c=[color_dict[i] for i in run_data.stop_status])
    plt.xlabel("Radius tumour")
    plt.ylabel("Concentration chemo")
    plt.show()


def run_batch_rep_con():
    """Run a batch run with repitition and concentration of chemo as variables"""

    # Determine the params
    fixed_params = {"width": 75,
                    "height": 75,
                    "radius": 10,
                    "vascularisation": 3}
    variable_params = {"chemo_repetition": range(1, 11, 1),
                       "concentration": range(100, 1100, 100)}

    # Create batch run
    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=350,
                            model_reporters={"stop_status": compute_stop_status})
    batch_run.run_all()

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()

    # Visualize the batch run
    color_dict = {'Succes': 'green', 'Fail': 'red', 'not_stopped': 'yellow'}
    plt.scatter(run_data.chemo_repetition, run_data.concentration, s=200, c=[color_dict[i] for i in run_data.stop_status])
    plt.xlabel("Chemo repitition")
    plt.ylabel("Concentration chemo")
    plt.show()


def run_batch_vasc_r():
    """Run a batch run with the vascularisation and radius of tumour as variables"""

    # Determine the params
    fixed_params = {"width": 75,
                    "height": 75,
                    "chemo_repetition": 3,
                    "concentration": 300}
    variable_params = {"radius": range(0, 31, 5),
                       "vascularisation": range(1, 11, 1)}

    # Create batch run
    batch_run = BatchRunner(Tumour_model,
                            variable_params,
                            fixed_params,
                            iterations=5,
                            max_steps=300,
                            model_reporters={"stop_status": compute_stop_status})
    batch_run.run_all()

    run_data = batch_run.get_model_vars_dataframe()
    run_data.head()

    # Visualize the batch run
    color_dict = {'Succes': 'green', 'Fail': 'red', 'not_stopped': 'yellow'}
    plt.scatter(run_data.radius, run_data.vascularisation, s=200, c=[color_dict[i] for i in run_data.stop_status])
    plt.xlabel("Radius tumour")
    plt.ylabel("Vascularisation tumour")
    plt.show()


arg = sys.argv[1]
if arg == "live":
    run_surfer()
elif arg == "concentration_radius":
    run_batch_con_r()
elif arg == "repitition_concentration":
    run_batch_rep_con()
elif arg == "vascularisation_radius":
    run_batch_vasc_r()
elif arg == "concentration_radius9_15":
    run_batch_con_r_9_15()

