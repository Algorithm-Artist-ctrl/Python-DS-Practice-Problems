def count_word_frequency(sentence):
    lst=sentence
    fre={}
    for i in lst:
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1
    print(fre)
sent=input("Enter Sentaces :\n")
count_word_frequency(sent)
