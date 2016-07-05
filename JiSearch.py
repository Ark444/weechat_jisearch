# -*- coding: utf-8 -*-
#
# ark <quentrg@gmail.com>
# GitHub: Ark444
#
# The MIT License (MIT)
#
# Copyright (c) 2016 ark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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


