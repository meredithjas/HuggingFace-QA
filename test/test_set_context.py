import requests
import json

def get_qa(topic, data):
    q = []
    a = []
    for d in data['data']:
        if d['title']==topic:
            for paragraph in d['paragraphs']:
                for qa in paragraph['qas']:
                    if not qa['is_impossible']:
                        q.append(qa['question'])
                        a.append(qa['answers'][0]['text'])
            return q,a

with open("../train-v2.0.json", 'r') as f:
  data = json.load(f)

questions, answers = get_qa(topic='Premier_League', data=data)

json_data = {
  'questions':questions,
  'answers':answers,
}

response = requests.post(
  'http://0.0.0.0:8000/set_context',
  json=json_data
)

print(response.json())