# Tumor growth model
### computational science - Madelief Verburg (14125331)
----------------------------------------------------

## Summary
This is a simplified tumour model. This model, aims to answer the research question: 
**What is the effect of the properties of the tumour and the concentration of chemotherapy on tumour growth?**

In this model, we consider two variable properties: size and division capabilities. It also looks at the effect of chemotherapy on tumour growth. The model contains two classes of agents namely : 
- chemo molecules (Chemo_agent)
- tumour cells (Tumour_agent)
    - stem_cell (divide) (blue coloured)
    - transit_amplifying (divide) (red coloured)
    - differentiated (do not divide) (pink coloured)
    
--------------------------------------------------
## Run model
- To run the model, run ``runner.py`` with command in this directory. e.g.

```
    $ python3 runner.py live
```
- several commands can be used:
    - live: to run live model in your browser.
    - concentration_radius: to do a batch run with variables concentration and radius.
    - concentration_radius9_15 : to do a batch run with variables concentration and radius specific for radius between 9-15.
    - repitition_concentration : to do a batch run with variables chemo repetition and concentration.
    - vascularisation_radius: to do a batch run with variables vascularisaiton and radius.


---------------------------------------------------

## Set up

### Variables
- Radius (of tumour)
- Concentration (of chemo molecules)
- Chemo repitition (repition of chemo dosis)
- Vasuclarisation (degree of vascularisation of tumour)


### Initation
- The tumour is initiated in the middle of the grid. With the size dicided by the radius.
    - The inner 1/3 will be stem cells, the middle wil become transit_amplifying cells and the outer cells will become differentiated cells. This way most of the cells will be differentiated and least will be stem cells, as is normal in tumours.
- Outside the tumour the chemo agents will be placed randomly. The amount of chemo agents placed is based on the concentration input


### Functions
#### tumour cells: 
- Every step 10% of the dividing cells **divide**. 
    - In real tumours this division rate is dependend on how agressive the tumour is. 10% however gives the most natural tumour progression
    - The stem_cells divide either into two stem_cells or in a stem_cell and a transit_amplifying cell. 
        - The way the stem_cell divide is based on its surounding cells. If it is surrounded by transit_ampifying cells it will also divide into one transit_amplyfing cell -> cellular communication.
    - The transit_amplyfing cell will divide into two transit_amplifying cells or into a transit_amplifying cell and a differentiated cell.
        - The way the transit_amplyfing cell divides is also based on its surrounding cells.
    - **expand** the tumour happens when the cells divide they will push the other cells outwards till there is space for them.

- **Death** of tumour cells
    - Transit_amplifying and differentiated cells can die based on their age .
        - Stem_cells are effectivelly immortal -> so their death is not taken into account in this model.
    - Stem_cells and transit_amplifying cells can die based on their surrounding.
        - If not enough other cells surround these cells this creates an unstable environment -> which lets the cells die. 

#### chemo cells:
- Every step all chemo agents **move**. 
    - The vascularisation degree decides how fast they move towards the tumour or not.

- Chemo agents can **kill** tumour agents that divide
    - Chemo molecules work only on dividing cells thus only can kill them

- Chemo agents can also be **worked out**.
    - If a chemo agent has killed a certain amount of tumour cells it will be removed.
    - If a chemo has reached a certain age it will be removed.
       
- **new chemo** can be added.
    - Depended on the chemo_repitiion new dose of chemo will be added after a number of steps.

### End of model
- Model stops when:
    - No stem cells are present any more (succes) (green in experiments visualization).
    - The cells reach the end of the grid (fail) (red in experiments visualization).
    - Model was stoped before end point was reached (not_stopped) (yellow in experiments visualizations).
----------------------------------------------------
## Files
- runner.py
    - Contains visualisation
        - shows grid
        - show graph with number of cells
        - shows sliders for variable adjustments
    - Contains several experiments:
        - run_batch_con_r: shows which concentration and which radius is succesfull (cancer gone) or failed (cancer survived)
            - visualized in a scatterplot
        - run_batch_con_r_9_15: shows which concentration and which radius is succesfull (cancer gone) or failed (cancer survived) specific for radius 9 -15
            - visualized in a scatterplot 
        - run_batch_repition_con: shows which repitition and concentration of chemo is succesfull and which is nog
            - visualized in a scatterplot
        - run_batch_vasc_radius: shows which vascularisation degree and which radius is succesfull or not
            - visualized in a scatterplot
        
- tumour_model.py
    - contains model
        - divide: divides tumour cells
        - new_chemo : adds dose of chemo

- tumour_agent.py
    - Tumour_agent
        - expand : expands tumour by moving cells outwards.
        - choice_direction: decides which side the moving cells go to.
        - death: decides if a cell dies and will be removed from model.
    - Chemo_agent
        - move: decides where the chemo agent will move to.
        - kill: decides if a tumour agent will be killed and removes that agent.
        - worked_out : decides if a chemo agent is worked out and will be removed from model.

- compute_tumour.py
    - contains compute functions:
        - compute_total_cells
        - compute_stem_cells
        - compute_transit_amplifying
        - compute_differentiated
        - compute_stop_status

- PROPOSAL.md
    - the proposal for this project

- PROCESS.md
    - a logbook of what is changed

- REVIEW.md
    - points discussed during review moment

- README.md
    - this document containing information about the model.
--------------------------------------------------- 
## Screencast

[Screencast tumour model](https://video.uva.nl/media/Screencast_tumour_model/0_yt6agmrh)

---------------------------------------------------   
## short theory behind the model
During mitosis, a stem cell can divide either asymmetrically or symmetrically. During asymmetric mitosis, one of the two daughter cells stays a stem cell and, thus replacing its parent. This means that a stem cell effectively never dies. It is quasi reincarnated after each division. The other daughter cell turns into a transitory amplifying cell, which moves outward. A stem cell may also divide symmetrically into two stem cells. 

Young transitory amplifying cells may divide, creating another transitory amplyfing cells. However have a finite number of divisions thus at a certain age they will stop dividing and die.  These can divide in symmetrically and asymetrically into a differentiated cell, which can no longer divide.

Most chemotherapy drugs are known as Mitosis and Synthesis poisons, inhibit cell division but generally do not cause cell death. Thus chemotherapy can be represented as killing only the dividing cells. As mitosis and synthesis only takes place in dividing cells. Therefore chemotherapy mainly kills the young transitory cells since only young cells divide and stemcells are mainly located in the centre of the tumor. Differentiated cells are not affected, however they continue ageing and finally pass away.

How easily the chemo acceses the tumour is partly determined by the vascularization. As tumours grow fast they need a lot of energy, proteins, minerals, etc. To get this to them tumours are highly vascularized. However this also means that the chemo can easily be transported to the tumour. The degree of vascularisation thus also has effect on the chemo.
