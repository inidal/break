to_reverse = "Hi, my name is Nidal!"

def reverseTheString(the_str):
    tmp = [0] * len(the_str)
    sentence = ""
    for i in range(len(the_str)):
        tmp[-(i+1)] = the_str[i]

    for letter in tmp:
        sentence = sentence + letter

    print("Result: " + sentence)

reverseTheString(to_reverse)
