#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - used to ensure creation of zombie processes
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0 always
 */
int main(void)
{
	int i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		i++;
	}
	infinite_while();
	return (0);
}
