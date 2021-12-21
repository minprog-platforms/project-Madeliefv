# Tumor growth model - assesment
----------------------------------------------------
## Points to pay attention to 

### Code
In the code I mainly looked at how I could represent the model as correctly as possible. Therefore the tumour had to grow as naturally as possbile. The biggest challenge and the thing I thus put the most effort in is the duplicate and mainly expand function. This function has had many different versions and eventhough this version is not perfect I think it is still quite a good function. Thereby I also tried to adjust the parameters in such a way that the tumour progressed as naturally as possible. This took some adjustments as there are quite a lot of factors that have an influence on the tumour growth. Even the non-variable factors like the chance a division becomes one cell or the other or the chance a cell dies.

### Interactieontwerp
To make the interaction as good as possible I made a live visualisation. This allowed the user to see Visualization, and to do adjustments to the variables very easily because of the sliders. Thereby I also added a nice graph that showed the number of cells even per cell type. I think the live visualization is the most important part of the interactieontwerp. Thereby I also added a command line argument which made it easier for the user to run certain experiments.

### Repository en documentatie
To really understand why I made certain choices for the model some background is required. This I also added in the documentation. I also tried to show as much as possible why the these choices are made in the README file, but also tried to keep it as much to the point as possible. So I hope the README gives a clear overview for the user. As I tried to explain the related background connected to certain parts of the model as much as possible.


------------------------------------------------------
## Biggest disicions

### The duplication of cells
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


### Screencast
It was very difficult to show all features and explain exactly how my model worked in only 6 minutes. Therefore I had to make some cuts. I therefore decided not to show the runner file where the experiments are shown and the visualizations. I also could not go into the conclusions and functionality as deeply as I would have liked and I had to talk really fast. If I would have more time I would  

