import cv2
import os
from src import project_path as pp
import numpy as np

class SupplyBot:

    saved_images_folder_path = os.path.join(pp.saved_results_folder_path, 'SB')
    os.makedirs(saved_images_folder_path, exist_ok=True)

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
            self.build_video_properties_dictionary()

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
                cv2.imwrite(os.path.join(SupplyBot.saved_images_folder_path,
                                         self.video_file_name.split('.')[0] + '.png'), image)
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


    def get_arena_center(self, frame_gray):
        circles = cv2.HoughCircles(frame_gray.copy(),
                                   cv2.HOUGH_GRADIENT,
                                   1,
                                   minDist=100,
                                   param1=175,
                                   param2=15,
                                   minRadius=5,
                                   maxRadius=25)

        arena_center_limit_left = self.video_properties['spatial_center'][0] - 50
        arena_center_limit_right = self.video_properties['spatial_center'][0] + 50
        arena_center_limit_top = self.video_properties['spatial_center'][1] - 50
        arena_center_limit_bottom = self.video_properties['spatial_center'][1] + 50

        for circle in circles[0]:
            if circle[0] > arena_center_limit_left and circle[0] < arena_center_limit_right and circle[1] > arena_center_limit_top and circle[1] < arena_center_limit_bottom:
                    return circle[0], circle[1], circle[2]

        return None, None, None

    def build_arena_landmarks_dictionary(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # Finding the Center of the Arena
        _, frame = self.video.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        x, y, r = self.get_arena_center(frame_gray)
        self.arena_landmarks['center'] = (x, y)
        self.arena_landmarks['center_radius'] = r

        # Finding the Nodes Center
        annotated_frame = frame_gray.copy()
        X, Y = np.ogrid[
               0:self.video_properties['spatial_resolution'][1],
               0:self.video_properties['spatial_resolution'][0]]


        annotated_frame = cv2.adaptiveThreshold(annotated_frame,
                                                maxValue=255,
                                                adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                thresholdType=cv2.THRESH_BINARY,
                                                blockSize=25,
                                                C=-18)
        outer_radius = 325
        inner_radius = 245
        annotated_frame[(X - self.arena_landmarks['center'][1]) ** 2 + (Y - self.arena_landmarks['center'][0]) ** 2 > outer_radius ** 2] = 0
        annotated_frame[(X - self.arena_landmarks['center'][1]) ** 2 + (Y - self.arena_landmarks['center'][0]) ** 2 < inner_radius ** 2] = 0

        annotated_frame[annotated_frame < 145] = 0
        annotated_frame[annotated_frame >= 145] = 255

        annotated_frame = cv2.erode(annotated_frame, kernel=np.ones(shape=(5, 5), dtype=np.uint8), iterations=1)
        annotated_frame = cv2.erode(annotated_frame, kernel=np.ones(shape=(3, 3), dtype=np.uint8), iterations=1)

        self.display_frame(annotated_frame)

        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
