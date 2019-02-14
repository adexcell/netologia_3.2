import requests

def translate_it(source_path, result_path, from_lang, to_lang='ru'):
  API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
  URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
  print('Start translation -', source_path)
    
  with open(source_path, encoding='utf-8') as source_f:
    text = source_f.read()

  params = {
    'key': API_KEY,
    'text': text,
    'lang': '{}-{}'.format(from_lang, to_lang),
  }

  response = requests.get(URL, params=params)
  json_ = response.json()
  output = ''.join(json_['text'])

  with open(result_path, 'w', encoding='utf-8') as result_f:
   result_f.write(output)

  print('End -', result_path)
  print()

translate_it('DE.txt', 'Translate_DE.txt', 'de')
translate_it('ES.txt', 'Translate_ES.txt', 'es')
translate_it('FR.txt', 'Translate_FR.txt', 'fr')
