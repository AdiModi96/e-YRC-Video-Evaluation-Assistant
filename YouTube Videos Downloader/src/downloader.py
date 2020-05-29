import os
import sys
import project_path as pp
import csv
from pytube import YouTube
import requests
from multiprocessing import Process


def is_internet_connected():
    ping_url = 'https://www.google.com'
    try:
        requests.get(ping_url)
        return True
    except Exception:
        return False


def download_theme(theme, teams_list):
    # Creating Theme folder path to save videos
    theme_folder_path = os.path.join(pp.data_folder_path, theme)
    if not os.path.isdir(theme_folder_path):
        os.mkdir(theme_folder_path)

    print('Downloading Theme {}...'.format(theme), '\t')

    # Creating logger
    with open(os.path.join(pp.logs_folder_path, theme + '.csv'), 'w', newline='') as file:
        csv_log_file = csv.writer(file, delimiter=',')
        csv_log_file.writerow(['Team Number', 'Task Type', 'Successful/Unsuccessful'])

        # Iterating over submission links to download
        total_videos = len(teams_list)
        for idx in range(total_videos):
            team_number = teams_list[idx][0]
            team_video_submission_link = teams_list[idx][1]
            team_task_type = teams_list[idx][2]
            print('Theme {}:\n\tDownloading Video of Team Number: {}'.format(theme, team_number), '\n\tTask Type: {}'.format(team_task_type))

            # Downloading youtube video with highest spatial resolution
            try:
                yt = YouTube(team_video_submission_link)
                yt.streams.get_highest_resolution().download(
                    output_path=theme_folder_path, filename=str(team_number) + "_" + team_task_type)
                csv_log_file.writerow([team_number, team_task_type, 'Successful'])
            except:
                csv_log_file.writerow([team_number, team_task_type, 'Unsuccessful'])

    print('Completed downloading Theme {}!'.format(theme), '\t')


def generate_data_dictionary_from_csv(csv_file_path):
    data_dictionary = {}

    # Opening CSV file
    with open(csv_file_path) as file:
        csv_file_reader = csv.reader(file)

        # Ignoring headers
        next(csv_file_reader)
        for row in csv_file_reader:

            # Extracting Content
            team_number = int(row[1])
            team_theme = row[2].upper()
            team_video_submission_link = row[3]
            team_task_type = row[4].lower()

            # Appending to Data Dictionary
            if team_theme not in data_dictionary:
                data_dictionary[team_theme] = []
            data_dictionary[team_theme].append((team_number, team_video_submission_link, team_task_type))

    return data_dictionary


def main():
    if not is_internet_connected():
        print('Error: Not connected to the internet. Quitting...')
        sys.exit(0)

    csv_file_path = os.path.join(pp.resrc_folder_path, 'YouTube Video Links.csv')
    data_dictionary = generate_data_dictionary_from_csv(csv_file_path)

    processes = []
    for theme in data_dictionary.keys():
        process = Process(target=download_theme, args=(theme, data_dictionary[theme]))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
