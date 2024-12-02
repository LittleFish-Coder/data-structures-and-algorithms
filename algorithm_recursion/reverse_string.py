def reverse(word):
    size = len(word)
    if size == 0:
        return 
    last_char = word[size-1]
    print(last_char)
    return reverse(word[0:size-1])

if __name__ == '__main__':
    reverse("Hello World")