import os
import project_path as pp
from assistants import SupplyBot as SB

final_sb_data_folder_path = os.path.join(pp.data_folder_path, 'SB', '03 - Cropped')

for video_file_name in os.listdir(final_sb_data_folder_path):
    video_file_path = os.path.join(final_sb_data_folder_path, video_file_name)

    sb = SB(video_file_path=video_file_path)
    sb.pretty_print_video_properties()
    sb.build_arena_landmarks_dictionary()