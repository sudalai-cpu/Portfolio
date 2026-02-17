from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100)
    header_title = models.CharField(max_length=100, default="Sudalaiyandi", help_text="Text to display in the header/navigation bar")
    greetings_text = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=200, default="I am a Full Stack Developer")
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/')
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    # Social Media & Contact Info
    email_address = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True, help_text="Link to your GitHub profile")
    about_summary = models.TextField(max_length=500, blank=True, null=True, help_text="A quick 2-line bio for the About page")

    def __str__(self):
        return self.name

class AboutSection(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    points = models.TextField(help_text="Enter bullet points separated by a new line or pipe |")
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class (e.g., 'fas fa-code')")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.heading

    def get_points(self):
        if "|" in self.points:
            return [p.strip() for p in self.points.split("|") if p.strip()]
        return [p.strip() for p in self.points.split("\n") if p.strip()]

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Normalize to Title Case (e.g., 'frontend' -> 'Frontend')
        self.name = self.name.title().strip()
        super().save(*args, **kwargs)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
