# PHSX815_Project1

This repository contains two programs from which the remainder is generated: DieRollCat.py and DiceAnalysisCat.py. Random.py contains the random class used to create
categorical distributions given the probabilities of each die face.

Use:
DieRollCat.py --> in a command line, input "python DieRollCat.py -seed number -p1 number -p2 number -p3 number -p4 number -p5 number -p6 number -Nroll number -Nexp number -output filename
Default probabilities for a fair die; default Nexp = Nroll = 1; default output file False.

DiceAnalysisCat.py --> in a command line, input "python DiceAnalysisCat.py -input0 filename_H0_data -input1 filename_H1_data -prob0 probability_list_H0 -prob1 probability_list_H1
Each probability list should contain fraction elements, with each probability representing the chance of rolling any one face. E.g., for a fair die, [1/6, 1/6, 1/6, 1/6, 1/6, 1/6].
Output will be critical_lambda, beta, incidence of 3 distribution plot for both hypotheses, and LLR distribution plot for both hypotheses.
