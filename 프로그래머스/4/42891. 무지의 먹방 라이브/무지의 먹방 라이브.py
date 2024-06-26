import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times)<=k:
        return -1
    
    q=[]
    for i in range(len(food_times)):
        #음식을 먹는데 걸리는 시간, 음식 번호
        heapq.heappush(q,(food_times[i],i+1))
        
        
    sum_value=0
    length=len(food_times)
    previous=0
    while sum_value+(q[0][0]-previous)*length<=k:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1
        previous=now
        
    result=sorted(q,key= lambda x:x[1])
    return result[(k-sum_value)%length][1]