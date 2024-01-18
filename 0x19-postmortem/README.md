Postmortem Task

At approximately 06:00 AM West African Time (WAT) here in Nigeria, an outage occurred on an ubuntu 20.04 container running an Apache web server. GET requests on the server returned 500 Server Errors instead of an html file of a simple Holberton WordPress site.

Debugging Process
Imagine going to a retaurant early and the waiter gets your order wrong. What a way to start a day. I immedietly started debugging the issue upon receiving an alert

Ran uptime to serr how long server had been up and its load average. All intervals wer okay.

Checked running processes using ps aux. Two apache2 processes - root and www-data - were properly running.

Looked in the sites-available folder of the /etc/apache2/ directory. Determined that the web server was serving content located in /var/www/html/.

Got the pid of the server and ran strace on it from a tmux window. In another window, I ran curl on loaclhost. Found nothing much.

Repeated above steps, except on the PID of the www-data process. In the strace log file found an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.

Looked through files in the /var/www/html/ directory one-by-one, using grep to locate file with line containing .phpp file extension. It was found in the wp-settings.php file. (require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

Deleted the extra p from the line.

Tried curl and got a 200 response.

Wrote a Puppet manifest to automate fixing of the error.

Summary
The outagewas due to a simple typo in the app setting and was unable to access requsted file
Solution was  a simple fix on the typo.

Prevention
To prevent such outages and respond faster use the following

Monotoring services like datadog could have alerted us earlier if we had on set up.

Comprehensively test apps before deploying. Error could have been addressed earlier had the app been tested.
