class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        max_profit=float("-inf")
        min_price=float("inf")
        for price in prices:
            if price<min_price:
                min_price=price
            amount=price-min_price
            if amount>max_profit:
                max_profit=amount
        return max_profit
            