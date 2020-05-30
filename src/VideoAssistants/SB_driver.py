import os
from src import project_path as pp
from SB import SupplyBot as SB

raw_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '01 - Raw')
trimmed_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '02 - Trimmed')
cropped_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '03 - Cropped')

for video_file_name in os.listdir(cropped_data_folder_path):
    video_file_path = os.path.join(cropped_data_folder_path, video_file_name)

    sb = SB(video_file_path=video_file_path)
    sb.pretty_print_video_properties()
    sb.build_arena_landmarks_dictionary()