# logbook
#### Madelief Verburg - tumour model
-------------------------------------------------------------------------

## 7-12-2021
- Creating framework -> (server.py, tumour_model.py and tumour_agent.py).
- Make sure it shows agents again, because they did not visualize in the beginning.
- Creating circle of tumour cells. This was more difficult than expecten, I was not even close.
--------------------------------------------------------------------------
## 8-12-2021
- Creating circle.
    - Trying many different kinds of circle ideas but all showed nothing.
    - Starting again with a square did not work.
        - Finaly getting a square. This worked. It turned out the shapes were was outside the grid.
- Then created a diamond form.
- Then tried circle again, which finally worked.
--------------------------------------------------------------------------
## 9 -12-2021
- Adjusted the circle so it showed different kinds of cells.
- Adding the class agent chemo.
- Making sure the chemo was placed outside the tumour.
--------------------------------------------------------------------------
## 10 -12 -2021
- Starting on the expension of tumour, which was rather difficult.
--------------------------------------------------------------------------
## 12-12-2021
- Expansion tumour continued.
    - First only stem cells divided and pusshed them outwards.
    - This worked only took 10 minutes for one step, which was not really usefull.
- Then adjusted it so it also pushes all other cells outwards.
- However I realizing this is not realy feasable as it takes too long, which made me rethink my model.
--------------------------------------------------------------------------
## 13-12-2021
- Continued on rethinking my model, maybe different strategy. Eventually sticked with my old strategy, but try to make it more efficient.
- Adjusting Chemo_agent, so it could move.
- Adjusting interface by adding sliders.
- Redoing expansion tumour, making it more efficient. 
--------------------------------------------------------------------------
## 14-12-2021
- Adjusting the step of the model, so it will make sure 0.5% of cells will divide.
- Adjusting tumour agent so the side it will be pushed to is different every time, thus far it only moved to the top of the grid.
    - First random north, east, norhteast, etc.
    - Then more specific eg. if on top side it will only go north bottem side only will go south.
- Making sure the chemo steps every step.

--------------------------------------------------------------------------
## 15-12-2021
- Changed the tumour_agent when expanding to look around if there are any empty places.
- Changed choice_direction in tumour agent, to assure it will never be x_plus = 0 and y_plus = 0 (which would mean it does not move).
- Ensuring chemo agent only kills dividing cells
- Added death to tumour agent.
    - Killing cells (non dividing and transitional div) after a certain age (dividing 2x long then non div).
    - Killing cells with less then 2 surounding cells
- Adjust divide so that stem_cells can also split into transit amplifying.
--------------------------------------------------------------------------
## 16-12-2021
- Adjusting expand() instead of placing model everytime just move it (I truly don't know why I placed it at first). Now there are no two cells in one place. Changed dividing cells to 10%.
- Inserted graph with toal N cells and N cells per cell kind of cell.
- Moved divide to model instead of in tumour_agent.
- Adjusted death (tumour agent) and kill (chemo agent).
    - Made two seperate schedules for tumour agents and for chemo agents -> so the killing of cells will nog interfere.
    - In order to use datacollector the tumour agent schedule had to change from schedule_cells, schedule otherwise it would not work.
- Adjusted tumour agent, as it had agents double
- Removed errors from chemo_agent.
- Tried to ajust frame, so metastasis could be added. However, this was not possible as then there would be a recursion error. So I kept the grid at 75X75.
- Added worked_out to Chemo_agent.
--------------------------------------------------------------------------
## 17-12-2021
- Added new_chemo and removed chemo placement in init as it was now unnescecairy. Only kept the new_chemo() to initialize chemo.
- Removed the calling of function choice direction, to get a more round division of cells. Before it was more of an X shape.
- Added chemo repitition. Which can be every 10 steps to every 100 steps. based on 1-10 scale. 10 is very often 1 is rarely.
- Added vascularisation which has effect on how much the chemo will be moved towards the tumour.
- Stop the model if there are no stem cells left -> succes.
    - Stop the model if it hits the border of the grid -> fail.
- Add experiment, using batch runner, to model.
    - This takes as variabless the radius and concentration and returns a succes or fail and plots this.
- Add more experiment.
- Adjusted parameters if necesary.
--------------------------------------------------------------------------
## 20-12-2021
- Rewrote README.md.
- Adjusted points from review:
    - Added commandline arguments in runner.py.
    - Overall style adjustements.
    - Adjusted comments.
    - Put compute function in a seperate file.
- Added review.
- Added summary to each python file.
- Adjusted batch runs.
- Assesment.md added.
- LISCENCE.md added.

