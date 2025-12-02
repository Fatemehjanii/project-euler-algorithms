""" A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 52 =5 ×5 =25; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,25, and the sum of the odd squares is 1 +9 +25 =35.

Among the first 129 thousand square numbers, what is the sum of all the odd squares?"""
total = 0
for num in range(1,129001):
    if num % 2 == 1 :
        num **= 2
        total += num
print(total)