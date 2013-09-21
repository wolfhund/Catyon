from twython import Twython, TwythonError
import ConfigParser

def user_login():    
    """
    Checks for existing auth tokens.
    """
    APP_KEY = 'waWSXq22ISeUCXgFsVRk5g'
    APP_SECRET = 'DjX5dzBYXFLogRIZhw2fzqeMnR4lbV6R5X64OfXI7iM'
    config = ConfigParser.ConfigParser()        
    config.read("config.ini")
    try:
        OAUTH_TOKEN = config.get("user1", "OAUTH_TOKEN")
    except:
        OAUTH_TOKEN = ''
    try:
        OAUTH_TOKEN_SECRET = config.get("user1", "OAUTH_TOKEN_SECRET")
    except:
        OAUTH_TOKEN_SECRET = ''
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
        twitter = get_auth_tokens(config, APP_KEY, APP_SECRET)
    return twitter    

def get_auth_tokens(objConfig, app_key, app_secret):
    """
    Gets new auth tokens and writes them in 'config.ini' file
    """    
    twitter = Twython(app_key, app_secret)
    auth = twitter.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    print "To get your PIN number please go to: ", auth['auth_url']
    oauth_verifier = raw_input('Please write your PIN number: ')
    print "PIN number introduced: ", oauth_verifier
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
        # save oauth_tokens in 'config.ini' file
        cfgfile = open("config.ini",'w')
        objConfig.add_section('user1')
        objConfig.set('user1','OAUTH_TOKEN', OAUTH_TOKEN)
        objConfig.set('user1','OAUTH_TOKEN_SECRET', OAUTH_TOKEN_SECRET)
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
        exito = twitter.create_friendship(screen_name=name, follow=True)
        print "You now follow @"+name+" user."
    except TwythonError as e:
        print e
        
def destroy_friendship(twitter, name):
    """
    Unfollows input user name 
    """
    try:    
        exito = twitter.destroy_friendship(screen_name=name)
        print "You unfollow @"+name+" user."
    except TwythonError as e:
        print e

def get_followers_list(twitter):
    friends = twitter.get_followers_list()
    return friends    
    
def get_mentions_timeline(twitter):
    tweets = twitter.get_mentions_timeline()
    return tweets
