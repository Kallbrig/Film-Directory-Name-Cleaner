import os
from pathlib import Path
import re
import sys




try:
    arg_path = sys.argv[1]
except:
    print('Please pass the path of the folders you\'d like renamed')
    sys.exit()

print(f'Parsing at path: {arg_path}')
if input("This can't be reversed. Are you sure you want to continue? (y/n)\n") == 'y':
    print()

    os.chdir(arg_path)

    path = Path('')

    dirs = [e for e in path.iterdir() if e.is_dir()]

    dir_list = [str(directory) for directory in dirs]


    for folder in dir_list:

        if ' ' in folder:

            print('Before Transform: ', folder)

            folder_new = (re.sub("\[.*\]", "", folder))

            folder_new = (re.sub("\(", "- ", folder_new))
            folder_new = re.sub("\)", "", folder_new)
            try:
                os.rename(folder, folder_new)
                print('After Transform:  ', folder_new, '\n')
            except:
                print('ERROR: UNABLE TO RENAME FOLDER')



        elif '.' in folder:
            print('Before Transform: ', folder)
            folder_new = (re.sub("\[.*\]", " ", folder))

            folder_new = re.sub("\.", "", folder_new)
            common_tags = ['WEB', 'H264', 'AMZN', 'H264-MIXED', 'COMPLETE', '10bit', '6CH', 'WEB-DL', 'Bluray', 'x264',
                           'anoXmous', 'WEBRip', 'x265-RARBG', 'AC3-EVO', 'XviD', 'HDRip', '720p', '1080p', 'BluRay,']

            for i in common_tags:
                folder_new = re.sub(i, "", folder_new)

            folder_new = re.sub("\d\d\d\d", "- \g<0>", folder_new)

            folder_new = re.sub("SEASON \d*", "S\g<0>", folder_new)
            folder_new = re.sub("season \d*", "S\g<0>", folder_new)
            folder_new = re.sub("Season \d*", "S\g<0>", folder_new)

            folder_new = "".join(folder_new.split())

            try:
                os.rename(folder, folder_new)
                print('After Transform:  ', folder_new, '\n')
            except:
                print('ERROR: UNABLE TO RENAME FOLDER')
