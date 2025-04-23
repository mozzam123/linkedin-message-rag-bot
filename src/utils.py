import re

def extract_names_from_answer(answer):
    """
    Extracts names from the answer text using simple regex and heuristics.
    """
    # A simple assumption: full names are two capitalized words together
    matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", answer)
    return matches