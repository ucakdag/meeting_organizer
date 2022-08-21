
def findmax(t,z):
    t=t.lower()
    z=z.lower()
    found=[]
    for i in range(len(z),0,-1):
        for j in range(0,len(z),1):
            if z[j:i] in t:
                if len(z[j:i])>1:
                    found.append(z[j:i])
    longest = sorted(found, key=lambda x: len(x), reverse=True)[0] 
    print(longest)
    count=0
    for i in found:
        if i==longest:
            count+=1
    print(count)
    result=count*len(longest)
    print(result)
    return -1
if __name__ == '__main__':
    findmax("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
