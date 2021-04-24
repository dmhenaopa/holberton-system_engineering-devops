## :pencil2: Shell I/O redirections and filters
This folder contains some useful scripts with basis Shell commands to navigate the filesystem, change directories, list the files (incluided hidden files), use of arguments with the commands, manipulate files and search information about the usage of some of this commands. Some of the commands used in this scripts:

| Scripts for |Commands used|
|--|--|
| Navigation | cd, pwd, ls | 
| Looking around | ls, less, file |
| Manipulating files | cp, mv, rm, mkdir|
| Other commands | type, which, help, man |

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script:
+ 0-hello_world: Prints "Hello, World".
+ 1-confused_smiley: Displays a confused smiley "(Ôo)'.
+ 2-hellofile: Display the content of the /etc/passwd file.
+ 3-twofiles: Display the content of /etc/passwd and /etc/hosts.
+ 4-lastlines: Display the last 10 lines of /etc/passwd.
+ 5-firstlines: Display the first 10 lines of /etc/passwd.
+ 6-third_line: Displays the third line of the file iacta -> "Alea iacta est ("The die is cast") is a Latin phrase attributed by Suetonius".
+ 7-file: Write a shell script that creates a file named exactly as the name contained in the script file: and containing the text Holberton School ending by a new line.
+ 8-cwd_state: Writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
+ 9-duplicate_last_line: Write a script that duplicates the last line of the file iacta.
+ 10-no_more_js: Deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
+ 11-directories: Counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted.
+ 12-newest_files: Displays the 10 newest files in the current directory. One file per line, sorted from the newest to the oldest.
+ 13-unique: Takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word. Words should be sorted.
+ 14-findthatword: Display lines containing the pattern "root" from the file /etc/passwd.
+ 15-countthatword: Display the number of lines that contain the pattern "bin" in the file /etc/passwd.
+ 16-whatsnext: Display lines containing the pattern "root" and 3 lines after them in the file /etc/passwd.
+ 17-hidethisword: Display all the lines in the file /etc/passwd that do not contain the pattern "bin".
+ 18-letteronly: Display all lines of the file /etc/ssh/sshd_config starting with a letter, include capital letters as well.
+ 19-AZ: Replace all characters A and c from input to Z and e respectively.
+ 20-hiago: Create a script that removes all letters c and C from input.
+ 21-reverse: Write a script that reverse its input.
+ 22-users_and_homes: Write a script that displays all users and their home directories, sorted by users.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MzMzMjA3Miw1ODA1NDc5NjhdfQ==
-->