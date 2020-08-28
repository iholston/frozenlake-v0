import gym, random, time
from tkinter import *

class flGUI:
    def __init__(self):
        # For Game
        self.letters = ['START', 'ICE', 'ICE', 'ICE', 'ICE', 'HOLE', 'ICE', 'HOLE', 'ICE', 'ICE', 'ICE', 'HOLE', 'HOLE', 'ICE', 'ICE', 'GOAL']
        self.colors = ['blue', 'white', 'white', 'white', 'white', 'firebrick1', 'white', 'firebrick1', 'white', 'white', 'white', 'firebrick1', 'firebrick1', 'white', 'white', 'green2']
        self.brain_trainingIterations = 0
        self.brainarray = [[0 for j in range(4)] for i in range(16)]
        self.brain_intelligence = 0
        self.alpha = 0.0
        self.gamma = 0.0
        self.epsilon = 0.0

        # For Training

        # For Brain Display
        self.master = Tk()
        self.main_menu(self.master)
        
    def main_menu(self, master):
        master.destroy() # for some reason self.master.destroy() does not work so i have to pass to the function to kill it
        self.master = Tk()
        self.master.geometry('+350+150')
        self.master.title("FrozenLake-v0 AI Tutorial")
        msg0 = 'BRAIN LVL:\n' + str(self.brain_intelligence) + '%'
        msg1 = 'CURRENT PARAMETERS\n-----------------------\nAlpha: ' + str(self.alpha) + '\nGamma: ' + str(self.gamma) + '\nEpsilon: ' + str(self.epsilon)
        msg2 = 'BRAIN TRAININGS:\n' + str(self.brain_trainingIterations)
        Label(self.master, text=msg0, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=0, row=0, sticky='EW')
        Label(self.master, text=msg1, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=1, row=0, sticky='EW')
        Label(self.master, text=msg2, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=2, row=0, sticky='EW')
        Button(self.master, text="PLAY", command=lambda: self.play_menu(), width=20, height=6).grid(column=0,row=1,sticky='EW')
        Button(self.master, text='TRAIN', command=lambda: self.train_menu(), width=20, height=6).grid(column=1, row=1, sticky='EW')
        Button(self.master, text='DISPLAY BRAIN', command=lambda: self.display_brain(), width=20, height=6).grid(column=2, row=1, sticky='EW')
        Button(self.master, text='Explain Game', command=lambda: self.explain(), height=2).grid(columnspan=3, row=2, sticky='EW')
        self.master.mainloop()

    def play_menu(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: Play Menu')
        self.master.geometry('+350+150')
        msg0 = 'BRAIN LVL:\n' + str(self.brain_intelligence) + '%'
        msg1 = 'CURRENT PARAMETERS\n-----------------------\nAlpha: ' + str(self.alpha) + '\nGamma: ' + str(self.gamma) + '\nEpsilon: ' + str(self.epsilon)
        msg2 = 'BRAIN TRAININGS:\n' + str(self.brain_trainingIterations)
        Label(self.master, text=msg0, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=0, row=0, sticky='EW')
        Label(self.master, text=msg1, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=1, row=0, sticky='EW')
        Label(self.master, text=msg2, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=2, row=0, sticky='EW')
        Button(self.master, text='Human Play', command=lambda: self.human_play(), width=20, height=6).grid(column=0, row=1,sticky='EW')
        Button(self.master, text='AI Play', command=lambda:self.ai_play(), width=20,height=6).grid(column=1,row=1,sticky='EW')
        Button(self.master, text='AI Play\n(No Display)', command=lambda:self.ai_play_nodisplay(), width=20, height=6).grid(column=2,row=1,sticky='EW')
        Button(self.master, text='Back', command=lambda: self.main_menu(self.master), height=2, width=60).grid(column=0, columnspan=3, row=2, sticky='EW')
        self.master.mainloop()

    def train_menu(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: Train Menu')
        self.master.geometry('+350+150')
        msg0 = 'BRAIN LVL:\n' + str(self.brain_intelligence) + '%'
        msg1 = 'CURRENT PARAMETERS\n-----------------------\nAlpha: ' + str(self.alpha) + '\nGamma: ' + str(self.gamma) + '\nEpsilon: ' + str(self.epsilon)
        msg2 = 'BRAIN TRAININGS:\n' + str(self.brain_trainingIterations)
        Label(self.master, text=msg0, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=0, row=0, sticky='EW')
        Label(self.master, text=msg1, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=1, row=0, sticky='EW')
        Label(self.master, text=msg2, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=2, row=0, sticky='EW')
        Button(self.master, text='TRAIN BRAIN', width=20, height=6).grid(column=0, columnspan=2, row=1, sticky='EW')
        Button(self.master, text='Tweak Parameters', command=lambda: self.tweak_params(), width=20, height=6).grid(column=2, row=1, sticky='EW')
        Button(self.master, text='Back', command=lambda: self.main_menu(self.master), height=2, width=60).grid(column=0,columnspan=3,row=2,sticky='EW')
        self.master.mainloop()

    def display_brain(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: Train Menu')
        self.master.geometry('+350+100')
        msg0 = 'BRAIN LVL:                  BRAIN ITERATIONS:\n' + str(self.brain_intelligence) + '%                                       ' + str(self.brain_trainingIterations) + '         '
        Label(self.master, text=msg0, bg='light cyan', font=('bold'), foreground='blue', height=6, width=60).grid(column=0, columnspan=5, row=0, sticky='EW')
        Label(self.master, text='State', bg='light cyan', foreground='black', width=12, borderwidth=2, relief='solid').grid(column=0,row=1,sticky='EW')
        Label(self.master, text='Left', bg='red', foreground='white',  width=12).grid(column=1,row=1,sticky='EW')
        Label(self.master, text='Down', bg='blue', foreground='white',  width=12).grid(column=2,row=1,sticky='EW')
        Label(self.master, text='Right', bg='green', foreground='white',  width=12).grid(column=3,row=1,sticky='EW')
        Label(self.master, text='Up', bg='yellow', foreground='black',  width=12).grid(column=4,row=1,sticky='EW')
        for i in range(16):
            state = str(i + 1)
            L = self.brainarray[i][0] * 10000
            D = self.brainarray[i][1] * 10000
            R = self.brainarray[i][2] * 10000
            U = self.brainarray[i][3] * 10000
            if L == D and D == R and R == U and U == 0:
                state += ' (HOLE)'
                Label(self.master, text=state, bg='light cyan', foreground='black', width=12, borderwidth=2, relief='solid').grid(column=0,row=i+3,sticky='EW')
            else:
                Label(self.master, text=state, bg='light cyan', foreground='black', width=12, borderwidth=2, relief='solid').grid(column=0,row=i+3,sticky='EW')
            if L > D and L > R and L > U:
                Label(self.master, text=L, highlightbackground='red', width=12).grid(column=1,row=i+3,sticky='EW')
                Label(self.master, text=D, width=12).grid(column=2,row=i+3,sticky='EW')
                Label(self.master, text=R, width=12).grid(column=3,row=i+3,sticky='EW')
                Label(self.master, text=U, width=12).grid(column=4,row=i+3,sticky='EW')
            elif D > R and D > U:
                Label(self.master, text=L, width=12).grid(column=1,row=i+3,sticky='EW')
                Label(self.master, text=D, highlightbackground='blue', width=12).grid(column=2,row=i+3,sticky='EW')
                Label(self.master, text=R, width=12).grid(column=3,row=i+3,sticky='EW')
                Label(self.master, text=U, width=12).grid(column=4,row=i+3,sticky='EW')
            elif R > U:
                Label(self.master, text=L, width=12).grid(column=1,row=i+3,sticky='EW')
                Label(self.master, text=D, width=12).grid(column=2,row=i+3,sticky='EW')
                Label(self.master, text=R, highlightbackground='green', width=12).grid(column=3,row=i+3,sticky='EW')
                Label(self.master, text=U, width=12).grid(column=4,row=i+3,sticky='EW')
            elif U != 0:
                Label(self.master, text=L, width=12).grid(column=1,row=i+3,sticky='EW')
                Label(self.master, text=D, width=12).grid(column=2,row=i+3,sticky='EW')
                Label(self.master, text=R, width=12).grid(column=3,row=i+3,sticky='EW')
                Label(self.master, text=U, highlightbackground='yellow', width=12).grid(column=4,row=i+3,sticky='EW')
            else:
                Label(self.master, text=L, width=12).grid(column=1,row=i+3,sticky='EW')
                Label(self.master, text=D, width=12).grid(column=2,row=i+3,sticky='EW')
                Label(self.master, text=R, width=12).grid(column=3,row=i+3,sticky='EW')
                Label(self.master, text=U, width=12).grid(column=4,row=i+3,sticky='EW')
        Button(self.master, text='Back', command=lambda: self.main_menu(self.master), height=2, width=60).grid(column=0,columnspan=5,row=19,sticky='EW')
        self.master.mainloop()

    def human_play(self):
        # Variables
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: Human Playthrough')
        self.master.geometry('+350+100')
        self.position_grid = [[i for i in range(4)] for j in range(4)]
        self.oldposition = [0,0]
        self.position = [0,0]
        self.labelarray = []
        
        # Build Game
        self.game_toplabel = Label(self.master, text='STANDING AT START\n-----------------------\nYou Moved: NONE', bg='light cyan', font=('bold'), foreground='blue', height=6)
        self.game_toplabel.grid(column=0, columnspan=4, row=0, sticky='EW') 
        for i in range(16):
            self.labelarray.append(Label(self.master, text=self.letters[i], bg=self.colors[i], height=6, width=15,borderwidth=3, relief='ridge'))
        ro = 1
        for index, label in enumerate(self.labelarray):
            if index % 4 == 0:
                ro += 1
            label.grid(column=index%4,row=ro,sticky='EW')
        Button(self.master, text='Back', command=lambda: self.play_menu(), height=2).grid(column=0, columnspan=4, row=6, sticky='EW')
        
        # PLAY on events
        self.master.bind("<Key>", self.on_keystroke)
        self.master.mainloop()

    def ai_play(self):
        # Variables
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: AI Playthrough')
        self.master.geometry('+350+100')
        self.position_grid = [[i for i in range(4)] for j in range(4)]
        self.oldposition = [0,0]
        self.position = [0,0]
        self.labelarray = []
        self.steps = 0
        
        # Build Game
        self.game_toplabel = Label(self.master, text='STANDING AT START\n-----------------------\nYou Moved: NONE\n\nSTEPS: 0', bg='light cyan', font=('bold'), foreground='blue', height=6)
        self.game_toplabel.grid(column=0, columnspan=4, row=0, sticky='EW') 
        for i in range(16):
            self.labelarray.append(Label(self.master, text=self.letters[i], bg=self.colors[i], height=6, width=15,borderwidth=3, relief='ridge'))
        ro = 1
        for index, label in enumerate(self.labelarray):
            if index % 4 == 0:
                ro += 1
            label.grid(column=index%4,row=ro,sticky='EW')
        msg1 = 'BRAIN LVL:\n' + str(self.brain_intelligence) + '%'
        if self.brain_intelligence == 0:
            msg1 += '\nBrute Forcing...'
        Label(self.master, text=msg1, bg='light cyan', font=('bold'), foreground='blue', height=6, width=15).grid(column=0, row=0, sticky='EW')
        msg2 = 'BRAIN TRAININGS:\n' + str(self.brain_trainingIterations)
        if self.brain_intelligence == 0:
            msg2 += '\nBrute Forcing...'
        Label(self.master, text=msg2, bg='light cyan', font=('bold'), foreground='blue', height=6, width=15).grid(column=3, row=0, sticky='EW')                                                                                        
        Button(self.master, text='Back', command=lambda: self.play_menu(), height=2).grid(column=0, columnspan=4, row=6, sticky='EW')


        # Get action from brain
        while True:
            self.master.update()
            time.sleep(.5)
            self.steps += 1
            if self.brain_trainingIterations == 0:
                actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
                action = actions[random.randint(0,3)]
                self.setposition(action)

            # Implement action on environment
            randomEvent = False
            self.labelarray[self.position[0]*4 + self.position[1]].configure(text='AI IS\nHERE', bg='cyan', relief='sunken')
            if self.position != self.oldposition:
                self.labelarray[self.oldposition[0]*4 + self.oldposition[1]].configure(text=self.letters[self.oldposition[0]*4 + self.oldposition[1]], bg=self.colors[self.oldposition[0]*4 + self.oldposition[1]])
            if self.letters[self.position[0]*4 + self.position[1]] == 'HOLE':
                self.hole_button(randomEvent, ai=True)
                break
            elif self.letters[self.position[0]*4 + self.position[1]] == 'GOAL':
                self.goal_button(randomEvent, ai=True)
                break
            else:
                self.game_toplabel.config(text=self.getText(action, randomEvent, ai=True))

    def ai_play_nodisplay(self):
        pass

    def on_keystroke(self, event):
        action = None
        randomEvent = False
        
        # Take their input
        if repr(event.char) == repr('\uf700'): # Up
            action = 'UP'
        elif repr(event.char) == repr('\uf701'): # Down
            action = 'DOWN'
        elif repr(event.char) == repr('\uf702'): # Left
            action = 'LEFT'
        elif repr(event.char) == repr('\uf703'): # Right
            action = 'RIGHT'
            
        # Decide if something random is going to happen
        if random.uniform(0,1) < .33:
            actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
            actions.remove(action)
            action = actions[random.randint(0,2)] 
            randomEvent = True
        self.setposition(action)

        # Implement action on environment
        self.labelarray[self.position[0]*4 + self.position[1]].configure(text='YOU ARE\nHERE', bg='cyan', relief='sunken')
        if self.position != self.oldposition:
            self.labelarray[self.oldposition[0]*4 + self.oldposition[1]].configure(text=self.letters[self.oldposition[0]*4 + self.oldposition[1]], bg=self.colors[self.oldposition[0]*4 + self.oldposition[1]])
        if self.letters[self.position[0]*4 + self.position[1]] == 'HOLE':
            self.master.unbind("<Key>")  # Stops accepting further keystrokes
            self.hole_button(randomEvent)
        elif self.letters[self.position[0]*4 + self.position[1]] == 'GOAL':
            self.master.unbind("<Key>")
            self.goal_button(randomEvent)
        else:
            self.game_toplabel.config(text=self.getText(action, randomEvent))

    def setposition(self, direction):
        self.oldposition = self.position.copy()
        if direction == 'UP':
            if self.position[0] == 0:
                return
            else:
                self.position[0] -= 1
        elif direction == 'DOWN':
            if self.position[0] == 3:
                return
            else:
                self.position[0] += 1
        elif direction == 'LEFT':
            if self.position[1] == 0:
                return
            else:
                self.position[1] -= 1
        elif direction == 'RIGHT':
            if self.position[1] == 3:
                return 
            else:
                self.position[1] += 1
                
    def getText(self, direction, randomOrNah, ai=False):
        if ai:
            if randomOrNah:
                if direction == 'goal':
                    return 'AI SLIPPED TO SAFETY!\n-----------------------\nRandom Move: Left\n\n' + 'STEPS: ' + str(self.steps) 
                if direction == 'hole':
                    return 'AI SLIPPED TO HIS DEATH\n-----------------------\nRandom Move: ' + direction + '\n\nSTEPS: ' + str(self.steps)
                return 'AI SLIPPED!\n-----------------------\nRandom Move: ' + direction + '\n\nSTEPS: ' + str(self.steps)
            else:
                if direction == 'goal':
                    return 'AI SURVIVED!\n-----------------------\nAI Moved: Left' + '\n\nSTEPS: ' + str(self.steps)
                if direction == 'hole':
                    return 'AI VOLUNTARILY KILLED ITSELF\n-----------------------\nAI Moved: ' + direction + '\n\nSTEPS: ' + str(self.steps)
                return 'BE CAREFUL!\n-----------------------\nAI Moved: ' + direction + '\n\nSTEPS: ' + str(self.steps)
        if randomOrNah:
            if direction == 'goal':
                return 'YOU SLIPPED TO SAFETY!\n-----------------------\nRandom Move: Left'
            if direction == 'hole':
                return 'YOU SLIPPED TO YOUR DEATH\n-----------------------\nRandom Move: ' + direction
            return 'YOU SLIPPED!\n-----------------------\nRandom Move: ' + direction
        else:
            if direction == 'goal':
                return 'YOU SURVIVED!\n-----------------------\nYou Moved: Left'
            if direction == 'hole':
                return 'YOU VOLUNTARILY KILLED YOURSELF\n-----------------------\nYou Moved: ' + direction
            return 'BE CAREFUL!\n-----------------------\nYou Moved: ' + direction

    def hole_button(self, randomEvent, ai=False):      
        self.game_toplabel.config(text=self.getText('hole', randomEvent, ai))
        col = self.position[1] 
        ro = self.position[0] + 2
        if ai:
            Button(self.master, text='The AI Died!\nRestart Game?\n(click here)', command=lambda: self.ai_play(), height=6, width=15).grid(column=col, row=ro, sticky='EW')
        else:
            Button(self.master, text='You Died!\nRestart Game?\n(click here)', command=lambda: self.human_play(), height=6, width=15).grid(column=col, row=ro, sticky='EW')

    def goal_button(self, randomEvent, ai=False):
        self.game_toplabel.config(text=self.getText('goal', randomEvent, ai))
        if ai:
            Button(self.master, text='The AI Made It!\nRestart Game?\n(click here)', command=lambda: self.ai_play(), height=6, width=15).grid(column=3, row=5, sticky='EW')
        else:
            Button(self.master, text='You Made It!\nRestart Game?\n(click here)', command=lambda: self.human_play(), height=6, width=15).grid(column=3, row=5, sticky='EW')

    def tweak_params(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title('FrozenLake-v0 AI Tutorial: Tweaking Params')
        self.master.geometry('+350+150')
        msg0 = 'BRAIN LVL:\n' + str(self.brain_intelligence) + '%'
        msg1 = 'CURRENT PARAMETERS\n-----------------------\nAlpha: ' + str(self.alpha) + '\nGamma: ' + str(self.gamma) + '\nEpsilon: ' + str(self.epsilon)
        msg2 = 'BRAIN TRAININGS:\n' + str(self.brain_trainingIterations)
        Label(self.master, text=msg0, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=0, row=0, sticky='EW')
        Label(self.master, text=msg1, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=1, row=0, sticky='EW')
        Label(self.master, text=msg2, bg='light cyan', font=('bold'), foreground='blue', height=6, width=20).grid(column=2, row=0, sticky='EW')
        Label(self.master, text='Alpha', width=10).grid(column=1,row=1, sticky='EW')
        Label(self.master, text='Gamma', width=10).grid(column=1,row=2, sticky='EW')
        Label(self.master, text='Epsilon', width=10).grid(column=1,row=3, sticky='EW')
        alpha = Entry(self.master)
        alpha.grid(column=2, row=1, sticky='EW')
        alpha.insert(0, str(self.alpha))
        gamma = Entry(self.master)
        gamma.grid(column=2, row=2,sticky='EW')
        gamma.insert(0, str(self.gamma))
        epsilon = Entry(self.master)
        epsilon.grid(column=2, row=3,sticky='EW')
        epsilon.insert(0, str(self.epsilon))
        Button(self.master, text='Submit', command=lambda: self.set_params(alpha, gamma, epsilon), height=2, width=60).grid(column=0,columnspan=5,row=5,sticky='EW')
        Button(self.master, text='Back', command=lambda: self.train_menu(), height=2, width=60).grid(column=0,columnspan=5,row=6,sticky='EW')
        self.master.mainloop()

    def set_params(self, a, b, c):
        self.alpha=a.get()
        self.gamma=b.get()
        self.epsilon=c.get()
        self.train_menu()

    def explain(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title('AI Explanation')
        self.master.geometry('+350+150')
        explanation = 'FROZEN LAKE\n-----------------------\nThe goal is to move from START to GOAL. '
        explanation += 'The lake is icy, and the ICE\n has HOLES which will kill you if you fall into them. '
        explanation += 'You can move UP, DOWN,\nLEFT, and RIGHT via the keyboard. '
        explanation += 'BUT, there is a 33% chance you slip on the ice\n and a RANDOM MOVE will be taken instead '
        explanation += '(which might kill you lol). GL!\n\n'
        explanation += 'PLAY\n-----------------------\nEither you or the AI can play the game.\n\n'
        explanation += 'TRAIN\n-----------------------\nSet parameters and train the AI then go to PLAY to watch it go!\n\n'
        explanation += 'BRAIN INTELLIGENCE\n-----------------------\n0% -> AI will just brute force the game.\n'
        explanation += '100% -> AI will make optimal decisions at all times.'
        explainButton = Label(self.master, text=explanation, bg='light cyan',  font= ('bold'), foreground='blue', justify='center', height=22).grid(column=0,columnspan=3,row=0, sticky='EW')
        backButton = Button(self.master, text='Back', command=lambda: s, height=2, width=60).grid(row=1, sticky='EW')
        self.master.mainloop()


tutorial = flGUI()
