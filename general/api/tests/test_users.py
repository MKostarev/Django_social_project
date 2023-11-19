from rest_framework import status
from rest_framework.test import APITestCase
from general.factories import UserFactory
import json
import time


class UserTestCase(APITestCase):
    #def setUp(self):
    #    print("Запуск метода setUp")
    #    self.user = UserFactory()
    #    print(f"username: {self.user.username}\n")
    #    self.client.force_authenticate(user=self.user)
    #    self.url = "/api/users/"
    #    time.sleep(1)


    def test_user_list(self):
        print("Запуск метода test_user_list")
        time.sleep(1)
        UserFactory.create_batch(20)
        response = self.client.get(path=self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.data["count"], 21)
        time.sleep(1)

    time.sleep(1)
#
#
   # def test_user_list_response_structure(self):
   #     print("Запуск метода test_user_list_response_structure")
   #     time.sleep(1)
   #     response = self.client.get(path=self.url, format="json")
   #     time.sleep(1)
   #     print("response")
   #     time.sleep(1)
   #     self.assertEqual(response.status_code, status.HTTP_200_OK)
   #     print("assertEqual")
   #     time.sleep(1)
   #     self.assertEqual(len(response.data["results"]), 1)
   #     print("assertEqual")
   #     time.sleep(1)
#
#
#
   #     expected_data = {
   #         "id": self.user.pk,
   #         "first_name": self.user.first_name,
   #         "last_name": self.user.last_name,
   #         "is_friend": False,
   #     }
   #     print("expected_data")
   #     time.sleep(1)
   #     self.assertDictEqual(response.data["results"][0], expected_data)
   #     time.sleep(1)
   #     print("конец test_user_list_response_structure")
   #     time.sleep(1)
#
    #def test_user_list_is_friend_field(self):
    #    # проверяем значение поля `is_friend`
    #    users = UserFactory.create_batch(5)
#
    #    self.user.friends.add(users[-1])
    #    self.user.save()
#
    #    response = self.client.get(path=self.url, format="json")
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.assertEqual(len(response.data["results"]), 6)
#
    #    self.assertTrue(response.data["results"][0]["is_friend"])
    #    self.assertFalse(response.data["results"][1]["is_friend"])
    #    self.assertFalse(response.data["results"][2]["is_friend"])
    #    self.assertFalse(response.data["results"][3]["is_friend"])
    #    self.assertFalse(response.data["results"][4]["is_friend"])
    #    self.assertFalse(response.data["results"][5]["is_friend"])
   ##     time.sleep(1)
##




