from statistics import mean

class Game:
    all = []

    # Game is initialized with a title
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
        
    # Returns the games title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and title:
            self._title = title
    
    # Object Relationship Methods and Properties
    #############################################
    
    ### Game results()
    # Returns a list of all results for that game
    # Results must be of type Result                      
    def results(self):
        return [result for result in Result.all if result.game is self]
    
    ### Game players()
    # Returns a unique list of all players that played a particular game
    # Players must be of type Player
    def players(self):
        return list({result.player for result in self.results()})

    # Aggregate and Association Methods
    ###################################

    ### Game average_score(player)
    # Receives a player object as argument
    # Returns the average of all the player's scores for a particular game instance
    # Reminder: you can calculate the average by adding up all the results' scores of the player specified and dividing by the number of those results
    def average_score(self, player):
        scores = [result.score for result in player.results() if result.game is self]
        return mean(scores) if len(scores) else 0 
    
######################################################################################
    
class Player:
    all = []
    
    # Player is initialized with a username
    def __init__(self, username):
        self.username = username

    # Returns the player's username
    @property
    def username(self):
        return self._username

    # Usernames must be of type str
    # Usernames must be between 2 and 16 characters, inclusive. 
    # Should be able to change after the player is instantiated
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

     # Object Relationship Methods and Properties
    #############################################
            
    ### Player results()
    # Returns a list of all results for that player
    # Results must be of type Result
    def results(self):
        return [result for result in Result.all if result.player is self]

    ### Player games_played()
    # Returns a unique list of all games played by a particular player
    # Games must be of type Game 
    def games_played(self):
        return list({result.game for result in self.results()})

    # Aggregate and Association Methods
    ###################################

    # Player played_game(game)
    # Receives a game object as argument
    # Returns True if the player has played the game object provided
    # Returns False otherwise
    def played_game(self, game):
        return game in self.games_played()

    # Player num_times_played(game)
    # Receives a game object as argument
    # Returns the number of times the player has played the game instance provided
    # Returns 0 if the player never played the game provided
    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

######################################################################################
    
class Result:
    all = []

    #Result is initialized with a Player instance, a Game instance, and a score.
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    ### Result property score
    # Returns the result's score
    # Scores must be of type int
    # Scores must be between 1 and 5000, inclusive
    # Should not be able to change after the result is instantiated
    # hint: hasattr()
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score

    # Object Relationship Methods and Properties
    ############################################

    # Result property player
    # Returns the player object for that result
    # Must be of type Player

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    # Result property game
    # Returns the game object for that result
    # Must be of type Game
   
    @property 
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
