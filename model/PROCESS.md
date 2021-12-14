
# logbook

## 7-12-2021
- Creating framework
- make sure it shows agents again because they did not work
- creating circle-> not even close 

## 8-12-2021
- creating circle
    - trying many different kinds of circle ideas but all showed nothing
    - starting again with a square did not work
        - finaly getting a square -> turns out it was outside the grid
- then made a diamond
- then tried circle again -> finaly worked

## 9 -12-2021
- adjusting circle so it showed different kinds of cells
- adding agent chemo
- making sure the chemo was printend and not on the tumour

## 10 -12 -2021
- starting on the expension of tumour -> did not come so far

## 12-12-2021
- expansion tumour
    - first only stem cells -> pusshing outwards
    - only takes 10 minutes for one step -> not really usefull
- then adjusted it so it also pushes all other cells outwards
- realizing this is not realy feasable as it takes too long -> rethink my model

## 13-12-2021
- regretting my model choice
- adjusting Chemo_agent -> making it move
- adjusting interface -> adding sliders
- redoing expansion tumour -> make it more efficient

## 14-12-2021
- adjusting the step so it will make sure 0.5% of cells will do a step
- adjusting tumour agent so the side it will be pushed to is variable 
    - first random north, east, norhteast, etc
    - then more specific eg. if on top side it will only go north bottem side only will go south
- trying to find out if I can adjust a model variable in the agent class
