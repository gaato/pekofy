# Copyright 2021-2022 Gakuto Furuya
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sudachipy import tokenizer
from sudachipy import dictionary


def pekofy(sentence: str) -> str:
    """語尾にぺこをつけるぺこ"""

    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C
    tokens = tokenizer_obj.tokenize(sentence, mode)
    pekofied_sentence = ''
    noun_flag = False
    final_form_flag = False
    for t in tokens:
        if noun_flag:
            if t.part_of_speech()[1] == '句点':
                pekofied_sentence += 'ぺこ' + t.surface()
            elif t.part_of_speech()[1] == '終助詞':
                pekofied_sentence += 'ぺこ' + t.surface()
            elif t.part_of_speech()[0] == '助動詞' and t.part_of_speech()[5] == '終止形-一般':
                pekofied_sentence += 'ぺこ' + t.surface()
            else:
                pekofied_sentence += t.surface()
            noun_flag = False
        elif final_form_flag:
            if t.part_of_speech()[0] == '助動詞':
                pekofied_sentence += t.surface()
            elif t.part_of_speech()[1] == '終助詞':
                if t.dictionary_form() == 'じゃん':
                    pekofied_sentence += 'ぺこ' + t.surface()
                elif t.dictionary_form() == 'よ':
                    pekofied_sentence += 'ぺこだ' + t.surface()
                else:
                    pekofied_sentence += t.surface()
            elif t.part_of_speech()[1] == '接続助詞':
                if t.dictionary_form() == 'と' or t.dictionary_form() == 'けれど':
                    pekofied_sentence += t.surface()
                else:
                    pekofied_sentence += 'ぺこだ' + t.surface()
            else:
                pekofied_sentence += 'ぺこ' + t.surface()
            final_form_flag = False
        elif t.part_of_speech()[0] == '名詞':
            pekofied_sentence += t.surface()
            noun_flag = True
        elif t.part_of_speech()[5] in ('終止形-一般', '命令形'):
            pekofied_sentence += t.surface()
            final_form_flag = True
        else:
            pekofied_sentence += t.surface()
    if noun_flag:
        pekofied_sentence += 'ぺこ'
    if final_form_flag:
        pekofied_sentence += 'ぺこ'
    return pekofied_sentence


if __name__ == '__main__':
    while True:
        sentence = input()
        print(pekofy(sentence))
