## :pencil2: Shell permissions
This folder contains some useful scripts with basis Shell commands to understand the multi-usesr capability of Unix-like sys Some of the commands used in this scripts:

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

+ 0-iam_betty: Changes your user ID to betty.
+ 1-who_am_i: Prints the effective userid of the current user.
+ 2-groups: Prints all the groups the current user is part of.
+ 3-new_owner: Changes the owner of the file hello to the user betty.
+ 4-empty: Creates an empty file called hello.
+ 5-execute: Adds execute permission to the owner of the file hello.
+ 6-multiple_permissions: Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
+ 7-everybody: Adds execution permission to the owner, the group owner and the other users, to the file hello.
+ 8-James_Bond: Write a script that sets the permission to the file hello as follows - Owner: no permission at all; Group: no permission at all; Other users: all the permissions.
+ 9-John_Doe: Sets the mode of the file hello to -rwxr-x-wx.
+ 10-mirror_permissions: Sets the mode of the file hello the same as olleh mode.
+ 11-directories_permissions: Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files doesn't be changed.
+ 12-directory_permissions: Creates a directory called dir_holberton with permissions 751 in the working directory.
+ 13-change_group: Changes the group owner to holberton for the file hello.
+ 14-change_owner_and_group: Changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
+ 15-symbolic_link_permissions: Changes the owner and the group owner of the file _hello to betty and holberton respectively.
+ 16-if_only: Changes the owner of the file hello to betty only if it is owned by the user guillaume.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwMDY3MzY0Miw3OTA3MjM1MzhdfQ==
-->