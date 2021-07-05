## :pencil2: # Regular expression - Regex
This folder contains some useful Ruby scripts with basic usage of regular expressions or patterns. Some of the expressions used in this scripts follow the next patterns:
| Pattern | Significance |
|--|--|
| [abc] | A single character of a, b or c  |
| [^abc] | A single character except a, b or c  |
| [a-z] | A single character between a and z  |
| [a-zA-Z] | A single character between a-z or A-Z  |
| ^ | Start of line  |
| $ | End of line |
| . | Any single character |
| \s | Any whitespace character  |
| \S | Any non whitespace character  |
| \d | Any digit |
| \D | Any non-digit |
| \w | Any letter, number, underscore |
| \W | Any non letter, non number, non underscore |
| (...) | Everything enclosed |
| (a \| b) | a or b |
| a? | Zero or one of a |
| a* | Zero or more of a |
| a+ | One or more of a |
| a{3} | Exactly 3 of a |
| a{3,} | 3 or more of a |
| a{3,6} | Between 3 and 6 of a |

> [Taken from Rugular: a Ruby regular expression editor](https://rubular.com/)

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.  Ruby: 1.9.3p484 (2013-11-22).

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file "string to analize" ###To execute the file

### Executable files:

Here a short description of each script:
+ 0-simply_match_holberton.rb: Script that found a regular expression that match Holberton.
+ 1-repetition_token_0.rb: Script that found the regular expression that will match the cases: hbttn, hbtttn, hbttttn, hbtttttn... one or more repetitions of t.
+ 2-repetition_token_1.rb: Script that found the regular expression that will match the cases: htn, hbtn... 0 or 1 repetition of b between h and t.
+ 3-repetition_token_2.rb: Script that found the regular expression that will match the cases: hbtn, hbttn, hbtttn, hbttttn... one or more t's between b and n.
+ 4-repetition_token_3.rb: Script that found the regular expression that will match the cases: hbn, hbtn, hbttn, hbtttn... 0 or more of any single character except the 'o' between the b and the n.
+ 5-beginning_and_end.rb: Script that found the regular expression that exactly match a string that starts with h ends with n and can have any single character in between.
+ 6-phone_number.rb: Script that found the regular expression that exactly match a 10 digit phone number.
+ 7-OMG_WHY_ARE_YOU_SHOUTING.rb: Script that found the regular expression that exactly match capital letters.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzI1NjQ3NzNdfQ==
-->