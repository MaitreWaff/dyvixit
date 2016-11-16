from django.db import models
from time import time
from django.utils import timezone


# Retourne le Nom De l'Image telechargee.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Consultant(models.Model):
    nom             = models.CharField(max_length=128)
    prenom          = models.CharField(max_length=128)
    phone           = models.IntegerField()
    email           = models.EmailField(unique=True)

    class Meta:
        ordering    = ['nom']
	unique_together = ['nom', 'prenom']

    def __unicode__(self):
        return self.nom

class Fournisseur(models.Model):
    compagnie       = models.CharField(max_length=128, unique=True)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField()
    address         = models.TextField()
    
    class Meta:
        ordering    = ['compagnie']
	unique_together = ['compagnie', 'phone', 'address']

    def __unicode__(self):
        return self.compagnie

class Client(models.Model):
    societe         = models.CharField(max_length=128, unique=True)
    phone           = models.IntegerField(unique=True)
    email           = models.EmailField()
    address         = models.TextField()

    class Meta:
        ordering    = ['societe']
	unique_together = ['societe', 'phone', 'address']

    def __unicode__(self):
        return self.societe

class Category(models.Model):
    titre        = models.CharField(max_length=48, unique=True)
    desc         = models.TextField()
    date         = models.DateTimeField('Date Creation', auto_now_add=True) #default=timezone.now)
    photo        = models.FileField(upload_to=get_upload_file_name, blank=True)

    class Meta:
        abstract = True
        ordering = ['titre']

    def __unicode__(self):
        return self.titre

class CategoryProduit(Category):
    pass

class CategoryService(Category):
    pass


class Article(Category):
    link  = models.URLField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return "Article - %s ( %d Likes!)" % (self.titre, self.likes)

class Info(Category):
    link  = models.URLField()
    likes = models.IntegerField(default=0)


    def __unicode__(self):
        return "Information - %s ( %d Likes!)" % (self.titre, self.likes)


class Produit(models.Model):
    libelle         = models.CharField(max_length=128, unique=True)
    desc            = models.TextField()
    category        = models.ForeignKey(CategoryProduit)
    prix_unitaire   = models.IntegerField()
    quantite        = models.IntegerField(default=100)
    fournisseur     = models.ForeignKey(Fournisseur)
    photo           = models.FileField(upload_to=get_upload_file_name, blank=True)
    date            = models.DateTimeField('Date De Creation du Produit', auto_now_add=True) #default=timezone.now)

    class Meta:
        ordering    = ['libelle']
	unique_together = ['libelle', 'fournisseur']

    def __unicode__(self):
        return self.libelle

class Service(models.Model):
    nom             = models.CharField(max_length=128, unique=True)
    desc            = models.TextField()
    type            = models.ForeignKey(CategoryService)
    prix            = models.IntegerField()
    consultant      = models.ForeignKey(Consultant) #ManyToManyField(Consultant)
    photo           = models.FileField(upload_to=get_upload_file_name, blank=True)
    date            = models.DateTimeField('Date Creation du Service', auto_now_add=True) #default=timezone.now)


    class Meta:
        ordering    = ['nom']
	unique_together = ['nom', 'type', 'prix']

    def __unicode__(self):
        return self.nom

class Commande(models.Model):
    #numero_reference = models.AutoField()
    client           = models.ForeignKey(Client)
    quantite         = models.IntegerField(default=1)
    produit          = models.ForeignKey(Produit)
    service          = models.ForeignKey(Service)
    date             = models.DateTimeField('Date De Commande', auto_now_add=True) #default=timezone.now)

    class Meta:
        ordering     = ['date']

    #def __unicode__(self):
        #return self.numero_reference

class Facture(models.Model):
    commande     = models.OneToOneField(Commande)
    date         = models.DateTimeField('Date De Validation De La Commande', auto_now_add=True) #default=timezone.now)
    #total       = models.IntegerField()

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return self.commande

class Like(models.Model):
    liker        = models.URLField()
    date         = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

class LikeArticle(Like):
    ref_like = models.ForeignKey(Article) # Article du Like


class LikeInfo(Like):
    ref_like = models.ForeignKey(Info) # Info du Like


class LikeProduit(Like):
    ref_like = models.ForeignKey(Produit) # Produit du Like


class LikeService(Like):
    ref_like = models.ForeignKey(Service) # Service du Like

