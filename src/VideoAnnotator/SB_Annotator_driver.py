import os
from src import project_path as pp
from SB_Annotator import Annotator

raw_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '01 - Raw')
trimmed_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '02 - Trimmed')
cropped_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '03 - Cropped')

for video_file_name in os.listdir(cropped_data_folder_path):
    video_file_path = os.path.join(cropped_data_folder_path, video_file_name)

    annotator = Annotator(video_file_path=video_file_path)
    annotator.build_video_properties_dictionary()
    annotator.pretty_print_video_properties()
    annotator.start_annotating_window()
