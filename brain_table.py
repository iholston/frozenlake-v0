import gym, random, tkinter

class brain:
    def __init__(self, env, alpha, gamma, epsilon, text_display=False, gui_display=False):
        self.brain = [[0] * env.action_space.n for i in range(env.observation_space.n)] # 4 actions 16 states
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.env = env
        self.text_display = text_display
        self.gui_display = gui_display
        if self.text_display:
            self.text_displayer('initialization')
        if self.gui_display:
            self.root = tkinter.Tk()
            self.gui_update('[ -------------------------------------------------- ]', '0')

    def gethighestrewardaction(self, state):
        # python is confusing here: self.brain matrix row for state -> get the max value from the row -> get the index for that action
        return self.brain[state].index(max(self.brain[state]))
    
    def train(self, iterations, display_increments=500):
        if self.text_display:
            self.text_displayer("train1")
        for i in range(iterations):
            if self.text_display == True and i % display_increments == 0: 
                self.text_displayer("train2", str(int(i/iterations * 100)))
            if self.gui_display and i % display_increments == 0:
                bar = '[ '
                for j in range(1, 50):
                    if float(j/50) <= float(i/iterations):
                        bar += chr(9608)
                    else:
                        bar += '-'
                bar += ' ]'
                percent = str(int(i/iterations * 100))
                self.gui_update(bar, percent)
            state = self.env.reset()
            reward = 0
            done = False
            if i > 10000 and random.uniform(0,1) < self.epsilon:
                for j in range(env.observation_space.n):
                    if self.brain[j][0] == 0 or self.brain[j][1] == 0 or self.brain[j][2] == 0 or self.brain[j][3] == 0:
                        self.env.env.s = j
                        state = j
            while not done:
                if random.uniform(0,1) < self.epsilon:
                  action = self.env.action_space.sample()
                else:
                  action = self.gethighestrewardaction(state)
                nextstate, reward, done, _ = self.env.step(action) # we don't need done or info
            
                # Update brain based on reward for action taken accoring to q algo
                oldvalue = self.brain[state][action]
                nextmax = max(self.brain[nextstate])
                finalvalue = (1-self.alpha)*oldvalue + self.alpha*(reward + self.gamma*nextmax)
                self.brain[state][action] = finalvalue
                state = nextstate
        if self.text_display:
            self.text_displayer('train3')
        if self.gui_display:
            bar = '[ '
            for i in range(50):
                bar += chr(9608)
            bar += ' ]'
            self.gui_update(bar, '100')

    def play(self):
        self.env.reset()
        steps = 0
        done = False
        state = 0
        while not done:
            if self.text_display:
                self.text_displayer("play", [state, self.brain[state].index(max(self.brain[state])), max(self.brain[state])])
            action = self.brain[state].index(max(self.brain[state]))
            state, reward, done, _ = self.env.step(action)
            steps += 1
        return steps

    def text_displayer(self, func, info=None):
        if func == 'initialization':
            print("Initializing Brain.\n------------------------\nEnv: {}".format(self.env.unwrapped.spec.id))
            print("Alpha: {}\nGamma: {}\nEpsilon: {}\n".format(self.alpha, self.gamma, self.epsilon))
            print("Smooth Brain. States: {}, Possible actions: {}".format(self.env.observation_space.n, self.env.action_space.n))
            print(self.brain)
            print()
        if func == 'train1':
            print("Initializing Training.\n{} Iterations".format(info))
            print("------------------------")
        if func == 'train2':
            print("Training Progress: " + info + "%")
        if func == 'train3':
            print("Training Progress: Complete\n")
            print("Rigid Brain:")
            print(self.brain)
        if func == "play":
            legend = {0:"South",1:"North",2:"East",3:"West",4:"Pickup",5:"Dropoff"}
            print("\nState: {}".format(info[0]))
            print("Headed: {}".format(legend[info[1]]))
            print("Expected Reward: {0:.2f}".format(info[2]))
            self.env.render()


    def gui_update(self, bar, percent):
        self.root.title('Q brain')
        self.root.geometry('+75+100')
        msg = 'Training Progress: ' + bar + ' ' + percent + '% Complete'
        tkinter.Button(self.root, text=msg, font='Courier',highlightbackground='black', height=3,width=25).grid(column=0,columnspan=5,row=0,sticky='EW')
        tkinter.Button(self.root, text='State', highlightbackground='black', width=25).grid(column=0,row=1,sticky='EW')
        tkinter.Button(self.root, text='Left', highlightbackground='red', width=25).grid(column=1,row=1,sticky='EW')
        tkinter.Button(self.root, text='Down', highlightbackground='blue', width=25).grid(column=2,row=1,sticky='EW')
        tkinter.Button(self.root, text='Right', highlightbackground='green', width=25).grid(column=3,row=1,sticky='EW')
        tkinter.Button(self.root, text='Up', highlightbackground='yellow', width=25).grid(column=4,row=1,sticky='EW')
        for i in range(16):
            state = str(i + 1)
            L = self.brain[i][0] * 10000
            D = self.brain[i][1] * 10000
            R = self.brain[i][2] * 10000
            U = self.brain[i][3] * 10000
            if L == D and D == R and R == U and U == 0:
                state += ' HOLE'
                tkinter.Button(self.root, text=state, highlightbackground='black', width=25).grid(column=0,row=i+2,sticky='EW')
            else:
                tkinter.Button(self.root, text=state, width=25).grid(column=0,row=i+2,sticky='EW')

            if L > D and L > R and L > U:
                tkinter.Button(self.root, text=L, highlightbackground='red', width=25).grid(column=1,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=D, width=25).grid(column=2,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=R, width=25).grid(column=3,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=U, width=25).grid(column=4,row=i+2,sticky='EW')
            elif D > R and D > U:
                tkinter.Button(self.root, text=L, width=25).grid(column=1,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=D, highlightbackground='blue', width=25).grid(column=2,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=R, width=25).grid(column=3,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=U, width=25).grid(column=4,row=i+2,sticky='EW')
            elif R > U:
                tkinter.Button(self.root, text=L, width=25).grid(column=1,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=D, width=25).grid(column=2,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=R, highlightbackground='green', width=25).grid(column=3,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=U, width=25).grid(column=4,row=i+2,sticky='EW')
            elif U != 0:
                tkinter.Button(self.root, text=L, width=25).grid(column=1,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=D, width=25).grid(column=2,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=R, width=25).grid(column=3,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=U, highlightbackground='yellow', width=25).grid(column=4,row=i+2,sticky='EW')
            else:
                tkinter.Button(self.root, text=L, width=25).grid(column=1,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=D, width=25).grid(column=2,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=R, width=25).grid(column=3,row=i+2,sticky='EW')
                tkinter.Button(self.root, text=U, width=25).grid(column=4,row=i+2,sticky='EW')
        self.root.update()


# Main()
if __name__ == "__main__":
    env = gym.make('FrozenLake-v0')
    alpha = .1
    gamma = .7
    epsilon = .2
    iterations = 10000

    '''# Interactive Game
    rootGame = tkinter.Tk()
    rootGame.geometry('+350+50')
    letters = ['S', 'F', 'F', 'F', 'F', 'H', 'F', 'H', 'F', 'F', 'F', 'H', 'H', 'F', 'F', 'G']
    colors = ['blue', None, None, None, None, 'brown', None, 'brown', None, None, None, 'brown', 'brown', None, None, 'green']
    ro = 0
    for i in range(16):
        if i % 4 == 0:
            ro += 1
        tkinter.Button(rootGame, text=letters[i], highlightbackground=colors[i], font=(None,20), width=10, height=5).grid(column=i%4,row=ro)
    tkinter.Button(rootGame, text='Left', height=3).grid(column=0, row =5, sticky='EW')
    tkinter.Button(rootGame, text='Up', height=3).grid(column=1, row =5, sticky='EW')
    tkinter.Button(rootGame, text='Down', height=3).grid(column=2, row =5, sticky='EW')
    tkinter.Button(rootGame, text='Right', height=3).grid(column=3, row =5, sticky='EW')
    tkinter.Button(rootGame, text='End Game', height=3).grid(column=0, columnspan=4, row=6, sticky='EW')
    rootGame.mainloop()'''

    # Brute forcing
    # Results

    # Create Brain, then train it
    lakebrain = brain(env, alpha, gamma, epsilon, text_display=False, gui_display=True)
    lakebrain.train(iterations, display_increments=500)

    # Play with brain
    # Print Results
    

