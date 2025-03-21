import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(1000)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 0.0)

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_metodi_palauttaa_true_false_oikein(self):
        onnistui = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(onnistui, True)

        epaonnistui = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(epaonnistui, False)

    def test_saldo_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

