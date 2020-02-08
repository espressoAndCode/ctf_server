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
The server is currently configured to run in `debug` mode and listens on `port 5000`. This can be modified by editing `server.py` as follows:
```
app.config['DEBUG'] = False
```
*However* - the debug mode is currently restarting the server automatically, so if this is changed there will need to be a process in place for restarting for any crash during game play.

#### KO Score Polling

The server will start a process that runs every 20 seconds to scan the urls listed in `data/ko_target_db.json`. This process interval can be changes by editing the `cron/ko_score_provider.py` file:

```
KO_POLLING_INTERVAL=20
```
#### KO Game Machine Polling Routes



```
{
  "KO001": {
    "score": 5,
    "path": "http://127.0.0.1:9000/index.html"
  },
  //add additional game machines here by duplicating the above sample
}
```

Right now there are 2 of these on localhost routes with ports 9000 and 9001. These lines should be edited with the actual KOTH VM URL's that will be scanned for flags.

#### Game Machine Flag example
I've included a `sample/index.html` file with an example of what the `ko_score_provider` method is parsing. This file should be included as-is on each game machine. The player should enter their team name between the `<koth>` tags as shown.


```
<html>
  <head>
  </head>
  <body>
    <!-- Put your team name between the koth tags below -->
    <koth>DC864</koth>
  </body>
</html>
```

If you don't serve these test sites prior to starting the main server or if the individual machine goes down during play the game server process won't crash, it just won't update the KOTH scores in `data/score_db.json` with info for that path.




