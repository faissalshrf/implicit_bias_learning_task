# IBLT Paradigm

This readme provides instructions for setting up and running the "PsychoPy" software along with the "IBLT_Sharif_Huang.py" code. The following steps outline the process:

1. Double-click on "PsychoPy" to open the software.
2. Add the path for "pylinkwrapper" in the preferences:
   - Go to Builder > File > Preference > General > Path.
   - Add the path of "pylinkwrapper" (e.g., "D:\RL\psychopy\pylinkwrapper").
   - Apply the changes and confirm.
3. Open the code:
   - Go to Runner > File > Add.
   - Open "IBLT_Sharif_Huang.py".
   
Now, you should see the file appear in the Runner window. Double-clicking the file will open the Coder, displaying the code. Make sure to install all the packages mentioned in the code.

If everything is set up correctly, follow these steps to run the code and see the experiment interface:

1. Click on Coder > Run Experiment.
2. The experiment interface will appear.

In the experiment, participants are asked to click the left or right button to choose the corresponding symbol. You can modify various parameters listed in the first few lines of the code. Some examples of parameters you can change are:

- `totmon/winloss`: Adjusts the stimulation strength.
- `outcomedur1/2`: Controls the experiment and waiting time.
- `winpos`: Indicates the symbol connected with "win".
  - Setting `winpos=1` connects "stima" with "win".
  - Setting `winpos=0` connects "stimb" with "win".
- `losspos`: Indicates the symbol connected with "loss".
  - Setting `losspos=1` connects "stima" with "loss".
  - Setting `losspos=0` connects "stimb" with "loss".
- `side`: Indicates the side at which the symbol is presented on the screen.
  - Setting `side=1` presents "stima" on the left side and "stimb" on the right side.
  - Setting `side=0` presents the two stim symbols on opposite sides.
- `order`: Indicates the order of presenting "win" and/or "loss".
  - For the first three blocks, `order=1` means only "win" is presented, while `order=0` means only "loss" is presented.
  - For the last three blocks, `order=1` means "win" is presented first, while `order=0` means "loss" is presented first.

Here's an example illustrating the symbol placement based on different parameter values:

- If `winpos=1`, `losspos=0`, `side=1`, and `order=0`:

```
             W 
A  x  B  ->  A  x  B  ->  A  x  B 
                   L            L
```

- If `winpos=1`, `losspos=0`, `side=0`, and `order=0`:

```
             W 
B  x  A  ->  B  x  A  ->  B  x  A 
                   L            L
```

The "block order" parameter swaps the "winpos" and "losspos" columns in the schedule file, resulting in a swap of volatility/stability for "win" and "loss" in the last three blocks. Two possible block orders are:

- Block order A:
  - 5th block: loss-volatile, win-stable.
  - 6th block: win-volatile, loss-stable.
  
- Block order B:
  - 5th block: win-volatile, loss-stable.
  - 6th block: loss-volatile, win-stable.

Please make sure to refer to the code and relevant documentation for further details and instructions.