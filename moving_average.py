class MovingAverage:

    def __init__(self, windowSize):
        self.windowSize = windowSize
        self.num_items = 0
        self.nums = []


    def next(self, val):

        self.nums.append(val)
        self.num_items = len(self.nums)

        if(len(self.nums) > self.windowSize):
            self.pop(0)  # this can be improved complexity wise
            self.num_items = len(self.nums)


        average = sum(self.nums) / self.num_items

        return average
