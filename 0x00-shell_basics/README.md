All files are shell scripts that perform specific operations some on specific files.

file 0-current_working_directory
Prints the absolute path name of the current working directory.

file 1-listit
Displays the contents list of your current directory.

file 2-bring_me_home
Changes the working directory to the user’s home directory.

file 3-listfiles
Displays current directory contents in a long format.

file 4-listmorefiles
Displays current directory contents, including hidden files (starting with .). Use the long format.

file 5-listfilesdigitonly
Displays current directory contents in long format with user and group IDs displayed numerically and hidden files (starting with .).

file 6-firstdirectory
Creates a directory named my_first_directory in the /tmp/ directory.

file 7-movethatfile
Moves the file betty from /tmp/ to /tmp/my_first_directory.

file 8-firstdelete
Deletes the file betty.

file 9-firstdirdeletion
Deletes the directory my_first_directory that is in the /tmp directory.

file 10-back
Changes the working directory to the previous one.

file 11-lists
Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

file 12-file_type
Prints the type of the file named iamafile.

file 13-symbolic_link
Creates a symbolic link to /bin/ls, named __ls__

file 14-copy_html
Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

file 100-lets_move
Moves all files beginning with an uppercase letter to the directory /tmp/u.

file 101-clean_emacs
Deletes all files in the current working directory that end with the character ~.

file 102-tree
Creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

file 103-commas
Lists all the files and directories of the current directory, separated by commas (,).

file school.mgc
Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0
