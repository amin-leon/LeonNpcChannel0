from django.db import models
from datetime import datetime


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sex = models.CharField(blank=True, null=True, default='None',
                           max_length=20,
                           choices=[('Male', 'Male'), ('Female', 'Female')]
                           )
    profile_pic = models.ImageField(null=True, default='profile.png')
    police_number = models.IntegerField(null=True)
    rank = models.CharField(max_length=20)
    telephone = models.IntegerField(null=True)
    faculty = models.CharField(blank=True, null=True, default='None',
                               max_length=20,
                               choices=[(' Modern Languages', 'Modern Languages'), ('Ict', 'Ict'),
                                        ('PPS', 'PPS'), ('Law', 'Law')])
    level = models.CharField(blank=True, null=True, default='None',
                             max_length=20,
                             choices=[(' Level I', 'Level I'), ('Level II', 'Level II'),
                                      ('Level III', 'Level III'), ('IV', 'Level IV')])
    registration_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=254, default='example@gmail.com')
    password = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.id}"


class Leader(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sex = models.CharField(blank=True, null=True, default='None',
                           max_length=20,
                           choices=[('Male', 'Male'), ('Female', 'Female')]
                           )
    profile_pic = models.ImageField(null=True, default='profile.png')
    police_number = models.IntegerField(null=True)
    rank = models.CharField(max_length=20)
    telephone = models.IntegerField(null=True)
    position = models.CharField(blank=True, null=True, default='None',
                                max_length=20,
                                choices=[(' OIC', 'OIC'), ('CI', 'CI'),
                                         ('Academic staff', 'Academic staff'), ('IO', 'IO')])

    registration_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.id}"


class Issue(models.Model):
    student_id = models.ForeignKey('Student', null=False, related_name='sender_id', on_delete=models.CASCADE)
    leader_id = models.ForeignKey('Leader', null=False, related_name='receiver_id', on_delete=models.CASCADE)
    issue_desc = models.TextField()
    sub_date = models.DateTimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.leader_id


class Annoucement(models.Model):
    leader_id = models.ForeignKey('Leader', null=False, related_name='leader_id', on_delete=models.CASCADE)
    annoucementTitle = models.CharField(max_length=100)
    anouncement_desc = models.TextField()
    announceDesc = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.leader_id}"


class comment(models.Model):
    issue_id = models.ForeignKey('Issue', null=False, related_name='issue_id', on_delete=models.CASCADE)
    leader_id = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200, default="ICT")
    desc = models.TextField()
    commentTime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.issue_id
