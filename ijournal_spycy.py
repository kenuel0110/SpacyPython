import spacy
import json
#python -m spacy download ru_core_news_lg
nlp = spacy.load("ru_core_news_lg")

text ='''
221Р111
Понедельник
1 Основы архитектуры и строительных конструкций Л Маношкина Г.В. 117
2 Технологические процессы в строительстве с 16.02 Л Храпова Т.Е. 115
Вторник
1 1 группа Технологические процессы в строительстве Л 2 группа Технологические процессы в строительстве ПЗ Храпова Т.Е. 115.
'''

doc = nlp(text)

data = {}
current_day = ""

for token in doc:
    if token.text in ["Понедельник", "Вторник"]:
        current_day = token.text
        data[current_day] = []
    elif token.text.isdigit():
        if current_day:
            additional_info = ""
            if doc[token.i].text in ["с", "по"]:
                additional_info = f"{doc[token.i].text} {doc[token.i].text} {doc[token.i].text}"
            group = ""
            if doc[token.i].text == "группа":
                group = doc[token.i + 2].text
            data[current_day].append({
                "номер": token.text,
                "предмет": doc[token.i].text,
                "преподаватель": doc[token.i].text,
                "аудитория": doc[token.i].text,
                "дополнительная информация": additional_info,
                "группа": group
            })

json_data = json.dumps(data, ensure_ascii=False, indent=2)
print(json_data)