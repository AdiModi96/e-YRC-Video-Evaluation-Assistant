import os
import tkinter as Tk
import project_path as pp


class ToolWidget:
    GENERIC_CONFIGS = {
        'level_1_label_frame': {
            'bd': 0,
            'font': ('Raleway', 18),
            'relief': Tk.RIDGE
        },
        'level_2_label_frame': {
            'bd': 4,
            'font': ('Raleway', 14),
            'relief': Tk.RIDGE
        },
        'button': {
            'bd': 4,
            'activebackground': '#FFF',
            'activeforeground': '#000',
            'font': ('Raleway', 12),
            'compound': Tk.LEFT,
            'width': 150
        }
    }

    def build_landmark_markers_label_frame(self):
        self.landmark_markers_label_frame = Tk.LabelFrame(master=self.markers_label_frame,
                                                          text='Landmarks',
                                                          cnf=ToolWidget.GENERIC_CONFIGS['level_2_label_frame'])
        self.landmark_markers_label_frame.grid({'row': 0, 'column': 0, 'sticky': Tk.N + Tk.W})

        center_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'center.png')),
        self.center_button = Tk.Button(master=self.landmark_markers_label_frame,
                                       text='Center',
                                       image=center_image,
                                       cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.center_button.image = center_image
        self.center_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 0, 'sticky': Tk.W})

        node_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'node.png')),
        self.node_button = Tk.Button(master=self.landmark_markers_label_frame,
                                     text='Node',
                                     image=node_image,
                                     cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.node_button.image = node_image
        self.node_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 1, 'sticky': Tk.E})

    def build_coins_markers_label_frame(self):
        self.coins_markers_label_frame = Tk.LabelFrame(master=self.markers_label_frame,
                                                       text='Coins',
                                                       cnf=ToolWidget.GENERIC_CONFIGS['level_2_label_frame'])
        self.coins_markers_label_frame.grid({'row': 1, 'column': 0, 'sticky': Tk.N + Tk.W})

        bot_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'red coin.png')),
        self.undo_button = Tk.Button(master=self.coins_markers_label_frame,
                                     text='Red Coin',
                                     image=bot_image,
                                     cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.undo_button.image = bot_image
        self.undo_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 0, 'sticky': Tk.W})

        green_coin_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'green coin.png')),
        self.green_coin_button = Tk.Button(master=self.coins_markers_label_frame,
                                           text='Green Coin',
                                           image=green_coin_image,
                                           cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.green_coin_button.image = green_coin_image
        self.green_coin_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 1, 'sticky': Tk.E})

    def build_bot_markers_label_frame(self):
        self.bot_markers_label_frame = Tk.LabelFrame(master=self.markers_label_frame,
                                                     text='Bot',
                                                     cnf=ToolWidget.GENERIC_CONFIGS['level_2_label_frame'])
        self.bot_markers_label_frame.grid({'row': 2, 'column': 0, 'sticky': Tk.N + Tk.W})

        bot_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'bot.png')),
        self.undo_button = Tk.Button(master=self.bot_markers_label_frame,
                                     text='Bot',
                                     image=bot_image,
                                     cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.undo_button.image = bot_image
        self.undo_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 0, 'sticky': Tk.W})

    def build_markers_label_frame(self):
        self.markers_label_frame = Tk.LabelFrame(master=self.root,
                                                 text='Markers',
                                                 cnf=ToolWidget.GENERIC_CONFIGS['level_1_label_frame'])
        self.markers_label_frame.grid({'padx': 15, 'pady': 15, 'row': 0, 'column': 0, 'sticky': Tk.N + Tk.W})
        self.build_landmark_markers_label_frame()
        self.build_coins_markers_label_frame()
        self.build_bot_markers_label_frame()

    def build_options_label_frame(self):
        self.options_label_frame = Tk.LabelFrame(master=self.root,
                                                 text='Options',
                                                 cnf=ToolWidget.GENERIC_CONFIGS['level_1_label_frame'])
        self.options_label_frame.grid({'padx': 15, 'pady': 15, 'row': 1, 'column': 0, 'sticky': Tk.N + Tk.W})

        undo_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'undo.png')),
        self.undo_button = Tk.Button(master=self.options_label_frame,
                                     text='Undo',
                                     image=undo_image,
                                     cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.undo_button.image = undo_image
        self.undo_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 0, 'sticky': Tk.W})

        clear_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'clear.png')),
        self.clear_button = Tk.Button(master=self.options_label_frame,
                                      text='Clear',
                                      image=clear_image,
                                      cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.clear_button.image = clear_image
        self.clear_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 0, 'column': 1, 'sticky': Tk.W})

        save_image = Tk.PhotoImage(file=os.path.join(pp.resrc_folder_path, 'VideoAnnotator', 'SB', 'images', 'save.png')),
        self.save_button = Tk.Button(master=self.options_label_frame,
                                     text='Save',
                                     image=save_image,
                                     width=ToolWidget.GENERIC_CONFIGS['button']['width'] * 2 + 40,
                                     cnf=ToolWidget.GENERIC_CONFIGS['button'])
        self.save_button.image = save_image
        self.save_button.grid({'padx': 10, 'pady': 10, 'ipadx': 5, 'ipady': 5, 'row': 1, 'column': 0, 'columnspan': 2})

    def build_widget(self):
        self.root = Tk.Tk()
        self.root.title("Marker Panel")
        self.root.resizable(0, 0)
        self.build_markers_label_frame()
        self.build_options_label_frame()
        self.root.mainloop()


def main():
    tw = ToolWidget()
    tw.build_widget()


if __name__ == '__main__':
    main()
