# 🚨 WordPress website outage incident report

<p align="center">
  <img src=https://user-images.githubusercontent.com/77861287/154872965-afafebe6-d813-4a0f-9866-31362ad133f4.gif>
</p>

<p align="center">Gif taken from: <a href="https://tenor.com/es/ver/everything-is-fine-dog-fire-burning-nothing-wrong-gif-15379714">junichols87</a></p>


## :memo:  Issue summary

On 02-15-2022, our WordPress website service was interrupted for more than a half-hour, from 7:00 am to 7:30 am (UTC−05:00). All the services offered by our website were affected. As a result of the problem, our website could not be accessed due to an internal server error (501).

## :globe_with_meridians:  Timeline (UTC−05:00)

- **7:00 am:** Error 501 was reported for the first time when trying to access the web page.
- **7:05 am:** The Apache server is restarted. It is verified that the 501 error continues to be generated.
- **7:07 am:** Server logs are examined. There is no report in the logs.
- **7:10 am:** It is evident that in the php.ini files, the PHP logging is disabled. The option to log these errors is enabled. The Apache server is restarted.
- **7:15 am:** The logs show errors related to the value of the variable `${APACHE_LOG_DIR}`.
- **7:20 am:** Use strace to trace the reason for the error.
- **7:25 am:** Syntax error in file /var/www/html/wp-settings.php
- **7:27 am:** The error in the file is corrected. The server is restarted.
- **7:30 am:** The tests are run. The content of the page in WordPress is now displayed correctly.

## :construction:  Root cause and resolution
The web service offered in WordPress runs on a LAMP-type software stack (Linux, Apache, MySQL, and PHP). During a scheduled exercise of maintenance and revision of the configuration files of the WordPress web page, the inconvenience arose. When saving the changes made in the maintenance, in the configuration files, and in an unintentional way, a typographical error was generated in the configuration file located in the path `/var/www/html/wp-settings.php`. 

This prevented the correct execution of the configuration files, generating a cascade of errors including:
- The configuration variable `${APACHE_LOG_DIR}` was not defined.
- There was no file or directory with path `/etc/apache2/${APACHE_LOG_DIR}`.
- Invalid mutex directory in argument file `${APACHE_LOG_DIR}`. 

The system could not access the files due to a mistake in typing the file extension to use. Instead of 'class-wp-locale.php' in the previously reported configuration file, this variable was being assigned the value 'class-wp-locale. phpp', which does not exist.

The only solution was to modify the configuration file `/var/www/html/wp-settings.php` again, modifying the value of the variable `${APACHE_LOG_DIR}`. Fixed file extension from phpp to php (class-wp-locale.php). Restarting the Apache server after the modifications caused the WordPress website to load properly.

## :goal_net:  Corrective and preventive measures

 - Any modification that is made, maintenance, incorporation of new
   functionalities..., must be evaluated and tested locally.

- Consider allowing logging of errors generated by the PHP module. Although there are some disadvantages as a decrease in the speed of the response or possible security problems due to attacks, it is important to evaluate that everything works properly, even temporarily.