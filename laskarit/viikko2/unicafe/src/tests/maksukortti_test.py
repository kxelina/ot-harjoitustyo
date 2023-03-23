import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_rahan_ottaminen(self):
        ota=self.maksukortti.ota_rahaa(1000)

        self.assertEqual(ota, True)

    def test_rahan_ottaminen_toinen(self):
        ota=self.maksukortti.ota_rahaa(4500)

        self.assertEqual(ota, False)
    


    
