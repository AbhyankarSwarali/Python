from collections import Counter
import re

text = '''Python is an easy programmar's language.
          Python syntax is like the English language.
          Python language is easy to learn and adapt to compared to Java and C.
          In Python language the same task can be performed in fewer lines of code.
          its easy learning and easy to code.'''

# words = text.split()
words = re.findall('\w+', text)

count = Counter(words)
print(count.most_common(3))