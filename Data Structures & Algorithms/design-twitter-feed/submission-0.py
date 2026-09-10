class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-time, tweetId, user, index))

        feed = []

        #get 10 newest tweets
        while heap and len(feed) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            #add the next older tweet from the same user
            if index > 0:
                next_index = index - 1
                time, next_tweetId = self.tweets[user][next_index]

                heapq.heappush(heap, (-time, next_tweetId, user, next_index ))
        
        return feed


      
       
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
