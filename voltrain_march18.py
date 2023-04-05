from psychopy import  visual, core, gui, data, event, monitors, sound, iohub
import copy, time, os, sys, random #from the std python libs
from psychopy.tools.filetools import fromFile, toFile
from comppsychHelper import *
import pylinkwrapper


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
outcomedur1=1   # duration of first outcome in secs (if not jittered)
outcomedur2=1   # duration of second outcome in secs (if not jittered)
totmon=1.5      # starting amount of money
winloss=0.15    # amount won or lost per trial
main_dir=os.getcwd()   # where psychopy script is being run from
winsound=sound.Sound(os.path.join(main_dir, 'stimuli','cha_ching.wav'))   # sound to play on win
losssound=sound.Sound(os.path.join(main_dir,'stimuli','error2.wav'))     # sound to play on loss
minjit=2        # min jitter duration in secs
maxjit=6        # max jitter duration in secs
stimlets=['a','F','G','h','K','o','b','f','j','i']      # letters to be used as stimuli
blocknum=1      # counter for blocks


if len(stimlets) < len(blocklength)*2:
    sys.exit("not enought letter stimuli!")

os.chdir(main_dir)

# date as month, day hour min

dateStr = time.strftime("%b_%d_%H%M", time.localtime())#add the current time

# experiment inf
expInfo = {'Subject Num':'', 'Block Order':9, 'dateStr':dateStr}

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
random.shuffle(stimlets)
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