import requests
import pytest

presList = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump", "Biden"]
url = 'https://api.duckduckgo.com'
reponse = requests.get(url + '/?q=presidents of the united states,&format=json')
data = reponse.json()

#print(len(data['RelatedTopics']))
#print(data['RelatedTopics']['Text'])
# for line in data['RelatedTopics']:
#     print(line['Text'])
@pytest.mark.parametrize("pres", presList)
def test_presidents_list(pres):
    found = False
    for line in data['RelatedTopics']:
        if pres in line['Text']:
            found = True
    if found:
        assert True
    else:
        assert False