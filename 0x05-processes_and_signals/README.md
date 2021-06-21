## :pencil2: Processes and signals
This folder contains some useful scripts with basis Shell commands. Use of different commands to obtain the process identification number PID and how to manage, trap, signals. Also how to kill a process with different strategies.

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:
Here a short description of each script:

+ 0-what-is-my-pid: A Bash script that displays its own PID.
+ 1-list_your_processes: A Bash script that displays a list of currently running processes. Show all processes, for all users, including those which might not have a TTY. Display in a user-oriented format. Show process hierarchy.
+ 2-show_your_bash_pid: A Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
+ 3-show_your_bash_pid_made_easy: A Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
+ 4-to_infinity_and_beyond: Bash script that displays To infinity and beyond indefinitely. In between each iteration of the loop, add a sleep 2.
+ 5-dont_stop_me_now: A Bash script that stops 4-to_infinity_and_beyond process.
+ 6-stop_me_if_you_can: A Bash script that stops 4-to_infinity_and_beyond process.
+ 7-highlander: A Bash script that displays "To infinity and beyond" indefinitely, with a sleep 2 in between eahc iteration and when receiving a SIGTERM signal prints "I am invincible!!!".
+ 8-beheaded_process: A Bash script that kills the process 7-highlander.
+ 100-process_and_pid_file: A Bash script that: Creates the file /var/run/holbertonscript.pid containing its PID. Displays To infinity and beyond indefinitely. Displays I hate the kill command when receiving a SIGTERM signal. Displays Y U no love me?! when receiving a SIGINT signal. Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal.
+
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk0Mjk2NTQ2OF19
-->