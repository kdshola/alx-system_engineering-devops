Bash 0x05-processes_and_signals task files
0-what-is-my-pid
A Bash script that displays its own PID.

1-list_your_processes
A Bash script that displays a list of currently running processes.

2-show_your_bash_pid
Get the PID of your Bash process

3-show_your_bash_pid_made_easy
A Bash script that displays the PID, along with the process name, of processes whose name contain the word bash

4-to_infinity_and_beyond
A Bash script that displays To infinity and beyond indefinitely.

5-dont_stop_me_now
A Bash script that stops 4-to_infinity_and_beyond process.

6-stop_me_if_you_can
A Bash script that stops 4-to_infinity_and_beyond process.

7-highlander  67-stop_me_if_you_can
Bash script that displays:
To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal

8-beheaded_process
Bash script that kills the process 7-highlander.

100-process_and_pid_file
A Bash script that:
Creates the file /var/run/myscript.pid containing its PID
Displays To infinity and beyond indefinitely
Displays I hate the kill command when receiving a SIGTERM signal
Displays Y U no love me?! when receiving a SIGINT signal
Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

101-manage_my_process manage_my_process
A Bash script that:
Indefinitely writes I am alive! to the file /tmp/my_process
In between every I am alive! message, the program should pause for 2 seconds
Bash (init) script 101-manage_my_process that manages manage_my_process

102-zombie.c
A C program that creates 5 zombie processes and displays their id.
