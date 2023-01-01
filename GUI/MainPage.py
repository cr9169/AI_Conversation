from tkinter import *


class ConvoPage:
    def __init__(self, window):
        self.main_label = Label(window, text="AI CONVERSATION")
        self.main_label.place(x=200, y=20)
        self.InfoPageButton = Button(window, text='Info', command=self.go_to_info_page)
        self.ConvoPageButton = Button(window, text='Start', command=self.go_to_convo_page)

    def go_to_info_page(self, window):
        # go to info page
        window.destroy()

    def go_to_convo_page(self, window):
        # go to convo page
        window.destroy()


def main():
    window = Tk()
    page = ConvoPage(window)
    window.geometry("500x500")
    window.mainloop()


if __name__ == '__main__':
    main()
