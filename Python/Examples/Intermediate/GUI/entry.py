'''Entry boxes in Tkinter'''
from tkinter import Tk, Entry, Button, END

root = Tk()


def submit():
    username = gatekeeper.get()
    print(f'Hello, {username}.')
    gatekeeper.config(state='disabled')


def backspace():
    gatekeeper.delete(len(gatekeeper.get())-1, END)


def delete():
    gatekeeper.delete(0, END)


gatekeeper = Entry(  # Our entry box
    root,
    font=('Arial', 11, 'bold'),
    fg='white',
    bg='black'
    )
gatekeeper.pack(side='left')
gatekeeper.insert(0, 'Enter your name please!')

submit_button = Button(  # A submit button
    root,
    text='submit',
    command=submit
    )
submit_button.pack(side='right')

backspace_button = Button(  # Backspace button
    root,
    text='backspace',
    command=backspace
    )
backspace_button.pack(side='right')

delete_button = Button(  # Delete all button
    root,
    text='delete',
    command=delete
    )
delete_button.pack(side='right')

root.mainloop()
