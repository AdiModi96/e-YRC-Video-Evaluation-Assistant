import os
import cv2
from matplotlib import pyplot as plt
import project_path as pp

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


    def display_frame(self, image):
        cv2.namedWindow(self.video_file_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(self.video_file_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(self.video_file_name, image)
        while True:
            key = cv2.waitKey()
            if key == 27:
                cv2.destroyAllWindows()
                break
            if key == ord('s'):
                # Save Function Here
                print('Image Saved Successfully!')
                cv2.destroyAllWindows()
                break

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
