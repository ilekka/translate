import deepl
import os
from dotenv import load_dotenv
import textwrap


def main():

    load_dotenv('/home/ilkka/Python/deepl.env')

    text = ''

    with open('/home/ilkka/.translate/translate_in.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line == '':
                text = text + '\n\n'
            else:
                text = text + line + ' '

    translator = deepl.Translator(auth_key=os.getenv('AUTH_KEY'),
                                  server_url='https://api-free.deepl.com')

    result = translator.translate_text(text, target_lang='EN-US')

    with open('/home/ilkka/.translate/translate_out.txt', 'w') as f:
        for line in result.text.split('\n'):
            if line == '':
                f.write('\n')
            else:
                wrapped = textwrap.wrap(line, width=79)
                for line in wrapped:
                    f.write(line + '\n')


if __name__ == '__main__':
    main()
