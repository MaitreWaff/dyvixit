from django.db import models

# Create your models here.
class Consultant(models.Model):
    nom     = models.CharField(max_length=128)
    prenom  = models.CharField(max_length=128)
    phone   = models.IntegerField()
    email   = models.EmailField(unique=True)

    class Meta:
        ordering = ['nom']
	unique_together = ['nom', 'prenom']

    def __unicode__(self):
        return self.nom

class Fournisseur(models.Model):
    compagnie = models.CharField(max_length=128, unique=True)
    phone     = models.IntegerField(unique=True)
    email     = models.EmailField()
    address   = models.TextField()
    
    class Meta:
        ordering = ['compagnie']
	unique_together = ['compagnie', 'phone', 'address']

    def __unicode__(self):
        return self.compagnie

class Client(models.Model):
    societe = models.CharField(max_length=128, unique=True)
    phone   = models.IntegerField(unique=True)
    email   = models.EmailField()
    address = models.TextField()

    class Meta:
        ordering = ['societe']
	unique_together = ['societe', 'phone', 'address']

    def __unicode__(self):
        return self.societe

class Category(models.Model):
    title = models.CharField(max_length=48, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

class CategoryProduit(Category):
    pass

class CategoryService(Category):
    pass

class Produit(models.Model):
    libelle       = models.CharField(max_length=128, unique=True)
    category      = models.ForeignKey(CategoryProduit)
    prix_unitaire = models.IntegerField()
    quantite      = models.IntegerField(default=100)
    fournisseur   = models.ForeignKey(Fournisseur)

    class Meta:
        ordering = ['libelle']
	unique_together = ['libelle', 'fournisseur']

    def __unicode__(self):
        return self.libelle

class Service(models.Model):
    nom        = models.CharField(max_length=128, unique=True)
    type       = models.ForeignKey(CategoryService)
    prix       = models.IntegerField()
    consultant = models.ForeignKey(Consultant) #ManyToManyField(Consultant)

    class Meta:
        ordering = ['nom']
	unique_together = ['nom', 'type', 'prix']

    def __unicode__(self):
        return self.nom

class Commande(models.Model):
    #numero_reference = models.AutoField()
    client           = models.ForeignKey(Client)
    quantite         = models.IntegerField(default=1)
    produit          = models.ForeignKey(Produit)
    service          = models.ForeignKey(Service)
    date_command     = models.DateTimeField('Date De Commande')

    class Meta:
        ordering = ['date_command']

    #def __unicode__(self):
        #return self.numero_reference

class Facture(models.Model):
    commande        = models.OneToOneField(Commande)
    date_validation = models.DateTimeField('Date De Validation De La Commande')
    #total           = models.IntegerField()

    class Meta:
        ordering = ['date_validation']

    def __unicode__(self):
        return self.commande
