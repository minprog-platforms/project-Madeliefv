# Proposal - Tumor treatment - computational science - Madelief Verburg
## Introduction
This project aims to create an Agent-Based Model of a tumour and its treatment. In this model, we consider a few properties, such as size, vascularisation. We also look at the effect of chemotherapy on tumour growth.

### research question
With this model, I would like to answer the research question. What is the effect of the properties of the tumour and the concentration of chemotherapy on tumour growth?

### short theory behind the model
During mitosis, a stem cell can divide either asymmetrically or symmetrically. During asymmetric mitosis, one of the two daughter cells stays a stem cell and, thus replacing its parent. This means that a stem cell effectively never dies. It is quasi reincarnated after each division. The other daughter cell turns into a transitory amplifying cell, which moves outward. A stem cell may also divide symmetrically into two stem cells. 

Young transitory amplifying cells may divide, creating another transitory amplyfing cells. However have a finite number of divisions thus at a certain age they will stop dividing and die.  These can divide in symmetrically and asymetrically into a differentiated cell, which can no longer divide.

Most chemotherapy drugs are known as Mitosis and Synthesis poisons, inhibit cell division but generally do not cause cell death. Thus chemotherapy can be represented as killing only the dividing cells. As mitosis and synthesis only takes place in dividing cells. Therefore chemotherapy mainly kills the young transitory cells since only young cells divide and stemcells are mainly located in the centre of the tumor. Differentiated cells are not affected, however they continue ageing and finally pass away.

How easily the chemo acceses the tumour is partly determined by the vascularization. As tumours grow fast they need a lot of energy, proteins, minerals, etc. To get this to them tumours are highly vascularized. However this also means that the chemo can easily be transported to the tumour. The degree of vascularisation thus also has effect on the chemo.

## Set up
### programme used
- Mesa 
    - This model will be built using Mesa. This model will use a grid model. 
- mathplotlib
- numpy

### Agents
The agents in this project will be:
- cancer stem cells
- transit amplyfing cells
- differentiated cells
- chemotherapy molecules

### Variables 
The variables in this model will be:
- one can choose the start size of the tumour
- one can choose the concentration of chemotherapy
- chose the repetition speed of chemotherapy
- chose the degree of vascularization


## How it works
One cell stays put, and the other moves outwards (to the surrounding grid and pushes other cells outwards). The chemotherapy can attack the outer cells(first has to kill all cells in the surrounding grid before moving on). The stem cells will divide symmetrically with a chance of being given by the user and asymmetrically based on the surounding cells. If many of them are transit cells the chance is bigger that this cell will also become a transit cell. The transit cells will always move outwards. The transit cells will divide based also on surrouding cells. 

How higher vascularized the tumour is the faster the chemo molecules will move towards the tumour

The model will show the cell count in a live graph.

## Example of what the model might look like
<img src="./doc/Screenshot 2021-12-06 at 14.26.50.png" alt="example" style="height:200px; width:350px;"/>

## External data
- ratio cancerstem cells to others:
    "As an example, CSC composition ratio in different tumors might range from 0.2% to 82.5%. "

## Making it bigger 
Possibilities for enlarging the project:
- adding other properties to the tumour like:
    - also adding the option of metastasis:
        - In this case, there will be a chance that one of the stemcells comes loose and will migrate to a different part where it will form a new tumour
- also adding other treatment options and seeing their effects
- add the immune system 
- 3D model 

## Biggest challenges
- making sure the dividing pushes the other cells outwards
- do I make the chemo go towards the tumour (as tumour has a lot of vessels so automatically a lot goes to it) or not (as the chemo does not go there consiously)
- to what detail will I go in this project-> a lot is possible but might be too much
- 3D modelling 

