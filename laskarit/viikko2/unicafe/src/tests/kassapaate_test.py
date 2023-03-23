import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class Testkassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate = Kassapaate()

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")


    def test_vaihtoraha_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        ota=self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(ota, False)

    def test_korttiosto_true(self):
        ota=self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(ota, True)
        

    def test_korttiosto(self):
        ota=self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(ota, True)

        ota=self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(ota, False)

        self.assertEqual(self.maksukortti.saldo, 260)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_voi_ladata_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2500)

        self.assertEqual(self.maksukortti.saldo, 3000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 102500)

    def test_kortille_ei_voi_ladata_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -2500)

        self.assertEqual(self.maksukortti.saldo, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
