import os
import cv2
from matplotlib import pyplot as plt
import project_path as pp
import numpy as np


class Annotator():

    def __init__(self, video_file_path):
        if not os.path.isfile(video_file_path):
            print('Video File Doesn\'t Exist!')
            del self
        else:
            self.video_file_path = os.path.abspath(video_file_path)
            self.video_file_name = str(self.video_file_path).split(os.sep)[-1]
            self.video = cv2.VideoCapture(self.video_file_path)
            self.video_properties = {}
            self.arena_landmarks = {}

    def build_video_properties_dictionary(self):
        if self.video == None:
            return None
        else:
            self.video_properties['number_of_frames'] = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
            self.video_properties['fps'] = self.video.get(cv2.CAP_PROP_FPS)
            self.video_properties['temporal_step'] = int(1000 // self.video_properties['fps'])
            self.video_properties['spatial_resolution'] = (
                int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            )
            self.video_properties['spatial_center'] = (
                self.video_properties['spatial_resolution'][0] // 2,
                self.video_properties['spatial_resolution'][1] // 2
            )

    def pretty_print_video_properties(self):
        print('=====' * 20)
        print('⦿ "{}" Video Properties:'.format(self.video_file_name))
        print('-----' * 20)
        print('• Duration of Video: {} minutes and {} seconds'.format(
            self.video_properties['number_of_frames'] // 60,
            self.video_properties['number_of_frames'] % 60
        ))
        print('• Number of Frames: {}'.format(self.video_properties['number_of_frames']))
        print('• Frames Per Second (FPS): {}'.format(self.video_properties['fps']))
        print('• Spatial Resolution: (W × H): ({} px × {} px)'.format(
            self.video_properties['spatial_resolution'][0],
            self.video_properties['spatial_resolution'][1]
        ))
        print('=====' * 20)

    def __update_frame_in_annotator_video(self):
        pass

    def start_annotating_window(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        plt.figure(num=self.video_file_name)

        plt.subplot2grid(shape=(10, 10), loc=(0, 1), rowspan=10, colspan=9)
        image_ax = plt.imshow(np.zeros(shape=(100, 100, 3), dtype=np.float64))
        while self.video.isOpened():
            print(True)
            _, frame = self.video.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) / 255
            image_ax.set_data(frame)
            plt.draw()

        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
