import string
import collections
from nltk.corpus import stopwords

with open("../../../dataset/The Catcher in the Rye (J. D. Salinger) (Z-Library).txt") as f:
    text = f.read()

stopwords = stopwords.words("english")
ls = list(string.punctuation)
text = text.lower()

for i in ls:
    text = text.replace(i, " ")
lis = text.split()

# counts = {}
#
# for i in lis:
#     if len(i) > 1:
#         counts[i] = counts.get(i, 0) + 1
#
# for word in stopwords:
#     counts.pop(word, 0)

cl = collections.Counter(lis)
for i in stopwords:
    cl.pop(i, 0)

print(cl.most_common(20))
