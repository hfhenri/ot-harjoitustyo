import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_raha_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassapaatteen_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_lounas_kateis_osto_toimii(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)

    def test_maukas_lounas_kateis_osto_toimii(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(460)

        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)

    def test_edullinen_lounas_kateisella_arvo_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kateisella_arvo_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_kateis_osto_yritys_toimii(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
    
    def test_maukas_lounas_kateis_osto_yritys_toimii(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_edullinen_lounas_kortti_osto_toimii(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(onnistui, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)

    def test_maukas_lounas_kortti_osto_toimii(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(onnistui, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.00)

    def test_edullinen_lounas_kortilla_arvo_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kortilla_arvo_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_kortti_osto_yritys_toimii(self):
        maksukortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(onnistui, False)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_lounas_kortti_osto_yritys_toimii(self):
        maksukortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(onnistui, False)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahamaara_ei_muutu_kortilla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_rahamaara_ei_muutu_kortilla_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    def test_rahamaara_muuttuu_korttia_lataessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.00)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.00)

    def test_rahamaara_ei_muutu_korttia_lataessa_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)

    

    
    