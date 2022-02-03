import unittest
import re
from math import log
from typing import List
import seqmanpy as smp

class TestDnaRna (unittest.TestCase):
    def test_dnarna (self):
        self.assertTrue (smp.dna_rna('atgc'), 'AUGC')
        self.assertTrue (smp.dna_rna('ATGCTAGC'), 'AUGCUAGC')

    def test_types (self):
        self.assertRaises (TypeError, smp.dna_rna, 23)
        self.assertRaises (TypeError, smp.dna_rna, [1, 2, 3])
        self.assertRaises (TypeError, smp.dna_rna, 3+5j)

class TestValidacao (unittest.TestCase):
    def test_validacao (self):
        #Test output when the input is DNA string
        self.assertTrue (smp.validacao_dna('atgctgatcgatg'), True)
        self.assertTrue (smp.validacao_dna('GCTAGCTAGCTTAGC'), True)
        self.assertFalse (smp.validacao_dna('atcgatgchatcg'), False)
        self.assertFalse (smp.validacao_dna('AUGCGUAGCUAG'), False)

    def test_types (self):
        self.assertRaises (TypeError, smp.validacao_dna, 23)
        self.assertRaises (TypeError, smp.validacao_dna, [1, 2, 3])
        self.assertRaises (TypeError, smp.validacao_dna, 3+5j)

class TestRnaDna (unittest.TestCase):
    def test_dnarna (self):
        self.assertTrue (smp.rna_dna('AUGC'), 'ATGC')
        self.assertTrue (smp.rna_dna('aucg'), 'ATCG')
        self.assertTrue (smp.rna_dna('AUGCGU'), 'ATGCGT')

    def test_types (self):
        self.assertRaises (TypeError, smp.rna_dna, 23)
        self.assertRaises (TypeError, smp.rna_dna, [1, 2, 3])
        self.assertRaises (TypeError, smp.rna_dna, 3+5j)

class TesteComplementoInverso (unittest.TestCase):
    def test_complementoinverso (self):
        self.assertTrue (smp.complemento_inverso('atgctagc'), 'GCTAGCAT')
        self.assertTrue (smp.complemento_inverso('ATGCGCGATCG'), 'CGATCGCGCAT')
        self.assertTrue (smp.complemento_inverso('ATGCTGA'), 'TCAGCAT')

    def test_types (self):
        self.assertRaises (TypeError, smp.complemento_inverso, 1234)
        self.assertRaises (TypeError, smp.complemento_inverso, ['atgc', 'cgta', 'agtca'])

class TestDnaRnaAminoErro (unittest.TestCase):
    def test_dna_rna_amino_erro (self):
        self.assertEqual (smp.dna_rna_amino_erro('atgcga'), 'DNA')
        self.assertEqual (smp.dna_rna_amino_erro('ATGC'), 'DNA')
        self.assertEqual (smp.dna_rna_amino_erro('augc'), 'RNA')
        self.assertEqual (smp.dna_rna_amino_erro('AUGCAGCUGU'), 'RNA')
        self.assertEqual (smp.dna_rna_amino_erro('mnkacd'), 'Aminoácidos')
        self.assertEqual (smp.dna_rna_amino_erro('MNPACDKL'), 'Aminoácidos')
        self.assertEqual (smp.dna_rna_amino_erro('MNPjKL'), 'Erro')
        self.assertEqual (smp.dna_rna_amino_erro('MNPOKL'), 'Erro')

    def teste_type (self):
        self.assertRaises (TypeError, smp.dna_rna_amino_erro, [1, 2, 'ola', 'adeus'])
        self.assertRaises (TypeError, smp.dna_rna_amino_erro, [1, 2, 3])
        self.assertRaises (TypeError, smp.dna_rna_amino_erro, 5432334)

class TestGetCodons (unittest.TestCase):
    def test_get_codons (self):
        self.assertEqual (smp.get_codons('atgctagat'), ['ATG', 'CTA', 'GAT'])
        self.assertEqual (smp.get_codons('ATGCGTACG'), ['ATG', 'CGT', 'ACG'])
        self.assertEqual (smp.get_codons('ATGGC'), ['ATG'])
        

    def test_types (self):
        self.assertRaises (TypeError, smp.get_codons, 13)
        self.assertRaises (TypeError, smp.get_codons, 'atgcta12345')
        self.assertRaises (TypeError, smp.get_codons, 'ATGCTAG12345')

class TestCodonToAmino (unittest.TestCase):
    def test_codon_to_amino (self):
        self.assertEqual (smp.codon_to_amino('augcgugcuagc'), 'MRAS')
        self.assertEqual (smp.codon_to_amino('GUAGGCGAC'), 'VGD')

    def test_types (self):
        self.assertRaises (TypeError, smp.codon_to_amino, 'tagtcgatg')
        self.assertRaises (TypeError, smp.codon_to_amino, 'ATGCTAGC')
        self.assertRaises (TypeError, smp.codon_to_amino, 12342)
        self.assertRaises (TypeError, smp.codon_to_amino, 'acug1guca')

class TestGetProts (unittest.TestCase):
    def test_get_prots (self):
        self.assertEqual (smp.get_prots('atgcccgaatga'), ['MPE_'])
        

    def test_types (self):
        self.assertRaises (TypeError, smp.get_prots, 'atg12cg')
        self.assertRaises (TypeError, smp.get_prots, 231)
        self.assertRaises (TypeError, smp.get_prots, 'augcccgaatga')

class TestDotPlot (unittest.TestCase):
    def test_dotplot (self):
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 3, 1), [[' ', ' ', ' ', 'G', 'T', 'C', 'G', 'A', 'T'], [' ', ' ', ' ', 'T', 'C', 'G', 'A', 'T', 'G'], [' ', ' ', ' ', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', 'T', 'G', '*', '*', ' ', ' ', '*', ' '], ['T', 'G', 'C', '*', '*', '*', ' ', ' ', '*'], ['G', 'C', 'T', '*', '*', ' ', '*', ' ', ' '], ['C', 'T', 'G', '*', '*', '*', ' ', '*', ' '], ['T', 'G', 'A', ' ', '*', '*', ' ', ' ', '*'], ['G', 'A', 'C', '*', ' ', ' ', '*', ' ', '*'], ['A', 'C', 'A', ' ', '*', '*', ' ', '*', ' ']] )
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 3, 2), [[' ', ' ', ' ', 'G', 'T', 'C', 'G', 'A', 'T'], [' ', ' ', ' ', 'T', 'C', 'G', 'A', 'T', 'G'], [' ', ' ', ' ', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', 'T', 'G', ' ', ' ', ' ', ' ', '*', ' '], ['T', 'G', 'C', ' ', ' ', ' ', ' ', ' ', '*'], ['G', 'C', 'T', ' ', ' ', ' ', '*', ' ', ' '], ['C', 'T', 'G', ' ', ' ', ' ', ' ', '*', ' '], ['T', 'G', 'A', ' ', ' ', '*', ' ', ' ', '*'], ['G', 'A', 'C', '*', ' ', ' ', '*', ' ', ' '], ['A', 'C', 'A', ' ', ' ', ' ', ' ', ' ', ' ']] )
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 3, 3), [[' ', ' ', ' ', 'G', 'T', 'C', 'G', 'A', 'T'], [' ', ' ', ' ', 'T', 'C', 'G', 'A', 'T', 'G'], [' ', ' ', ' ', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', 'T', 'G', ' ', ' ', ' ', ' ', '*', ' '], ['T', 'G', 'C', ' ', ' ', ' ', ' ', ' ', '*'], ['G', 'C', 'T', ' ', ' ', ' ', ' ', ' ', ' '], ['C', 'T', 'G', ' ', ' ', ' ', ' ', ' ', ' '], ['T', 'G', 'A', ' ', ' ', ' ', ' ', ' ', ' '], ['G', 'A', 'C', ' ', ' ', ' ', ' ', ' ', ' '], ['A', 'C', 'A', ' ', ' ', ' ', ' ', ' ', ' ']] )
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 2, 2), [[' ', ' ', 'G', 'T', 'C', 'G', 'A', 'T', 'G'], [' ', ' ', 'T', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', 'T', ' ', ' ', ' ', ' ', '*', ' ', ' '], ['T', 'G', ' ', ' ', ' ', ' ', ' ', '*', ' '], ['G', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '*'], ['C', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['T', 'G', ' ', ' ', ' ', ' ', ' ', '*', ' '], ['G', 'A', ' ', ' ', ' ', '*', ' ', ' ', ' '], ['A', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['C', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] )
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 2, 1), [[' ', ' ', 'G', 'T', 'C', 'G', 'A', 'T', 'G'], [' ', ' ', 'T', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', 'T', '*', ' ', ' ', ' ', '*', ' ', ' '], ['T', 'G', ' ', '*', '*', ' ', ' ', '*', ' '], ['G', 'C', '*', '*', ' ', '*', ' ', ' ', '*'], ['C', 'T', '*', ' ', '*', ' ', '*', ' ', ' '], ['T', 'G', ' ', '*', '*', ' ', ' ', '*', ' '], ['G', 'A', '*', ' ', ' ', '*', ' ', ' ', '*'], ['A', 'C', ' ', '*', ' ', ' ', '*', ' ', '*'], ['C', 'A', ' ', ' ', '*', '*', ' ', ' ', ' ']] )
        self.assertEqual (smp.dotplot('atgctgaca', 'gtcgatgc', 1, 1), [[' ', 'G', 'T', 'C', 'G', 'A', 'T', 'G', 'C'], ['A', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' '], ['T', ' ', '*', ' ', ' ', ' ', '*', ' ', ' '], ['G', '*', ' ', ' ', '*', ' ', ' ', '*', ' '], ['C', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*'], ['T', ' ', '*', ' ', ' ', ' ', '*', ' ', ' '], ['G', '*', ' ', ' ', '*', ' ', ' ', '*', ' '], ['A', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' '], ['C', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*'], ['A', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ']] )

    def test_types (self):
        self.assertRaises (TypeError, smp.dotplot, 'atgctagcagct', 'atgctagctg', 2, 3)
        self.assertRaises (TypeError, smp.dotplot, 23, 'atgctagctg', 3, 2)
        self.assertRaises (TypeError, smp.dotplot, 'atgctagcagct', 32, 1, 1)

class TestPWM (unittest.TestCase):
    def test_pwm (self):
        self.assertEqual (smp.pwm(['atgctga', 'atgctga'], pseudo = 0, printing = False), [{'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}, {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}])
        self.assertEqual (smp.pwm(['ATTG','ATCG','ATTC','ACTC'], pseudo = 0.5, printing = False), [{'A': 0.75, 'C': 0.08333333333333333, 'G': 0.08333333333333333, 'T': 0.08333333333333333}, {'A': 0.08333333333333333, 'C': 0.25, 'G': 0.08333333333333333, 'T': 0.5833333333333334}, {'A': 0.08333333333333333, 'C': 0.25, 'G': 0.08333333333333333, 'T': 0.5833333333333334}, {'A': 0.08333333333333333, 'C': 0.4166666666666667, 'G': 0.4166666666666667, 'T': 0.08333333333333333}])

    def test_type (self):
        self.assertRaises (TypeError, smp.pwm, ['atgc'])
        self.assertRaises (TypeError, smp.pwm, 23)
        self.assertRaises (TypeError, smp.pwm, ('atgca', 'ctgac'))

class TestPSSM (unittest.TestCase):
    def test_pssm (self):
        self.assertEqual (smp.pssm(['AACGTT', 'ATACCG', 'GACCAT', 'CAGGTT', 'AAACGT', 'TACCGT', 'GACGCT', 'AAACCT'], 1, False), [{'A': 0.7369655941662062, 'C': -0.5849625007211563, 'G': 0.0, 'T': -0.5849625007211563}, {'A': 1.4150374992788437, 'C': -1.5849625007211563, 'G': -1.5849625007211563, 'T': -0.5849625007211563}, {'A': 0.4150374992788437, 'C': 0.7369655941662062, 'G': -0.5849625007211563, 'T': -1.5849625007211563}, {'A': -1.5849625007211563, 'C': 1.0, 'G': 0.4150374992788437, 'T': -1.5849625007211563}, {'A': -0.5849625007211563, 'C': 0.4150374992788437, 'G': 0.0, 'T': 0.0}, {'A': -1.5849625007211563, 'C': -1.5849625007211563, 'G': -0.5849625007211563, 'T': 1.4150374992788437}])
        self.assertEqual (smp.pssm(['AACGTT', 'ATACCG', 'AAACCT'], 1, False), [{'A': 1.1926450779423958, 'C': -0.8073549220576043, 'G': -0.8073549220576043, 'T': -0.8073549220576043}, {'A': 0.7776075786635519, 'C': -0.8073549220576043, 'G': -0.8073549220576043, 'T': 0.19264507794239583}, {'A': 0.7776075786635519, 'C': 0.19264507794239583, 'G': -0.8073549220576043, 'T': -0.8073549220576043}, {'A': -0.8073549220576043, 'C': 0.7776075786635519, 'G': 0.19264507794239583, 'T': -0.8073549220576043}, {'A': -0.8073549220576043, 'C': 0.7776075786635519, 'G': -0.8073549220576043, 'T': 0.19264507794239583}, {'A': -0.8073549220576043, 'C': -0.8073549220576043, 'G': 0.19264507794239583, 'T': 0.7776075786635519}])

    def test_type (self):
        self.assertRaises (TypeError, smp.pssm, ['atgc'])
        self.assertRaises (TypeError, smp.pssm, 23)
        self.assertRaises (TypeError, smp.pssm, ('atgca', 'ctgac'))

class TestSeqMaisProvavel (unittest.TestCase):
    def test_alinhamentos (self):
        self.assertEqual (smp.seq_mais_prob(['ATTG','ATCG','ATTC','ACTC'], "TACCGTGCA", pseudo = 0.5), ('ACCG', '0.01953125'))

    def test_type (self):
        self.assertRaises (TypeError, smp.seq_mais_prob, 'ATGCT')
        self.assertRaises (TypeError, smp.seq_mais_prob, 23)
        self.assertRaises (TypeError, smp.seq_mais_prob, ('atgct', 'cggag', 'tgat'))


class TestAlinhamentos (unittest.TestCase):
    def test_alinhamentos (self):
        self.assertEqual (smp.alinhamentos('ATGCT', 'GTCGA', False, 2, 0, -1, False, False), (['ATGCT', 'GTCGA']))
        self.assertEqual (smp.alinhamentos('ATGCTGT', 'ACGTGTG', blossum=True, local=True, mat_print=False), (['ATGC-TGT', 'A--CGTGT']))
        self.assertEqual (smp.alinhamentos('ATGCT', 'GATGCGA', False, 2, 0, -1, True, False), (['ATGCT', 'ATGCG']))

    def test_type (self):
        self.assertRaises (TypeError, smp.alinhamentos, ['atgc'])
        self.assertRaises (TypeError, smp.alinhamentos, 12342)
        self.assertRaises (TypeError, smp.alinhamentos, ('atgca', 'cc'))
        self.assertRaises (TypeError, smp.alinhamentos, 3j)
        self.assertRaises (TypeError, smp.alinhamentos, -45)
        self.assertRaises (TypeError, smp.alinhamentos, 'atgcgg')

class TestAlinhamentoProgressivo (unittest.TestCase):
    def test_align_prog (self):
        self.assertEqual (smp.alinhamento_progressivo("ACTCAT AGTCAT ACGTCCT".split()), ['AC-TCAT', 'A-GTCAT', 'ACGTCCT'])
        self.assertEqual (smp.alinhamento_progressivo(["ACTCAT", "AGTCAT", "ACGTCCT"]), ['AC-TCAT', 'A-GTCAT', 'ACGTCCT'])
        self.assertEqual (smp.alinhamento_progressivo("TGACTA TACGTA TGGTA GAT".split()), ['TGAC-TA', 'T-ACGTA', 'TG--GTA', '-GA--T-'])
        self.assertEqual (smp.alinhamento_progressivo("GTTGCACCA GTCAGCA TTCCCA GCAGA".split())
, ['GTTGCACCA', 'G-T-CAGCA', '-TT-C-CCA', '---GCA-GA'])

    def test_type (self):
        self.assertRaises (TypeError, smp.alinhamento_progressivo, 1234)
        self.assertRaises (TypeError, smp.alinhamento_progressivo, 3j)
        self.assertRaises (TypeError, smp.alinhamento_progressivo, 'agctgac')
        self.assertRaises (TypeError, smp.alinhamento_progressivo, 'GCTGAC')
