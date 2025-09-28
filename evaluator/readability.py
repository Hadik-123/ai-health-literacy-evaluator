from textstat import textstat

def compute_readability(text: str) -> dict:
    text = text.strip()
    return {
        "words": textstat.lexicon_count(text, removepunct=True),
        "sentences": textstat.sentence_count(text),
        "fk_grade": textstat.flesch_kincaid_grade(text),
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "gunning_fog": textstat.gunning_fog(text),
        "smog": textstat.smog_index(text),
        "dale_chall": textstat.dale_chall_readability_score(text),
    }
