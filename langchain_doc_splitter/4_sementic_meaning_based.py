from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

text="""
Cricket is a popular sport played between two teams of eleven players. 
The aim is to score more runs than the opposing team. It promotes teamwork, 
discipline, and fitness and is loved by millions around the world.
A farmer grows crops and raises animals to provide food for people. 
Farmers work hard in all weather conditions and play a vital role in the 
country's economy. They are often called the backbone of the nation.

Terrorism is the use of violence or threats to create fear and achieve political, 
religious, or ideological goals. It causes harm to people and society. 
Promoting peace, unity, and cooperation is essential to prevent terrorism and build a safer world.
"""

# Create Semantic Chunker
text_splitter = SemanticChunker(embeddings,breakpoint_threshold_type='standard_deviation',breakpoint_threshold_amount=1)

docs=text_splitter.create_documents(text)

print(len(docs))
print(docs)