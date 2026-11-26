class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        n=len(deck)
        q=deque(range(n))
        result=[0]*n
        for card in deck:
            index=q.popleft()
            result[index]=card
            if q:
                q.append(q.popleft())
        return result
        