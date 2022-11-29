import os
import json
from kivy.storage.jsonstore import JsonStore

"""
data.json
{
    "dabloons": 1000,
    "transactions": [
        {
            "id": 1,
            "action": "deposit",
            "price": 100,
            "name": "",
            "date": "01.01.1970",
            "time": "12:00:00"
        },
        {
            "id": 2,
            "action": "purchase",
            "price": 100,
            "name": "Sword",
            "date": "01.01.1970",
            "time": "12:00:00"
        }
    ]
}

"""
#def load_data():
#    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'data.json')):
#        save_data({'dabloons': 0, 'transactions': []})
#
#    with open(os.path.join(os.path.dirname(__file__), 'data.json')) as f:
#        data = json.load(f)
#    return data
#
#def save_data(data):
#    with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'w') as f:
#        json.dump(data, f, indent=4)


class Dabloons(int):
    def __init__(self):
        self.data = JsonStore('data.json')
    
    @property
    def credits(self):
        return self.data['dabloons']['credits']
    
    @credits.setter
    def credits(self, value):
        self.data['dabloons']['credits'] = value

    def __add__(self, value):
        self.data['dabloons']['credits'] += value
    
    def __iadd__(self, value):
        self.data['dabloons']['credits'] += value
        return self
    
    def __radd__(self, value) -> int:
        self.data['dabloons']['credits'] += value
        return self.data['dabloons']['credits']
    
    def __mul__(self, value):
        return self.data['dabloons']['credits'] * value
    
    def __rmul__(self, value):
        return self.data['dabloons']['credits'] * value
    
    def __imul__(self, value):
        self.data['dabloons']['credits'] *= value
        return self
    
    def __sub__(self, value):
        return self.data['dabloons']['credits'] - value
    
    def __rsub__(self, value):
        return self.data['dabloons']['credits'] - value

    def __isub__(self, value):
        self.data['dabloons']['credits'] -= value
        return self
    
    def __mod__(self, value):
        return self.data['dabloons']['credits'] % value
    
    def __rmod__(self, value):
        return self.data['dabloons']['credits'] % value
    
    def __imod__(self, value):
        self.data['dabloons']['credits'] %= value
        return self
    
    def __floordiv__(self, value):
        return self.data['dabloons']['credits'] // value
    
    def __rfloordiv__(self, value):
        return self.data['dabloons']['credits'] // value
    
    def __ifloordiv__(self, value):
        self.data['dabloons']['credits'] //= value
        return self
    
    def __truediv__(self, value):
        return self.data['dabloons']['credits'] / value
    
    def __rtruediv__(self, value):
        return self.data['dabloons']['credits'] / value
    
    def __itruediv__(self, value):
        self.data['dabloons']['credits'] /= value
        return self
    
    def __pow__(self, value):
        return self.data['dabloons']['credits'] ** value
    
    def __rpow__(self, value):
        return self.data['dabloons']['credits'] ** value
    
    def __ipow__(self, value):
        self.data['dabloons']['credits'] **= value
        return self
    
    def __eq__(self, value):
        return self.data['dabloons']['credits'] == value
    
    def __ne__(self, value):
        return self.data['dabloons']['credits'] != value
    
    def __lt__(self, value):
        return self.data['dabloons']['credits'] < value
    
    def __le__(self, value):
        return self.data['dabloons']['credits'] <= value
    
    def __gt__(self, value):
        return self.data['dabloons']['credits'] > value
    
    def __ge__(self, value):
        return self.data['dabloons']['credits'] >= value

    def __round__(self, n=None):
        return round(self.data['dabloons']['credits'], n)
    
    def __floor__(self):
        return int(self.data['dabloons']['credits'])

    def __int__(self):
        return int(self.data['dabloons']['credits'])
    
    def __float__(self):
        return float(self.data['dabloons']['credits'])
    
    def __bool__(self):
        return bool(self.data['dabloons']['credits'])

    def __str__(self):
        return str(self.data['dabloons']['credits'])
    
    def __repr__(self):
        return repr(self.data['dabloons']['credits'])
    
    def __dir__(self):
        return dir(self.data['dabloons']['credits'])
    
    
    
    



class Transactions:
    def __init__(self):
        self.data = JsonStore('data.json')
    
    def __get__(self):
        return self.data['transactions']
    
    def __set__(self, value):
        self.data['transactions'] = value
    
    def append(self, value):
        self.data['transactions'].append(value)

    def clear(self):
        self.data['transactions'] = []
    
    def copy(self):
        return self.data['transactions'].copy()
    
    def count(self, item):
        return self.data['transactions'].count(item)
    
    def index(self, item):
        return self.data['transactions'].index(item)
    
    def insert(self, index, item):
        self.data['transactions'].insert(index, item)
    
    def pop(self, index):
        self.data['transactions'].pop(index)
    
    def remove(self, item):
        self.data['transactions'].remove(item)
    
    def reverse(self):
        self.data['transactions'].reverse()
    
    def sort(self, key=None, reverse=False):
        self.data['transactions'].sort(key=key, reverse=reverse)

    def __len__(self):
        return len(self.data['transactions'])
    
    def __iter__(self):
        return iter(self.data['transactions'])
    
    def __contains__(self, item):
        return item in self.data['transactions']
    
    def __repr__(self):
        return str(self.data['transactions'])
    
    def __str__(self):
        return str(self.data['transactions'])
    
    def __getitem__(self, index):
        return self.data['transactions'][index]
    
    def __setitem__(self, index, value):
        self.data['transactions'][index] = value
    
    def __delitem__(self, index):
        del self.data['transactions'][index]
    
    def edit(self, index, key, value):
        self.data['transactions'][index][key] = value
    





