class Question:
    def __init__(self, text, options, correct, explanation):
        self.text = text
        self.options = options  # dict like {'A': '...', 'B': '...'}
        self.correct = correct
        self.explanation = explanation
