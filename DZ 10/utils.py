import json

from candidate import Candidate

# Загружаем кандидатов
def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Получение данных о кандидатах
def get_all(data):
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

# Получаем кандидата по номеру
def get_by_pk(pk, data):
    for item in data:
        if item == pk:
            return pk

# Получаем кандидата по скиллу
def get_by_skill(skill_name, data):
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
        return arr
