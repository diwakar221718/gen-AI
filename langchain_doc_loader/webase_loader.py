from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url='https://aistudio.google.com/prompts/new_chat'
loader=WebBaseLoader(url)  # we can also pass multiple url (but all url should be in list)

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt=PromptTemplate(
    template='answer the following question \n{question} from the follwing text-\n{text}',
    input_variables=['question','text']
)

parser=StrOutputParser()

docs=loader.load()

print(len(docs))
print(docs[0].page_content)

chain=prompt | model | parser

result=chain.invoke({'question':'to whom we are taking about','text':docs[0].page_content})
print(result)
