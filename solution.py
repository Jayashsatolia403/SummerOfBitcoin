class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents, ans):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parent = parents
        self.track = ans
    
    def parse(self):
        canAdded = True
        if self.parent and self.parent not in self.track:
            canAdded = False
        
        if canAdded:
            self.track.append(self.txid)
            return str(self.txid) + "\n"
        
        



def parse_mempool_csv():
    """Parse the CSV file and return a list of MempoolTransactions."""
    with open('mempool.csv') as f:
        f.readline()
        ans = []
        return([MempoolTransaction(*line.strip().split(','), ans).parse() for line in f.readlines() if MempoolTransaction(*line.strip().split(','), ans).parse()])

z = open('ans.txt', "a")
x = parse_mempool_csv()
print(x)
z.writelines(x)
z.close()