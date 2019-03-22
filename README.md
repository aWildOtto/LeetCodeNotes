## LeetCodeNotes
## My Own LeetCode Notes(Most are written in Python and C) :)
#### I will write down all my thoughts while I am solving the problems. I would not say my solution is the best and beat 99% of the submission, I aim to solve the problems in reasonable time.
#### Find Problems [here](https://leetcode.com/problemset/all/)
### 1. Two Sum:
##### Given a list of nums and a taget, return a list where contains two digit whose sum is equal to target.
##### e.g.[1, 2, 3, 4] target = 7.
##### Create a [dictionay](https://docs.python.org/3/tutorial/datastructures.html)[Dictionary is very useful data structure you may use it from time to time]. For each digit y in list, cast it as value in dictionary, and caculate number x as key to that key so that x + y = target e.g. {"6": 1, "5": 2, "4": 3, "3": 4} [{"key": vale}]. Use for loop to generate a dictionary, once you find digit y exist in dictionary as a key which means you found the demand pair. You can simply return [dict[x], i]
### 2. Add Two Numbers:
##### Given two linked list, each linked list representing two non-negative integers but in reverse order.[2->3->4 stands for 432] you need add thoes two integers and reprent result in linked list in reverse order. [(2 -> 4 -> 3) + (5 -> 6 -> 4) result: 7 -> 0 -> 8. 342+564=807] 
##### Personal speaking, I would use C to implement this. But using Python to implement linked list worth trying. Because you probably never use python to create class or struct in school.
##### The implementation is quite straight forward. You parallelly go through each node in LL1 and LL2, and add two node up, if the sum is greater than 9 which means there is carry, you need to track carry digit. Use module to get the last digit(21/10 = 1, carry is 2). Then put the last digit into result Linked list.
### 3. Longest Substring Without Repeating Characters
