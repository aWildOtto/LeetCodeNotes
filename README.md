## LeetCodeNotes
## My Own LeetCode Notes(Most are written in Python and C) :)
#### I will write down all my thoughts while I am solving the problems. I would not say my solution is the best and beat 99% of the submission, I aim to solve the problems in reasonable time.
#### Find Problems [here](https://leetcode.com/problemset/all/)
### 1. Two Sum:
##### Give a list of nums and a taget, return a list where contains two digit whose sum is equal to target.
##### e.g.[1, 2, 3, 4] target = 7.
##### Create a [dictionay](https://docs.python.org/3/tutorial/datastructures.html)[Dictionary is very useful data structure you may use it from time to time]. For each digit y in list, cast it as value in dictionary, and caculate number x as key to that key so that x + y = target e.g. {"6": 1, "5": 2, "4": 3, "3": 4} [{"key": vale}]. Use for loop to generate a dictionary, once you find digit y exist in dictionary as a key which means you found the demand pair. You can simply return [dict[x], i]

