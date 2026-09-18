class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st = []
        for i in operations:
            if i != 'C' and i != 'D' and i != '+':
                st.append(int(i))
            elif i == 'D':
                st.append(st[-1] * 2)
            elif i == 'C':
                st.pop()
            elif i == '+':
                st.append(st[-1] + st[-2])
        return sum(st)