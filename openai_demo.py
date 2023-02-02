#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://jugis-openai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Extrahiere die Produktkategorie:\nWelche Alkoholhaltigen Getränke auf Traubenbasis bietet Netto an?\nProduktkategorie:\nAlkoholhaltige Getränke auf Traubenbasis\nWie nennt man diese auch?\nWein",
  temperature=0.6,
  max_tokens=100,
  top_p=0.5,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=1,
  stop=None)

