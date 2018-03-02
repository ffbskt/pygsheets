"""
This file is for manual testing of pygsheets
"""
import sys
import IPython
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import pygsheets

from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.metadata.readonly']
CREDS_FILENAME = path.join(path.dirname(__file__), 'data/creds.json')

# credentials = ServiceAccountCredentials.from_json_keyfile_name('data/service_creds.json', SCOPES)

# gc = pygsheets.authorize(service_file='./data/service_creds.json')

gc = pygsheets.authorize(outh_file='/home/denis/Program/work/sheets.googleapis.com-python.json')
print(gc.get_range('1B1vEqp6uK7x2B8pV0dSH3S9DetFesaDP8n83Ewy53Yk', 'A1:D3' ))
gridrange = {
  "sheetId": 0,
  "startRowIndex": 0,
  "endRowIndex": 2,
  "startColumnIndex": 0,
  "endColumnIndex": 2,
}

editors = {
  "users": [
    'ffbskt@gmail.com',
  ],
  "groups": [
  ],
  "domainUsersCanEdit": True,
}
request = {"addProtectedRange": {
            "protectedRange": {
                "range": gridrange,
                "editors": editors
            },

        }}
print(gc.sh_batch_update('1B1vEqp6uK7x2B8pV0dSH3S9DetFesaDP8n83Ewy53Yk', request, None, False))
# wks = gc.open_by_key('18WX-VFi_yaZ6LkXWLH856sgAsH5CQHgzxjA5T2PGxIY')
#c = pygsheets.authorize(outh_file='other.json')
#c.sh_batch_update('1B1vEqp6uK7x2B8pV0dSH3S9DetFesaDP8n83Ewy53Yk', request, None, False)
#ss = gc.open('pygsheetTest')
#print (ss)

#wks = ss.sheet1
#print (wks)

# import  pandas as pd
# import numpy as np
#
# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
# ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

pass
#IPython.embed()
