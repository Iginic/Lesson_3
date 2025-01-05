def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    return string in list_to_search

calls = 0
print(string_info('foxtrot'))
print(string_info('CAsABLANKA'))
print(string_info('renO'))
print(string_info('Alexander'))
print(is_contains('urban', ['ban', 'BaNaN', 'urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
