#Question 1
""" If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3,5,6,9 and the sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

n=1000
multiple_of_3=(n-1)//3
multiple_of_5=(n-1)//5
multiple_of_15=(n-1)//15 # Just so we donot get the common multiple twice
sum_of_3=0
sum_of_5=0
sum_of_15=0
# print(multiple_of_3)
for i in range (1,multiple_of_3+1):
    sum_of_3+=i
sum_of_3=3*sum_of_3
# print(sum_of_3)
for i in range(1,multiple_of_5+1):
    # print(i)
    sum_of_5+=i
sum_of_5=5*sum_of_5
# print(sum_of_5)

for i in range(1,multiple_of_15+1):
    sum_of_15+=i
sum_of_15=15*sum_of_15

#total sum
total=sum_of_3+sum_of_5-sum_of_15
print(total)

