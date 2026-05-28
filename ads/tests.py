from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Ad, Profile, Category, Review, Favorite


class ProfileAutoCreateTest(TestCase):
    def test_profile_created_on_user_save(self):
        user = User.objects.create_user(username="testuser", password="pass")
        self.assertTrue(Profile.objects.filter(user=user).exists())


class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="seller", password="pass")
        self.category = Category.objects.create(name="Elektronika")
        self.ad = Ad.objects.create(
            title="iPhone 14",
            price=50000,
            description="Otlichnoe sostoyanie",
            city="Moskva",
            author=self.user,
            category=self.category,
            is_published=True,
        )

    def test_ad_str(self):
        self.assertEqual(str(self.ad), "iPhone 14")

    def test_ad_defaults(self):
        self.assertEqual(self.ad.views, 0)
        self.assertEqual(self.ad.favorites_count, 0)
        self.assertFalse(self.ad.is_promoted)


class AdListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="u1", password="pass")
        self.category = Category.objects.create(name="Auto")
        Ad.objects.create(
            title="BMW X5",
            price=3000000,
            description="Khoroshee avto",
            city="SPb",
            author=self.user,
            category=self.category,
            is_published=True,
        )

    def test_ad_list_status_200(self):
        response = self.client.get(reverse("ad_list"))
        self.assertEqual(response.status_code, 200)

    def test_ad_list_contains_ad(self):
        response = self.client.get(reverse("ad_list"))
        self.assertContains(response, "BMW X5")

    def test_ad_list_search_match(self):
        response = self.client.get(reverse("ad_list") + "?q=BMW")
        self.assertContains(response, "BMW X5")

    def test_ad_list_search_no_match(self):
        response = self.client.get(reverse("ad_list") + "?q=Toyota")
        self.assertNotContains(response, "BMW X5")


class AdDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="u2", password="pass")
        self.category = Category.objects.create(name="Telefony")
        self.ad = Ad.objects.create(
            title="Samsung S24",
            price=80000,
            description="Noviy",
            city="Kazan",
            author=self.user,
            category=self.category,
            is_published=True,
        )

    def test_detail_status_200(self):
        response = self.client.get(reverse("ad_detail", args=[self.ad.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detail_increments_views_for_visitor(self):
        User.objects.create_user(username="visitor", password="pass")
        self.client.login(username="visitor", password="pass")
        self.client.get(reverse("ad_detail", args=[self.ad.pk]))
        self.ad.refresh_from_db()
        self.assertEqual(self.ad.views, 1)

    def test_detail_no_view_increment_for_author(self):
        self.client.login(username="u2", password="pass")
        self.client.get(reverse("ad_detail", args=[self.ad.pk]))
        self.ad.refresh_from_db()
        self.assertEqual(self.ad.views, 0)


class ReviewModelTest(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="reviewer", password="pass")
        self.target = User.objects.create_user(username="seller2", password="pass")

    def test_create_review(self):
        review = Review.objects.create(
            author=self.author,
            target=self.target,
            rating=5,
            text="Good seller",
        )
        self.assertEqual(review.rating, 5)
        self.assertEqual(str(review), "reviewer → seller2")


class FavoriteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="buyer", password="pass")
        self.seller = User.objects.create_user(username="seller3", password="pass")
        self.category = Category.objects.create(name="Raznoe")
        self.ad = Ad.objects.create(
            title="Velosiped",
            price=15000,
            description="Skorostnoy",
            city="Novosibirsk",
            author=self.seller,
            category=self.category,
            is_published=True,
        )

    def test_toggle_favorite_adds(self):
        self.client.login(username="buyer", password="pass")
        self.client.post(reverse("toggle_favorite", args=[self.ad.pk]))
        self.assertTrue(Favorite.objects.filter(user=self.user, ad=self.ad).exists())

    def test_toggle_favorite_removes(self):
        self.client.login(username="buyer", password="pass")
        Favorite.objects.create(user=self.user, ad=self.ad)
        self.client.post(reverse("toggle_favorite", args=[self.ad.pk]))
        self.assertFalse(Favorite.objects.filter(user=self.user, ad=self.ad).exists())
