
'''
the following section reads from a text file that contains a graph of cities
and cost between cities
'''


class FileRead:
    # this class takes a weighted txt file and initilizes it in a dictionary
    def __init__(self):
        self.wd = dict()

    def readFile(self, path):
        # this method read a weighted file and initializes it to a dictionary
        with open(path, 'r') as f:
            ltemp = 0
            for i in f:
                ltemp = i.split()
                if len(ltemp) == 1:
                    self.wd[ltemp[0]] = None
                else:
                    self.wd[ltemp[0]] = dict()

                    i = 1
                    while True:
                        if i + 2 >= len(ltemp):
                            break
                        self.wd[ltemp[0]][ltemp[i]] = list()
                        self.wd[ltemp[0]][ltemp[i]].append(float(ltemp[i + 1]))
                        self.wd[ltemp[0]][ltemp[i]].append(float(ltemp[i + 2]))
                        i = i + 3
        return self.wd

    def showdict(self):
        print("hello")
        print(self.wd)
        for i in self.wd:
            print(i, ':', self.wd[i])
        return None
