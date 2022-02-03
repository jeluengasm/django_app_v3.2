from django.db import models

class User(models.Model):
    """Model definition of user"""
    first_name = models.CharField("First name", max_length=100)
    last_name  = models.CharField("Last name", max_length=100)
    email      = models.EmailField("E-mail address", max_length=254)
    resume     = models.FileField("CV", null=True, upload_to='uploads/', max_length=100)
    image      = models.ImageField("Profile photo", upload_to='images/', height_field=None, width_field=None, max_length=None)
    headline   = models.CharField("About", max_length=50)
    location   = models.CharField("Location", max_length=50)

    def __str__(self):
        """Unicode representation of User."""
        return f"{self.first_name} {self.last_name}"

class Education(models.Model):
    """Model definition for Education."""
    institution = models.CharField("School/Institution", max_length=100)
    degree      = models.CharField("", max_length=50)
    start_date  = models.DateTimeField("Start date")
    end_date    = models.DateTimeField("End date")
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Unicode representation of Education."""
        return self.institution

class JobSkills(models.Model):
    """Model definition for JobSkills."""
    skill = models.CharField("Skill", max_length=70, unique=True)

    def __str__(self):
        """Unicode representation of JobSkills."""
        return self.skill

class Experience(models.Model):
    """Model definition for Experience."""
    company    = models.CharField("Company", max_length=50) 
    job_title  = models.CharField("Job title", max_length=50) 
    localtion  = models.CharField("Location", max_length=50) 
    start_date = models.DateTimeField("Start date")
    end_date   = models.DateTimeField("End date")
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    skills     = models.ManyToManyField(JobSkills, blank=True)

    def __str__(self):
        """Unicode representation of Experience."""
        return f"{self.job_title} - {self.company}"


