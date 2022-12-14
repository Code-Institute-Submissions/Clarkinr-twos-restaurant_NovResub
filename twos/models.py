"""
models to be used
"""
from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Pending"), (1, "Approved"))

'''defines the time slots available each day.'''
TIME_SLOTS = (
    ('18:00', '18:00'),
    ('20:30', '20:30'),
)
'''defines a number of people which can
be selected for the party size in the booking model'''
NUM_PEOPLE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


class Booking(models.Model):
    '''
    Model for the information to be stored about each booking
    and so users can create and update bookings
    '''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_book"
        )
    first_name = models.TextField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(null=True, blank=True)
    party_size = models.CharField(
        max_length=1, choices=NUM_PEOPLE, default='1'
        )
    reservation_time = models.CharField(
        max_length=10, choices=TIME_SLOTS, default="18:00"
        )
    booking_date = models.DateField()
    Status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()

    class Meta:
        """
        orders all created bookings by booking date
        """
        ordering = ["-booking_date"]

    def __str__(self):
        return str(self.first_name)


class Feedback(models.Model):
    '''
    Model created so that users can provide feedback
    This model is used with the FeedbackList view in order to
    display customer feedback on the homepage
    '''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_feedback"
        )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    comment = models.TextField(max_length=350)
    feedback_made = models.DateTimeField(auto_now=True)
    Status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()

    class Meta:
        ''' Determines the order feedback
        shows up on page from newest to oldest
        '''

        ordering = ["-feedback_made"]
