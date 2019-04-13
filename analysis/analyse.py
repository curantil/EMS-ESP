
import numpy as np

def getKey(datagram):
    bytes = datagram.split(" ")
    return int(bytes[2],16), int(bytes[3],16), int(bytes[4],16)
    #return int(bytes[1],16), int(bytes[2],16), int(bytes[3],16)

def parse(filename):
    srcKeylist = {}
    tgtKeylist = {}
    typeKeylist = {}
    support = np.array([])
    support.resize((1,1,1), refcheck=False)

    with open(filename,"r") as f:
        for line in f:
            if line != "\n":
                src, tgt, type = getKey(line)
                if not src in srcKeylist.keys():
                    index = len(srcKeylist)
                    srcKeylist[src] = index
                    support.resize((index+1, support.shape[1], support.shape[2]), refcheck=False)
                if not tgt in tgtKeylist.keys():
                    index = len(tgtKeylist)
                    tgtKeylist[tgt] = index
                    support.resize((support.shape[0], index+1, support.shape[2]), refcheck=False)
                if not type in typeKeylist.keys():
                    index = len(typeKeylist)
                    typeKeylist[type] = index
                    support.resize((support.shape[0], support.shape[1], index+1), refcheck=False)
                support[srcKeylist[src], tgtKeylist[tgt], typeKeylist[type]] += 1
        print (support)
        print (support.shape)

if __name__== "__main__":
    parse("long-raw.log")