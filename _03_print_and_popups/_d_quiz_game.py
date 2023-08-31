from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__=='__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    spanish = simpledialog.askstring(title= None, prompt = 'What country has the most spanish speakers')
    if spanish == 'Mexico':
        score = score + 2
        messagebox.showinfo(title=None, message='Correct')
    else:
        score = score - 1
        messagebox.showinfo(title=None, message='False')
    mostspeakers = simpledialog.askstring(title= None, prompt = 'What language has the most amount of speakers')
    if mostspeakers == 'English':
        score += 2
        messagebox.showinfo(title=None, message='Correct')
    else:
        score -= 1
        messagebox.showinfo(title=None, message='False')

    europe = simpledialog.askstring(title= None, prompt = 'What language has the most amount of native speakers in europe')
    if europe == 'Russian':
        score += 2
        messagebox.showinfo(title= None, message = 'Correct')
    else:
        score -=1
        messagebox.showinfo(title=None, message='False')
    messagebox.showinfo(title= None, message= 'Your final score is '+str(score))
    #      // 2.  Ask the user a question
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
