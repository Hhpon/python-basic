L = ['Hello', 'World', 18, 'Apple', None]

lower = [s.lower() for s in L if isinstance(s, str)]

print(lower)