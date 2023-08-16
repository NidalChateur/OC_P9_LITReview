from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

FULL_STAR = "★"
EMPTY_STAR = "☆"


class Ticket(models.Model):
    """fields of the book or article."""

    title = models.CharField(
        max_length=128,
        verbose_name="Titre",
    )
    description = models.TextField(max_length=2048, blank=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(null=True)
    time_edited = models.DateTimeField(null=True, blank=True)
    time_last_entry = models.DateTimeField(null=True)
    slug = models.SlugField(max_length=128, null=True)

    def __str__(self):
        return f"{self.title}"

    def resize_image(self):
        pass

    def save(self, *args, **kwargs):
        # modification time
        if self.time_created:
            self.time_edited = self.time_last_entry = timezone.now()

        # creation time
        if not self.time_created:
            self.time_created = self.time_last_entry = timezone.now()

        self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Review(models.Model):
    """fields of the review.
    If the author of the ticket and the review are the same : it is a self_review ! """

    rating = models.IntegerField(
        verbose_name="Note",
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
    )
    star = models.CharField(null=True, max_length=5)
    headline = models.CharField(max_length=128, verbose_name="Intitulé", null=True)
    body = models.TextField(
        max_length=8192, verbose_name="Commentaire", blank=True, null=True
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    time_created = models.DateTimeField(null=True)
    time_edited = models.DateTimeField(null=True, blank=True)
    time_last_entry = models.DateTimeField(auto_now_add=True, null=True)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True)
    is_self_review = models.BooleanField(default=False)
    self_review = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True)

    def set_null(self, *args, **kwargs):
        """erase the tierce review"""

        self.user = None
        self.rating = None
        self.star = None
        self.headline = None
        self.body = None
        self.time_created = None
        self.time_edited = None
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.time_last_entry = timezone.now()
        # modification time
        if self.user and self.time_created:
            self.time_edited = timezone.now()

        # creation time
        if self.user and not self.time_created:
            self.time_created = timezone.now()

        # star field
        if self.user:
            self.star = self.rating * FULL_STAR + (5 - self.rating) * EMPTY_STAR

        if self.user == self.ticket.user:
            self.is_self_review = True

        super().save(*args, **kwargs)


class Relation(models.Model):
    """offer users the ability to follow or block other users"""

    # user_1 can follow or block user_2
    user_1 = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower"
    )
    # user_2 can followed or blocked by user_1
    user_2 = models.ForeignKey(
        verbose_name="Nom d'utilisateur",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed",
    )
    # type of the relation : 'follows' or 'blocks'
    type = models.CharField(
        max_length=128,
        null=True,
        choices=(
            ("blocks", "blocks"),
            ("follows", "follows"),
        ),
    )
    description = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = (
            "user_1",
            "user_2",
        )

    def save(self, *args, **kwargs):
        self.description = f"{str(self.user_1).capitalize()} {self.type} {str(self.user_2).capitalize()}"
        super().save(*args, **kwargs)
