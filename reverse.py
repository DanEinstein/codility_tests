# This is the program that i will be using to learn how i can a reverse a string in python without using (::-1)
#identify the problem-> The string can be split to individual characters using the list() function in python
#use an array method for loop to loop across
#Assign the last element n in the array of strings to be the first element in the reversed string
#from the reversed string assign it back to the string method. In jS we use the stringify method
# I can try to implement this using the python functions
# forward_string = ''
# forward_array =list(forward_string)
# for i in range(0, len(forward_array)-1):

def reverseStringRec(array,l,r):
    if l>r:
        return
    array[l],array[r] = array[r],array[l]
    #swapping the first element of the arrray to be the last one and the last on to be the first element
    reverseStringRec(array,l+1,r-1) #decreasing the right pointer and increasing the left pointer to continue swapping the next elements until they meet in the middle

def reverseString(string):
    array = list(string) #This is the list function that converts the string into an array of characters so that we can manipulate it using the recursive function defined above
    #converting the string into individual characters
    reverseStringRec(array,0,len(array)-1)
    #Converting the individual characters back to a string is the next step
    return ''.join(array)
string = "Danson"
print(reverseString(string))

