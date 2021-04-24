## :pencil2: Shell init files, variables and expansions
This folder contains some useful scripts with basic shell commands to create an alias, execute commands, perform arithmetic operations with the shell, how to use expansions, create/update/delete shell variables. Some of the commands used in this scripts:

| Scripts for |Commands used|
|--|--|
| Obtain and set environment variables | printenv, set, unset, export | 
| Replace/modificate a command | alias, unalias|
| Execute a file | source |
| Display the given value on terminal window | printf

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script:

+ [0-alias](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias): Create a script that creates an alias.
+ [1-hello_you](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you): Prints hello user, where user is the current Linux user.
+ [2-path](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path): Add /action to the PATH.
+ [3-paths](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths): Counts the number of directories in the PATH.
+ [4-global_variables](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables): Lists environment variables.
+ [5-local_variables](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables): Lists all local variables and environment variables, and functions.
+ [6-create_local_variable](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable): Creates a new local variable.
+ [7-create_global_variable](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable): Creates a new global variable.
+ [8-true_knowledge](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge): Prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
+ [9-divide_and_rule](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule): Prints the result of POWER divided by DIVIDE, followed by a new line. POWER and DIVIDE are environment variables.
+ [10-love_exponent_breath](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath): Displays the result of BREATH to the power LOVE. BREATH and LOVE are environment variables.
+ [11-binary_to_decimal](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal): Write a script that converts a number from base 2 to base 10. The number in base 2 is stored in the environment variable BINARY.
+ [12-combinations](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations): Prints all possible combinations of two letters, except oo. Letters are lower cases, from a to z. One combination per line. The output should be alpha ordered, starting with aa Your script file should contain maximum 64 characters.
+ [13-print_float](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float): rints a number with two decimal places, followed by a new line. The number will be stored in the environment variable NUM.
+ [14-decimal_to_hexadecimal](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/14-decimal_to_hexadecimal): Converts a number from base 10 to base 16. The number in base 10 is stored in the environment variable DECIMAL. The script should display the number in base 16, followed by a new line. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwMzA4MjkwMiwtMTgzMzkzNjMzNCwxND
cwMTgwOTU3LC00MDQxODY5NDgsLTExODgxOTI4MTRdfQ==
-->