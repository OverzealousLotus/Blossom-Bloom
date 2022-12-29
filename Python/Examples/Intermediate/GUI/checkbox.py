"""Checkboxes in Tkinter."""
from tkinter import Checkbutton, IntVar, PhotoImage, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Main function of the program."""
    def display() -> None:
        """Display logic."""
        if(x.get() == 1):
            print("You have agreed!")
        else:
            print("You do not agree ;-;")


    root = Tk()

    x = IntVar()  # Custom variables from Tkinter

    zeus = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/zeus.png")

    check_button = Checkbutton(  # Our checkbox
        root,
        text="I agree to trot alongside the path of darkness.",
        font=("Arial", 11, "bold"),
        fg="white",
        bg="black",
        activeforeground="white",
        activebackground="black",
        padx=15,
        pady=15,
        image=zeus,
        compound="top",
        variable=x,  # Allows us to modify x with our check
        onvalue=1,  # defines x as 1 if active
        offvalue=0,  # defines x as 0 when inactive
        command=display
    )
    check_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
