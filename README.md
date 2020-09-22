# Discord-Bot
A mini-project to create a discord bot with multiple functionalities

## Pre Requisites ## 
You need the following modules to be able to run this file
* discord.py
* os
* random

To run this bot in your server, do the following:
* Create a file named token.txt in the same directory as that of the bot.py
* In this file, add your discord bot token.

## Run The Bot ##

You have to run the bot.py in your machine.
After you have gone through the prerequisites, you can now run this bot

To run this type the following in the command line in the cloned directory '$python3 bot.py'
If no errors have occured, the bot should start functioning

To run this file in your terminal in the background do the following:
```
$python3 bot.py &
```

To keep this file running even after you close your terminal, do the following:
```
$nohup python3 bot.py > log.out 2> log.err &
```

To kill this program, you have to first identify the pid of your program.
To do this, type `$pidof python3 bot.py`

The first number <pid> is generally the one that has to be killed by you to stop the execution of the program.

Kill it using the folliwng command: `kill <pid>`
Here `log.out` will contain the stdout while `log.err` will contain the error messages received by the bot

## Add the Bot on your server ###

* To do this, go to your discord applications, OAuth2 tab.
* Click on the option bot from the set of options available.
* Next click on the permissions you want to give it.
* Copy the generated url.
* Paste this url on a browser.
* Select the server in which you want to deploy it.

Voila! You have added this bot in your server. Have fun!