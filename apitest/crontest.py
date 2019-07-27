__author__ = 'chenzhiyuan'

def getSum(n):
    rangelist = []
    sum = 0
    for i in range(1,n):
        sum += i
        rangelist.append(str(i))
    SumExp = '+'.join(rangelist)
    print("%s = %s" %(SumExp,sum))

if __name__=='__main__':
    getSum(4)

