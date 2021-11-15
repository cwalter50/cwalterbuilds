from django.test import TestCase, Client
from .models import Question, Result, Option, randomCode
import random

# Create your tests here.

# to run tests type 'python3 manage.py test' in terminal

class OrderSorterTestCase(TestCase):

    def setUp(self):
        # Create Question
        q1 = Question.objects.create(question="What is your favorite fruit?", description="listing a bunch of different fruits...", code="AAAAAA")
        
        # Create options
        fruits = ["Apple", "Watermelon", "Strawberry", "Grapes", "Pear", "Plum", "Orange", "Pineapple", "Peach"]
        for fruit in fruits:
            Option.objects.create(question=q1, optionText=fruit)

        #create results
        for i in range(0, 10):
            random.shuffle(fruits)
            Result.objects.create(question=q1, name="Test", order = {'items': fruits})

    def testResultsCount(self):
        q = Question.objects.get(code="AAAAAA")
        self.assertEqual(q.results.count(), 10)

    def test_index(self):
        c = Client()
        # response = c.get("/ordersorter/")
        response = c.get("/ordersorter/")
        # print(response.context)
        # This makes sure that the website loads ok. HTTP 200 means ok
        self.assertEqual(response.status_code, 200)
        # this will test the context that gets passed in from the render
        # print(response.context['questions'])
        # self.assertEqual(response.context['questions'].count(), 1)
        





# These are the tests written for Flight in CS50. Im using them as a template.... Delete after you use them
# from django.db.models import Max
# from django.test import Client, TestCase

# from .models import Airport, Flight, Passenger

# # Create your tests here.
# class FlightTestCase(TestCase):

#     def setUp(self):

#         # Create airports.
#         a1 = Airport.objects.create(code="AAA", city="City A")
#         a2 = Airport.objects.create(code="BBB", city="City B")

#         # Create flights.
#         Flight.objects.create(origin=a1, destination=a2, duration=100)
#         Flight.objects.create(origin=a1, destination=a1, duration=200)
#         Flight.objects.create(origin=a1, destination=a2, duration=-100)

#     def test_departures_count(self):
#         a = Airport.objects.get(code="AAA")
#         self.assertEqual(a.departures.count(), 3)

#     def test_arrivals_count(self):
#         a = Airport.objects.get(code="AAA")
#         self.assertEqual(a.arrivals.count(), 1)

#     def test_valid_flight(self):
#         a1 = Airport.objects.get(code="AAA")
#         a2 = Airport.objects.get(code="BBB")
#         f = Flight.objects.get(origin=a1, destination=a2, duration=100)
#         self.assertTrue(f.is_valid_flight())

#     def test_invalid_flight_destination(self):
#         a1 = Airport.objects.get(code="AAA")
#         f = Flight.objects.get(origin=a1, destination=a1)
#         self.assertFalse(f.is_valid_flight())

#     def test_invalid_flight_duration(self):
#         a1 = Airport.objects.get(code="AAA")
#         a2 = Airport.objects.get(code="BBB")
#         f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
#         self.assertFalse(f.is_valid_flight())

#     def test_index(self):
#         c = Client()
#         response = c.get("/flights/")
#         print(response)
#         # This makes sure that the website loads ok. HTTP 200 means ok
#         self.assertEqual(response.status_code, 200)
#         # this will test the context that gets passed in from the render
#         self.assertEqual(response.context["flights"].count(), 3)

#     def test_valid_flight_page(self):
#         a1 = Airport.objects.get(code="AAA")
#         f = Flight.objects.get(origin=a1, destination=a1)

#         c = Client()
#         response = c.get(f"/flights/{f.id}")
#         self.assertEqual(response.status_code, 200)

#     def test_invalid_flight_page(self):
#         # get the flight with the highest flight_id
#         max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

#         c = Client()
#         # check if a flight that's id is higher than the max id
#         response = c.get(f"/flights/{max_id + 1}")
#         self.assertEqual(response.status_code, 404)

#     def test_flight_page_passengers(self):
#         f = Flight.objects.get(pk=1)
#         p = Passenger.objects.create(first="Alice", last="Adams")
#         f.passengers.add(p)

#         c = Client()
#         response = c.get(f"/flights/{f.id}")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context["passengers"].count(), 1)

#     def test_flight_page_non_passengers(self):
#         f = Flight.objects.get(pk=1)
#         p = Passenger.objects.create(first="Alice", last="Adams")

#         c = Client()
#         response = c.get(f"/flights/{f.id}")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context["non_passengers"].count(), 1)
