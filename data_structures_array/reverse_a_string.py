def reverse(string):
    backwards = []
    for i in range(len(string)-1, -1, -1):
        backwards.append(string[i])    
    return ''.join(backwards)

x = reverse("I am Fish")
print(x)