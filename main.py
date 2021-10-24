import requests
import pytest

def main():
    url = 'https://api.duckduckgo.com'
    reponse = requests.get(url + '/?q=presidents of the united states,&format=json')
    data = reponse.json()
    print(len(data['RelatedTopics']))
    for line in data['RelatedTopics']:
        print(line['Text'])
    # response = requests.get(url,auth=('djw-test','password1'))
    # # for auth key github
    # response = requests.get(url,headers={'Authorization' : 'Bearer key'})
    #
    # # returns dictionary structure
    # my_json = response.json()
    # for key in my_json.keys():
    #     print(key)

def test_presidents_test():


    assert True


if __name__ == '__main__':
    main()