from langchain_community.document_loaders import CSVLoader


loader=CSVLoader(file_path='insurance.csv')

docs=loader.load()
print(len(docs)) #fro every row of data we get i document (total document equal to number of rows) 
print(docs[1])