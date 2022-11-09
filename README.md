# π Games

## Project Description
After memorizing by hearth the first 2000 digits of π (for fun and mental training) I wanted a simple CLI system to revise them from time to time.
I also like to play games with friends like "Tell me the 512th digit of π!" (It's 4 btw) and see how much time I need to answer.
This project solves all these needs for me and for whoever wants to use it. It is extremely easy to install and you can play it on any computer with Python.
Have fun with π Games and let me know how to improve it!

---

## How to Install and Run the Project

After cloning the repo, i recommend to use a virtual environment like **venv** which is included with your Python installation.
Simply go to the directory where you cloned the repo:
```
cd pi_games
```
Run the snippet below within the directory to create the virtual environment:
```
python3 -m venv venv
```
Start the virtual environment with:
```
source venv/bin/activate
```
Install the dependencies that are included in the 'requirements.txt' file by running:
```
python3 -m pip install -r requirements.txt
``` 
You are ready to go!

---

## How to Use the Project


To use the script just run:
```
python3 start_here.py
```
And follow the prompts ;)

---

## Statistics
What would be an app without a database? An app without data! Therefore you will find already implemented a nice sqlite3 database called 'sessions'db' that will be created the first time you run either game 5 or 6. It will contain all the data regarding the sessions you did: game_no (Number of the game),date (when you did the session),mistakes_no (number of mistakes),mistakes (which mistakes were done in a useful python dictionary format),time (how much time you needed to finish each game), pi_series (which series of digits you played with). Please notice: sqlite3 is already included in your Python installation, so you do not need to install additional dependencies.
If you know how to use sqlite3, feel free to create your own queries and get all the data you need from your 'sessions.sb' file.
One thing you can do for example is to export all your session in CSV format. 
The easiest way to do this is by running this simple sqlite3 command:

```
sqlite3 -header -csv sessions.db < select_all.sql > all_sessions.csv
```

After running this, you will find the file 'all_sessions.csv' in your directory.

---

## Credits
- π to 1.000.000: https://www.gutenberg.org/files/50/50.txt
- "Colorama" by Jonathan Hartley: https://pypi.org/project/colorama/


