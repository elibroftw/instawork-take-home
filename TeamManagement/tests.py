from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
from .models import TeamMember


class TeamMemberViewTests(TestCase):
    def test_list_ok(self):
        response = self.client.get(reverse(('TeamManagement:index')))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have 0 team members.')

    def test_add_ok(self):
        response = self.client.get(reverse(('TeamManagement:add-member')))
        self.assertEqual(response.status_code, 200)

    def test_edit_ok(self):
        TeamMember.objects.create(first_name="Pablo", last_name="Escobar", email="pabloescobar@gmail.com", phone_number="5062345678", role="ADMIN")
        response = self.client.get(reverse('TeamManagement:edit-member', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_members_exist_in_list(self):
        TeamMember.objects.create(first_name="Pablo", last_name="Escobar", email="pabloescobar@gmail.com", phone_number="5062345678", role="ADMIN")
        response = self.client.get(reverse(('TeamManagement:index')))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have 1 team members.')
