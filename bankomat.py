from num2words import num2words

def number_to_words(num):
    if num < 1 and num > 100000:
        return "Сумма должна быть равна от 1 до 100 000"
    words = num2words(num, lang = 'ru')
    ending = num%10
    if ending == 1 and num% 100 != 11:
        end = "рубль"
    elif 1 < ending < 5 and (num%100 < 10 or num %100 >21):
        end = "рубля"
    else:
        end = "рублей"
