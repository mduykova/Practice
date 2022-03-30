TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()
    
keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
    }
