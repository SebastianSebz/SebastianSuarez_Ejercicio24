import numpy as np
import matplotlib.pyplot as plt

#prob. de medir lambda de 0 a 1
Prob0a1 = 0
#prob. de medir lambda de 1 a 20
Prob1a20 = 1

prb = 99

def ProbLambda(lamb):
    if((lamb < 1) or (lamb > 100):

       return 0

    else:
       return 1/prb

def distr(lamb, x):

	distr = (1/lamb)*np.exp((-1)*(x/lamb))
	return distr

x = [1.2, 2.5, 2.8, 5.0]

#def prob_x











