## :pencil2: Shell I/O redirections and filters
This folder contains some useful scripts with basis Shell commands to display a line or more of text, how to redirect standard output to a file, how to get standard input from a file, how to concatenate files and print on the standard output, how to reverse a string, how to remove sections from each line of files, how to send the output from one program to the input of another, how to combine commands and filters with redirections. Some of the commands used in this scripts:

| Scripts for |Commands used|
|--|--|
| Redirect and filter | echo, cat, head, tail, find, wc, sort, uniq, grep, tr, rev, cut, paswd | 

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script:
+ [0-hello_world](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world): Prints "Hello, World".
+ [1-confused_smiley](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley): Displays a confused smiley "(Ôo)'.
+ [2-hellofile](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile): Display the content of the /etc/passwd file.
+ [3-twofiles](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles): Display the content of /etc/passwd and /etc/hosts.
+ [4-lastlines](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines): Display the last 10 lines of /etc/passwd.
+ [5-firstlines](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines): Display the first 10 lines of /etc/passwd.
+ [6-third_line](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line): Displays the third line of the file iacta -> "Alea iacta est ("The die is cast") is a Latin phrase attributed by Suetonius".
+ [7-file](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/7-file): Write a shell script that creates a file named exactly as the name contained in the script file: and containing the text Holberton School ending by a new line.
+ [8-cwd_state](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state): Writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
+ [9-duplicate_last_line](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line): Write a script that duplicates the last line of the file iacta.
+ [10-no_more_js](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js): Deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
+ [11-directories](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories): Counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted.
+ [12-newest_files](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files): Displays the 10 newest files in the current directory. One file per line, sorted from the newest to the oldest.
+ [13-unique](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique): Takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word. Words should be sorted.
+ [14-findthatword](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword): Display lines containing the pattern "root" from the file /etc/passwd.
+ [15-countthatword](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword): Display the number of lines that contain the pattern "bin" in the file /etc/passwd.
+ [16-whatsnext](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext): Display lines containing the pattern "root" and 3 lines after them in the file /etc/passwd.
+ [17-hidethisword](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword): Display all the lines in the file /etc/passwd that do not contain the pattern "bin".
+ [18-letteronly](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly): Display all lines of the file /etc/ssh/sshd_config starting with a letter, include capital letters as well.
+ [19-AZ](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ): Replace all characters A and c from input to Z and e respectively.
+ [20-hiago](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago): Create a script that removes all letters c and C from input.
+ [21-reverse](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse): Write a script that reverse its input.
+ [22-users_and_homes](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes): Write a script that displays all users and their home directories, sorted by users.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI3NjY0NDU5NCwxNzczMDQ5MDQyLC0xND
kwMDYxNDg0LDU4MDU0Nzk2OF19
-->