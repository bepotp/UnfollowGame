######################################################################################################
#  			UNFOLLOW GAME
# Author: Bepotp
# Be Carreful : Quick and Dirty
# Unfollow the friends who tweets about this fucking game http://en.wikipedia.org/wiki/The_Game_(mind_game)
######################################################################################################
import twitter

#Declare account token
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#Declare searched words
KEY_WORDS = [["perdre","jeu"],["lost","game"],["perdu","jeu"]]


#Return 1 if the tweet contains words from KEY_WORDS 0 else
def searchTheGame(tweet):
	bool_words = 0
	bool_word = 1
	for words in KEY_WORDS :
		for word in words:
			if tweet.find(word) != -1 :
				bool_word = bool_word & 1
			else :
				bool_word = bool_word & 0
		bool_words = bool_words | bool_word
	return bool_words


#Api connexion
api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_KEY, access_token_secret=ACCESS_SECRET)
api.VerifyCredentials()  

#We get Friends Timeline(retweets included)
timeline = api.GetFriendsTimeline(retweets='Yes')

#Foreach tweet
for tweet in timeline :
	#If the tweet contains a couple of searched words
	if searchTheGame(tweet.text) == 1 :
		#The User was unfollow
		unFollowUser = t.user
		api.DestroyFriendship(unFollowUser.id)
		print "The User \"" + unFollowUser.name +"\" was unfollowed for his tweet : " +tweet.text


