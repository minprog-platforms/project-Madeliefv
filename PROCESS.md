# logbook
#### Madelief Verburg - tumour model
-------------------------------------------------------------------------

## 7-12-2021
- Creating framework -> (server.py, tumour_model.py and tumour_agent.py)
- make sure it shows agents again because they did not work
- creating circle of tumour cells-> not even close 
--------------------------------------------------------------------------
## 8-12-2021
- creating circle
    - trying many different kinds of circle ideas but all showed nothing
    - starting again with a square did not work
        - finaly getting a square -> turns out it was outside the grid
- then made a diamond
- then tried circle again -> finally worked
--------------------------------------------------------------------------
## 9 -12-2021
- adjusting circle so it showed different kinds of cells
- adding agent chemo
- making sure the chemo was printend and not on the tumour
--------------------------------------------------------------------------
## 10 -12 -2021
- starting on the expension of tumour -> did not come so far
--------------------------------------------------------------------------
## 12-12-2021
- expansion tumour
    - first only stem cells -> pusshing outwards
    - only takes 10 minutes for one step -> not really usefull
- then adjusted it so it also pushes all other cells outwards
- realizing this is not realy feasable as it takes too long -> rethink my model
--------------------------------------------------------------------------
## 13-12-2021
- rethinking my model, maybe different strategy -> eventually sticked with my old strategy
- adjusting Chemo_agent -> making it move
- adjusting interface -> adding slidrs
- redoing expansion tumour -> make it more efficient
--------------------------------------------------------------------------
## 14-12-2021
- adjusting the step so it will make sure 0.5% of cells will do a step
- adjusting tumour agent so the side it will be pushed to is variable 
    - first random north, east, norhteast, etc
    - then more specific eg. if on top side it will only go north bottem side only will go south
- making sure the chemo steps every step.

--------------------------------------------------------------------------
## 15-12-2021
- changed the tumour_agent when expanding to look around if there are any empty places
- changed choice_direction in tumour agent -> to assure it will never be x_plus = 0 and y_plus = 0 (which would mean it does not move)
- Ensuring chemo agent only kills dividing cells
- added death to tumour agent 
    - killing cells (non dividing and transitional div) after a certain age (dividing 2x long then non div)
    - killing cells with less then 2 surounding cells
- adjust duplicate so that stem_cells can also split into transitional div
--------------------------------------------------------------------------
## 16-12-2021
- inserted graph with toal N cells and N cells per cell kind
- moved duplicate to model 
- adjusted death (tumour agent) and kill (chemo agent)
    - made two seperate schedules for tumour agents and for chemo agents -> so the killing of cells will nog interfere
    - in order to use datacollector the tumour agent schedule had to change from schedule_cells -> schedule otherwise it would not work.
- adjusted tumour agent-> as it had agents double
- removed errors from chemo agent
- tried to ajust frame -> so metastasis could be added. However this was not possible as then there would be a recursion error. -> kept the grid at 75X75
- added worked_out to chemo
--------------------------------------------------------------------------
## 17-12-2021
- added new chemo -> removed chemo in init as it was now unnescecairy
- removed the calling of function choice direction -> to get a more round division
- added chemo repitition. Which can be every 10 steps to every 100 steps. based on 1-10 scale -> 10 very often 1 rarely.
- added vascularisation which has effect on how much the chemo will be moved towards the tumour
- stop the model if there are no stem cells left -> succes
    - stop the model if it hits the border of the grid -> fail
- add experiment -> batch runner to model 
    - this takes as variabless the radius and concentration and returns a succes or fail and plots this
- add another experiment
--------------------------------------------------------------------------
## 20-12-2021
- rewrote README.md
- adjusted points from review:
    - added commandline arguments in runner.py
    - overall style adjustements
    - adjusted comments
    - put compute function in a seperate file
- Added review
- Added summary to each python file
- Adjusted batch runs 
- Assesment.md added 
- LISCENCE.md added

