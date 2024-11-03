def count_letters(text):
    letters_str = ''
    for letter in text.lower():
        if letter.isalpha() and letter not in letters_str:
            letters_str += letter
    data = {}
    for letter in letters_str:
        data[letter] = text.lower().count(letter)
    return data


def calculate_frequency(letters_dict):
    data_freq = {}
    letters_in_text = 0
    for letter in main_str:
        if letter.isalpha():
            letters_in_text += 1
    for item in letters_dict:
        data_freq[item] = f"{round(letters_dict[item] / letters_in_text, 2):.2f}"
    return data_freq


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

result_dict = calculate_frequency(count_letters(main_str))

for letter, freq in result_dict.items():
    print(letter + ": " + str(freq))
