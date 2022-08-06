import json

from candidate import Candidate

# Загружаем кандидатов
def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Получаем данные кандидата
def get_all(data):
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

# Поиск кандидата по pk
def get_by_pk(pk, data):
    for item in data:
        if item == pk:
            return pk

# Поиск кандидата по навыкам
def get_by_skill(skill_name, data):
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
        return arr
