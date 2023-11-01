import re
from utils import prompts

# Handle prompts expressed in a more complex sentence
def match_prompt(query):
    '''
    Input: string of text
    Output: prompt, string.

    Search for specific patterns in a sentence and return the correct prompt
    '''
    for prompt in prompts:
        prt = re.search(prompt, query)
        if prt != None:
            return prt.group(0)
