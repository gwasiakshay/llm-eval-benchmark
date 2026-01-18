def score_relevance(output, expected):
    return 5 if expected.lower() in output.lower() else 3


def score_hallucination(output, expected):
    return 5 if expected.lower() in output.lower() else 2


def score_instruction(output):
    if len(output.split()) < 80:
        return 5
    return 3
