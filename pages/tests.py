from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(this):
        response = this.client.get("/")
        this.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(this):
        response = this.client.get(reverse("home"))
        this.assertEqual(response.status_code, 200)

    def test_template_name_correct(this):
        response = this.client.get(reverse("home"))
        this.assertTemplateUsed(response, "home.html")

    def test_template_content(this):
        response = this.client.get(reverse("home"))
        this.assertContains(response, "<h1>Homepage</h1>")

        
            
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(this):
        response = this.client.get("/about/")
        this.assertEqual(response.status_code, 200)

    def test_url_available_by_name(this):
        response = this.client.get(reverse("about"))
        this.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(this):
        response = this.client.get(reverse("about"))
        this.assertTemplateUsed(response, "about.html")

    def test_template_content(this):
        response = this.client.get(reverse("about"))
        this.assertContains(response, "<h1>About</h1>")
        
