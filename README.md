# Proposal - Tumor treatment - computational science - Madelief Verburg
## Introduction
This project aims to create an Agent-Based Model of a tumour and its treatment. In this model, we consider a few properties, such as size and division capabilities. We also look at the effect of chemotherapy on tumour growth.

### research question
With this model, I would like to answer the research question. What is the effect of the properties of the tumour and the concentration of chemotherapy on its eradication?

### short theory behind the model
During mitosis, a stem cell can divide either asymmetrically or symmetrically. During asymmetric mitosis, one of the two daughter cells stays a stem cell and, thus replacing its parent. This means that a stem cell effectively never dies. It is quasi reincarnated after each division. The other daughter cell turns into a transitory cell, which moves outward. A stem cell may also divide symmetrically into two stem cells. 

Young transitory cells may divide, creating another transitory cells. However have a finite number of divisions thus at a certain age they will stop dividing and die. 

Most chemotherapy drugs are known as Mitosis and Synthesis poisons, inhibit cell division but generally do not cause cell death. Thus chemotherapy can be represented as killing only the dividing cells. As mitosis and synthesis only takes place in dividing cells. Therefore chemotherapy mainly kills the young transitory cells since only young cells divide and stemcells are mainly located in the centre of the tumor. Older, non-dividing transitory cells are not affected, however they continue ageing and finally pass away.

## Set up
### programme used
- Mesa 
    - This model will be built using Mesa. This model will use a grid model. 
- mathplotlib
- numpy

### Agents
The agents in this project will be:
- cancer stem cells
- transitory cancer cells
- chemotherapy molecules

### Variables 
The variables in this model will be:
- one can choose the start size of the tumour
- one can choose the concentration of chemotherapy
- can choose de division rate
- stemcell division symmetrically

## How it works
One cell stays put, and the other moves outwards (to the surrounding grid with the least other cells). The chemotherapy can attack the outer cells(first has to kill all cells in the surrounding grid before moving on). The stem cells will divide symmetrically with a chance of being given by the user and asymmetrically with a chance of 1- the probability of symmetrically dividing. The transitory cells will always move outwards. The transitory will divide with a chance of the division rate

## Example of what the model might look like
<img src="./doc/Screenshot 2021-12-06 at 14.26.50.png" alt="example" style="height:100 px; width:150 px;"/>

## External data
papers used during project (not yet found the best ones)

## Making it bigger 
Possibilities for enlarging the project:
- adding other properties to the tumour like:
    - also adding the option of metastasis:
        - In this case, there will be a chance that one of the stemcells comes loose and will migrate to a different part where it will form a new tumour
- also adding other treatment options and seeing their effects
- add the immune system 