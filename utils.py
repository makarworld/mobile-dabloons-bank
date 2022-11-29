import os
import json

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
def load_data():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'data.json')):
        save_data({'dabloons': 0, 'transactions': []})

    with open(os.path.join(os.path.dirname(__file__), 'data.json')) as f:
        data = json.load(f)
    return data

def save_data(data):
    with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'w') as f:
        json.dump(data, f, indent=4)

def saver(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'[{func}] use saver for data', args[0].data)
        save_data(args[0].data)
        return result
    return wrapper

def loader(func):
    def wrapper(*args, **kwargs):
        args[0].data = load_data()
        result = func(*args, **kwargs)
        return result
    return wrapper


class Dabloons(int):
    def __init__(self):
        self.data = load_data()
    
    @property
    def credits(self):
        return self.data['dabloons']
    
    @credits.setter
    @loader
    @saver
    def credits(self, value):
        self.data['dabloons'] = value

    @loader
    @saver
    def __add__(self, value):
        self.data['dabloons'] += value
    
    @loader
    @saver
    def __iadd__(self, value):
        self.data['dabloons'] += value
        return self
    
    @loader
    @saver
    def __radd__(self, value) -> int:
        self.data['dabloons'] += value
        return self.data['dabloons']
    
    @loader
    @saver
    def __mul__(self, value):
        return self.data['dabloons'] * value
    
    @loader
    @saver
    def __rmul__(self, value):
        return self.data['dabloons'] * value
    
    @loader
    @saver
    def __imul__(self, value):
        self.data['dabloons'] *= value
        return self
    
    @loader
    @saver
    def __sub__(self, value):
        return self.data['dabloons'] - value
    
    @loader
    @saver
    def __rsub__(self, value):
        return self.data['dabloons'] - value

    @loader
    @saver
    def __isub__(self, value):
        self.data['dabloons'] -= value
        return self
    
    @loader
    @saver
    def __mod__(self, value):
        return self.data['dabloons'] % value
    
    @loader
    @saver
    def __rmod__(self, value):
        return self.data['dabloons'] % value
    
    @loader
    @saver
    def __imod__(self, value):
        self.data['dabloons'] %= value
        return self
    
    @loader
    @saver
    def __floordiv__(self, value):
        return self.data['dabloons'] // value
    
    @loader
    @saver
    def __rfloordiv__(self, value):
        return self.data['dabloons'] // value
    
    @loader
    @saver
    def __ifloordiv__(self, value):
        self.data['dabloons'] //= value
        return self
    
    @loader
    @saver
    def __truediv__(self, value):
        return self.data['dabloons'] / value
    
    @loader
    @saver
    def __rtruediv__(self, value):
        return self.data['dabloons'] / value
    
    @loader
    @saver
    def __itruediv__(self, value):
        self.data['dabloons'] /= value
        return self
    
    @loader
    @saver
    def __pow__(self, value):
        return self.data['dabloons'] ** value
    
    @loader
    @saver
    def __rpow__(self, value):
        return self.data['dabloons'] ** value
    
    @loader
    @saver
    def __ipow__(self, value):
        self.data['dabloons'] **= value
        return self
    
    def __eq__(self, value):
        return self.data['dabloons'] == value
    
    def __ne__(self, value):
        return self.data['dabloons'] != value
    
    def __lt__(self, value):
        return self.data['dabloons'] < value
    
    def __le__(self, value):
        return self.data['dabloons'] <= value
    
    def __gt__(self, value):
        return self.data['dabloons'] > value
    
    def __ge__(self, value):
        return self.data['dabloons'] >= value

    def __round__(self, n=None):
        return round(self.data['dabloons'], n)
    
    def __floor__(self):
        return int(self.data['dabloons'])

    def __int__(self):
        return int(self.data['dabloons'])
    
    def __float__(self):
        return float(self.data['dabloons'])
    
    def __bool__(self):
        return bool(self.data['dabloons'])

    def __str__(self):
        return str(self.data['dabloons'])
    
    def __repr__(self):
        return repr(self.data['dabloons'])
    
    def __dir__(self):
        return dir(self.data['dabloons'])
    
    
    
    



class Transactions:
    def __init__(self):
        self.data = load_data()
    
    def __get__(self):
        return self.data['transactions']
    
    @loader
    @saver
    def __set__(self, value):
        self.data['transactions'] = value
    
    @loader
    @saver
    def append(self, value):
        self.data['transactions'].append(value)

    @loader
    @saver
    def clear(self):
        self.data['transactions'] = []
    
    def copy(self):
        return self.data['transactions'].copy()
    
    def count(self, item):
        return self.data['transactions'].count(item)
    
    def index(self, item):
        return self.data['transactions'].index(item)
    
    @loader
    @saver
    def insert(self, index, item):
        self.data['transactions'].insert(index, item)
    
    @loader
    @saver
    def pop(self, index):
        self.data['transactions'].pop(index)
    
    @loader
    @saver
    def remove(self, item):
        self.data['transactions'].remove(item)
    
    @loader
    @saver
    def reverse(self):
        self.data['transactions'].reverse()
    
    @loader
    @saver
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
    
    @loader
    @saver
    def __getitem__(self, index):
        return self.data['transactions'][index]
    
    @loader
    @saver
    def __setitem__(self, index, value):
        self.data['transactions'][index] = value
    
    @loader
    @saver
    def __delitem__(self, index):
        del self.data['transactions'][index]
    
    @loader
    @saver
    def edit(self, index, key, value):
        self.data['transactions'][index][key] = value
    





