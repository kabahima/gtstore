from django.test import TestCase

from accounts.models import CustomUser


class CustomUserAuthTests(TestCase):
    def test_users_can_be_found_by_email_or_phone_number(self):
        user = CustomUser.objects.create_user(
            email='buyer@example.com',
            phone_number='1234567890',
            password='secure-password-123',
            whatsapp_number='1234567890',
        )

        self.assertEqual(CustomUser.objects.get_by_natural_key('buyer@example.com'), user)
        self.assertEqual(CustomUser.objects.get_by_natural_key('1234567890'), user)

    def test_phone_only_user_can_sign_in_with_phone_number(self):
        user = CustomUser.objects.create_user(
            email='',
            phone_number='9876543210',
            password='secure-password-123',
            whatsapp_number='9876543210',
        )

        self.assertEqual(CustomUser.objects.get_by_natural_key('9876543210'), user)
