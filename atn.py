class Frame:
    def __init__(self, concept, frames=[]):
        self.concept = concept
        self.frames = frames # Concept frames

class ATRANS:
    def __init__(self, recip, obj, actor, result = None):
        self.recipt = recip
        self.obj = obj
        self.actor = actor
        self.result = result

    def summarize(self):
        return ""
        
    def display(self):
        # Maybe something with pdfLatex
