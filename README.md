# Beat Saber Custom Level Folder Renamer
A simple program that renames the folders of custom levels in Beat Saber to the level's name and author.  
Level information is read from the 'info.dat' file of a custom level.

Custom levels downloaded from beatsaver would usually have a uid name such as  
fd7e25c79800d792a177ebbbf6930599dfb369e6  
This program will fix it.


## HOW TO USE
1. Put the py file file outside the folder that contains all the custom levels.  
Usually in '\steamapps\common\Beat Saber\Beat Saber_Data'.  
2. Run the py file.  


## Variables and Settings
1. Change *MAIN_FOLDER* to the desired name if you want to use other folders.  
2. *PREFIX* and *SUFFIX* could be changed to use other keys in the info see below for details.
3. Change *CONNECT* if you want to use other characters to connect *PREFIX* and *SUFFIX*.  
Be aware that some characters are not allowed in directory names.  
4. Set *FORCED* to **True** if you want to force rename all folders.


### Keys in info.dat
Base on the example custom level 'Beat Saber', here is some possible keys:  
'_songName'  
'_songSubName'  
'_songAuthorName'  
'_levelAuthorName'  
'_beatsPerMinute'


