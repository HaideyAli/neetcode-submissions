class TimeMap:

    def __init__(self):
        self.store = {} # key=string, value: list of pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        listOfValues = self.store.get(key, [])
        
        l, r = 0, len(listOfValues) -1
        while l <= r:
            m = (l+r) // 2
            stamp = listOfValues[m][1]

            if stamp <= timestamp:
                l = m + 1
                res = listOfValues[m][0]
            else:
                r = m - 1                

        return res