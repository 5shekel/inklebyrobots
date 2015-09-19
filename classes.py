'''
Created on 19 Sep 2015

@author: @alexparsons
'''

import math
import time
import twitter

class RobotMaster(object):
    
    bots = []
    
    def __init__(self):
        
        self.bots = RobotMaster.bots
        
        self.seconds = time.time()
        self.minutes = math.floor(self.seconds/60)
        self.hours = self.minutes/60
        self.retweet_creds = None
        
    def register(self,bot):
        self.bots.append(bot)
        
    def register_retweet(self,cres): # pass a dictionary of credentials to have one account retweet all bots
        self.retweet_creds = cres
        
        
    def retweet(self,tweets):
        
        if self.retweet_creds and tweets:
            api = twitter.api(**self.retweet_creds)
            for t in tweets:
                api.PostRetweet(t.id)
        
        
    def run(self):
        
        robot_count = 0
        tweets = []
        print "checking for pending robots"
        for b in self.bots:
            if b.check(self):
                robot_count += 1
                result = b.tweet()
                if result:
                    if isinstance(result,list):
                        tweets.extend(result)
                    if isinstance(result,dict):
                        tweets.append(result)

        self.retweet(tweets)
        print "{0} robots run".format(robot_count)
        


class Robot(object):
    
    def __init__(self,name,tweet_function,*args,**kwargs):
        
        self.name = name
        self.minutes = 0
        self.hours = 0 
        self.force_run = False
        self._tweet = tweet_function
        self.__dict__.update(**kwargs)
        
    def check(self,master):
        """
        Sees if correct number of minutes or hours have passed since the epoch
        """
        
        if self.force_run:
            print "forcing"
            return True
        
        lengths = ['minutes','hours']
        for l in lengths:
            if getattr(self,l):
                if getattr(master,l) % getattr(self,l) == 0:
                    return True
        
        return False
        
    def tweet(self):
        print "tweeting {0}".format(self.name)
        return self._tweet()
        print "done"