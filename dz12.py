st = "Замените в этой строке все появления буквы 'о' на букву '0', кроме первого и последнего вхождения"

first = st.find("о")
last = st.rfind("о")


if first == -1 or last == -1 or first == last:
    result = st
else:
    temp = st.replace("о", "0")
    result = temp[:first] + "о" + temp[first+1:last] + "о" + temp[last+1:]

print(result)