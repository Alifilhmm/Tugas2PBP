from django.test import TestCase, Client

# Create your tests here.
class PBP3Test(TestCase):
    def test_menu_url_exist(self):
        response = Client().get("/mywatchlist/")
        self.assertEqual(response.status_code, 200)

    def test_html_url_exist(self):
        response = Client().get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)

    def test_xml_url_exist(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)

    def test_json_url_exist(self):
        response = Client().get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)