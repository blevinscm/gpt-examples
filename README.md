## A collection of examples for accessing GPT-3 API in Python programs. 

## Examples

### [Sceenplay Generator](/samples/gpt_screenplay.py)

This is a simple example of how to use the GPT-3 API in Python. It uses the [OpenAI API](https://beta.openai.com/docs/api-reference/introduction) to generate a response to a prompt.  The prompt is generated based on the Joseph Campbell monomyth, which is a common structure for stories.  The prompt is constructed in a crude TK app then sent to the API, and then the script generates a scrrenplay to a txt. file.  The screenplay is not a full script and is meant to be used as a starting point for your own projects.

Unimpressive sample output
```text
Basic Plot:
In a fantasy world where trees are the dominant life form. Each grove raises and trains humans to be protectors and to fight for the grove.  This story is about the fight for equality in the world from the infantilization of the grove masters. 


1. Ordinary World
Characters involved: , 
Scene description:

Dialogue:
: (Hero) could say: "For too long, we've been treated like mere pawns in their game. It's time we rise up, not just as protectors of the grove, but as equal and respected members of this world. We have the power to break free from their chains and fight for a future where humans and trees stand side by side, as equals."
: (Mentor): "For generations, we have entrusted our lives to the grove masters. They have provided us with protection and guidance, but at what cost? We have been relegated to mere servants, stripped of our autonomy and treated like children. But today, we must rise up and demand our rights. We are not just mere tools in their war against their enemies. We are sentient beings with our own motivations and desires. Only when we fight for equality can we truly be free."



2. Call to Adventure
Characters involved: , , 
Scene description:
```
### [Least common word finder and GPT-Lookup](/samples/leastcommon.ipynb)

This is a Jupyter notebook that uses the [GPT-3 API](https://platform.openai.com/docs/api-reference/chat) to return the meaning of the least common words in a given text.  In the exmple it uses A Tale of Two Cities.txt. It calls the Chat-GPT API with a system prompt of "You are a 6th grade literature teacher" [GPT Chat API](https://platform.openai.com/docs/api-reference/chat) to find the definition of the least common word.  The notebook also uses the [GPT-3 API](https://beta.openai.com/docs/api-reference/introduction) to generate a response to a prompt.  The least common words are found using Pandas to do a series count.  

## Instructions

```bash
# Ensure you are in the root directory of the project
pwd
# Create Virtual Environment and activate it
python3 -m venv .venv
source .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

```bash
# Create a config.ini file
touch config.ini
```
Add your OpenAI API key to the config.ini file using your favorite shell.
```bash
echo "[openai]" >> config.ini
echo "api_key = YOUR_API_KEY" >> config.ini
```
Or manually edit the config.ini file to add your API key.
```ini
[openai]
api_key = YOUR_API_KEY
```
Ensure your API key is correct in your config parser.
```python
# If you move things around ensure your config parser is pointing to the correct file by putting the path to the file in the read() method. The default is that the config.in file is in the root directory of the project.
config = configparser.ConfigParser()
config.read("../config.ini")
openai.api_key = config.get("openai", "api_key")
```
