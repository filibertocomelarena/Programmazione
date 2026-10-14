# Write a Python program find a list of integers
# with exactly two occurrences of nineteen
# and at least three occurrences of five. Go to the editor
#Input:
#[19, 19, 15, 5, 3, 5, 5, 2]
#Output:
#True
#Input:
#[19, 15, 15, 5, 3, 3, 5, 2]
#Output:
#False
#Input:
#[19, 19, 5, 5, 5, 5, 5]
#Output:
#True

def find_numbers(lista):
    count5=0
    count19= 0
    for i in lista:
        if i == 5:
            count5= count5+1
        elif i == 19:
            count19= count19+1
    if count19 == 2 and count5 ==3:
        return True
    return False

#or....

def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3



nums = [19,19,15,5,3,5,2]

print(find_numbers(nums))
