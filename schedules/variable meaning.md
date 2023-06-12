winpos: indicates the symbol which connects with "win". 
	For winpos=1, stima will be connected with "win", while stimb will be connected with "win" if winpos=0.
losspos: indicates the symbol which connects with "loss".
	For losspos=1, stima will be connected with "loss", while stimb will be connected with "loss" if losspos=0.
side: indicates the side at which the symbol is presented at the screen. 
	For side=1, stima will be presented at the left side, while stimb will be presented at the right side. 
	For side=0, the two stim symbols will be presented at the opposite side.
order: indicates the order of presenting "win" and/or "loss". 
	For the first three blocks, order=1 means only "win" is presented in this trial, while 0 means only "loss". 
	For the last three blocks, order=1 means "win" is presented first in this trial, while 0 means "loss" is presented first.
*example:

	if winpos=1, losspos=0, side=1, order=0:
                                     W 
A  x  B  ->  A  x  B  ->  A  x  B 
                           L                L

	if winpos=1, losspos=0, side=0, order=0:
                                            W 
B  x  A  ->  B  x  A  ->  B  x  A 
                   L                L

block order: swap the "winpos" and "losspos" columns in the schedule file, thus swapping the volatility/stability of "win" and "loss" at the last three blocks.


