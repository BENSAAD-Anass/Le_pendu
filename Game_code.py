import pandas as pd

wordlist = pd.read_csv('liste_francais.txt', sep="\t", header = 1)
print(wordlist)
