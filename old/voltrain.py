from psychopy import core, visual, gui, data, event
import copy, time, os, sys #from the std python libs
from psychopy.tools.filetools import fromFile, toFile

# control variables

leftstimx=-8
rightstimx=8
stimy=0
outy=2.5
stimsize=2
boxwidth=2
fixdur=1
monitordur=1
outcomedur1=1
outcomedur2=1




main_dir='C:\\Users\\michaelb\\Documents\\MRC_intermediate_fellowship\\training_task\\psychopy'
os.chdir(main_dir)

# date as month, day hour min

dateStr = time.strftime("%b_%d_%H%M", time.localtime())#add the current time

# experiment info
expInfo = {'Subject Num':'', 'Traintype':1, 'dateStr':dateStr}

# get subject number and training type
dlg = gui.DlgFromDict(expInfo, title='simple voltrain experiment', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)#save params to file for next time

# import experiment schedule
Sched=data.importConditions("schedules\\2_opt_linked_80_10.xlsx")

#make a text file to save data
fileName = expInfo['Subject Num'] + expInfo['dateStr']
dataFile = open(os.path.join(main_dir,'results',fileName+'.csv'), 'w')#a simple text file with 'comma-separated-values'


#create window and stimuli
win = visual.Window((1600, 1200),fullscr=False,allowGUI=True, monitor='testMonitor', units='deg', screen=1)
stima = visual.TextStim(win,text='a', units='deg', color='black',font='agathodaimon',height=stimsize)
stimb = visual.TextStim(win,text='b', units='deg', color='black',font='agathodaimon',height=stimsize)
choicebox=visual.ShapeStim(win, units='deg', lineWidth=4, fillColor='grey', lineColor='black',fillColorSpace='rgb', vertices=((-boxwidth, -boxwidth), (-boxwidth, boxwidth), (boxwidth, boxwidth),(boxwidth,-boxwidth)))
winmes=visual.TextStim(win,text='win',colorSpace='rgb',color=[0.0, 1.0, 0.0])
lossmes=visual.TextStim(win,text='loss',colorSpace='rgb',color=[1.0, 0.0 ,0.0])
fixation = visual.TextStim(win,text='X',color='black')

#and some handy clocks to keep track of time
globalClock = core.Clock()


#display instructions and wait
message1 = visual.TextStim(win, pos=[0,+3],text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0,-3],
    text="Then press left or right to identify the deg probe.")
message1.draw()
message2.draw()
fixation.draw()
win.flip()#to show our newly drawn 'stimuli'
#pause until there's a keypress
event.waitKeys()

trialhandle=data.TrialHandler(Sched, nReps=1, method='sequential', dataTypes=None, extraInfo=None, seed=None, originPath=None, name='', autoLog=True)
trialhandle.data.addDataType('Choice')
trialhandle.data.addDataType('RT')
trialhandle.data.addDataType('choiceside')
trialhandle.data.addDataType('winchosen')
trialhandle.data.addDataType('losschosen')
trialhandle.data.addDataType('trialnumber')
ntrial=0
for indtrial in range(0,2):
#for indtrial in trialhandle:
    thistrial=trialhandle.next()
    trialhandle.data.add('trialnumber',ntrial+1)
    # allow to escape window
    if 'escape' in event.getKeys():
        core.quit()
    
    trialclock=core.Clock()
    rtclock=core.Clock()
    trialclock.reset()
    
    # use for timing of stimuli
    countDown = core.CountdownTimer()
    countDown.add(fixdur)
    # present fixation cross for 500ms
    fixation.draw()
    win.flip()
    while countDown.getTime()>0:
        core.wait(0.1)
    
    #now present both stimuli until choice made
    if Sched[ntrial]['side'] == 1:
        stima.setPos([leftstimx,stimy])
        stimb.setPos([rightstimx,stimy])
    else:
        stimb.setPos([leftstimx,stimy])
        stima.setPos([rightstimx,stimy])
        
    fixation.draw()
    stima.draw()
    stimb.draw()
    win.flip()
    rtclock.reset()
    resp=event.waitKeys(keyList=['b','m'], timeStamped=rtclock)
    trialhandle.data.add('choiceside', resp[0][0])
    trialhandle.data.add('RT', resp[0][1])
    
    # put the choice box in the correct place, work out which option was chosen and whether a win and/or loss was received
    
    if resp[0][0]=='b':                                 #chose left option
        choicebox.setPos([leftstimx,stimy])
        if Sched[ntrial]['side']==1:                # option 1 on left
            trialhandle.data.add('choice',1)        #chose option 1
            if Sched[ntrial]['winpos']==1:          # win for option 1
                trialhandle.data.add('winchosen',1)
            else:
                trialhandle.data.add('winchosen',0)
            if Sched[ntrial]['losspos']==1:         # loss for option 1
                trialhandle.data.add('losschosen',1)
            else:
                trialhandle.data.add('losschosen',0)
        else:                                       # option 1 on right
            trialhandle.data.add('choice',0)        # chose option 2
            if Sched[ntrial]['winpos']==1:          # win for option 1
                trialhandle.data.add('winchosen',0)
            else:
                trialhandle.data.add('winchosen',1)
            if Sched[ntrial]['losspos']==1:         # loss for option 1
                trialhandle.data.add('losschosen', 0)
            else:
                trialhandle.data.add('losschosen',1)
    else:                                           # chose right option
        choicebox.setPos([rightstimx,stimy])
        if Sched[ntrial]['side']==1:  
            trialhandle.data.add('choice',0)        #chose option 2
            if Sched[ntrial]['winpos']==1:          # win for option 1
                trialhandle.data.add('winchosen',0)
            else:
                trialhandle.data.add('winchosen',1)
            if Sched[ntrial]['losspos']==1:         # loss for option 1
                trialhandle.data.add('losschosen', 0)
            else:
                trialhandle.data.add('losschosen',1)
        else:                                       #chose option 1
            trialhandle.data.add('choice',1)            #chose option 1
            if Sched[ntrial]['winpos']==1:           # win for option 1
                trialhandle.data.add('winchosen',1)
            else:
                trialhandle.data.add('winchosen',0)
            if Sched[ntrial]['losspos']==1:             # loss for option 1
                trialhandle.data.add('losschosen',1)
            else:
                trialhandle.data.add('losschosen',0)
    
  
        
    # present participant choice
  
    fixation.draw()
    choicebox.draw()
    stima.draw()
    stimb.draw()
    win.flip()
    countDown.reset()
    countDown.add(monitordur)
    while countDown.getTime()>0:
        core.wait(0.1)
    
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
        choicebox.draw()
        stima.draw()
        stimb.draw()
        winmes.draw()
        win.flip()
        # present for outcome duration
        countDown.reset()
        countDown.add(outcomedur1)
        while countDown.getTime()>0:
            core.wait(0.1)
        
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
        choicebox.draw()
        stima.draw()
        stimb.draw()
        winmes.draw()
        lossmes.draw()
        win.flip()
        # present for outcome duration
        countDown.reset()
        countDown.add(outcomedur2)
        while countDown.getTime()>0:
            core.wait(0.1)
        
        
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
        choicebox.draw()
        stima.draw()
        stimb.draw()
        lossmes.draw()
        win.flip()
        # present for outcome duration
        countDown.reset()
        countDown.add(outcomedur2)
        while countDown.getTime()>0:
            core.wait(0.1)
        
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
        choicebox.draw()
        stima.draw()
        stimb.draw()
        lossmes.draw()
        winmes.draw()
        win.flip()
        # present for outcome duration
        countDown.reset()
        countDown.add(outcomedur1)
        while countDown.getTime()>0:
            core.wait(0.1)
        
    
    
    ntrial+=1
    
trialhandle.saveAsText(os.path.join(main_dir,'results',fileName), dataOut=['choice_raw', 'choiceside_raw','RT_raw', 'winchosen_raw','losschosen_raw'])




win.close()
core.quit()