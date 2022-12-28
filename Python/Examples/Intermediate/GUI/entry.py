"""Entry boxes in Tkinter."""
from tkinter import END, Button, Entry, Tk

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Main function of our program."""
    root = Tk()


    def submit() -> None:
        username = gatekeeper.get()
        print(f"Hello, {username}.")
        gatekeeper.config(state="disabled")


    def backspace() -> None:
        gatekeeper.delete(len(gatekeeper.get())-1, END)


    def delete() -> None:
        gatekeeper.delete(0, END)


    gatekeeper = Entry(  # Our entry box
        root,
        font=("Arial", 11, "bold"),
        fg="white",
        bg="black"
        )
    gatekeeper.pack(side="left")
    gatekeeper.insert(0, "Enter your name please!")

    submit_button = Button(  # A submit button
        root,
        text="submit",
        command=submit
        )
    submit_button.pack(side="right")

    backspace_button = Button(  # Backspace button
        root,
        text="backspace",
        command=backspace
        )
    backspace_button.pack(side="right")

    delete_button = Button(  # Delete all button
        root,
        text="delete",
        command=delete
        )
    delete_button.pack(side="right")

    root.mainloop()


if __name__ == "__main__":
    main()
