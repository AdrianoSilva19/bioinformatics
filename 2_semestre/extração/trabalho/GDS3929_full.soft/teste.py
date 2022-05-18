import pandas as pd

df = pd.read_csv(r'C:\Users\ampsi\OneDrive\Ambiente de Trabalho\second_semestre\extração\trabalho\GDS3929_full.soft\GDS3929_full.soft', delimiter = "\t")
df.to_csv(r'C:\Users\ampsi\OneDrive\Ambiente de Trabalho\second_semestre\extração\trabalho\GDS3929_full.soft\aberto.csv')