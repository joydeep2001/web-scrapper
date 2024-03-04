# Please Note: Due to security reasons chess.com will block the script to execute. But if you still want to give a try read ahead!
## This script is created to download game archive data (pgn files) from chess.com archive.

### Prerequisites
- Firefox Browser

(You May use chrome as well but you have to change the code accordingly. Do your own research for that) 

### To run this script follow the steps: (Commands are for Linux/MacOS/WINDOWS)
- Create virtual environment
  `python3 -m venv venv`
- Install the Dependencies
  `pip install -r requirements.txt`
- Activate virtual env
  `source venv/bin/activate`
  
Yes That's it the step is complete...

### Instructions to run
- Replace `archive_url` varaibale's value with the link of your archive page of chess.com
- Run script `python3 web_scrapper.py`
- After you run the script a new window will open on automatically on chess.com.  
- Put your userid password manually on the chess.com page. The code will wait untill you go back to the terminal and press enter.
- After login go back to the terminal and press enter.
- Rest part will be done by the script.

*Final Notes: Although the code is suppose to download all your chess pgn files from the
   archive_url provided but it will not work probably as chess.com will keep blocking selenium but if you have any trick please let us know.*
