import twitter
from twitter import Twitter
from twitter import OAuth

oauth_token = "1219034994-UU6fd8lmiO9WMXuJ3wJyBwsEW3pllr5deJsv1Yz"
oauth_token_secret = "m8OhrVTEmQUVaA2Y3SnIUvYpftU3KLneFYaM0w978eo"


CONSUMER_KEY = "pG5rPkXCCD0XxkVQ8TQXxw"
CONSUMER_SECRET = "h8nD6gfEKJyAyR4KvrwiDq21Nu1IfwLegaVjAexGHY"



twitter = Twitter(auth=OAuth(oauth_token,oauth_token_secret,CONSUMER_SECRET,CONSUMER_KEY))
twitter.statuses.update(status="I'm tweeting from Python!")


