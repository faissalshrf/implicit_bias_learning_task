#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Apr  4 18:49:30 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'IBLT'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/faissal/Library/CloudStorage/OneDrive-Nexus365/2023 – NAP Study/IBLT/IBLT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Start" ---
InstrBkg = visual.Rect(
    win=win, name='InstrBkg',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
PreCondImage = visual.ImageStim(
    win=win,
    name='PreCondImage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0.05], size=[0.45,0.9],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PreCondInstEN = visual.TextStim(win=win, name='PreCondInstEN',
    text='',
    font='Helvetica',
    pos=[0,0.7], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
PreCondInstCN = visual.TextStim(win=win, name='PreCondInstCN',
    text='',
    font='PingFang SC',
    pos=(-0.2,0.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
InstrKeyResp = keyboard.Keyboard()
PreCondMouse = event.Mouse(win=win)
x, y = [None, None]
PreCondMouse.mouseClock = core.Clock()
PreCondSubmit = visual.ButtonStim(win, 
    text='CONTINUE', font='Helvetica',
    pos=[0.7, -0.8],
    letterHeight=0.06,
    size=[0.3, 0.1], borderWidth=0.0,
    fillColor=[0.8824, 0.6392, 0.4432], borderColor=None,
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='PreCondSubmit'
)
PreCondSubmit.buttonClock = core.Clock()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from code


from psychopy import  visual, core, gui, data, event, monitors, sound, iohub
import copy, time, os, sys, random #from the std python libs
from psychopy.tools.filetools import fromFile, toFile
from comppsychHelper import *
#import pylinkwrapper


# update march 2018-- include control variables which switch tracker on or off, use jitter or not for outcomes, control length of blocks

# control variables
usetrack=0      # use the eyetracker
usejitter=0     # jitter timings (e.g. for eye tracker)
blocklength=[80,80,80]    # number and length of blocks
leftstimx=-6    # x position left stimulus
rightstimx=6    # x position right stimulus
stimy=0         # y position main stimuli
outy=2.2        # y distance between main stimulus and outcome text
stimsize=1.8    # size of stimuli
boxwidth=1.6    # width of choice box
fixdur=1        # duration of fixation in secs
monitordur=1    # duration of monitor in secs
outcomedur1=0.5   # duration of first outcome in secs (if not jittered) (previously 1)
outcomedur2=0.5   # duration of second outcome in secs (if not jittered) (previously 1)
totmon=1.5      # starting amount of money
winloss=0.15    # amount won or lost per trial
main_dir=os.getcwd()   # where psychopy script is being run from
winsound=sound.Sound(os.path.join(main_dir, 'stimuli','cha_ching.wav'))   # sound to play on win
losssound=sound.Sound(os.path.join(main_dir,'stimuli','error2.wav'))     # sound to play on loss
minjit=2        # min jitter duration in secs
maxjit=6        # max jitter duration in secs
#stimlets=[''F','G','h','K','o','b','f','j','i']      # letters to be used as stimuli
stimlets=['F','G']      # letters to be used as stimuli

blocknum=1      # counter for blocks


#if len(stimlets) < len(blocklength)*2:
#    sys.exit("not enought letter stimuli!")

os.chdir(main_dir)

# date as month, day hour min

dateStr = time.strftime("%b_%d_%H%M", time.localtime())#add the current time

# experiment inf
expInfo = {'Subject Num':'', 'Block Order':1, 'dateStr':dateStr}

# window stuff
mm=monitors.Monitor('testMonitor')
monsize=mm.getSizePix()



# get subject number and block order
while expInfo['Subject Num']=='' or (expInfo['Block Order']!= 1 and expInfo['Block Order']!=2):
    enterSubjInfo(expInfo, 'simple voltrain experiment')


# import experiment schedule
Sched=data.importConditions(os.path.join(main_dir,'schedules','2_opt_linked_80_10.xlsx'))   # ths should point to the schedule file
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

#make a text file to save data
fileName = expInfo['Subject Num'] + '_' + expInfo['dateStr']
dataFile = open(os.path.join(main_dir,'results',fileName+'.txt'), 'w')#a simple text file with 'taba-separated-values'

# data collected for each trial
trialdat=['Trialnumber','Winpos','Losspos','Side','Order','Choice','RT','Choiceside','Winchosen','LossChosen','TotalMoney','Fixonset','Choiceonset','Monitoronset','Winresonset','Lossresonset','stima','stimb','Blocknum']


# write basic info, task parameters and headers
writeToFile(dataFile,['Subject Num',expInfo['Subject Num'],'Block Order',expInfo['Block Order'],'date',expInfo['dateStr']])
writeToFile(dataFile,trialdat)

#create window and stimuli
win = visual.Window(monsize,fullscr=True,allowGUI=False, monitor='testMonitor', units='deg', screen=1)
stima = visual.TextStim(win,text='a', units='deg', color='black',font='agathodaimon',height=stimsize)
stimb = visual.TextStim(win,text='b', units='deg', color='black',font='agathodaimon',height=stimsize)
choicebox=visual.ShapeStim(win, units='deg', lineWidth=4, fillColor='grey', lineColor='black',fillColorSpace='rgb', vertices=((-boxwidth, -boxwidth), (-boxwidth, boxwidth), (boxwidth, boxwidth),(boxwidth,-boxwidth)))
winmes=visual.TextStim(win,text='win',colorSpace='rgb',color=[0.0, 1.0, 0.0])
lossmes=visual.TextStim(win,text='loss',colorSpace='rgb',color=[1.0, 0.0 ,0.0])
fixation = visual.TextStim(win,text='X',color='black')
tottext=visual.TextStim(win,text=u'Total \xa3'+ str(totmon),units='deg',color='black',height=1, pos=(0.0,-2))

#Initiate eye-tracker link and open EDF
if usetrack:
    trackname=expInfo['Subject Num'][0:4]+'_t'
    tracker = pylinkwrapper.Connect(win, trackname)   # note edf filename must be less than 9 characters. Use this and then rename on transfer. If you need to get it off the eyelink, look for file which is first 5 lets of subname then _t

# Calibrate eye-tracker
    tracker.calibrate()

#and some handy clocks to keep track of time
globalClock = core.Clock()

# set up stim
#random.shuffle(stimlets)
stimcount=0
stima.setText(stimlets[stimcount])
stimb.setText(stimlets[stimcount+1])

# set mouse up
mouse = event.Mouse(visible=False, newPos=None, win=win)

#display instructions and wait
pauseclick("Press left or right to select a shape\nTry to win as much money as possible\n\nClick Either Button to Start",win,mouse)


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
    # present fixation cross for 500ms
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
    tottext.setText(u'Total \xa3'+ str(totmon))
    # write data to a file at the end of each trial to make sure nothing is lost 
    td=trialhandle.data
    writeToFile(dataFile,list([int(td['Trialnumber'][ntrial]),Sched[ntrial]['winpos'],Sched[ntrial]['losspos'],Sched[ntrial]['side'],Sched[ntrial]['order'],
    int(td['Choice'][ntrial]),float(td['RT'][ntrial]),"".join(td['Choiceside'][ntrial]),int(td['Winchosen'][ntrial]),int(td['Losschosen'][ntrial]),totmon,
    fixonset,choiceonset,monitoronset,winresonset,lossresonset,stima.text,stimb.text,blocknum]))
    
    ntrial+=1
    
    if any(map(lambda x: ntrial == x, np.cumsum(blocklength[:-1]))):
        blocknum+=1
        stimcount=stimcount+2
        stima.setText(stimlets[stimcount])
        stimb.setText(stimlets[stimcount+1])
        pauseclick("Rest Session\nPress Either Button to Restart",win,mouse)
    
if usetrack:
#stop tracker
    tracker.record_off()
# Retrieve EDF
    tracker.end_experiment(os.path.join(main_dir,'results','tracker'))
    os.rename(os.path.join(main_dir,'results','tracker',trackname+'.edf'),os.path.join(main_dir,'results','tracker',fileName+'_tracker.edf'))

# just in case-- at end of task save all data again
trialhandle.saveAsText(os.path.join(main_dir,'results',fileName), dataOut=['Choice_raw', 'Choiceside_raw','RT_raw', 'Winchosen_raw','Losschosen_raw'])




win.close()
core.quit()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('0_Instructions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Start" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    PreCondImage.setImage(PreCondInstTextImage)
    PreCondInstEN.setText(PreCondInstTextEN)
    PreCondInstCN.setText(PreCondInstTextCN)
    InstrKeyResp.keys = []
    InstrKeyResp.rt = []
    _InstrKeyResp_allKeys = []
    # setup some python lists for storing info about the PreCondMouse
    PreCondMouse.x = []
    PreCondMouse.y = []
    PreCondMouse.leftButton = []
    PreCondMouse.midButton = []
    PreCondMouse.rightButton = []
    PreCondMouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    StartComponents = [InstrBkg, PreCondImage, PreCondInstEN, PreCondInstCN, InstrKeyResp, PreCondMouse, PreCondSubmit]
    for thisComponent in StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Start" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstrBkg* updates
        if InstrBkg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrBkg.frameNStart = frameN  # exact frame index
            InstrBkg.tStart = t  # local t and not account for scr refresh
            InstrBkg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrBkg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrBkg.started')
            InstrBkg.setAutoDraw(True)
        
        # *PreCondImage* updates
        if PreCondImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PreCondImage.frameNStart = frameN  # exact frame index
            PreCondImage.tStart = t  # local t and not account for scr refresh
            PreCondImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondImage.started')
            PreCondImage.setAutoDraw(True)
        
        # *PreCondInstEN* updates
        if PreCondInstEN.status == NOT_STARTED and isChinese==False:
            # keep track of start time/frame for later
            PreCondInstEN.frameNStart = frameN  # exact frame index
            PreCondInstEN.tStart = t  # local t and not account for scr refresh
            PreCondInstEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstEN.started')
            PreCondInstEN.setAutoDraw(True)
        
        # *PreCondInstCN* updates
        if PreCondInstCN.status == NOT_STARTED and isChinese==True:
            # keep track of start time/frame for later
            PreCondInstCN.frameNStart = frameN  # exact frame index
            PreCondInstCN.tStart = t  # local t and not account for scr refresh
            PreCondInstCN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondInstCN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondInstCN.started')
            PreCondInstCN.setAutoDraw(True)
        
        # *InstrKeyResp* updates
        waitOnFlip = False
        if InstrKeyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrKeyResp.frameNStart = frameN  # exact frame index
            InstrKeyResp.tStart = t  # local t and not account for scr refresh
            InstrKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrKeyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrKeyResp.started')
            InstrKeyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrKeyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrKeyResp.status == STARTED and not waitOnFlip:
            theseKeys = InstrKeyResp.getKeys(keyList=['space'], waitRelease=False)
            _InstrKeyResp_allKeys.extend(theseKeys)
            if len(_InstrKeyResp_allKeys):
                InstrKeyResp.keys = _InstrKeyResp_allKeys[-1].name  # just the last key pressed
                InstrKeyResp.rt = _InstrKeyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *PreCondMouse* updates
        if PreCondMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondMouse.frameNStart = frameN  # exact frame index
            PreCondMouse.tStart = t  # local t and not account for scr refresh
            PreCondMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('PreCondMouse.started', t)
            PreCondMouse.status = STARTED
            PreCondMouse.mouseClock.reset()
            prevButtonState = PreCondMouse.getPressed()  # if button is down already this ISN'T a new click
        if PreCondMouse.status == STARTED:  # only update if started and not finished!
            buttons = PreCondMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = PreCondMouse.getPos()
                    PreCondMouse.x.append(x)
                    PreCondMouse.y.append(y)
                    buttons = PreCondMouse.getPressed()
                    PreCondMouse.leftButton.append(buttons[0])
                    PreCondMouse.midButton.append(buttons[1])
                    PreCondMouse.rightButton.append(buttons[2])
                    PreCondMouse.time.append(PreCondMouse.mouseClock.getTime())
        
        # *PreCondSubmit* updates
        if PreCondSubmit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            PreCondSubmit.frameNStart = frameN  # exact frame index
            PreCondSubmit.tStart = t  # local t and not account for scr refresh
            PreCondSubmit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCondSubmit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCondSubmit.started')
            PreCondSubmit.setAutoDraw(True)
        if PreCondSubmit.status == STARTED:
            # check whether PreCondSubmit has been pressed
            if PreCondSubmit.isClicked:
                if not PreCondSubmit.wasClicked:
                    PreCondSubmit.timesOn.append(PreCondSubmit.buttonClock.getTime()) # store time of first click
                    PreCondSubmit.timesOff.append(PreCondSubmit.buttonClock.getTime()) # store time clicked until
                else:
                    PreCondSubmit.timesOff[-1] = PreCondSubmit.buttonClock.getTime() # update time clicked until
                if not PreCondSubmit.wasClicked:
                    continueRoutine = False  # end routine when PreCondSubmit is clicked
                    None
                PreCondSubmit.wasClicked = True  # if PreCondSubmit is still clicked next frame, it is not a new click
            else:
                PreCondSubmit.wasClicked = False  # if PreCondSubmit is clicked next frame, it is a new click
        else:
            PreCondSubmit.wasClicked = False  # if PreCondSubmit is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Start" ---
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if InstrKeyResp.keys in ['', [], None]:  # No response was made
        InstrKeyResp.keys = None
    trials.addData('InstrKeyResp.keys',InstrKeyResp.keys)
    if InstrKeyResp.keys != None:  # we had a response
        trials.addData('InstrKeyResp.rt', InstrKeyResp.rt)
    # store data for trials (TrialHandler)
    trials.addData('PreCondMouse.x', PreCondMouse.x)
    trials.addData('PreCondMouse.y', PreCondMouse.y)
    trials.addData('PreCondMouse.leftButton', PreCondMouse.leftButton)
    trials.addData('PreCondMouse.midButton', PreCondMouse.midButton)
    trials.addData('PreCondMouse.rightButton', PreCondMouse.rightButton)
    trials.addData('PreCondMouse.time', PreCondMouse.time)
    trials.addData('PreCondSubmit.numClicks', PreCondSubmit.numClicks)
    if PreCondSubmit.numClicks:
       trials.addData('PreCondSubmit.timesOn', PreCondSubmit.timesOn)
       trials.addData('PreCondSubmit.timesOff', PreCondSubmit.timesOff)
    else:
       trials.addData('PreCondSubmit.timesOn', "")
       trials.addData('PreCondSubmit.timesOff', "")
    # the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = []
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
