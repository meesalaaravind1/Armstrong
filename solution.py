# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        li=list(str(num))
        sum=0
        for i in li:
                sum+=int(i)**3
        if sum==num:
                return True
        return False
