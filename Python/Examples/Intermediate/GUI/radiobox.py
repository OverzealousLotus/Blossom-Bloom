"""Radioboxes in Tkinter."""
from tkinter import IntVar, PhotoImage, Radiobutton, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Main function of our program."""
    backgrounds = ["Sinister", "Aerial", "Inferno"]

    root = Tk()

    zeus = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/zeus.png")
    tail = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/tail.png")
    peace = PhotoImage(file="Python/Examples/Intermediate/GUI/assets/peace.png")

    background_images = [zeus, tail, peace]

    x = IntVar()

    for index in range(len(backgrounds)):

        quest_list = Radiobutton(
            root,
            text=backgrounds[index],  # Adds text to our buttons
            variable=x,  # Groups our buttons if they share the same variable
            value=index,  # Assigns each button a different value
            padx=15,
            pady=15,
            font=("Arial", 12, "bold"),
            image=background_images[index])  # Assigns background image
        quest_list.pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()
