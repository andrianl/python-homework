text1=input('\n')
text2=input('\n')

text1=text1.split()
text1=''.join(text1)


text2=text2.split()
text2=''.join(text2)

l=len(text1)
for i in range(l//2):
    if text1[i] != text1[-1-i]:
        print("Перший текст не є паліндромом")
        quit()

print("Перший текст є паліндромом")

l2=len(text1)
for i in range(l//2):
    if text2[i] != text2[-1-i]:
        print("Другий текст не є паліндромом")
        quit()


print("Другий текст є паліндромом")