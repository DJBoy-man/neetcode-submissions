class MedianFinder:

    def __init__(self):
        self.left = [] #maxHeap
        self.right = [] #minHeap
        

    def addNum(self, num: int) -> None:
        #put nummber into left
        heapq.heappush(self.left, -num)

        #Move largest from left to right
        max_left = -heapq.heappop(self.left)
        heapq.heappush(self.right, max_left)

        #keep left same size or 1 bigger
        if len(self.right) > len(self.left):
            min_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -min_right)
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
        
        