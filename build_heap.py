# python3

def build_heap(data):
    
    swaps=[]
    
    for i in range (len(data)-1,0,-1):
        
        parent=(i-1)//2
        
        
        while i>0 and data[parent]>data[i]:
            
            data[parent],data[i]=data[i],data[parent]
            swaps.append((parent,i))
            i=parent
            parent=(i-1)//2
    return swaps

def main():
    
    izvele=input()
    if "F" in menu:
        
        Fpath=str(input())
        with open("./tests/"+ Fpath,'r') as F:
            
            x=int(F.readline())
            data=list(map(int, F.readline().split()))
            
    elif "I" in menu:
      
        x=int(input())
        data=list(map(int, input() .split()))
   
    assert len (data) ==x

  
    swaps=build_heap(data)


    for i in range(len(data)):
        
        if 2i+1<len (data) and data[2i+1]<data [i]:
            
            return False
        
        if 2i+2<len(data) and data[2i+2]<data [i]:
            
            return False
        
    return True

    print(len(swaps))
    for x,y in swaps:
        
        print (x,y)

if name== "main":
    main()
