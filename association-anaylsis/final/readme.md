
#How to Run
The Association Rule code starts with the main.py
The folders in the data, input and result are empty.
I've just added them so that it makes life much easier for you to execute.
Just place the .data file in input/whatever-dataset you want test.
I've added links of the dataset in the main.pdf

#Preproccessing
To generate the initial data.p file,  simply look for the preprocess script and then the transx script for that dataset.

Run them in the order
1.) Preprocess
2.) Transx

#Now you are all set to go.

#Calculation and Result
1.) For each of the support value and for each confidence in that I've written a calling for loop
2.) Currently it is commented out but you should be able to run one instance
3.) In case if you plan to run all 9 in one go, uncomment it.
4.) It will take a little bit, but I've tried to optimise it.

Results can be found in results folder and the console will show you
1.) Candidates
2.) Frequent
3.) Maximal
4.) Closed
5.) Total Relations built

Also to flip the use of Fk-1 * Fk-1 & Fk-1 * F1 just go to apriori and the seventh line and uncomment one and comment the other

Similarly to flip the use of confidence for lift go to ruleGen.py and do the same in calc_conf function

The excel file will show you the pruned one.

Thank You! :)