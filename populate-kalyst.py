import os

list_cat_prod = ['Ecrans', 'Claviers', 'Souris', 'Unites Centrales', 'Imprimantes', 'Switches', 'Routeurs', 'Tablettes', 'Telephones']
list_cat_serv = ['Services Informatiques', 'Telephonie', 'Materiel & Reseaux', 'Solutions Hebergees', 'Logiciel Sur Mesure']

def populate():
    #from datetime import datetime
    #from django.utils import timezone



    reseau_cat    = add_cat_materiel('Equipement Reseau', ' -- Equipement reseau passif (cables, prises, panneaux de brassage, armoire reseau, ...) et actif (switch, routeur, firewall, ...)')
    electrique_cat       = add_cat_materiel('Equipement electrique (PDU, onduleur, ...)', 'UNIX Equipement electrique (PDU, onduleur, ...)')
    monitoring_cat      = add_cat_materiel('Monitoring (sonde, capteur, ...)', 'LINUX  Monitoring (sonde, capteur, ...)')
    imprimente_cat        = add_cat_materiel('Imprimante, copieur, fax', 'OSX  Imprimante, copieur, fax -- ')
    pcfixe_cat        = add_cat_materiel('PC fixe', ' PC fixe -- ')
    pcportable_cat        = add_cat_materiel('PC portable', 'PC portable -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    serveur_cat        = add_cat_materiel('Serveur', 'Serveur -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    sauvegarde_cat        = add_cat_materiel('Materiel de sauvegarde (NAS, SAN, DAT, ...)', 'Materiel de sauvegarde (NAS, SAN, DAT, ...) --')



    progra_cat          = add_cat_service('Programmation', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    database_cat        = add_cat_service('DataBase', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    securite_cat        = add_cat_service('Securite', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    system_cat          = add_cat_service('Systeme', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    cloud_cat           = add_cat_service('Systeme', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    cluster_cat         = add_cat_service('Cluster', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    virtualisation_cat  = add_cat_service('Virtualisation', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    telephonie_cat      = add_cat_service('Telephonie', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    telephoniesurip_cat = add_cat_service('Telephonie sur IP', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')





    art_un    = add_astuce('Article Premier', 'http://www.premier.com', 'ARTICLE PREMIER -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    art_deux  = add_astuce('Article Deuxieme', 'http://www.deuxieme.com', 'ARTICLE DEUXIEME -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    art_trois = add_astuce('Article Troisieme', 'http://www.troisieme.com', 'ARTICLE TROISIEME -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')

    add_like_astuce('https://www.facebook.com/maitre.waff', art_un)
    add_like_astuce('https://www.facebook.com/maitre.waff', art_deux)

    inf_un    = add_info('Info Un', 'http://www.un.com', 'INFORMATION UN -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    inf_deux  = add_info('Info Deux', 'http://www.deux.com', 'INFORMATION DEUX -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')
    inf_trois = add_info('Info Trois', 'http://www.trois.com', 'INFORMATION TROIS -- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.')

    add_like_info('https://www.facebook.com/maitre.waff', inf_deux)
    add_like_info('https://www.facebook.com/maitre.waff', inf_trois)







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



    ec_hp_prod = add_materiel(lib="Ecran HP",
    cat=pcfixe_cat,
    desc= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="15000", 
    qte="110", 
    four=Hp_four)
    ec_dell_prod = add_materiel(lib="Ecran Del",
    cat=pcfixe_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="17000", 
    qte="130", 
    four=Dell_four)
    uc_toshiba_prod = add_materiel(lib="UC Toshiba",
    cat=pcportable_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="45000", 
    qte="40", 
    four=Toshiba_four)
    uc_azus_prod = add_materiel(lib="UC Azus",
    cat=reseau_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="45000", 
    qte="200", 
    four=Azus_four)
    cl_hp_prod = add_materiel(lib="Serveurs HP Pavillon",
    cat=serveur_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="250000",
    qte="20", 
    four=Hp_four)
    cl_dell_prod = add_materiel(lib="Clavier Dell",
    cat=imprimente_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="5000",
    qte="20", 
    four=Dell_four)
    sr_mac_prod = add_materiel(lib="Souris Mac",
    cat=reseau_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="2500",
    qte="299", 
    four=Mac_four)
    sr_dell_prod = add_materiel(lib="Souris Dell",
    cat=imprimente_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix_u="2500",
    qte="299", 
    four=Dell_four)
    sw_cisco_prod = add_materiel(lib="Switch Cisco",
    cat=reseau_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
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
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="50000",
    cons=waffo_cons)
    progra_python_svc = add_service(nom="Programmation Python", 
    type=progra_cat, 
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="150000",
    cons=waffo_cons)
    progra_django_svc = add_service(nom="Programmation Web Avec Django", 
    type=progra_cat, 
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="250000",
    cons=waffo_cons)
    progra_php_svc = add_service(nom="Programmation PHP", 
    type=progra_cat, 
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="750000",
    cons=wouleu_cons)
    reseau_install_svc = add_service(nom="Installation Reseau", 
    type=cluster_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
    prix="250000",
    cons=fotso_cons)
    reseau_depann_svc = add_service(nom="Depannage Reseau", 
    type=cloud_cat,
    desc="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus optio beatae iste architecto, laudantium eaque perferendis fugit quae iure voluptate quaerat! Molestias atque ea, accusamus aliquid dolorum omnis esse neque.",
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


    nziko_facture = add_facture(nziko)

    add_ligne_command_materiel(cli=nziko, qte="3", prod=uc_toshiba_prod, fact=nziko_facture)
    add_ligne_command_materiel(cli=nziko, qte="8", prod=sr_dell_prod, fact=nziko_facture)
    add_ligne_command_materiel(cli=nziko, qte="17", prod=uc_toshiba_prod, fact=nziko_facture)
    add_ligne_command_materiel(cli=nziko, qte="9", prod=sw_cisco_prod, fact=nziko_facture)

    fokou_facture = add_facture(fokou)
    add_ligne_command_materiel(cli=fokou, qte="3", prod=sr_dell_prod, fact=fokou_facture)
    add_ligne_command_service(cli=fokou, qte="8", cat=progra_python_svc, fact=fokou_facture)
    add_ligne_command_materiel(cli=fokou, qte="17", prod=uc_toshiba_prod, fact=fokou_facture)
    add_ligne_command_service(cli=fokou, qte="9", cat=progra_c_svc, fact=fokou_facture)




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
    for c in CategoryMateriel.objects.all():
        for p in Materiel.objects.filter(category=c):
	        print "[+] Produit: {0} ( Category: {1} ) --".format(str(p), str(c))

    print "Liste Des Services Par Categories"
    for c in CategoryService.objects.all():
        for s in Service.objects.filter(category=c):
	        print "[+] Service: {0} ( Type: {1} ) --".format(str(s), str(c))

    #print "Liste Des "

def add_cat_materiel(titre, desc):
    c_p = CategoryMateriel.objects.get_or_create(titre=titre, desc=desc)[0]
    return c_p

def add_cat_service(titre, desc):
    c_s = CategoryService.objects.get_or_create(titre=titre, desc=desc)[0]
    return c_s

def add_astuce(titre, link, desc):
    c_s = Astuce.objects.get_or_create(titre=titre, link=link, desc=desc)[0]
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

def add_materiel(lib, cat, desc, prix_u, qte, four):
    p = Materiel.objects.get_or_create(libelle=lib, category=cat, desc=desc, prix=prix_u, quantite=qte, fournisseur=four)[0]
    return p

def add_service(nom, type, desc, prix, cons):
    s = Service.objects.get_or_create(libelle=nom, category=type, desc=desc, prix=prix, consultant=cons)[0]
    return s

def add_ligne_command_materiel(cli, qte, prod, fact):
    com_prod = LigneCommandeMateriel.objects.get_or_create(client=cli, quantite=qte, article=prod, facture=fact)[0]
    return com_prod


def add_ligne_command_service(cli, qte, cat, fact):
    com_serv = LigneCommandeService.objects.get_or_create(client=cli, quantite=qte, article=cat, facture=fact)[0]
    return com_serv

def add_facture(cli,): #
    f = Facture.objects.get_or_create(client=cli, cloturee=False)[0]
    return f

def add_like_astuce(liker, ref_like):
    l = LikeAstuce.objects.get_or_create(liker=liker, ref_like=ref_like)
    return l


def add_like_info(liker, ref_like):
    l = LikeInfo.objects.get_or_create(liker=liker, ref_like=ref_like)
    return l


def add_like_materiel(liker, ref_like):
    l = LikeMateriel.objects.get_or_create(liker=liker, ref_like=ref_like)
    return l


def add_like_service(liker, ref_like):
    l = LikeService.objects.get_or_create(liker=liker, ref_like=ref_like)
    return l

if __name__ == '__main__':
    print "[*] Starting DyvixIT Population Script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','dyvixproject.settings')
    from dyvixitsolutions.models import Fournisseur, Client, Consultant, CategoryMateriel, CategoryService, Astuce, \
        Info, Materiel, Service, LigneCommandeMateriel, LigneCommandeService, Facture, LikeAstuce, LikeInfo, \
        LikeMateriel, LikeService
    populate()
    print "[+] DyvixIT DataBase Populated Successfully!!!"
