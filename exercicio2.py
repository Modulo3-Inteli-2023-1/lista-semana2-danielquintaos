def is_anagram():
  a = str(input("insira a palavra: "))
  b = str(input("insira a palavra: "))

  a = a.lower()
  b = b.lower()

  a = sorted(a)
  b = sorted(b)

  if a == b:
    return True
  else:
    return False

anagram = is_anagram()
print(anagram)