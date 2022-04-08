import tabula.io
import pandas as pd
df = tabula.io.convert_into('XLDocs', 'XLDocs', output_format="csv", java_options=None)

for i in range(len(df)):
 df[i].to_excel('CERT_'+str(i)+'.xlsx')
