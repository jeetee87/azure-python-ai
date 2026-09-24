# Azure AI Python Project

Een eenvoudige AI-chatbot gebouwd met **Python, Azure AI Foundry en Streamlit**.

Met dit project leer ik hoe ik vanuit Python verbinding maak met een AI-model via een API en hoe ik daar een eenvoudige webinterface omheen bouw.

## Screenshot

![Azure AI Chatbot](screenshots/Screenshot Azure AI Chatbot.png)

## Wat doet dit project?

De applicatie is een eenvoudige chatbot waarmee je vragen kunt stellen aan een AI-model dat draait via Azure AI Foundry.

De chatbot:

- verwerkt gebruikersvragen via een Streamlit-interface
- maakt verbinding met Azure AI via de OpenAI Python SDK
- onthoudt recente berichten binnen de chatsessie
- gebruikt eerdere vragen en antwoorden als context voor vervolgvragen
- houdt de Azure API-key veilig in een `.env` bestand

## Technologieën

- **Python**
- **Azure AI Foundry**
- **Phi-4-mini-instruct**
- **OpenAI Python SDK**
- **Streamlit**
- **python-dotenv**
- **Git & GitHub**

## Hoe werkt het?

De gebruiker stelt een vraag via de Streamlit-chat.

```text
Gebruiker
    ↓
Streamlit
    ↓
app.py
    ↓
ask_question()
    ↓
main.py
    ↓
Azure AI Foundry
    ↓
Phi-4-mini-instruct
    ↓
Antwoord
    ↓
Streamlit
```

De chatgeschiedenis wordt bijgehouden met `st.session_state`. Hierdoor kan de chatbot eerdere berichten gebruiken als context voor vervolgvragen.

De Azure-configuratie en API-key worden opgeslagen in een `.env` bestand en niet opgenomen in GitHub.

## Projectstructuur

```text
azure-python-ai/
│
├── app.py
├── main.py
├── README.md
├── screenshots/
│   └── Screenshot Azure AI Chatbot.png
├── .gitignore
└── .env
```

### Bestanden

**`app.py`**  
Bevat de Streamlit-interface en de chatgeschiedenis.

**`main.py`**  
Bevat de verbinding met Azure AI en de functie die vragen naar het AI-model stuurt.

**`.env`**  
Bevat de Azure-configuratie en API-key. Dit bestand wordt niet naar GitHub gestuurd.

**`screenshots/`**  
Bevat afbeeldingen van de applicatie voor de README.

## Installatie

### 1. Repository clonen

```bash
git clone https://github.com/jeetee87/azure-python-ai.git
```

Ga naar de projectmap:

```bash
cd azure-python-ai
```

### 2. Virtuele omgeving maken

Maak een virtual environment:

```bash
python -m venv .venv
```

Activeer deze op Windows:

```bash
.venv\Scripts\activate
```

Als het gelukt is, zie je `(.venv)` vooraan in je terminal.

### 3. Benodigde packages installeren

Installeer de benodigde Python-packages:

```bash
pip install openai python-dotenv streamlit
```

### 4. Azure-configuratie instellen

Maak in de hoofdmap van het project een bestand met de naam:

```text
.env
```

Voeg daarin je eigen Azure-configuratie toe:

```env
AZURE_OPENAI_ENDPOINT=jouw_azure_endpoint
AZURE_OPENAI_KEY=jouw_azure_api_key
AZURE_OPENAI_DEPLOYMENT=jouw_deployment_naam
```

Gebruik hier je eigen gegevens uit Azure AI Foundry.

> **Let op:** deel je API-key nooit publiekelijk en commit het `.env` bestand niet naar GitHub.

### 5. Applicatie starten

Start de Streamlit-app:

```bash
streamlit run app.py
```

Streamlit opent vervolgens de applicatie in je browser.

## Doel van dit project

Dit project is onderdeel van mijn ontwikkeling richting **Python en AI**.

Ik ben vanuit een achtergrond in de muziekwereld overgestapt naar softwareontwikkeling en gebruik praktische projecten om ervaring op te doen met Python, API's, AI-modellen en cloudtechnologie.

Dit project is een volgende stap in het leren bouwen van AI-applicaties met Python en Azure.
