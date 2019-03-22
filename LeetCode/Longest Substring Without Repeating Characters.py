class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # tempString = ''
        # totalNonDuplicatedList = []
        # totalLength = len(s)
        # i = 0
        # p = 1
        # sum = 0
        # while i < totalLength:
        #     for cursor in s:
        #         if cursor not in tempString:
        #             tempString += cursor
        #             totalNonDuplicatedList.append(len(tempString))
        #         else:
        #             p = s.index(cursor)+1
        #             s = s[p:]
        #             tempString = ''
        #             sum += p
        #             break
        #     i += 1
        #     if sum == totalLength:
        #         break
        # return max(totalNonDuplicatedList) if totalNonDuplicatedList else 0
        '''
        time limit exceeded
        '''
        
        maxlength, pM =  0, 0
        d = {}
        for i in range(len(s)):
            x = s[i]
            if x in d and pM <= d[x]:
                pM = d[x] + 1
            else:
                c = i-pM+1
                if maxlength > c:
                    pass
                else:
                    maxlength = c
            d[x] = i
            
        return maxlength