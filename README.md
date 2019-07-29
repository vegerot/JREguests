# JREguests
This is a program that will generate a list of the most frequent guests that have appeared on the Joe Rogan Experience

steps to run:
1. `git clone https://github.com/vegerot/JREguests.git`
2. `./api.py`
3. profit?

Bugs:
* This is not perfect.  It does not take into account things like:

* *Nicknames (e.g. Joey "CoCo" Diaz vs. Joey Diaz)
* *Alternate spellings (e.g. Neil deGrasse Tyson vs. Neil DeGrasse Tyson)
*For some reason, Dom Irrera's episode has been blocked on copywrite grounds.  Workarounds for this have been put in place
Please, if anybody wants to work on fixing these issues, please feel free to fork me!


Options:
*Downloading the titles of all the videos are slow.  
By default the videos are pulled from an already-downloaded set (`allTitles.txt`) that includes everything as of 7/28/2019
To get more recent videos included, uncomment line #51 and comment line #54
*I am not including people that have only appeared once.  To see all guests, simply print `viewCounts` instead of `relevantCounts`

Feel free to fork me!
