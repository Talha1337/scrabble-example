# scrabble-example
Building scrabble on the CL

# Starting 
## required files:

You may need to download the list of scrabble words in advance of playing this [here](https://drive.google.com/file/d/1oGDf1wjWp5RF_X9C7HoedhIWMh5uJs8s/view)

Name this file "scrabble_words.txt" in the same directory as the repository.

## Running with uv:

```
uv run game.py
```

## Running with pip:

```
source .venv/bin/activate
pip install -r requirements.txt
python3 game.py
```

# Testing

If you have changed features you may want to run `test_game.py`, which will run games with known moves and known outcomes, which can be found in the `testing_games` folder. Within each of these folders, a JSON file and a CSV file of game moves exist. Game moves are played out and the final board is compared with the correct JSON file. This should run without errors, meaning tests have passed.




