from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404


from apps.group.models import Group
from apps.student.models import Student
from apps.utils.upload import PathAndRename


VISIBILITY = [
    ('Pub', 'Public - Visible par tous'),
    ('Mem', 'Membres - Visible uniquement par les membres du groupe')
]

COLORS = [
    ('primary', 'Bleu'),
    ('success', 'Vert'),
    ('danger', 'Rouge'),
    ('warning', 'Jaune'),
    ('secondary', 'Gris'),
    ('dark', 'Noir')
]

path_and_rename = PathAndRename("events/pictures")


class BaseEvent(models.Model):
    """
    A basic event model for groups
    """
    date = models.DateTimeField(verbose_name='Date de l\'événement')
    title = models.CharField(
        max_length=200, verbose_name='Titre de l\'événement')
    description = models.TextField(verbose_name='Description de l\'événement')
    location = models.CharField(max_length=200, verbose_name='Lieu')
    publicity = models.CharField(
        max_length=200, verbose_name='Visibilité de l\'événement', choices=VISIBILITY)
    group = models.SlugField(verbose_name='Groupe organisateur')
    slug = models.SlugField(
        verbose_name='Slug de l\'événement', unique=True, null=True)
    participants = models.ManyToManyField(
        to=Student, verbose_name='Participants', blank=True)
    ticketing = models.CharField(
        verbose_name='Lien vers la billeterie', blank=True, max_length=200, null=True)
    image = models.ImageField(verbose_name="Une image, une affiche en lien avec l'evenement ?",
                              upload_to=path_and_rename, null=True, blank=True)
    color = models.CharField(max_length=200, verbose_name='Couleur de fond',
                             choices=COLORS, null=True, default='primary')

    @property
    def get_group(self):
        return Group.get_group_by_slug(self.group)

    @property
    def get_number_participants(self) -> int:
        return self.participants.all().count()

    def is_participating(self, user: User) -> bool:
        student = Student.objects.filter(user=user).first()
        return student in self.participants.all()

    def save(self, *args, **kwargs):
        self.slug = f'bevent--{slugify(self.title)}-{self.date.year}-{self.date.month}-{self.date.day}'
        super(BaseEvent, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event:detail', args=[self.slug])

    @staticmethod
    def get_event_by_slug(slug: str):
        type_slug = slug.split('--')[0]
        if type_slug == 'bevent':
            return get_object_or_404(BaseEvent, slug=slug)
        elif type_slug == 'eevent':
            return EatingEvent.objects.get(slug=slug)


class EatingEvent(BaseEvent):
    """
    Events that features meals.
    They can show a menu, ask people about their eating habbits...
    """
    menu = models.TextField(verbose_name='Menu de l\'événement')

    def save(self, *args, **kwargs):
        self.slug = f'eevent--{slugify(self.title)}'
        super(EatingEvent, self).save(*args, **kwargs)
