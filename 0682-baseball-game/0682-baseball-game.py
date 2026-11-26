class Solution(object):
    def calPoints(self, operations):
        record =[]
        for ch in operations:
            if ch=="+":
                record.append(record[-1]+record[-2])
            elif ch=="D":
                record.append(record[-1]*2)
            elif ch=="C":
                record.pop()
            else:
                record.append(int(ch))
        return sum(record)