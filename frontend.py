from tkinter import *
from functools import partial
from playsound import playsound
import backend


# Start Page -----------------------------------------------------------------------------------------------------------
def callDrawStart(root):
    for x in root.winfo_children():
        x.destroy()

    drawStart(root)


def drawStart(root):
    # Configure weights of the root's grid
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Top Frame
    # #e4000f is red pokeball color
    # #362D5C is purple masterball color
    if backend.DIFFICULTY == 'EASY':
        top_frm = Frame(master=root, bg='#e4000f', padx=5, pady=5)

    else:
        top_frm = Frame(master=root, bg='#362D5C', padx=5, pady=5)
        
    top_frm.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 5), sticky='nsew')
    top_frm.grid_propagate(FALSE)

    top_frm.rowconfigure(0, weight=1)
    top_frm.columnconfigure(0, weight=1)

    # Bottom Frame
    bottom_frm = Frame(master=root, bg='white', padx=5, pady=5)
    bottom_frm.grid(row=1, column=0, columnspan=3, padx=10, pady=(5, 10), sticky='nsew')
    bottom_frm.grid_propagate(FALSE)

    bottom_frm.rowconfigure(0, weight=2, uniform='fred')
    bottom_frm.rowconfigure(1, weight=1, uniform='fred')
    bottom_frm.rowconfigure(2, weight=2, uniform='fred')
    bottom_frm.columnconfigure(0, weight=2, uniform='fred')
    bottom_frm.columnconfigure(1, weight=1, uniform='fred')
    bottom_frm.columnconfigure(2, weight=2, uniform='fred')

    # Logo Label
    title_lbl = Label(master=top_frm, text='Pokémon Guesser', font=('Roboto', 50),
                      borderwidth=5, relief='solid', bg='white', padx=20, pady=20)
    title_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Play Button
    action_with_arg = partial(callDrawQuestion, root, title_lbl)
    play_btn = Button(master=root,
                      text='Start guessing',
                      font=('Roboto', 20),
                      relief='solid',
                      borderwidth=10,
                      fg='black', bg='white',
                      padx=20, pady=20,
                      command=action_with_arg,
                      cursor='hand2')

    play_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Add settings button to bottom frame
    action_with_arg = partial(drawSettings, root)
    settings_btn = Button(master=bottom_frm, text='Settings', font=('Roboto', 15),
                          borderwidth=5, relief='raised', cursor='hand2', command=action_with_arg)
    settings_btn.grid(row=1, column=1, sticky='nsew')


# Question Page --------------------------------------------------------------------------------------------------------
def nextQuestion(root, question_lbl, score_lbl, answerA, answerB, answerC, answerD):
    backend.SCORE = backend.SCORE + 1
    #Sound for getting question correct
    try:
        playsound('12_4.mp3')
    
    except:
        print('cannot open audio file')
        
    if backend.SCORE == backend.TOTAL_POSSIBLE_PKMN:
        drawGameOver(root, True)
    else:
        play(root, question_lbl, score_lbl, answerA, answerB, answerC, answerD)


def callDrawQuestion(root, title_lbl):
    title_lbl.place_forget()
    for x in root.winfo_children():
        x.destroy()

    drawQuestion(root)


def drawQuestion(root):
    # Top Frame
    if backend.DIFFICULTY == 'EASY':
        top_frm = Frame(master=root, bg='#e4000f', padx=5, pady=5)

    else:
        top_frm = Frame(master=root, bg='#362D5C', padx=5, pady=5)

    top_frm.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 5), sticky='nsew')
    top_frm.grid_propagate(FALSE)

    top_frm.rowconfigure(0, weight=1)
    top_frm.rowconfigure(1, weight=1)
    top_frm.columnconfigure(0, weight=1)

    # Bottom Frame
    bottom_frm = Frame(master=root, bg='white', padx=5, pady=5)
    bottom_frm.grid(row=1, padx=10, pady=(5, 10), sticky='nsew')
    bottom_frm.grid_propagate(FALSE)

    bottom_frm.rowconfigure(0, weight=1)
    bottom_frm.rowconfigure(1, weight=1)
    bottom_frm.columnconfigure(0, weight=1, uniform='fred')
    bottom_frm.columnconfigure(1, weight=1, uniform='fred')

    # Add the question to the top frame
    question_lbl = Label(master=top_frm, font=('Roboto', 20), borderwidth=5, relief='solid', padx=20, pady=20,
                         justify='center', wraplength=600)
    question_lbl.grid(row=0, padx=20, pady=(20, 5))

    # Add score to the top frame
    score_lbl = Label(master=top_frm, text=f'SCORE: {backend.SCORE}', font=('Roboto', 20), borderwidth=5,
                      relief='solid', padx=20, pady=20, justify='center')
    score_lbl.grid(row=1, padx=20, pady=(5, 20))

    # Add the answer choices to the bottom frame
    answerA = Button(master=bottom_frm, font=('Roboto', 15), borderwidth=5, relief='raised', cursor='hand2')
    answerB = Button(master=bottom_frm, font=('Roboto', 15), borderwidth=5, relief='raised', cursor='hand2')
    answerC = Button(master=bottom_frm, font=('Roboto', 15), borderwidth=5, relief='raised', cursor='hand2')
    answerD = Button(master=bottom_frm, font=('Roboto', 15), borderwidth=5, relief='raised', cursor='hand2')

    answerA.grid(row=0, column=0, sticky='nsew', padx=(10, 5), pady=(10, 5))
    answerB.grid(row=0, column=1, sticky='nsew', padx=(5, 10), pady=(10, 5))
    answerC.grid(row=1, column=0, sticky='nsew', padx=(10, 5), pady=(5, 10))
    answerD.grid(row=1, column=1, sticky='nsew', padx=(5, 10), pady=(5, 10))

    play(root, question_lbl, score_lbl, answerA, answerB, answerC, answerD)


def play(root, question_lbl, score_lbl, answerA, answerB, answerC, answerD):
    # Default to Gen I selected if none are
    if True not in backend.GENERATIONS:
        backend.GENERATIONS[0] = True

    # Generate question and answers
    if backend.DIFFICULTY == 'EASY':
        data = backend.newQuestionEasy()
    else:
        data = backend.newQuestionHard()

    question = data[0]
    answer = data[2]
    a = data[1][0]
    b = data[1][1]
    c = data[1][2]
    d = data[1][3]

    # Update GUI
    question_lbl.configure(text=question)
    score_lbl.configure(text=f'Score: {backend.SCORE}')
    answerA.configure(text=a.capitalize())
    answerB.configure(text=b.capitalize())
    answerC.configure(text=c.capitalize())
    answerD.configure(text=d.capitalize())

    # Add functionality to the answer choice buttons
    buttons = [answerA, answerB, answerC, answerD]
    count = 0
    for x in buttons:
        if count == answer:
            action_with_arg = partial(nextQuestion, root, question_lbl, score_lbl, answerA, answerB, answerC, answerD)
            x.configure(command=action_with_arg)
        else:
            action_with_arg = partial(drawGameOver, root, False)
            x.configure(command=action_with_arg)
        count = count + 1


# Game Over Page -------------------------------------------------------------------------------------------------------
def drawGameOver(root, result):
    for x in root.winfo_children():
        x.destroy()

    # Top Frame
    if backend.DIFFICULTY == 'EASY':
        top_frm = Frame(master=root, bg='#e4000f', padx=5, pady=5)

    else:
        top_frm = Frame(master=root, bg='#362D5C', padx=5, pady=5)
        
    top_frm.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 5), sticky='nsew')
    top_frm.grid_propagate(FALSE)

    top_frm.rowconfigure(0, weight=3)
    top_frm.rowconfigure(1, weight=1)
    top_frm.columnconfigure(0, weight=1)

    # Bottom Frame
    bottom_frm = Frame(master=root, bg='white', padx=5, pady=5)
    bottom_frm.grid(row=1, column=0, padx=10, pady=(5, 10), sticky='nsew')
    bottom_frm.grid_propagate(FALSE)

    bottom_frm.rowconfigure(0, weight=1)
    bottom_frm.columnconfigure(0, weight=1, uniform='fred')
    bottom_frm.columnconfigure(1, weight=1, uniform='fred')

    # Add the question to the top frame
    gameOver_lbl = Label(master=top_frm, text='GAME OVER', font=('Roboto', 50),
                         borderwidth=5, relief='solid', padx=20, pady=20)
    if result:
        gameOver_lbl.configure(text='YOU WIN!')
    gameOver_lbl.grid(row=0, pady=(20, 10))

    # Add score to the top frame
    score_lbl = Label(master=top_frm, text=f'Score: {backend.SCORE}', font=('Roboto', 40), borderwidth=5,
                      relief='solid', padx=20, pady=20)
    score_lbl.grid(row=1, pady=(10, 20))

    backend.SCORE = 0
    backend.USED_PKMN.clear()

    # Add retry button to bottom frame
    action_with_arg = partial(drawQuestion, root)
    retry_btn = Button(master=bottom_frm, text='Retry', font=('Roboto', 30), borderwidth=5, relief='raised',
                       cursor='hand2', command=action_with_arg)
    retry_btn.grid(row=0, column=0, sticky='nsew', padx=(10, 5), pady=10)

    # Add settings button to bottom frame
    action_with_arg = partial(drawSettings, root)
    settings_btn = Button(master=bottom_frm, text='Settings', font=('Roboto', 30), borderwidth=5, relief='raised',
                          cursor='hand2', command=action_with_arg)
    settings_btn.grid(row=0, column=1, sticky='nsew', padx=(5, 10), pady=10)


# Settings Page --------------------------------------------------------------------------------------------------------
def genClick(button, gen):
    if backend.GENERATIONS[gen]:
        button.configure(relief='raised')
    else:
        button.configure(relief='sunken')

    backend.toggleGeneration(gen)


def setGenButtonRelief(button, gen):
    if backend.GENERATIONS[gen]:
        button.configure(relief='sunken')
    else:
        button.configure(relief='raised')


def toggleDif(easy_btn, hard_btn, option):
    if option == 'EASY':
        backend.DIFFICULTY = 'EASY'
        easy_btn.configure(relief='sunken')
        hard_btn.configure(relief='raised')
    else:
        backend.DIFFICULTY = 'HARD'
        easy_btn.configure(relief='raised')
        hard_btn.configure(relief='sunken')


def drawSettings(root):
    for x in root.winfo_children():
        x.destroy()

    # Top Frame
    if backend.DIFFICULTY == 'EASY':
        top_frm = Frame(master=root, bg='#e4000f', padx=5, pady=5)

    else:
        top_frm = Frame(master=root, bg='#362D5C', padx=5, pady=5)

    top_frm.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 5), sticky='nsew')
    top_frm.grid_propagate(FALSE)

    top_frm.rowconfigure(0, weight=1)
    top_frm.rowconfigure(1, weight=2)
    top_frm.rowconfigure(2, weight=1)
    top_frm.columnconfigure(0, weight=1)
    top_frm.columnconfigure(1, weight=20)

    # Bottom Frame
    bottom_frm = Frame(master=root, bg='white', padx=5, pady=5)
    bottom_frm.grid(row=1, padx=10, pady=(5, 10), sticky='nsew')
    bottom_frm.grid_propagate(FALSE)

    bottom_frm.rowconfigure(0, weight=1, uniform='fred')
    bottom_frm.rowconfigure(1, weight=1, uniform='fred')
    bottom_frm.columnconfigure(0, weight=2)
    bottom_frm.columnconfigure(1, weight=1, uniform='fred')
    bottom_frm.columnconfigure(2, weight=1, uniform='fred')
    bottom_frm.columnconfigure(3, weight=1, uniform='fred')
    bottom_frm.columnconfigure(4, weight=1, uniform='fred')
    bottom_frm.columnconfigure(5, weight=1, uniform='fred')
    bottom_frm.columnconfigure(6, weight=1, uniform='fred')
    bottom_frm.columnconfigure(7, weight=1, uniform='fred')

    # Add Home Button to top frame
    action_with_arg = partial(callDrawStart, root)
    home_btn = Button(master=top_frm, text='BACK', font=('Roboto', 30), borderwidth=5, relief='raised', padx=20,
                      pady=20, cursor='hand2', command=action_with_arg)
    home_btn.grid(row=1, column=0, sticky='nsew', padx=(20, 10), pady=20)

    # Add the label to the top frame
    settings_lbl = Label(master=top_frm, text='SETTINGS', font=('Roboto', 30), bg='white', borderwidth=5,
                         relief='solid', padx=20, pady=20)
    settings_lbl.grid(row=1, column=1, padx=(10, 20), pady=20, sticky='nsew')

    # Add generations label to the bottom frame
    generations_lbl = Label(master=bottom_frm, text='GENERATIONS:', font=('Roboto', 20), borderwidth=5, relief='solid',
                            padx=20, pady=20)
    generations_lbl.grid(row=0, padx=(20, 10), pady=(20, 10), sticky='nsew')

    # Add generations buttons to bottom frame
    genI_btn = Button(master=bottom_frm, text='I', font=('Roboto', 20), borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genI_btn, 0)
    genI_btn.configure(command=action_with_arg)
    genI_btn.grid(row=0, column=1, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genI_btn, 0)

    genII_btn = Button(master=bottom_frm, text='II', font=('Roboto', 20),
                       borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genII_btn, 1)
    genII_btn.configure(command=action_with_arg)
    genII_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genII_btn, 1)

    genIII_btn = Button(master=bottom_frm, text='III', font=('Roboto', 20),
                        borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genIII_btn, 2)
    genIII_btn.configure(command=action_with_arg)
    genIII_btn.grid(row=0, column=3, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genIII_btn, 2)

    genIV_btn = Button(master=bottom_frm, text='IV', font=('Roboto', 20),
                       borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genIV_btn, 3)
    genIV_btn.configure(command=action_with_arg)
    genIV_btn.grid(row=0, column=4, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genIV_btn, 3)

    genV_btn = Button(master=bottom_frm, text='V', font=('Roboto', 20),
                      borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genV_btn, 4)
    genV_btn.configure(command=action_with_arg)
    genV_btn.grid(row=0, column=5, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genV_btn, 4)

    genVI_btn = Button(master=bottom_frm, text='VI', font=('Roboto', 20),
                       borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genVI_btn, 5)
    genVI_btn.configure(command=action_with_arg)
    genVI_btn.grid(row=0, column=6, sticky='nsew', padx=5, pady=(20, 10))
    setGenButtonRelief(genVI_btn, 5)

    genVII_btn = Button(master=bottom_frm, text='VII', font=('Roboto', 20),
                        borderwidth=5, relief='raised', cursor='hand2')
    action_with_arg = partial(genClick, genVII_btn, 6)
    genVII_btn.configure(command=action_with_arg)
    genVII_btn.grid(row=0, column=7, sticky='nsew', padx=(5, 20), pady=(20, 10))
    setGenButtonRelief(genVII_btn, 6)

    # Add difficulty label to the bottom frame
    difficulty_lbl = Label(master=bottom_frm, text='DIFFICULTY:', font=('Roboto', 20),
                           borderwidth=5, relief='solid', padx=10, pady=10)
    difficulty_lbl.grid(row=1, padx=(20, 10), pady=(10, 20), sticky='nsew')

    # Add Easy button to bottom frame
    easy_btn = Button(master=bottom_frm, text="EASY", font=('Roboto', 20),
                      borderwidth=5, relief='raised', cursor='hand2')

    # Add Hard button to bottom frame
    hard_btn = Button(master=bottom_frm, text="HARD", font=('Roboto', 20),
                      borderwidth=5, relief='raised', cursor='hand2')

    action_with_arg = partial(toggleDif, easy_btn, hard_btn, 'EASY')
    easy_btn.configure(command=action_with_arg)
    action_with_arg = partial(toggleDif, easy_btn, hard_btn, 'HARD')
    hard_btn.configure(command=action_with_arg)

    if backend.DIFFICULTY == 'EASY':
        easy_btn.configure(relief='sunken')

    else:
        hard_btn.configure(relief='sunken')

    easy_btn.grid(row=1, column=1, sticky='nsew', padx=5, pady=(10, 20), columnspan=3)
    hard_btn.grid(row=1, column=4, sticky='nsew', padx=(5, 10), pady=(10, 20), columnspan=3)