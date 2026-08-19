from langchain_text_splitters import RecursiveCharacterTextSplitter


text="""
Artificial Intelligence (AI) engineers are professionals who design, develop, and deploy 
intelligent systems that can perform tasks requiring human-like decision-making, learning, and 
problem-solving. They combine knowledge of programming, mathematics, machine learning, and 
data science to create AI-powered applications such as chatbots, recommendation systems, virtual 
assistants, autonomous vehicles, and medical diagnosis tools. AI engineers work with programming 
languages like Python and use frameworks such as TensorFlow, PyTorch, and Scikit-learn to build 
and train machine learning models. 

They also collaborate with data scientists, software developers, 
and business teams to ensure AI solutions meet real-world needs. As AI continues to transform 
industries like healthcare, finance, education, manufacturing, and entertainment, the demand for 
skilled AI engineers is growing rapidly. Their work helps organizations automate processes, 
improve efficiency, make better decisions, and develop innovative products, making AI engineering 
one of the most exciting and impactful careers in modern technology."""

#initialize the spliiter
splitter=RecursiveCharacterTextSplitter(
         chunk_size=500,
         chunk_overlap=0
)

# perform the split
chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)
