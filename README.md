# Implicit Bias Learning Task (IBLT)

##  Overview
The IBLT is a probabilistic learning task where participants aim to maximize monetary rewards across **480 trials** and **6 phases**. Participants are presented with two shapes, selecting between them to either win (+£0.15), lose (-£0.15), or neither (±£0.00). The probabilistic characteristics of these wins and losses are manipulated during each phase. All of these metrics can be adjusted in the code and the schedule files.

- **Learning Objective**: Participants associate choices with a reward and/or loss and adapt behavior when previously learned reward patterns are reversed.
- **Reversal Learning**: Demands participants to adapt to changing reward/loss patterns across phases, generating prediction errors when outcomes are not as expected.

</br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/158cfa23-fdf2-44cf-bf70-9a8f629a7949" alt="IBLT2" height="300"/>
</p>
</br>


## Phases and Trials
- **Total Trials**: 480
- **Phases**: 6 (80 trials per phase)
- **Shape Alternation**: Shapes alternate left-right positions randomly across trials.

Each shape has a phase-specific probability of winning or losing, which may be **stable** (50%) or **volatile** (15%-85%). These probabilities switch after a minimum of 4 trials to enhance learning of perceived patterns and elicit prediction errors.

### Probabilistic Evolution
- **Stable Phases**: Win/Loss probabilities remain fixed at 50%.
- **Volatile Phases**: Win/Loss probabilities fluctuate between 15% and 85%, forcing participants to adapt their learning patterns.
</br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/fa5dd8aa-726e-4198-99b1-a905493ee0a3" alt="IBLT" height="300"/>
</p>
</br>


## Folder Structure
- **/data/**: Contains participant data from the experiment.
- **/schedules/**: Contains Excel files that dictate the trial sequences and conditions.
  - `ScheduleNew_short.xlsx`: Short version of the schedule.
  - `ScheduleNew_v2.xlsx`: Alternative schedule.
  - `ScheduleNew_v3.xlsx`: Latest version of the schedule.
- **/matlab/**: Contains MATLAB scripts, if applicable.
- **/pylinkwrapper/**: Files related to interfacing with eye-tracking.
- **/stimuli/**: Contains images of the shapes used in the task.


## Setting Up and Running the Task
1. **Open PsychoPy**:
   - Double-click to launch the software.

2. **Add the pylinkwrapper Path**:
   - Go to **Builder > File > Preferences > General > Path**.
   - Add the path to the `pylinkwrapper` folder (e.g., `"D:\RL\psychopy\pylinkwrapper"`).
   - Apply changes and confirm.

3. **Open the IBLT Code**:
   - In **Runner > File > Add**, select `IBLT_Sharif_Huang.py`.
   - The code will appear in the Runner window.

4. **Install Dependencies**:
   - Ensure all necessary packages listed in the Python code are installed.

5. **Run the Experiment**:
   - Click **Coder > Run Experiment** to start the task.

## Customizing Parameters
You can modify several parameters within the code to adjust the task settings:
- **totmon**: Adjusts the initial monetary value.
- **winpos**: Determines which symbol is associated with a win.
  - `winpos=1`: Associates "stima" with a win.
  - `winpos=0`: Associates "stimb" with a win.
- **losspos**: Determines which symbol is associated with a loss.
  - `losspos=1`: Associates "stima" with a loss.
  - `losspos=0`: Associates "stimb" with a loss.
- **side**: Controls which side the shapes appear on.
  - `side=1`: "stima" on the left, "stimb" on the right.
  - `side=0`: "stimb" on the left, "stima" on the right.
- **order**: Defines the order of presenting win/loss outcomes.
  - `order=1`: Win presented first.
  - `order=0`: Loss presented first.

### Block Orders
Two block orders (A and B) are available, which swap win/loss conditions in the final phases:
- **Block Order A**: 
  - 5th block: loss-volatile, win-stable.
  - 6th block: win-volatile, loss-stable.
- **Block Order B**:
  - 5th block: win-volatile, loss-stable.
  - 6th block: loss-volatile, win-stable.


## Task Dynamics

### Learning Process
Participants are asked to maximize their monetary gains by learning the win/loss patterns across 6 phases. Each phase presents shapes with probabilistic win/loss outcomes, which can be stable or volatile, and participants must adapt their choices based on the evolving conditions. Sudden switches in probability enhance learning and prediction error measurement.

### Prediction Errors
- **Positive Prediction Error**: Occurs when an expected loss turns into a win.
- **Negative Prediction Error**: Occurs when an expected win turns into a loss.
- Participants' attention to these prediction errors influences their learning rate, particularly for loss patterns, which may be more pronounced in negative affective biases.

## Additional Information
- This version of the IBLT is based on the design by [Pulcu & Browning (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5633345/) and adapted for this experiment.
- The task is programmed in PsychoPy 2023.1.1.

## Contact
For questions or issues regarding the experiment, please contact [**Faissal Sharif**](mailto:faissal.sharif@stx.ox.ac.uk).
