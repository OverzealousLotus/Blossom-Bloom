"""Windows in Tkinter."""
from tkinter import PhotoImage, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Main function of the program."""
    # Widgets are elements such as: buttons, textboxes, labels, and images
    # Windows serve as containers for Widgets

    root = Tk()  # instantiate an instance of a window
    root.geometry("420x420")  # Define the dimensions of our window
    root.title("My first GUI in Python!")  # The title of our window

    # We can change the icon, but first, we must define our image as PhotoImage
    icon = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/zeus.png")
    root.iconphoto(True, icon)  # Now, we call the modified image
    root.config(background="black")  # Changes background color, can be hex

    root.mainloop()  # Place window on screen, and listen for events


if __name__ == "__main__":
    main()
