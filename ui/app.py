import customtkinter as ctk

from ui.windows.main_window import MainWindow


def main():

    # Tema
    ctk.set_appearance_mode("dark")

    ctk.set_default_color_theme("blue")

    # App
    app = MainWindow()

    app.mainloop()


if __name__ == "__main__":
    main()