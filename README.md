## LeetCodeNotes
## My Own LeetCode Notes (Most are written in Python and C) :)
#### This project includes all my thoughts while I am solving problems. I would not say my solution is the best and beat 99% of the submission, I aim to solve the problems in reasonable time.
#### Special thanks to [Jiaran99](https://github.com/Jiaran98) for formatting README
#### Find Problems [here](https://leetcode.com/problemset/all/)
### 1. Two Sum:
`Easy`
#### Given a list of nums and a target, return a list where contains two digit whose sum is equal to target.
```
e.g.[1, 2, 3, 4] target = 7.
```
1. Create a [dictionay](https://docs.python.org/3/tutorial/datastructures.html)[Dictionary is very useful data structure you may use it from time to time].
2.   For each digit y in list, cast it as value in dictionary, and caculate number x as key to that key so that x + y = target e.g. {"6": 1, "5": 2, "4": 3, "3": 4} [{"key": vale}]. 
3. Use for loop to generate a dictionary, once you found digit y exists in dictionary as a key, you found the demand pair. You can simply return [dict[x], i]

### 2. Add Two Numbers:
`Medium`
#### Given two linked list, each linked list representing two non-negative integers but in reverse order.
```
[2->3->4 stands for 432] you need add thoses two integers and represent result in linked-list in reverse order. 
[(2 -> 4 -> 3) + (5 -> 6 -> 4) result: 7 -> 0 -> 8. 342+564=807] 
```
#### Personal speaking, I would use C to implement this. But using Python to implement linked list worth trying. Because you probably never use python to create class or struct in school.

The implementation is quite straight forward. 
1. First, parallelly go through each node in LL1 and LL2
2. Add two node up, if the sum is greater than 9, there is carry. To track carry digit, use module to get the last digit. (21/10 = 1, carry is 2). Then put the last digit into result Linked-list.

### 3. Longest Substring Without Repeating Characters:
`Medium`
##### I just realize I should include my bad approach so that you can avoid it.
#### Given a string, you need to find the length of longest substring which does not contain repeated characters: 
```
e.g.["pwwkew" return 3("kew")]
Again, I use dictionary to implement this. 
```
1. First of all, you need a mark M to track the first character without any repeating character before it. You need to dictionary to check if there is a character exists in previous substring. 
e.g.["abba", {"a": 0} -> {"a": 0, "b": 1} -> in the third iteration, program would add the index of the second "b" to dictionary, but dictionary already has "b" in it. So you need to store this b's index and assign it to M] 
2. The length of current valid substring can be written as [i-M +1 why plus one? I think you can figure out by yourself].
3. Since this problem requires the length not the substring, you can simply compare the current length to maxLength for each iteration.

### 4. Median of Two Sorted Arrays:
`Hard`
#### Given two sorted list a and b, and find the median of a and b.
#### You should have knowledge of [median](https://www.mathsisfun.com/median.html). 
#### Let's deduct this problem into intuitive mathmatical problem, since lists are sorted:

```
If the length of list is odd, the median is located at middle of the list
If the length of list is even, the median should be the average of middle two integer.
Ultimately, we can rephrase this problem :
Find the kth(index of middle position) minimum number if length is odd
Find the kth and kth - 1 if length is even.
[5, 9, 11, 16, 22] kth = 5//2 = 2
 0  1   2   3   4
        |
So 11 is the median.
```
#### We need to use devided and conquer. I would say this is the hardest part.

```
A:[A1 A2 A3 ... An]; len(A) = m
B:[B1 B2 B3 ... Bn]; len(B) = n
We nee to find kth[(m+n)//2] or (kth and kth - 1) minium integer(s) in C [A and B is cut from C[sort(A+B)]. It may sound abstract.].
Let's cut A and B into two lists:
[A1 A2 A3 ... A(m//2-1)] | [A(m//2) A(m//2+1) A(m//2+2) ... Am]
          AA1                               AA2
[B1 B2 B3 ... B(n//2-1)] | [B(n//2) B(n//2+1) B(n//2+2) ... Bn]
          BB1                               BB2
```
To solve this question, I implement a function to find the kth minimun integer in two array. 
1. For A, the median is either A(m//2-1) or (A(m//2-1) + A(m//2))/2. Same as B.
2. If m//2 + n//2 is less than k which means the kth integer is not in either [A1 A2 A3 ... A(m//2-1)] or [B1 B2 B3 ... B(n//2-1)], and we need to wipe out some small integer, do not forget to decrease value of k. 
3. If median(A) greater than median(B), we can get rid of BB1. Since all integer in BB1 is less than C(kth) [the kth integer]. k will be k - n//2 - 1. Vice versa
4. If m//2 + n//2 is greater than k, you need to wipe some large integer.
5. If median(A) greater than median(B), you need to get rid of AA2.
6. Recursively do step 1-5
