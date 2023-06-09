from psychopy import visual, core, gui, data, event, monitors, sound, iohub
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from psychopy import locale_setup, prefs, sound, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from comppsychHelper import *

# import pylinkwrapper  # uncomment if necessary

# whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
from psychopy.hardware import keyboard

import os
import sys
import time
import copy
import random
import textwrap
import re
import numpy as np


# update march 2018-- include control variables which switch tracker on or off, use jitter or not for outcomes, control length of blocks

# control variables
usetrack=0      # use the eyetracker
usejitter=0     # jitter timings (e.g. for eye tracker)
blocklength=[0,0,0]    # number and length of blocks
leftstimx=-8    # x position left stimulus
rightstimx=8    # x position right stimulus
stimy=0         # y position main stimuli
outy=3        # y distance between main stimulus and outcome text
stimsize=3    # size of stimuli
boxwidth=2    # width of choice box
fixdur=1        # duration of fixation in secs
monitordur=1    # duration of monitor in secs
outcomedur1=1   # duration of first outcome in secs (if not jittered) (previously 1)
outcomedur2=1   # duration of second outcome in secs (if not jittered) (previously 1)
totmon=1.5      # starting amount of money
winloss=0.15    # amount won or lost per trial
_thisDir = os.path.dirname(os.path.abspath(__file__))   # where psychopy script is being run from
winsound=sound.Sound(os.path.join(_thisDir, 'stimuli','cha_ching.wav'))   # sound to play on win
losssound=sound.Sound(os.path.join(_thisDir,'stimuli','error2.wav'))     # sound to play on loss
minjit=2        # min jitter duration in secs
maxjit=6        # max jitter duration in secs
stimlets=['F','G','h','K','o','b','f','j','i']      # letters to be used as stimuli
#stimlets=['F','G']      # letters to be used as stimuli
blocknum=1      # counter for blocks
greyde=0        #grey degree of the circle at the top left corner for epoching


#if len(stimlets) < len(blocklength)*2:
#    sys.exit("not enought letter stimuli!")

# Ensure that relative paths start from the same directory as this script
os.chdir(_thisDir)

# Get the current date and format it as a string with the format "YYYY-MM-DD"
dateStr = time.strftime("%Y-%m-%d-%H%M", time.localtime())
expName = 'IBLT'

# experiment inf
expInfo = {
    'Participant_ID': 'P00',
    'Block Order':1,
    'Type': '',
    'dateStr':dateStr
}

# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# import experiment schedule
if expInfo['Type'] == '1':
    schedulefile = 'ScheduleNew.xlsx'
    blocklength=[60,120,80,80,80]
elif expInfo['Type'] == '2':
    schedulefile = 'ScheduleNew_v2.xlsx'
    blocklength=[40,40,120,80,80,80]


Sched = data.importConditions(os.path.join(_thisDir, 'schedules', schedulefile))
if sum(blocklength) != len(Sched):
    sys.exit("length of blocks does not sum to length of trials")

#edit this line above to short_version to run only 10 lines
#should normally be 2_opt_linked_80_10
#Block order 2 swaps winpos and losspos in schedule file!
if expInfo['Block Order']==2:
    wp=[d['winpos'] for d in Sched]
    lp=[d['losspos'] for d in Sched]
    for a in range(0,Sched.__len__()):
        Sched[a]['winpos']=lp[a]
        Sched[a]['losspos']=wp[a]



# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#make a text file to save data
# create the filename and data directory
filename = f"{expInfo['Participant_ID']}-{dateStr}.txt"
data_dir = os.path.join(_thisDir, 'data', expInfo['Participant_ID'])

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# open the data file in the data directory
dataFile = open(os.path.join(data_dir, filename), 'w') #a simple text file with 'tab-separated-values'

# data collected for each trial
trialdat=['Trialnumber','Winpos','Losspos','Side','Order','Choice','RT','Choiceside','Winchosen','LossChosen','TotalMoney','Fixonset','Choiceonset','Monitoronset','Winresonset','Lossresonset','stima','stimb','Blocknum']

# write basic info, task parameters and headers
writeToFile(dataFile,['Participant_ID',expInfo['Participant_ID'],'Block Order',expInfo['Block Order'],'Date', dateStr])
writeToFile(dataFile,trialdat)

# An ExperimentHandler isn't essential but helps with data saving
#thisExp = data.ExperimentHandler(name=expName, version='',
#    extraInfo=expInfo, runtimeInfo=None,
#    originPath='/Users/faissal/Library/CloudStorage/OneDrive-Nexus365/2023 – NAP Study/IBLT_Task/IBLT_Sharif/IBLT_lastrun.py',
#    savePickle=True, saveWideText=True,
#    dataFileName=filename)

# create a monitor object
m = monitors.Monitor('testMonitor')
# get the size of the monitor in pixels
monsize = m.getSizePix()
#create window and stimuli

win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', colorSpace='rgb', color=[0,0,0],
    blendMode='avg', useFBO=True, units='deg')
win.setColor('black')
win.mouseVisible = True

stima = visual.TextStim(win,text='a', units='deg', color='white',font='agathodaimon',height=stimsize)
stimb = visual.TextStim(win,text='b', units='deg', color='white',font='agathodaimon',height=stimsize)
choicebox = visual.ShapeStim(win, units='deg', lineWidth=4, lineColor=[0.8824, 0.6392, 0.4432], vertices=((-boxwidth, -boxwidth), (-boxwidth, boxwidth), (boxwidth, boxwidth), (boxwidth, -boxwidth)))
winmes = visual.TextStim(win,text='win',colorSpace='rgb',color=[0.0, 1.0, 0.0])
lossmes = visual.TextStim(win,text='loss',colorSpace='rgb',color=[1.0, 0.0 ,0.0])
fixation = visual.TextStim(win,text='X',color='white')
tottext = visual.TextStim(win,text=u'Total \xa3'+ str(round(totmon,2)),units='deg', colorSpace='rgb', color=[0.8824, 0.6392, 0.4432],height=1, pos=(0.0,-5.5))
circle = visual.Circle(win, units='deg', radius=3, pos=(-28.5,18), colorSpace='rgb255', color=greyde)

#Initiate eye-tracker link and open EDF
if usetrack:
    trackname=expInfo['Participant_ID'][0:4]+'_t'
    tracker = pylinkwrapper.Connect(win, trackname)   # note edf filename must be less than 9 characters. Use this and then rename on transfer. If you need to get it off the eyelink, look for file which is first 5 lets of subname then _t

# Calibrate eye-tracker
    tracker.calibrate()

#and some handy clocks to keep track of time
globalClock = core.Clock()

# set up stim
random.shuffle(stimlets)
stimcount=0
stima.setText(stimlets[stimcount])
stimb.setText(stimlets[stimcount+1])

# set mouse up
mouse = event.Mouse(visible=False, newPos=None, win=win)


#display instructions and wait
def pauseclick(text, win, mouse, pos=(0.0, 0.0), height=1.2, color=[1, 1, 1], wrap_width=100):
    """
    A function that displays a message and waits for the participant to click
    either button before continuing.

    Args:
        text (str): The message to be displayed.
        win (psychopy.visual.Window): The PsychoPy window in which to display the message.
        mouse (psychopy.event.Mouse): The PsychoPy mouse object used to detect clicks.
        pos (tuple): The position of the text stimulus (default is the center of the screen).
        height (float): The height of the text stimulus in visual degrees.
        color (list): The color of the text stimulus as an RGB triplet (values between 0 and 1).
    """
    #click = False
    left_press=False
    right_press=False
    win.setColor('black')
    text = re.sub(r'(?<=[.!]) +', '\n\n', text) # add line breaks after periods and exclamation points
    wrapped_text = "\n".join(textwrap.wrap(text, width=wrap_width))
    message = visual.TextStim(win=win, text=wrapped_text, pos=pos, height=height, color=color)
    #message.draw()
    #win.flip()
    while True not in (left_press, right_press):
        greyde = 0
        circle.setColor(greyde)
        circle.draw()
        message.draw()
        win.flip()
        (left_press,middle_press,right_press)=mouse.getPressed()
#    while not click:
#        message.draw()
#        win.flip()
#        buttons = mouse.getPressed()
#        if buttons[0] or buttons[1]:
#                click = True
#                core.wait(0.2)

pauseclick("Press left or right on the mouse to select a shape.\n Try to win as much money as possible! Click either button to start.", win, mouse)


#timer for task
taskclock=core.Clock()
taskclock.reset()
trialhandle=data.TrialHandler(Sched, nReps=1, method='sequential', dataTypes=trialdat, extraInfo=None, seed=None, originPath=None, name='', autoLog=True)



#start tracker
if usetrack:
    tracker.record_on()
ntrial=0
#for indtrial in range(0,10):
for thistrial in trialhandle:
    #thistrial=trialhandle.next()
    
    #part A
    if blocknum<=len(blocklength)-3:
        trialhandle.data.add('Trialnumber',ntrial+1)
        # allow to escape window
        if 'escape' in event.getKeys():
            core.quit()
        
        trialclock=core.Clock()
        rtclock=core.Clock()
        trialclock.reset()
        
        # use for timing of stimuli
        countDown = core.CountdownTimer()
        countDown.add(fixdur)
        
        trialhandle.data.add('stima',stima.text)
        trialhandle.data.add('stimb',stimb.text)        
        # present fixation cross for 1000ms (original one is 500ms)
        greyde = 40
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        fixonset=taskclock.getTime()
        if usetrack:
            msg='Fixation trial %d' % (ntrial+1)
            tracker.send_message(msg)
        win.flip()
        while countDown.getTime()>0:
            pass
        trialhandle.data.add('Fixonset',fixonset)
        if Sched[ntrial]['side'] == 1:
            stima.setPos([leftstimx,stimy])
            stimb.setPos([rightstimx,stimy])
        else:
            stimb.setPos([leftstimx,stimy])
            stima.setPos([rightstimx,stimy])
        
        greyde = 80
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        stima.draw()
        stimb.draw()
        if usetrack:
            msg='Choice trial %d' % (ntrial+1)
            tracker.send_message(msg)
        choiceonset=taskclock.getTime()
        win.flip()
        rtclock.reset()
        left_press=False
        right_press=False
        mouse.clickReset()
        while True not in (left_press, right_press):
            (left_press,middle_press,right_press),(left_time,mid_time,right_time)=mouse.getPressed(getTime=True)
        if left_press & right_press:
            if left_time<right_time:
                rt=left_time
                butpress='left'
            else:
                rt=right_time
                butpress='right'
        if left_press:
            rt=left_time
            butpress='left'
        if right_press:
            rt=right_time
            butpress='right'
        #resp=event.waitKeys(keyList=['b','m'], timeStamped=rtclock)
        trialhandle.data.add('Choiceside', butpress)
        trialhandle.data.add('RT', rt)
        trialhandle.data.add('Choiceonset',choiceonset)
        
        # figure out win/loss received
        if Sched[ntrial]['order'] == 1: # only consider win
            if butpress=='left':                                 #chose left option
                choicebox.setPos([leftstimx,stimy])
                if Sched[ntrial]['side']==1:                # option 1 on left
                    trialhandle.data.add('Choice',1)        #chose option 1
                    if Sched[ntrial]['winpos']==1:          # win for option 1
                        trialhandle.data.add('Winchosen',1)
                        totmon=totmon+winloss
                    else:
                        trialhandle.data.add('Winchosen',0)
                else:                                       # option 1 on right
                    trialhandle.data.add('Choice',0)        # chose option 2
                    if Sched[ntrial]['winpos']==1:          # win for option 1
                        trialhandle.data.add('Winchosen',0)
                    else:
                        trialhandle.data.add('Winchosen',1)
                        totmon=totmon+winloss
            else:                                           # chose right option
                choicebox.setPos([rightstimx,stimy])
                if Sched[ntrial]['side']==1:  
                    trialhandle.data.add('Choice',0)        #chose option 2
                    if Sched[ntrial]['winpos']==1:          # win for option 1
                        trialhandle.data.add('Winchosen',0)
                    else:
                        trialhandle.data.add('Winchosen',1)
                        totmon=totmon+winloss
                else:                                       #chose option 1
                    trialhandle.data.add('Choice',1)            #chose option 1
                    if Sched[ntrial]['winpos']==1:           # win for option 1
                        trialhandle.data.add('Winchosen',1)
                        totmon=totmon+winloss
                    else:
                        trialhandle.data.add('Winchosen',0)
            trialhandle.data.add('Losschosen',-1)    
        else: # only consider loss
            if butpress=='left':                                 #chose left option
                choicebox.setPos([leftstimx,stimy])
                if Sched[ntrial]['side']==1:                # option 1 on left
                    trialhandle.data.add('Choice',1)        #chose option 1
                    if Sched[ntrial]['losspos']==1:         # loss for option 1
                        trialhandle.data.add('Losschosen',1)
                        totmon=totmon-winloss
                    else:
                        trialhandle.data.add('Losschosen',0)
                else:                                       # option 1 on right
                    trialhandle.data.add('Choice',0)        # chose option 2
                    if Sched[ntrial]['losspos']==1:         # loss for option 1
                        trialhandle.data.add('Losschosen', 0)
                    else:
                        trialhandle.data.add('Losschosen',1)
                        totmon=totmon-winloss
            else:                                           # chose right option
                choicebox.setPos([rightstimx,stimy])
                if Sched[ntrial]['side']==1:  
                    trialhandle.data.add('Choice',0)        #chose option 2
                    if Sched[ntrial]['losspos']==1:         # loss for option 1
                        trialhandle.data.add('Losschosen', 0)
                    else:
                        trialhandle.data.add('Losschosen',1)
                        totmon=totmon-winloss
                else:                                       #chose option 1
                    trialhandle.data.add('Choice',1)            #chose option 1
                    if Sched[ntrial]['losspos']==1:             # loss for option 1
                        trialhandle.data.add('Losschosen',1)
                        totmon=totmon-winloss
                    else:
                        trialhandle.data.add('Losschosen',0)
            trialhandle.data.add('Winchosen',-1)

        # present participant choice
        greyde = 120
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        choicebox.draw()
        stima.draw()
        stimb.draw()
        if usetrack:
            msg='Monitor trial %d' % (ntrial+1)
            tracker.send_message(msg)
        monitoronset=taskclock.getTime()
        win.flip()
        countDown.reset()
        countDown.add(monitordur)
        while countDown.getTime()>0:
            pass
        trialhandle.data.add('Monitoronset',monitoronset)

        
        # now present outcomes
        if Sched[ntrial]['order'] == 1: # only consider win
            # present win
            if Sched[ntrial]['winpos']==1:              #i.e. win for option 1
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([leftstimx,outy])
                else:
                    winmes.setPos([rightstimx,outy])    #option 1 on right
            else:                                       # win for option 2
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([rightstimx,outy])
                else:
                    winmes.setPos([leftstimx,outy])    #option 1 on right
            greyde = 160
            circle.setColor(greyde)
            circle.draw()
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            winmes.draw()
            if usetrack:
                msg='Win Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            winresonset=taskclock.getTime()
            #lossresonset=taskclock.getTime()
            lossresonset = -1
            if trialhandle.data['Winchosen'][ntrial]==1:
                winsound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur1)
                
            while countDown.getTime()>0:
                core.wait(0.05)
            
            
        else:   # i.e. only consider loss 
            #present loss
            if Sched[ntrial]['losspos']==1:             #i.e. loss for option 1
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([leftstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([rightstimx,-outy])
            else:                                       #loss for option 2
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([rightstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([leftstimx,-outy])
            greyde = 200
            circle.setColor(greyde)
            circle.draw()
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            lossmes.draw()
            if usetrack:
                msg='Loss Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            lossresonset=taskclock.getTime()
            #winresonset=taskclock.getTime()
            winresonset = -1
            if trialhandle.data['Losschosen'][ntrial]==1:
                losssound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur2)
                
            while countDown.getTime()>0:
                core.wait(0.05)
            
            


                        
    #part B
    if blocknum>len(blocklength)-3:
        trialhandle.data.add('Trialnumber',ntrial+1)
        # allow to escape window
        if 'escape' in event.getKeys():
            core.quit()
        
        trialclock=core.Clock()
        rtclock=core.Clock()
        trialclock.reset()
        
        # use for timing of stimuli
        countDown = core.CountdownTimer()
        countDown.add(fixdur)
        
        trialhandle.data.add('stima',stima.text)
        trialhandle.data.add('stimb',stimb.text)
        # present fixation cross for 1000ms (original one is 500ms)
        greyde = 40
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        fixonset=taskclock.getTime()
        if usetrack:
            msg='Fixation trial %d' % (ntrial+1)
            tracker.send_message(msg)
        win.flip()
        while countDown.getTime()>0:
            pass
        trialhandle.data.add('Fixonset',fixonset)
        #now present both stimuli until choice made
        if Sched[ntrial]['side'] == 1:
            stima.setPos([leftstimx,stimy])
            stimb.setPos([rightstimx,stimy])
        else:
            stimb.setPos([leftstimx,stimy])
            stima.setPos([rightstimx,stimy])
            
        greyde = 80
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        stima.draw()
        stimb.draw()
        if usetrack:
            msg='Choice trial %d' % (ntrial+1)
            tracker.send_message(msg)
        choiceonset=taskclock.getTime()
        win.flip()
        rtclock.reset()
        left_press=False
        right_press=False
        mouse.clickReset()
        while True not in (left_press, right_press):
            (left_press,middle_press,right_press),(left_time,mid_time,right_time)=mouse.getPressed(getTime=True)
        if left_press & right_press:
            if left_time<right_time:
                rt=left_time
                butpress='left'
            else:
                rt=right_time
                butpress='right'
        if left_press:
            rt=left_time
            butpress='left'
        if right_press:
            rt=right_time
            butpress='right'
        #resp=event.waitKeys(keyList=['b','m'], timeStamped=rtclock)
        trialhandle.data.add('Choiceside', butpress)
        trialhandle.data.add('RT', rt)
        trialhandle.data.add('Choiceonset',choiceonset)
        # put the choice box in the correct place, work out which option was chosen and whether a win and/or loss was received
        
        if butpress=='left':                                 #chose left option
            choicebox.setPos([leftstimx,stimy])
            if Sched[ntrial]['side']==1:                # option 1 on left
                trialhandle.data.add('Choice',1)        #chose option 1
                if Sched[ntrial]['winpos']==1:          # win for option 1
                    trialhandle.data.add('Winchosen',1)
                    totmon=totmon+winloss
                else:
                    trialhandle.data.add('Winchosen',0)
                if Sched[ntrial]['losspos']==1:         # loss for option 1
                    trialhandle.data.add('Losschosen',1)
                    totmon=totmon-winloss
                else:
                    trialhandle.data.add('Losschosen',0)
            else:                                       # option 1 on right
                trialhandle.data.add('Choice',0)        # chose option 2
                if Sched[ntrial]['winpos']==1:          # win for option 1
                    trialhandle.data.add('Winchosen',0)
                else:
                    trialhandle.data.add('Winchosen',1)
                    totmon=totmon+winloss
                if Sched[ntrial]['losspos']==1:         # loss for option 1
                    trialhandle.data.add('Losschosen', 0)
                else:
                    trialhandle.data.add('Losschosen',1)
                    totmon=totmon-winloss
        else:                                           # chose right option
            choicebox.setPos([rightstimx,stimy])
            if Sched[ntrial]['side']==1:  
                trialhandle.data.add('Choice',0)        #chose option 2
                if Sched[ntrial]['winpos']==1:          # win for option 1
                    trialhandle.data.add('Winchosen',0)
                else:
                    trialhandle.data.add('Winchosen',1)
                    totmon=totmon+winloss
                if Sched[ntrial]['losspos']==1:         # loss for option 1
                    trialhandle.data.add('Losschosen', 0)
                else:
                    trialhandle.data.add('Losschosen',1)
                    totmon=totmon-winloss
            else:                                       #chose option 1
                trialhandle.data.add('Choice',1)            #chose option 1
                if Sched[ntrial]['winpos']==1:           # win for option 1
                    trialhandle.data.add('Winchosen',1)
                    totmon=totmon+winloss
                else:
                    trialhandle.data.add('Winchosen',0)
                if Sched[ntrial]['losspos']==1:             # loss for option 1
                    trialhandle.data.add('Losschosen',1)
                    totmon=totmon-winloss
                else:
                    trialhandle.data.add('Losschosen',0)
        
    
            
        # present participant choice
        greyde = 120
        circle.setColor(greyde)
        circle.draw()
        fixation.draw()
        tottext.draw()
        choicebox.draw()
        stima.draw()
        stimb.draw()
        if usetrack:
            msg='Monitor trial %d' % (ntrial+1)
            tracker.send_message(msg)
        monitoronset=taskclock.getTime()
        win.flip()
        countDown.reset()
        countDown.add(monitordur)
        while countDown.getTime()>0:
            pass
        trialhandle.data.add('Monitoronset',monitoronset)
        
        # now present outcomes
        if Sched[ntrial]['order']==1:                   # i.e. win first
            # present win
            
            if Sched[ntrial]['winpos']==1:              #i.e. win for option 1
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([leftstimx,outy])
                else:
                    winmes.setPos([rightstimx,outy])    #option 1 on right
            else:                                       # win for option 2
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([rightstimx,outy])
                else:
                    winmes.setPos([leftstimx,outy])    #option 1 on right
            greyde = 160
            circle.setColor(greyde)
            circle.draw()
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            winmes.draw()
            if usetrack:
                msg='Win Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            winresonset=taskclock.getTime()
            if trialhandle.data['Winchosen'][ntrial]==1:
                winsound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur1)
                
            while countDown.getTime()>0:
                core.wait(0.05)
            
            #now present loss
            if Sched[ntrial]['losspos']==1:             #i.e. loss for option 1
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([leftstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([rightstimx,-outy])
            else:                                       #loss for option 2
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([rightstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([leftstimx,-outy])
                
            greyde = 200
            circle.setColor(greyde)
            circle.draw()        
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            winmes.draw()
            lossmes.draw()
            if usetrack:
                msg='Loss Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            lossresonset=taskclock.getTime()
            if trialhandle.data['Losschosen'][ntrial]==1:
                losssound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur2)
            while countDown.getTime()>0:
                core.wait(0.05)
            
            
        else:   # i.e. loss first
            
            #present loss
            if Sched[ntrial]['losspos']==1:             #i.e. loss for option 1
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([leftstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([rightstimx,-outy])
            else:                                       #loss for option 2
                if Sched[ntrial]['side']==1:            # option 1 on left
                    lossmes.setPos([rightstimx,-outy])
                else:                                   #option 1 on right
                    lossmes.setPos([leftstimx,-outy])
    
            greyde = 200
            circle.setColor(greyde)
            circle.draw()
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            lossmes.draw()
            if usetrack:
                msg='Loss Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            lossresonset=taskclock.getTime()
            if trialhandle.data['Losschosen'][ntrial]==1:
                losssound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur2)
                
            while countDown.getTime()>0:
                core.wait(0.05)
            
            #win second
            if Sched[ntrial]['winpos']==1:              #i.e. win for option 1
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([leftstimx,outy])
                else:
                    winmes.setPos([rightstimx,outy])    #option 1 on right
            else:                                       # win for option 2
                if Sched[ntrial]['side']==1:             #option 1 on left
                    winmes.setPos([rightstimx,outy])
                else:
                    winmes.setPos([leftstimx,outy])    #option 1 on right
            
            greyde = 160
            circle.setColor(greyde)
            circle.draw()        
            fixation.draw()
            tottext.draw()
            choicebox.draw()
            stima.draw()
            stimb.draw()
            lossmes.draw()
            winmes.draw()
            if usetrack:
                msg='Win Outcome trial %d' % (ntrial+1)
                tracker.send_message(msg)
            winresonset=taskclock.getTime()
            if trialhandle.data['Winchosen'][ntrial]==1:
                winsound.play()
            win.flip()
            # present for outcome duration
            countDown.reset()
            if usejitter:
                countDown.add(flatjitter(minjit,maxjit,10))
            else:
                countDown.add(outcomedur1)
            while countDown.getTime()>0:
                core.wait(0.05)
        
        
    trialhandle.data.add('Winresonset',winresonset)
    trialhandle.data.add('Lossresonset',lossresonset) 
    trialhandle.data.add('TotalMoney',totmon)
    tottext.setText(u'Total \xa3'+ str(round(totmon,2)))
    # write data to a file at the end of each trial to make sure nothing is lost 
    td=trialhandle.data
    writeToFile(dataFile,list([int(td['Trialnumber'][ntrial]),Sched[ntrial]['winpos'],Sched[ntrial]['losspos'],Sched[ntrial]['side'],Sched[ntrial]['order'],
    int(td['Choice'][ntrial]),float(td['RT'][ntrial]),"".join(td['Choiceside'][ntrial]),int(td['Winchosen'][ntrial]),int(td['Losschosen'][ntrial]),round(totmon,2),
    fixonset,choiceonset,monitoronset,winresonset,lossresonset,stima.text,stimb.text,blocknum]))
        
    ntrial+=1
    if any(map(lambda x: ntrial == x, np.cumsum(blocklength[:-1]))):
        blocknum+=1
        stimcount=stimcount+2
        stima.setText(stimlets[stimcount])
        stimb.setText(stimlets[stimcount+1])
        pauseclick("Well done! You can now take a break. Press either button to continue.", win, mouse)
        print("User paused the task")
    
if usetrack:
#stop tracker
    tracker.record_off()
# Retrieve EDF
    tracker.end_experiment(os.path.join(_thisDir,'results','tracker'))
    os.rename(os.path.join(_thisDir,'results','tracker',trackname+'.edf'),os.path.join(_thisDir,'results','tracker',filename+'_tracker.edf'))

# just in case-- at end of task save all data again
trialhandle.saveAsText(os.path.join(data_dir, filename), dataOut=['Choice_raw', 'Choiceside_raw','RT_raw', 'Winchosen_raw','Losschosen_raw'])


pauseclick("Thank you!", win, mouse)
win.close()
core.quit()