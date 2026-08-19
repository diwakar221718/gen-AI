from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader=DirectoryLoader(
    path='dy',              # path name
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs=loader.load() 
docs=loader.lazy_load()
# print(docs[5].page_content)
# print(docs[5].metadata)
# print(len(docs))

# apply on lazy_load
for document in docs:
    print(document.metadata)