class Dna:
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        
    def gc_content(self):
        total_gc = self.sequence.count('G') + self.sequence.count('C')
        return total_gc / len(self.sequence)
    
    def reverse_complement(self):
        translation_table = str.maketrans({'A':'T', 'T':'A', 'G':'C', 'C':'G'})
        inverted_sequence = self.sequence[::-1]
        return inverted_sequence.translate(translation_table)
    
    def __iter__(self):
        for each in self.sequence:
            yield each

    def __eq__(self, other):
        if isinstance(other, Dna):
            return self.sequence == other.sequence
        return NotImplemented
    
    def __hash__(self):
        return hash(self.sequence)
    
    def transcribe(self):
        translation_table = str.maketrans({'T':'U'})
        return Rna(self.sequence.translate(translation_table))


class Rna:
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        
    def gc_content(self):
        total_gc = self.sequence.count('G') + self.sequence.count('C')
        return total_gc / len(self.sequence)
    
    def reverse_complement(self):
        translation_table = str.maketrans({'A':'U', 'U':'A', 'G':'C', 'C':'G'})
        inverted_sequence = self.sequence[::-1]
        return inverted_sequence.translate(translation_table)
    
    def __iter__(self):
        for each in self.sequence:
            yield each

    def __eq__(self, other):
        if isinstance(other, Dna):
            return self.sequence == other.sequence
        return NotImplemented
    
    def __hash__(self):
        return hash(self.sequence)
