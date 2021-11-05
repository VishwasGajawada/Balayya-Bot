# Balayya-Bot
Reddit comment bot emulating Telugu actor N. Bala Krishna.

## Project structure
 - `config.py` contains Bot's higher level configuration.
 - `generate_queue.py` decides which action to take after parsing the comment and adds it to the queue.
 - `main.py` executes the pending actions in queue. 
 - `utils.py` contains utilities for comment-scraping, comments-parsing, logging, stats, etc.
 - `/resources` contains comments and replies databases for each distinct action. Examples below.
   - `/resources/triggers.csv` contains replies for trigger words found in user comments.
   - `/resources/drinking.txt` contains replies if there is a trigger word for drinking.
   - `/resources/salutation.txt` contains replies if there is a trigger word for salutation.

## Contribution Guidelines
 - There will only ever be a single branch to make the project simpler.
**Step1:** Fork the repo.<br>
**Step2:** Make changes.<br>
**Step3:** Create pull request.

## More info
 - [BalayyaBot Reddit page](https://www.reddit.com/user/BalayyaBot)
