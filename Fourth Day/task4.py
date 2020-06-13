text=input("Введіть перший текст:")
text2=input("Введіть другий текст:")
half1 = text2[:int((len(text2)+1)/2)]
half2 = text2[int((len(text2)+1)/2):]
print("Результат:", half1+text+half2)