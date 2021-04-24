## :pencil2: Shell basic commands

| Scripts for |Commands used|
|--|--|
| Navigation | cd, pwd, ls | 
| Looking around | ls, less, file |
| Manipulating files | cp, m|
|  |  |

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script:

+ [0-current_working_directory](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory): Prints the absolute path name of the current working directory.
+ [1-listit](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/1-listit): Display the contents list of your current directory. 
+ [2-bring_me_home](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home): Changes the working directory to the users home directory. 
+ [3-listfiles](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles): Display current directory contents in a long format. 
+ [4-listmorefiles](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles): Display current directory contents, including hidden files.
+ [5-listfilesdigitonly](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly): Display current directory contents using a long format with user and group IDs displayed numerically and hidden files.
+ [6-firstdirectory](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory): Creates a directory named holberton in the /tmp/ directory.
+ [7-movethatfile](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile): Move the file betty from /tmp/ to /tmp/holberton.
+ [8-firstdelete](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete): Delete the file betty that is in /tmp/holberton/ directory.
+ [9-firstdirdeletion](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion): Delete the directory holberton that is in the /tmp directory.
+ [10-back](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/10-back): Changes the working directory to the previous one.
+ [11-lists](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/11-lists): Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
+ [12-file_type](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type): Prints the type of the file named /tmp/iamafile. 
+ [13-symbolic_link](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link): Create a symbolic link to /bin/ls, named __ls__, in the current working directory.
+ [14-copy_html](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html): Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
+ [15-lets_move](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/15-lets_move): Moves all files beginning with an uppercase letter to the directory /tmp/u.
+ [16-clean_emacs](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/16-clean_emacs): Deletes all files in the current working directory that end with the character ~.
+ [17-tree](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/17-tree): Creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
+ [18-commas](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/18-commas): Command that lists all the files and directories of the current directory, separated by commas (,). Directory names should end with a slash (/). Files and directories starting with a dot (.) should be listed. The listing should be alpha ordered, except for the directories (.) and (..) which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTc1NzQxNDksMTIwOTY1Njc0NiwzNz
Y3MTYzNzEsLTM2ODA1NjYyNiwxNDYzMjE1OTAyLDE5MTQxNzI5
NzRdfQ==
-->