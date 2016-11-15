import os

list_cat_prod = ['Ecrans', 'Claviers', 'Souris', 'Unites Centrales', 'Imprimantes', 'Switches', 'Routeurs', 'Tablettes', 'Telephones']
list_cat_serv = ['Reseaux', 'Programmation', 'DataBases', 'Systemes', 'Securite', 'Cloud', 'Clusters', 'Virtualisation', 'Telephonie', 'Telephonie sur IP']

def populate():
    #from datetime import datetime
    #from django.utils import timezone


    ecran_cat      = add_cat_produit('Ecrans', 'ECRANS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    clavier_cat    = add_cat_produit('Claviers', 'CLAVIERS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    souris_cat     = add_cat_produit('Souris', 'SOURIS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    uc_cat         = add_cat_produit('Unites Centrales', 'UNITES CENTRALES -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    imprimante_cat = add_cat_produit('Imprimantes', 'IMPRIMANTE -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    switch_cat     = add_cat_produit('Switches', 'SWITCHES  -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    routeur_cat    = add_cat_produit('Routeurs', 'ROUTEURS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    tablette_cat   = add_cat_produit('Tablettes', 'TABLETTES -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    telephone_cat  = add_cat_produit('Telephones', 'TELEPHONES -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')



    windows_cat    = add_cat_produit('Windows', 'WINDOWS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    unix_cat       = add_cat_produit('Unix', 'UNIX -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    linux_cat      = add_cat_produit('Linux', 'LINUX -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    osx_cat        = add_cat_produit('OS X', 'OSX -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')



    reseau_cat          = add_cat_service('Reseaux', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    progra_cat          = add_cat_service('Programmation', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    database_cat        = add_cat_service('DataBase', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    securite_cat        = add_cat_service('Securite', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    system_cat          = add_cat_service('Systeme', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    cloud_cat           = add_cat_service('Systeme', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    cluster_cat         = add_cat_service('Cluster', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    virtualisation_cat  = add_cat_service('Virtualisation', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    telephonie_cat      = add_cat_service('Telephonie', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    telephoniesurip_cat = add_cat_service('Telephonie sur IP', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')





    add_article('Article Premier', 'http://www.premier.com', 'ARTICLE PREMIER -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    add_article('Article Deuxieme', 'http://www.deuxieme.com', 'ARTICLE DEUXIEME -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    add_article('Article Troisieme', 'http://www.troisieme.com', 'ARTICLE TROISIEME -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    add_info('Info Un', 'http://www.un.com', 'INFORMATION UN -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    add_info('Info Deux', 'http://www.deux.com', 'INFORMATION DEUX -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    add_info('Info Trois', 'http://www.trois.com', 'INFORMATION TROIS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')

    Hp_four      = add_fournisseur(compagnie="HP", 
    phone="97164538463", 
    email="hp@hp.com", 
    address="HP Houston")
    Dell_four    = add_fournisseur(compagnie="Dell", 
    phone="97164426353", 
    email="dell@dell.com", 
    address="Dell Abu Dhabi")
    Mac_four     = add_fournisseur(compagnie="Machintosh", 
    phone="97152423373", 
    email="machintosh@mac.com", 
    address="Machintosh Denver")
    Azus_four    = add_fournisseur(compagnie="Azus", 
    phone="97163543422", 
    email="azus@azus.com", 
    address="Azus Paris")
    Toshiba_four = add_fournisseur(compagnie="Toshiba", 
    phone="97156339262", 
    email="toshiba@toshiba.com", 
    address="Toshiba Tokyo")
    Cisco_four = add_fournisseur(compagnie="Cisco", 
    phone="97153945262", 
    email="cisco@cisco.com", 
    address="Cisco Us, Atlanta DC")

    ec_hp_prod = add_produit(lib="Ecran HP",
    cat=ecran_cat, 
    prix_u="15000", 
    qte="110", 
    four=Hp_four)
    ec_dell_prod = add_produit(lib="Ecran Del",
    cat=ecran_cat, 
    prix_u="17000", 
    qte="130", 
    four=Dell_four)
    uc_toshiba_prod = add_produit(lib="UC Toshiba",
    cat=uc_cat, 
    prix_u="45000", 
    qte="40", 
    four=Toshiba_four)
    uc_azus_prod = add_produit(lib="UC Azus",
    cat=uc_cat, 
    prix_u="45000", 
    qte="200", 
    four=Azus_four)
    cl_hp_prod = add_produit(lib="Clavier HP",
    cat=clavier_cat, 
    prix_u="5000", 
    qte="20", 
    four=Hp_four)
    cl_dell_prod = add_produit(lib="Clavier Dell",
    cat=clavier_cat, 
    prix_u="5000", 
    qte="20", 
    four=Dell_four)
    sr_mac_prod = add_produit(lib="Souris Mac",
    cat=souris_cat, 
    prix_u="2500", 
    qte="299", 
    four=Mac_four)
    sr_dell_prod = add_produit(lib="Souris Dell",
    cat=souris_cat, 
    prix_u="2500", 
    qte="299", 
    four=Dell_four)
    sw_cisco_prod = add_produit(lib="Switch Cisco",
    cat=switch_cat, 
    prix_u="210000", 
    qte="347", 
    four=Cisco_four)

    waffo_cons     = add_consultant(nom="Waffo",
    prenom="Luc",
    phone="699581262", 
    email="waffoluc@gmail.com")
    wouleu_cons   = add_consultant(nom="Wouleu", 
    prenom="Franklin", 
    phone="696241088", 
    email="wouleuf@gmail.com")
    feugwang_cons = add_consultant(nom="Feugwang", 
    prenom="Valere", 
    phone="699580265", 
    email="v.feugwang@gmail.com")
    fotso_cons    = add_consultant(nom="Fotso", 
    prenom="Valere", 
    phone="699450688", 
    email="valere.fotso@gmail.com")
    tata_cons     = add_consultant(nom="Tata", 
    prenom="Kim", 
    phone="699775522", 
    email="tata.kimbanz@gmail.com")

    progra_c_svc = add_service(nom="Programmation C", 
    type=progra_cat, 
    prix="50000", 
    cons=waffo_cons)
    progra_python_svc = add_service(nom="Programmation Python", 
    type=progra_cat, 
    prix="150000", 
    cons=waffo_cons)
    progra_django_svc = add_service(nom="Programmation Web Avec Django", 
    type=progra_cat, 
    prix="250000", 
    cons=waffo_cons)
    progra_php_svc = add_service(nom="Programmation PHP", 
    type=progra_cat, 
    prix="750000", 
    cons=wouleu_cons)
    reseau_install_svc = add_service(nom="Installation Reseau", 
    type=reseau_cat, 
    prix="250000", 
    cons=fotso_cons)
    reseau_depann_svc = add_service(nom="Depannage Reseau", 
    type=reseau_cat, 
    prix="20000", 
    cons=fotso_cons)

    alan_and_steve  = add_client(societe="Ets Alan And Steve", 
    phone="699127737", 
    email="alan_and_steve@yahoo.fr", 
    address="Cite Verte G31")
    koryn_and_nancy = add_client(societe="Koryn Nancy", 
    phone="699374736", 
    email="koryn_and_nancy@yahoo.fr", 
    address="Cite Verte H52")
    fokou           = add_client(societe="Ets Fokou", 
    phone="699735338", 
    email="fokou@yahoo.fr", 
    address="Mokolo en bas")
    nziko           = add_client(societe="Ets Nziko", 
    phone="699669900", 
    email="nziko@yahoo.fr", 
    address="Bertoua")

    nziko_cmd = add_command(cli=nziko, 
    qte="12", 
    prod=ec_hp_prod, 
    serv=progra_c_svc,)
    fokou_cmd = add_command(cli=fokou, 
    qte="15", 
    prod=ec_dell_prod, 
    serv=progra_c_svc,)


    nziko_facture = add_facture(com=nziko_cmd)
    fokou_facture = add_facture(com=fokou_cmd)

    print "Liste Des Donnes Dans la BD:"
    print "Liste Des Clients:"
    for c in Client.objects.all():
        print c
    print "Liste Des Fournisseurs:"
    for f in Fournisseur.objects.all():
        print f
    print "Liste Des Consultants"
    for c in Consultant.objects.all():
        print c

    print "Liste Des Produits Par Categories"
    for c in CategoryProduit.objects.all():
        for p in Produit.objects.filter(category=c):
	    print "[+] Produit: {0} ( Category: {1} ) --".format(str(p), str(c))

    print "Liste Des Services Par Categories"
    for c in CategoryService.objects.all():
        for s in Service.objects.filter(type=c):
	    print "[+] Service: {0} ( Type: {1} ) --".format(str(s), str(c))

    #print "Liste Des "

def add_cat_produit(titre, desc):
    c_p = CategoryProduit.objects.get_or_create(titre=titre, desc=desc)[0]
    return c_p

def add_cat_service(titre, desc):
    c_s = CategoryService.objects.get_or_create(titre=titre, desc=desc)[0]
    return c_s

def add_article(titre, link, desc):
    c_s = Article.objects.get_or_create(titre=titre, link=link, desc=desc)[0]
    return c_s

def add_info(titre, link, desc):
    c_s = Info.objects.get_or_create(titre=titre, link=link, desc=desc)[0]
    return c_s

def add_fournisseur(compagnie, phone, email, address):
    f = Fournisseur.objects.get_or_create(compagnie=compagnie, phone=phone, email=email, address=address)[0]
    return f

def add_client(societe, phone, email, address):
    c = Client.objects.get_or_create(societe=societe, phone=phone, email=email, address=address)[0]
    return c

def add_consultant(nom, prenom, phone, email):
    c = Consultant.objects.get_or_create(nom=nom, prenom=prenom, phone=phone, email=email)[0]
    return c

def add_produit(lib, cat, prix_u, qte, four):
    p = Produit.objects.get_or_create(libelle=lib, category=cat, prix_unitaire=prix_u, quantite=qte, fournisseur=four)[0]
    return p

def add_service(nom, type, prix, cons):
    s = Service.objects.get_or_create(nom=nom, type=type, prix=prix, consultant=cons)[0]
    return s

def add_command(cli, qte, prod, serv):
    c = Commande.objects.get_or_create(client=cli, quantite=qte, produit=prod, service=serv)[0]
    return c

def add_facture(com):
    f = Facture.objects.get_or_create(commande=com)[0]
    return f

if __name__ == '__main__':
    print "Starting DyvixIT Population Script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','dyvixproject.settings')
    from dyvixitsolutions.models import Fournisseur, Client, Consultant, CategoryProduit, CategoryService, Article, Info, Produit, Service, Commande, Facture
    populate()
