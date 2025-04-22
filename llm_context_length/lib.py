import re


TOKEN_LENGTH = 4
# https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them


def str_to_tokens(str: str) -> float:
    return len(str) / TOKEN_LENGTH

def str_to_processing_tokens(str: str) -> int:
    standalone_punctuation = re.sub(r'[.,?!:;()[\]{}]', ' . ', str)
    words = standalone_punctuation.split()
    return len(words)
