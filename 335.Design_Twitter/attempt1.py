class Twitter(object):

    def __init__(self):
        self.posts = list()
        self.followList = {} # map of set
        

    def postTweet(self, userId, tweetId):
        self.posts.insert(0, (userId, tweetId))
        

    def getNewsFeed(self, userId):
        feeds = list()

        for user, post in self.posts:
            if user == userId or \
               userId in self.followList and user in self.followList[userId]:
                feeds.append(post)
                if len(feeds) == 10: break
        return feeds
        

    def follow(self, followerId, followeeId):
        if followerId not in self.followList:
            self.followList[followerId] = set()
        self.followList[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followerId in self.followList and followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)