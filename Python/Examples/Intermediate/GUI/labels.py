"""Labels in Tkinter."""
from tkinter import Label, PhotoImage, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Main function of our program."""
    root = Tk()

    zeus = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/zeus.png")

    our_label = Label(
        root,
        text="Silence... Is great.",  # Actual text
        font=("Arial", 11, "bold"),  # Font
        fg="purple",  # Foreground
        bg="black",  # Background
        relief="raised",  # Border type
        bd=10,  # Border perimeter
        padx=20,  # Text distance from border x
        pady=20,  # Text distance from border y
        image=zeus,  # Image
        compound="top")  # Location of image

    our_label.pack()  # "Packs" our label
    # our_label.place(x=0, y=0)  # Places our label in a set position

    root.mainloop()


if __name__ == "__main__":
    main()
