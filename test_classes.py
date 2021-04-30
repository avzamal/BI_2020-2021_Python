import unittest
from Classes import Dna, Rna


class TestDna(unittest.TestCase):
    def setUp(self):
        self.dna = Dna('ATGCTACG')

    def test_gc_content(self):
        self.assertEqual(self.dna.gc_content(), 0.5)

    def test_reverse_complement(self):
        self.assertEqual(self.dna.reverse_complement(), 'CGTAGCAT')

    def test_transcribe(self):
        rna_output = self.dna.transcribe()
        self.assertEqual(rna_output.sequence, 'AUGCUACG')


class TestRna(unittest.TestCase):
    def setUp(self):
        self.rna = Rna('AUGCUACG')

    def test_gc_content(self):
        self.assertEqual(self.rna.gc_content(), 0.5)

    def test_reverse_complement(self):
        self.assertEqual(self.rna.reverse_complement(), 'CGUAGCAU')


if __name__ == '__main__':
    unittest.main()
