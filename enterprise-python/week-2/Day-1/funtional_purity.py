dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
def puralize(words):
   result = []
   for word in words:
       word = words[i]
       if word.endswith('s') or word.endswith('x'):
           plural = word + 'es'
       if word.endswith('y'):
           plural = word[:-1] + 'ies'
       else:
           plural = +  's'
       result.append(plural)
       return result

def test_pluralize():
    result = pluralize(dictionary)
    assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']