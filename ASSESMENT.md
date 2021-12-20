# Tumor growth model - assesment
----------------------------------------------------
## Points to pay attention to 
- The duplication of cells and the movement caused by expand
- Visualization


------------------------------------------------------
## Biggest disicions

### the duplication of cells
    When creating the model it was quite difficult to duplicate the cells realistically. This meant that a cell had to duplicate and push the other cells outwards. This was not as simple and the first version took 10 minutes per step. At that moment I doubted wheter I should maybe make a model with only one kind of cells which just added a cell on the outside of the tumour. However, I thought this took away some of the best features of this model so I tried to make a better expand function which worked. This was more efficient, it still could possibly be more efficient, but for this time frame and my experience level this was already quite a efficient function.

### Making the grid bigger
    Later on I wanted to make the grid bigger. This so I could also possibly add metastasis. However when I tried to do this and got an recursion error. I tried to change this recursion limit, however this gave me a segmentation fault. So I either had to change my whole expand function or keep the grid small. So I decided to keep the grid small as this was still a decent size for the model. Thereby not adding metastasis.

### Chemo repetition
    I did add the option for the repitition of chemo dosis. The chemo slowly works out and dissapears. In real life chemo is also not given in one dose only therefore I decided that an extra feature of chemo repetition might be good (which was not in my original plan).

### Vascularisation
    When my models first version was finished the tumour was never killed. This was because the chemo agents always randomly moved and did not move significantly fast enough towards the tumour. Therefore it was not as representable. In reallife chemo goes through the blood and because tumours are highly vascularized it goes there faster. Therefore adding vascularisation which moves the blood towards the tumour (middle) was a good addition.

    I also doubted if I would let the chemo move towards the centre of the tumour mass (by taking the average of the cell coordinates) or the centre of the grid (where tumour is placed) and decided that it should be the centre of the grid. Vascularisation is not always perfect and thus does not always point to the middle. when the tumour grows it does not grow perfectly round so the middle mass would slightly move. Therefore moving towards the middle is atleast as representable as calculating the middle mass. 

### What biological characteristics to take into account and which not
    The biggest challenge for this model was to set its limits. Tumours are imensly complex and to take all factors into account is just not feasable. Therefore decisions had to be made, what to take into account and what not. This made that this model is a overly simplefied model of a tumour. However I do think it shows the interaction between characteristics of the tumour and the intensity of the treatment.

