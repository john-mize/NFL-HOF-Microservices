import flask
import RB_HOF_predict
import WR_HOF_predict
 
app = flask.Flask(__name__)
app.json.sort_keys = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
# app.config["DEBUG"] = True

# homepage
@app.route("/")
def index():
    index_string = """<pre>
    Welcome to John's NFL Wide Receiver and Running Back Hall of Fame Predictions! You can find the add the following paths to the end of the current URL to query different information, 
    starting with /[position] (wr for wide receivers, rb for running backs): 

    1. /[position]/predictions: the full list of predicted HOF players 
    2. /[position]/player_list: this lists all players, ranks, and full stats 
    3. /[position]/players: a simplified version of the previous query, only returns players and their rankings (useful for obtaining names to query individual players) 
    4. /[position]/players/[Player_Name]: this returns just the individual player's full stats, must be separated by an underscore
    
    examples: /wr/players/Jerry_Rice or /rb/predictions
    <pre>"""
    return index_string

def dictMaps(position, dictionary, player=None):
    posMaps = {
    "wr, predict": WR_HOF_predict.HOF_predict,
    "wr, stats": WR_HOF_predict.playerStatsDict,
    "wr, players": WR_HOF_predict.playersNameDict,
    "wr, playerStats": WR_HOF_predict.playersDict,
    "rb, predict": RB_HOF_predict.HOF_predict,
    "rb, stats": RB_HOF_predict.playerStatsDict,
    "rb, players": RB_HOF_predict.playersNameDict,
    "rb, playerStats": RB_HOF_predict.playersDict
    }
    if position == "wr" or position == "rb":
        if not player:
            return posMaps[f"{position}, {dictionary}"]
        if player:
            return posMaps[f"{position}, {dictionary}"][f"{player}"]
    else:
        return "error: you must enter either 'wr' or 'rb'"

# predictions list
@app.route("/<position>/predictions", methods=['GET'])
def get_predictions(position):
    return dictMaps(position, "predict")

# list of all players, rankings, and full stats
@app.route("/<position>/player_list", methods=['GET'])
def get_list(position):
    return dictMaps(position, "stats")

# list of all players and rankings
@app.route("/<position>/players", methods=['GET'])
def get_names(position):
    return dictMaps(position, "players")

# query individual players' full stats by name, with no quotes and first/last names separated by underscore
@app.route("/<position>/players/<player>", methods=['GET'])
def get_name(position, player):
    fixed_name = player.replace("_", " ")
    return dictMaps(position, "playerStats", fixed_name)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)