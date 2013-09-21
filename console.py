# -*- coding: utf-8 -*-

import cmd
import os
from twython_functions import *
from myFunctions import MyFunctions
from colors import Colors

class Console(cmd.Cmd):
    """
    Parse results from twython_functions in a cmd.Module instance
    """
    prompt = "Catyon> "
    doc_header = "Catyon Helper. Type 'help' and command listed bellow to describe its functions"
    logo = Colors.YELLOW + """
      _____      _                     
     / ____|    | |                    
    | |     __ _| |_ _   _  ___  _ __  
    | |    / _` | __| | | |/ _ \| '_ \ 
    | |___| (_| | |_| |_| | (_) | | | |
     \_____\__,_|\__|\__, |\___/|_| |_|
                      __/ |            
                     |___/             
    """ + Colors.ENDC
    
    def __init__ (self):
        """
        Console constructor
        """
        self.objTwitter = user_login()
        cmd.Cmd.__init__(self)
            
    def do_home (self, name):
        """
        Shows user timeline
        """
        news = get_user_timeline(self.objTwitter)
        for tweet in news:
            print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
            print tweet['text'].encode('utf-8'), '\n'
        
    def do_tweet (self, text):
        """
        Update your status
        """
        mystatus = text
        update_status(self.objTwitter, mystatus)
        
    def do_search (self, terms):
        """
        Search tweets of given terms
        """
        results = search(self.objTwitter, terms)
        for tweet in results['statuses']:
            print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
            print tweet['text'].encode('utf-8'), '\n'
    
    def do_follow(self, name):
        """
        Follows an user name given
        """
        create_friendship(self.objTwitter, name)
    
    def do_unfollow(self, name):
        """
        Unfollows an user name given
        """
        destroy_friendship(self.objTwitter, name)
    
    def do_followers(self, name):
        """
        List user followers 
        """
        results = get_followers_list(self.objTwitter)
        for tweet in results['users']:
            print tweet['screen_name'].encode('utf-8')  
    
    def do_mentions(self, name):
        """
        List mentions of current user
        """
        results = get_mentions_timeline(self.objTwitter)
        for tweet in results:
            print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['user']['created_at'])
            print tweet['text'].encode('utf-8'), '\n'
        
    def do_quit (self, s):
        print "Bye, bye…"
        return True

    def help_quit (self):
        print "Quits the console"

    do_EOF = do_quit
    help_EOF = help_quit


