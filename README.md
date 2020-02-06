# DefCON864 CTF Server
The backend for DefCon864's Capture the Flag project.

### Installation

```
git clone https://github.com/espressoAndCode/ctf_server.git

cd ctf_server

pip install -r requirements.txt

```
To run:

```
python server.py
```
The server is currently configured to run in `debug` mode and listens on `port 5000`.


### Notes

The server will start a process that runs every 5 seconds (this is way too often, but just for development). It scans the urls listed in `data/ko_target_db.json`. Right now there are 2 of these on localhost routes with ports 9000 and 9001. These lines should be edited with the actual KOTH VM URL's that will be scanned for flags.

I've included a `sample/index.html` file that shows what I'm currently parsing with the regex. For testing, I am serving an instance of this file on the ports referenced above.

If you don't serve these test sites prior to starting the main server, the process won't crash, it just won't update the KOTH scores in `data/score_db.json`




