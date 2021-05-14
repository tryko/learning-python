# def reverse_words(str):
#   return ' '.join(w[::-1] for w in str.split(' '))

def reverse_words(str):
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)