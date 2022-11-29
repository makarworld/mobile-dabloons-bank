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

def loader(func):
    def wrapper(*args, **kwargs):
        args[0].data = JsonStore('data.json')
        result = func(*args, **kwargs)
        return result
    return wrapper

class Dabloons(int):
    def __init__(self):
        self.data = JsonStore('data.json')
        if not self.data.exists('dabloons'):
            self.data.put('dabloons', credits=0)
        
        if not self.data.exists('transactions'):
            self.data.put('transactions', transactions=[])
    
    @property
    @loader
    def credits(self):
        return self.data['dabloons']['credits']
    
    @credits.setter
    @loader
    def credits(self, value):
        self.data['dabloons']['credits'] = value

    @loader
    def __add__(self, value):
        self.data['dabloons']['credits'] += value
    
    def __iadd__(self, value):
        self.data['dabloons']['credits'] += value
        return self
    
    @loader
    def __radd__(self, value) -> int:
        self.data['dabloons']['credits'] += value
        return self.data['dabloons']['credits']
    
    @loader
    def __mul__(self, value):
        return self.data['dabloons']['credits'] * value
    
    def __rmul__(self, value):
        return self.data['dabloons']['credits'] * value
    
    def __imul__(self, value):
        self.data['dabloons']['credits'] *= value
        return self
    
    @loader
    def __sub__(self, value):
        return self.data['dabloons']['credits'] - value
    
    @loader
    def __rsub__(self, value):
        return self.data['dabloons']['credits'] - value

    @loader
    def __isub__(self, value):
        self.data['dabloons']['credits'] -= value
        return self
    
    @loader
    def __mod__(self, value):
        return self.data['dabloons']['credits'] % value
    
    @loader
    def __rmod__(self, value):
        return self.data['dabloons']['credits'] % value
    
    @loader
    def __imod__(self, value):
        self.data['dabloons']['credits'] %= value
        return self
    
    @loader
    def __floordiv__(self, value):
        return self.data['dabloons']['credits'] // value
    
    @loader
    def __rfloordiv__(self, value):
        return self.data['dabloons']['credits'] // value
    
    @loader
    def __ifloordiv__(self, value):
        self.data['dabloons']['credits'] //= value
        return self
    
    @loader
    def __truediv__(self, value):
        return self.data['dabloons']['credits'] / value
    
    @loader
    def __rtruediv__(self, value):
        return self.data['dabloons']['credits'] / value
    
    @loader
    def __itruediv__(self, value):
        self.data['dabloons']['credits'] /= value
        return self
    
    @loader
    def __pow__(self, value):
        return self.data['dabloons']['credits'] ** value
    
    @loader
    def __rpow__(self, value):
        return self.data['dabloons']['credits'] ** value
    
    @loader
    def __ipow__(self, value):
        self.data['dabloons']['credits'] **= value
        return self
    
    @loader
    def __eq__(self, value):
        return self.data['dabloons']['credits'] == value
    
    @loader
    def __ne__(self, value):
        return self.data['dabloons']['credits'] != value
    
    @loader
    def __lt__(self, value):
        return self.data['dabloons']['credits'] < value
    
    @loader
    def __le__(self, value):
        return self.data['dabloons']['credits'] <= value
    
    @loader
    def __gt__(self, value):
        return self.data['dabloons']['credits'] > value
    
    @loader
    def __ge__(self, value):
        return self.data['dabloons']['credits'] >= value

    @loader
    def __round__(self, n=None):
        return round(self.data['dabloons']['credits'], n)
    
    @loader
    def __floor__(self):
        return int(self.data['dabloons']['credits'])

    @loader
    def __int__(self):
        return int(self.data['dabloons']['credits'])
    
    @loader
    def __float__(self):
        return float(self.data['dabloons']['credits'])
    
    @loader
    def __bool__(self):
        return bool(self.data['dabloons']['credits'])

    @loader
    def __str__(self):
        return str(self.data['dabloons']['credits'])
    
    @loader
    def __repr__(self):
        return repr(self.data['dabloons']['credits'])
    
    @loader
    def __dir__(self):
        return dir(self.data['dabloons']['credits'])
    
    
    
    



class Transactions:
    def __init__(self):
        self.data = JsonStore('data.json')

        if not self.data.exists('dabloons'):
            self.data.put('dabloons', credits=0)
        
        if not self.data.exists('transactions'):
            self.data.put('transactions', transactions=[])
            
    @loader
    def __get__(self):
        return self.data['transactions']
    
    @loader
    def __set__(self, value):
        self.data['transactions'] = value
    
    @loader
    def append(self, value):
        self.data['transactions'].append(value)

    @loader
    def clear(self):
        self.data['transactions'] = []
    
    @loader
    def copy(self):
        return self.data['transactions'].copy()
    
    @loader
    def count(self, item):
        return self.data['transactions'].count(item)
    
    @loader
    def index(self, item):
        return self.data['transactions'].index(item)
    
    @loader
    def insert(self, index, item):
        self.data['transactions'].insert(index, item)
    
    @loader
    def pop(self, index):
        self.data['transactions'].pop(index)
    
    @loader
    def remove(self, item):
        self.data['transactions'].remove(item)
    
    @loader
    def reverse(self):
        self.data['transactions'].reverse()
    
    @loader
    def sort(self, key=None, reverse=False):
        self.data['transactions'].sort(key=key, reverse=reverse)

    @loader
    def __len__(self):
        return len(self.data['transactions'])
    
    @loader
    def __iter__(self):
        return iter(self.data['transactions'])
    
    @loader
    def __contains__(self, item):
        return item in self.data['transactions']
    
    @loader
    def __repr__(self):
        return str(self.data['transactions'])
    
    @loader
    def __str__(self):
        return str(self.data['transactions'])
    
    @loader
    def __getitem__(self, index):
        return self.data['transactions'][index]
    
    @loader
    def __setitem__(self, index, value):
        self.data['transactions'][index] = value
    
    @loader
    def __delitem__(self, index):
        del self.data['transactions'][index]
    
    @loader
    def edit(self, index, key, value):
        self.data['transactions'][index][key] = value
    





