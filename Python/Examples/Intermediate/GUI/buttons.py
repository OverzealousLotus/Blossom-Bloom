"""Buttons in Tkinter."""
from tkinter import Button, PhotoImage, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Main function of the program."""
    root = Tk()


    def click() -> None:
        """When clicked, prints."""
        print("*Crackle..*")


    head = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/zeus.png")

    switch = Button(  # Button creation
        root,
        text="*Whirring winds*",
        font=("Arial", 11, "bold"),
        fg="blue",
        bg="black",
        activeforeground="blue",  # When button is hovered over, or pressed
        activebackground="grey",
        image=head,
        compound="top",
        command=click)  # A command to do when button is pressed
    switch.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
