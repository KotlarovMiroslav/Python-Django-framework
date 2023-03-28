
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

# class PostTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.post = Post.objects.create(text="This is a test!")
#     def test_model_content(self):
#         self.assertEqual(self.post.text, "This is a test!")
#     def test_url_exists_at_correct_location(self): # new
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 200)
#     def test_url_available_by_name(self): # new
#         response = self.client.get(reverse("home"))
#         self.assertEqual(response.status_code, 200)
#     def test_template_name_correct(self): # new
#         response = self.client.get(reverse("home"))
#         self.assertTemplateUsed(response, "home.html")
#     def test_template_content(self): # new
#         response = self.client.get(reverse("home"))
#         self.assertContains(response, "This is a test!")



# class HomepageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(this):
#         response = this.client.get("/")
#         this.assertEqual(response.status_code, 200)
        
#     def test_url_available_by_name(this):
#         response = this.client.get(reverse("home"))
#         this.assertEqual(response.status_code, 200)

#     def test_template_name_correct(this):
#         response = this.client.get(reverse("home"))
#         this.assertTemplateUsed(response, "home.html")

#     def test_template_content(this):
#         response = this.client.get(reverse("home"))
#         this.assertContains(response, "<h1>Homepage</h1>")

        
            
# class AboutpageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(this):
#         response = this.client.get("/about/")
#         this.assertEqual(response.status_code, 200)

#     def test_url_available_by_name(this):
#         response = this.client.get(reverse("about"))
#         this.assertEqual(response.status_code, 200)
    
#     def test_template_name_correct(this):
#         response = this.client.get(reverse("about"))
#         this.assertTemplateUsed(response, "about.html")

#     def test_template_content(this):
#         response = this.client.get(reverse("about"))
#         this.assertContains(response, "<h1>About</h1>")
        
