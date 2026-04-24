# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
with open("romeo_and_juliet.txt","r") as f:
    content = f.read()

count = {}
list = content.split()
for word in list:
    if word in count:
        count[word] += 1
    
    else:
        count[word] = 1

print(count["Juliet"])  
####
#### YOUR CODE HERE 
####

# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
####
