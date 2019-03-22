class Solution:
    # @return a string
    def longestPalindrome(self, s):
      max = 1
      t = len(s)
      start = 0
      for i in range(1, t):
        a = s[i-max-1:i+1]
        b = s[i-max:i+1]
        #adding an element to ecah end      tat -> atata
        if i-max > 0 and a == a[::-1]:
          start = i-max-1
          max += 2
        #adding an element ot end  pppp->ppppp
        elif  b == b[::-1]:
          start = i-max
          max+=1
      return s[start:start+max]