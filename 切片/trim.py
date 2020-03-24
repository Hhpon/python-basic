def my_trim(texts):
  if len(texts) == 0:
    return texts
  while texts[0] == ' ':
    texts = texts[1:]
    if len(texts) == 0:
      return s
  while texts[-1] == ' ':
    texts = texts[:-1]
    if len(texts) == 0:
      return texts
  return texts

content = my_trim(' hello  world')
print(content)

trimContent = 'hello world   '.strip()
print(trimContent)