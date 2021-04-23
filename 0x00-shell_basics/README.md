## :pencil2: Shell basic commands


### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script:

+ [0-current_working_directory](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory): Prints the absolute path name of the current working directory. *Example:*
```
$ ./0-current_working_directory
/Users/holbertonschool/holbertonschool-sysadmin_devops/0x00-shell_basics
$
```
+ [1-listit](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/1-listit): Display the contents list of your current directory. *Example:*
```
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```
+ [2-bring_me_home](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home): Changes the working directory to the users home directory. *Example:*
+ [3-listfiles](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles): Display current directory contents in a long format. *Example:*
+ [4-listmorefiles](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles): Display current directory contents, including hidden files. *Example:*
+ [5-listfilesdigitonly](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly): Display current directory contents using a long format with user and group IDs displayed numerically and hidden files. *Example:*
+ 6-firstdirectory: Creates a directory named holberton in the /tmp/ directory. *Example:*
+ 7-movethatfile: Move the file betty from /tmp/ to /tmp/holberton. *Example:*
+ 8-firstdelete: Delete the file betty that is in /tmp/holberton/ directory. *Example:*
+ 9-firstdirdeletion: Delete the directory holberton that is in the /tmp directory. *Example:*
+ 10-back: Changes the working directory to the previous one. *Example:*
+ 11-lists: Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format. *Example:*
+ 12-file_type: Prints the type of the file named /tmp/iamafile. *Example:*
+ 13-symbolic_link: Create a symbolic link to /bin/ls, named __ls__, in the current working directory. *Example:*
+ 14-copy_html: Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. *Example:*
+ 15-lets_move: Moves all files beginning with an uppercase letter to the directory /tmp/u. *Example:*
+ 16-clean_emacs: Deletes all files in the current working directory that end with the character ~. *Example:*
+ 17-tree: Creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory. *Example:*
+ 18-commas: Command that lists all the files and directories of the current directory, separated by commas (,). Directory names should end with a slash (/). Files and directories starting with a dot (.) should be listed. The listing should be alpha ordered, except for the directories (.) and (..) which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first.  *Example:*
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc5MDkyNjM3NSwtMzY4MDU2NjI2LDE0Nj
MyMTU5MDIsMTkxNDE3Mjk3NF19
-->