class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append([i,tickets[i]])
        time=0
        while q:
            person=q.popleft()
            person[1]-=1
            time+=1
            if person[1]>0:
                q.append(person)
            elif person[0]==k:
                return time
        return time
        