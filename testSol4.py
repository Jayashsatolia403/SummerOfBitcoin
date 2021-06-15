def parse_mempool_csv():
    diff = {}
    result = []
    totalFee = 0
    totalWeight = 0
    mempool = open("mempool.csv")
    mempool.readline()

    for line in mempool.readlines():
        x = line.strip().split(',')
        if x[3] == "" or x[3] in result:
            if int(x[1])-int(x[2]) in diff:
                diff[int(x[1])-int(x[2])].append([int(x[1]), int(x[2]), x[0]])
            else:
                diff[int(x[1])-int(x[2])] = [[int(x[1]), int(x[2]), x[0]]]
    
    sortedFees  = sorted(diff.keys())
    sortedFees.reverse()

    for i in sortedFees:
        for j in diff[i]:
            totalWeight += j[1]
            if totalWeight > 4000000:
                break
            totalFee += j[0]
            result.append(j[2]+"\n")

        if totalWeight > 4000000:
            totalWeight -= j[1]
            break
            
    
    print("4 >> ", totalFee, " >> ", totalWeight, " >>> ", len(result))

    
    z = open("ansz.txt", "a")
    z.writelines(result)
    z.close

parse_mempool_csv()