"""
Idea - The Whole logic behind this code is just take difference of fee and weight and then
       Arrange them in Decending Order. we can use hashtables to map values of fee, weight 
       & transactionIDs because Because we need to keep track of total fee and total weight
       and also transactionIDs.

Other Ideas - I have attached Files of code which i tried before reaching to this solution
              in OtherSolution Folder on github on link - .
              But This is Perfect Solution in best of my idea.
       
"""



def parse_mempool_csv():

    diff = {} # HashTable to keep track of difference of Fee and Weight of txn
    result = [] # Result List to keep track of trasactionID's after Maximizing Fee
    totalFee = 0
    totalWeight = 0

    mempool = open("mempool.csv") # Open input file
    mempool.readline() # Skip first line

    for line in mempool.readlines(): # Iterate through whole CSV file line by line

        txnDetail = line.strip().split(',') # Extracting txn Details
        txnID = txnDetail[0]
        txnFee = txnDetail[1]
        txnWeight = txnDetail[2]
        parentTxn = txnDetail[3:]

        for parentTxn in parentTxn:

            if parentTxn == "" or parentTxn in result: # check if all parent txns have been scene before

                if int(txnFee)-int(txnWeight) in diff: # to handle duplicates in Dict
                    diff[int(txnFee)-int(txnWeight)].append([int(txnFee), int(txnWeight), txnID])

                else:
                    diff[int(txnFee)-int(txnWeight)] = [[int(txnFee), int(txnWeight), txnID]]
    
    sortedFees = sorted(diff.keys()) # Sort Fees 
    sortedFees.reverse() # Reverse to get max fee first

    for i in sortedFees: # Iterate through Max Fees
        for j in diff[i]:

            totalWeight += j[1]

            if totalWeight > 4000000: # Check if totalWeight is Exceeding 4000000 as per given Max Weight of Block

                z = open("block.txt", "a") # Opening a writable file of named >>> "block.txt"
                z.writelines(result) # Writing line by line output of list
                z.close # Closing file

                totalWeight -= j[1]

                return totalFee, totalWeight
            
            totalFee += j[0]
            result.append(j[2]+"\n")

    # If totalWeight is not exceding max limit then we can just return solution
    
    z = open("block.txt", "a") # Opening a writable file of named >>> "block.txt"
    z.writelines(result) # Writing line by line output of list
    z.close # Closing file

    return totalFee, totalWeight



parse_mempool_csv() # Making Function Call