from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'shine':
                try:
                    new_name = filename
                    extension='noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension='noname'
                    file_exists = os.path.isfile(extensions_folders[extension] + '/' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(path + '/' + new_name)
                    src = folder_to_track + "/" + filename

                    current_datetime = datetime.datetime.now()
                    year = current_datetime.year
                    month = current_datetime.month
                    
                    folder_destination_path = os.path.join(path, str(year), str(month))


                    if not os.path.exists(folder_destination_path):
                        os.makedirs(folder_destination_path)

                    new_name = os.path.join(folder_destination_path, new_name)
                    os.rename(src, new_name) 
                except Exception:
                    print(filename) 
            
extensions_folders ={
    #no Name
    'noname' : "/Users/shine/Desktop/shine/Text/Other/Uncategorized",
    #audios
    '.aif' : "/Users/shine/Desktop/shine/Media/Audio",
    '.cda' : "/Users/shine/Desktop/shine/Media/Audio",
    '.mid' : "/Users/shine/Desktop/shine/Media/Audio",
    '.midi' : "/Users/shine/Desktop/shine/Media/Audio",
    '.mp3' : "/Users/shine/Desktop/shine/Media/Audio",
    '.mpa' : "/Users/shine/Desktop/shine/Media/Audio",
    '.ogg' : "/Users/shine/Desktop/shine/Media/Audio",
    '.wav' : "/Users/shine/Desktop/shine/Media/Audio",
    '.wma' : "/Users/shine/Desktop/shine/Media/Audio",
    '.wpl' : "/Users/shine/Desktop/shine/Media/Audio",
    #TextFiles
    '.txt' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.doc' : "/Users/shine/Desktop/shine/Text/Microsoft/Word",
    '.docx' : "/Users/shine/Desktop/shine/Text/Microsoft/Word",
    '.odt' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.pdf' : "/Users/shine/Desktop/shine/Text/PDF",
    '.rtf' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.tex' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.wks' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.wps' : "/Users/shine/Desktop/shine/Text/TextFiles",
    '.wpd' : "/Users/shine/Desktop/shine/Text/TextFiles",
    #videos
    '.3g2' : "/Users/shine/Desktop/shine/Media/Video",
    '.3gp' : "/Users/shine/Desktop/shine/Media/Video",
    '.avi' : "/Users/shine/Desktop/shine/Media/Video",
    '.flv' : "/Users/shine/Desktop/shine/Media/Video",
    '.h264' : "/Users/shine/Desktop/shine/Media/Video",
    '.m4v' : "/Users/shine/Desktop/shine/Media/Video",
    '.mkv' : "/Users/shine/Desktop/shine/Media/Video",
    '.mov' : "/Users/shine/Desktop/shine/Media/Video",
    '.mp4' : "/Users/shine/Desktop/shine/Media/Video",
    '.mpg' : "/Users/shine/Desktop/shine/Media/Video",
    '.mpeg' : "/Users/shine/Desktop/shine/Media/Video",
    '.rm' : "/Users/shine/Desktop/shine/Media/Video",
    '.swf' : "/Users/shine/Desktop/shine/Media/Video",
    '.vob' : "/Users/shine/Desktop/shine/Media/Video",
    '.wmv' : "/Users/shine/Desktop/shine/Media/Video",
    #Images
    '.ai' : "/Users/shine/Desktop/shine/Media/Images",
    '.bmp' : "/Users/shine/Desktop/shine/Media/Images",
    '.gif' : "/Users/shine/Desktop/shine/Media/Images",
    '.ico' : "/Users/shine/Desktop/shine/Media/Images",
    '.jpg' : "/Users/shine/Desktop/shine/Media/Images",
    '.jpeg' : "/Users/shine/Desktop/shine/Media/Images",
    '.png' : "/Users/shine/Desktop/shine/Media/Images",
    '.ps' : "/Users/shine/Desktop/shine/Media/Images",
    '.psd' : "/Users/shine/Desktop/shine/Media/Images",
    '.svg' : "/Users/shine/Desktop/shine/Media/Images",
    '.tif' : "/Users/shine/Desktop/shine/Media/Images",
    '.tiff' : "/Users/shine/Desktop/shine/Media/Images",
    #internet
    '.asp' : "/Users/shine/Desktop/shine/Other/Internet",
    '.aspx' : "/Users/shine/Desktop/shine/Other/Internet",
    '.cer' : "/Users/shine/Desktop/shine/Other/Internet",
    '.cfm' : "/Users/shine/Desktop/shine/Other/Internet",
    '.cgi' : "/Users/shine/Desktop/shine/Other/Internet",
    '.pl' : "/Users/shine/Desktop/shine/Other/Internet",
    '.css' : "/Users/shine/Desktop/shine/Other/Internet",
    '.htm' : "/Users/shine/Desktop/shine/Other/Internet",
    # '.html' : "/Users/shine/Desktop/shine/Other/Internet",
    '.js' : "/Users/shine/Desktop/shine/Other/Internet",
    '.jsp' : "/Users/shine/Desktop/shine/Other/Internet",
    '.part' : "/Users/shine/Desktop/shine/Other/Internet",
    '.php' : "/Users/shine/Desktop/shine/Other/Internet",
    '.rss' : "/Users/shine/Desktop/shine/Other/Internet",
    '.xhtml' : "/Users/shine/Desktop/shine/Other/Internet",
    #compressed files
    '.7z' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.arj' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.deb' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.pkg' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.rar' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.rpm' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.tar.gz' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.z' : "/Users/shine/Desktop/shine/Other/Compressed",
    '.zip' : "/Users/shine/Desktop/shine/Other/Compressed",
    #disc
    '.bin' : "/Users/shine/Desktop/shine/Other/Disc",
    '.dmg' : "/Users/shine/Desktop/shine/Other/Disc",
    '.iso' : "/Users/shine/Desktop/shine/Other/Disc",
    '.toast' : "/Users/shine/Desktop/shine/Other/Disc",
    '.vcd' : "/Users/shine/Desktop/shine/Other/Disc",
    #data
    '.csv' : "/Users/shine/Desktop/shine/Programming/Database",
    '.dat' : "/Users/shine/Desktop/shine/Programming/Database",
    '.db' : "/Users/shine/Desktop/shine/Programming/Database",
    '.dbf' : "/Users/shine/Desktop/shine/Programming/Database",
    '.log' : "/Users/shine/Desktop/shine/Programming/Database",
    '.mdb' : "/Users/shine/Desktop/shine/Programming/Database",
    '.sav' : "/Users/shine/Desktop/shine/Programming/Database",
    '.sql' : "/Users/shine/Desktop/shine/Programming/Database",
    '.tar' : "/Users/shine/Desktop/shine/Programming/Database",
    '.xml' : "/Users/shine/Desktop/shine/Programming/Database",
    '.json' : "/Users/shine/Desktop/shine/Programming/Database",
    #executables
    '.apk' : "/Users/shine/Desktop/shine/Other/Executables",
    '.bat' : "/Users/shine/Desktop/shine/Other/Executables",
    '.com' : "/Users/shine/Desktop/shine/Other/Executables",
    '.exe' : "/Users/shine/Desktop/shine/Other/Executables",
    '.gadget' : "/Users/shine/Desktop/shine/Other/Executables",
    '.jar' : "/Users/shine/Desktop/shine/Other/Executables",
    '.wsf' : "/Users/shine/Desktop/shine/Other/Executables",
    #Fonts
    '.fnt' : "/Users/shine/Desktop/shine/Other/Fonts",
    '.fon' : "/Users/shine/Desktop/shine/Other/Fonts",
    '.otf' : "/Users/shine/Desktop/shine/Other/Fonts",
    '.ttf' : "/Users/shine/Desktop/shine/Other/Fonts",
    #presentations
    '.key' : "/Users/shine/Desktop/shine/Text/Presentations",
    '.odp' : "/Users/shine/Desktop/shine/Text/Presentations",
    '.pps' : "/Users/shine/Desktop/shine/Text/Presentations",
    '.ppt' : "/Users/shine/Desktop/shine/Text/Presentations",
    '.pptx' : "/Users/shine/Desktop/shine/Text/Presentations",
    #Programming
    '.c' : "/Users/shine/Desktop/shine/Programming/C&C++",
    '.class' : "/Users/shine/Desktop/shine/Programming/Java",
    '.dart' : "/Users/shine/Desktop/shine/Programming/Dart",
    '.py' : "/Users/shine/Desktop/shine/Programming/Python",
    '.sh' : "/Users/shine/Desktop/shine/Programming/Shell",
    '.swift ' : "/Users/shine/Desktop/shine/Programming/Swift",
    '.html' : "/Users/shine/Desktop/shine/Programming/C&C++",
    '.h' : "/Users/shine/Desktop/shine/Programming/C&C++",
    #spreadsheets
    '.ods' : "/Users/shine/Desktop/shine/Text/Microsoft/Excel",
    '.xlr' : "/Users/shine/Desktop/shine/Text/Microsoft/Excel",
    '.xls' : "/Users/shine/Desktop/shine/Text/Microsoft/Excel",
    '.xlsx' : "/Users/shine/Desktop/shine/Text/Microsoft/Excel",


}

folder_to_track = '/Users/shine/Desktop'
folder_destination = '/Users/shine/Desktop/shine'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
  
