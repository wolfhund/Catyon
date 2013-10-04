from twython import Twython, TwythonError
import base64
import ConfigParser

def decode(skey, string):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string)
    for i in xrange(len(string)):
        key_c = skey[i % len(skey)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string

def get_keys(objConfig):
    objConfig.read("config.ini")
    keys = []

    try:
        APP_KEY = objConfig.get("catyon", "APP_KEY")
    except:
        print "Fatal Error: APP_KEY not found"
    try:
        APP_SECRET = objConfig.get("catyon", "APP_SECRET")
    except:
        print "Fatal Error: APP_SECRET not found"
    try:
        HASH_KEY = objConfig.get("hash", "HASH_KEY")
    except:
        print "Fatal Error: HASH_KEY not found"

    APP_KEY = decode(HASH_KEY, APP_KEY)
    APP_SECRET = decode(HASH_KEY, APP_SECRET)
    keys.append(APP_KEY)
    keys.append(APP_SECRET)

    return keys

def get_tokens(objConfig):
    objConfig.read("tokens.ini")
    tokens = []
    try:
        OAUTH_TOKEN = objConfig.get("user", "OAUTH_TOKEN")
    except:
        OAUTH_TOKEN = ''
    try:
        OAUTH_TOKEN_SECRET = objConfig.get("user", "OAUTH_TOKEN_SECRET")
    except:
        OAUTH_TOKEN_SECRET = ''

    tokens.append(OAUTH_TOKEN)
    tokens.append(OAUTH_TOKEN_SECRET)

    return tokens

def user_login():
    """
    Checks for user tokens.
    """
    config = ConfigParser.ConfigParser()

    # get keys
    app_keys = get_keys(config)
    APP_KEY = app_keys[0]
    APP_SECRET = app_keys[1]

    # get tokens'

    app_tokens= get_tokens(config)
    OAUTH_TOKEN = app_tokens[0]
    OAUTH_TOKEN_SECRET = app_tokens[1]

    if OAUTH_TOKEN != '' and OAUTH_TOKEN_SECRET != '':	
        try:
            twitter = Twython(APP_KEY, APP_SECRET,
                              OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            print "Login successful."
            print "Account: "+twitter.verify_credentials()['screen_name']
        except TwythonError as e:
            print e
    else:
        print "Authorization tokens needed."
        twitter = create_tokens(config, APP_KEY, APP_SECRET)
    return twitter

def create_tokens(objConfig, app_key, app_secret):
    """
    Gets new auth tokens and writes them in 'config.ini' file
    """
    twitter = Twython(app_key, app_secret)
    auth = twitter.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    print "To get your PIN number please go to: "
    print auth['auth_url']+"\n"
    oauth_verifier = raw_input('Please enter your PIN number: ')
    twitter = Twython(app_key, app_secret,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    final_step = twitter.get_authorized_tokens(oauth_verifier)
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

    try:
        twitter = Twython(app_key, app_secret,
                          OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        user = twitter.verify_credentials()['screen_name']
        print "Login successful."
        print "Account: "+user
        # save oauth_tokens in file
        cfgfile = open("tokens.ini",'w')
        objConfig.add_section('user')
        objConfig.set('user','OAUTH_TOKEN', OAUTH_TOKEN)
        objConfig.set('user','OAUTH_TOKEN_SECRET', OAUTH_TOKEN_SECRET)
        objConfig.write(cfgfile)
        cfgfile.close()
        return twitter
    except TwythonError as e:
        print e



def get_user_timeline(twitter):
    """
    Gets current user timeline
    """
    try:
        timeline = twitter.get_user_timeline()
    except TwythonError as e:
        print e

    return timeline

def update_status(twitter, mystatus):
    """
    Update current user status
    """
    try:
        twitter.update_status(status = mystatus)
    except TwythonError as e:
        print e

def search(twitter, terms):
    """
    Search and shows up to 10 tweets that contains words given in terms
    """
    try:
        search_results = twitter.search(q=terms, count=10)
        return search_results
    except TwythonError as e:
        print e


def create_friendship(twitter, name):
    """
    Follows input user name
    """
    try:
        twitter.create_friendship(screen_name=name, follow=True)
        print "You now follow @"+name+" user."
    except TwythonError as e:
        print e

def destroy_friendship(twitter, name):
    """
    Unfollows input user name
    """
    try:
        twitter.destroy_friendship(screen_name=name)
        print "You unfollow @"+name+" user."
    except TwythonError as e:
        print e

def get_followers_list(twitter):
    friends = twitter.get_followers_list()
    return friends

def get_mentions_timeline(twitter):
    tweets = twitter.get_mentions_timeline()
    return tweets
