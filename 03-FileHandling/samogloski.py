t = "To be,or not to be,that is the question"
import re

samogloski=re.findall('[aeiouy]',t)

x = len(samogloski)

print('nr samoglosek: ',x)