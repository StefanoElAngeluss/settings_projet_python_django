from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):

  options = (
    ("brouillon", "Brouillon"),
    ("publier", "Publié"),
  )

  titre = models.CharField(max_length=255)
  sous_titre = models.CharField(max_length=100)
  # image = models.ImageField(upload_to="blog/images/", null=True, blank=True)
  slug = models.SlugField(max_length=255, unique=True)
  auteur = models.ForeignKey(
    User, on_delete=models.CASCADE,
    related_name="article_auteur"
  )
  contenu = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=10, choices=options, default="draft")

  class Meta:
    ordering = ("-created_at",)

  def __str__(self):
    return self.titre
