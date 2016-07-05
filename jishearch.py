#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import weechat

info = (
        'JiSearch',
        'ark',
        '0.1',
        'MIT',
        'Requests the jisho\'s API',
        '',
        'utf-8'
        )

url = 'http://beta.jisho.org/api/v1/search/words?keyword='

def jisho_search(data, buffer, message):
    r = requests.get(url+message)
    
    result = b'[JiSearch] '
    try:
        data = json.loads(r.text)['data'][0]

        try:
            result += b'kanji: %s | ' % data['japanese'][0]['word'].encode('utf-8')
        except KeyError:
            pass
        result += b'reading: %s | ' % data['japanese'][0]['reading'].encode('utf-8')
        result += b'meaning: %s' % data['senses'][0]['english_definitions'][0].encode('utf-8')

    except:
        result += 'no results found.'
    weechat.prnt(weechat.current_buffer(), result)
    return weechat.WEECHAT_RC_OK

if weechat.register(*info):
    weechat.hook_command(
            'jisearch',
            'Calls Jisho\'s API to search for english words, kanji or kana',
            '[kanji | kana | english]',
            '',
            '',
            'jisho_search',
            '')


