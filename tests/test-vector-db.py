import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="europa")

collection.upsert(
documents=[
    "Invest Stemos will open an office in Brazil.",
    "Invest Stemos will open an office in France.",
    "Invest Stemos will open an office in Japan.",
    "Invest Stemos will open an office in Germany.",
    "Invest Stemos will open an office in Canada.",
    "Invest Stemos will open an office in Australia.",
    "Invest Stemos will open an office in Italy.",
    "Invest Stemos will open an office in Argentina.",
    "Invest Stemos will open an office in Spain.",
    "Invest Stemos will open an office in Russia."
  ],
  ids=["country1", "country2", "country3", "country4", "country5", "country6", "country7", "country8", "country9", "country10"]
)

result = collection.query(
  query_texts=["Invest Stemos will have an office at Estadio do Maracanã?"],
  n_results=3
)

print(result)
