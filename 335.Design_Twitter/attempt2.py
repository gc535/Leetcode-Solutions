import bisect

class Twitter(object):

    def __init__(self):
        self.posts = {} # map of list
        self.feeds = {} # map of list
        self.followerList = {} # map of set
        self.logicPostId = 0
        

    def postTweet(self, userId, tweetId):
        ts = self.logicPostId

        if userId not in self.posts:
            self.posts[userId] = list()
        self.posts[userId].insert(0, (ts, tweetId))

        # get all the followers
        followers = [userId]
        if userId in self.followerList:
            followers += self.followerList[userId]

        # update all followers feed list
        for follower in followers:
            if follower not in self.feeds:
                self.feeds[follower] = list()
            self.feeds[follower].insert(0, (-ts, userId, tweetId))
        
        self.logicPostId += 1

    def getNewsFeed(self, userId):
        if userId not in self.feeds:
            self.feeds[userId] = list()

        feeds = list()
        for ts, user, tweet in self.feeds[userId]:
            feeds.append(tweet)
            if len(feeds) == 10: return feeds
        return feeds
        

    def follow(self, followerId, followeeId):
        if followeeId not in self.followerList:
            self.followerList[followeeId] = set()

        if followerId not in self.followerList[followeeId]:
            self.followerList[followeeId].add(followerId)

            # merge new followee's all post with self's feeds
            if followeeId in self.posts:
                if followerId not in self.feeds:
                    self.feeds[followerId] = list()
                for ts, tweet in self.posts[followeeId]:
                    idx = bisect_left(self.feeds[followerId], (-ts, followeeId, tweet))
                    self.feeds[followerId].insert(idx, (-ts, followeeId, tweet))
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followerList and followerId in self.followerList[followeeId]:
            self.followerList[followeeId].remove(followerId)
        
            # clean up unfollowed user's feed in self's list
            if followerId in self.feeds:
                idx = 0
                while idx < len(self.feeds[followerId]):
                    if self.feeds[followerId][idx][1] == followeeId:
                        self.feeds[followerId].pop(idx)
                    else: idx += 1


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)