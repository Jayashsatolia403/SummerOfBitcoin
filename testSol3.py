import pandas

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parent = str(parents)
    
    def parse(self, fees, weights, ans):
        canAdded = True
        if self.parent and self.parent not in ans:
            canAdded = False
        
        if canAdded:
            weights.append(self.weight)
            if sum(weights) < 4000000:
                fees.append(self.fee)
                ans.append(self.txid)
                return str(self.txid) + "\n"
            else:
                weights.pop()
                return "EXIT"
        
        return
            



def parse_mempool_csv():
    with open('mempool.csv') as f:
        f.readline()
        weights = []
        fees = []
        ans = []
        x = []

        for line in f.readlines():
            p = MempoolTransaction(*line.strip().split(',')).parse(fees, weights, ans)
            if p == "EXIT":
                break
            elif p:
                x.append(p)
    
    print("3 >> ", sum(fees), " >> ", sum(weights))

    
    '''z = open("ansx.txt", "a")
    z.writelines(x)
    z.close()'''

parse_mempool_csv()