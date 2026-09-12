# Marketplace Vendor Portal

Module de portail vendeur pour la plateforme ElysiumShop.

## Description

Le module `marketplace_vendor_portal` fournit une interface de portail moderne pour les vendeurs du marketplace ElysiumShop.

### Fonctionnalités

- **Tableau de bord**: Vue d'ensemble avec statistiques en temps réel
- **Gestion des produits**: Créer, modifier, supprimer les produits
- **Gestion des commandes**: Suivi des commandes et statuts
- **Suivi des livraisons**: État des livraisons en temps réel
- **Gestion SAV**: Tickets de support et réponses
- **Centre de notifications**: Alertes et messages
- **Design responsive**: Interface adaptée pour desktop et mobile
- **Couleurs ElysiumShop**: Thème visuel cohérent avec la marque

## Routes disponibles

| Route | Description | Authentification |
|-------|-------------|------------------|
| `/vendor/portal` | Tableau de bord principal | Oui |
| `/vendor/products` | Liste des produits | Oui |
| `/vendor/add-product` | Ajouter un nouveau produit | Oui |
| `/vendor/orders` | Liste des commandes | Oui |
| `/vendor/delivery` | Suivi des livraisons | Oui |
| `/vendor/sav` | Tickets de support | Oui |
| `/vendor/notifications` | Centre de notifications | Oui |

## Sécurité

### Groupes d'accès

- **Vendor Portal User**: Groupe d'accès au portail vendeur

### Droits d'accès

```
Model                           | Read | Write | Create | Delete
--------------------------------|------|-------|--------|-------
product.template               |  ✓   |   ✗   |   ✗    |   ✗
sale.order                      |  ✓   |   ✗   |   ✗    |   ✗
marketplace.delivery.task       |  ✓   |   ✗   |   ✗    |   ✗
marketplace.sav.ticket          |  ✓   |   ✗   |   ✗    |   ✗
marketplace.notification        |  ✓   |   ✗   |   ✗    |   ✗
```

## Installation

1. Copier le module dans `addons_path`
2. Mettre à jour la liste des applications
3. Installer le module `marketplace_vendor_portal`
4. Assigner le groupe `Vendor Portal User` aux utilisateurs

## Dépendances

- `base`: Module de base Odoo
- `website`: Module website Odoo
- `sale`: Module vente Odoo
- `product`: Module produit Odoo
- `marketplace_delivery`: Module livraison du marketplace
- `marketplace_sav`: Module SAV du marketplace
- `marketplace_notifications`: Module notifications du marketplace

## Architecture

### Structure des fichiers

```
marketplace_vendor_portal/
├── controllers/
│   ├── __init__.py
│   └── portal_controller.py          # Routes HTTP et logique métier
├── security/
│   ├── portal_groups.xml             # Définition des groupes
│   └── ir.model.access.csv           # Matrice d'accès
├── static/
│   └── src/
│       └── css/
│           └── portal.css             # Styles du portail
├── views/
│   └── portal_templates.xml           # Templates HTML/QWeb
├── __init__.py
├── __manifest__.py
└── README.md
```

### Contrôleur

Le fichier `portal_controller.py` définit 7 routes principales:

1. `vendor_portal_dashboard()`: Tableau de bord
2. `vendor_products()`: Liste des produits
3. `vendor_add_product()`: Formulaire ajout produit
4. `vendor_orders()`: Liste des commandes
5. `vendor_delivery()`: Suivi des livraisons
6. `vendor_sav_tickets()`: Tickets SAV
7. `vendor_notifications()`: Notifications

### Méthodes utilitaires

- `_get_current_vendor()`: Récupère le partenaire courant
- `_check_vendor_access()`: Vérifie les droits d'accès

### Templates

7 templates QWeb correspondant aux 7 pages:

- `portal_dashboard`: Tableau de bord avec statistiques
- `portal_products`: Liste des produits
- `portal_add_product`: Formulaire ajout produit
- `portal_orders`: Liste des commandes
- `portal_delivery`: Suivi des livraisons
- `portal_sav`: Tickets SAV
- `portal_notifications`: Notifications

### Styles

Le fichier `portal.css` inclut:

- Variables CSS (couleurs ElysiumShop)
- Styles des cartes
- Styles des boutons
- Styles des formulaires
- Styles des tableaux
- Media queries responsive
- Animations

## Couleurs utilisées

```
Primary:    #FF6B35 (Orange)
Secondary:  #004E89 (Bleu foncé)
Accent:     #9D4EDD (Violet)
Success:    #10B981 (Vert)
Warning:    #F59E0B (Jaune/Orange)
Danger:     #EF4444 (Rouge)
Dark:       #1A1A1A (Noir)
```

## Utilisation

### Accès au portail

1. L'utilisateur se connecte au compte Odoo
2. L'utilisateur accède à `/vendor/portal`
3. Si l'utilisateur a le groupe `Vendor Portal User`, il voit le portail
4. Sinon, il est redirigé vers la page de connexion

### Gestion des produits

1. Cliquer sur "Mes produits"
2. Voir la liste de tous les produits
3. Cliquer sur "Ajouter un produit"
4. Remplir le formulaire et valider

### Suivi des commandes

1. Cliquer sur "Commandes"
2. Voir la liste des commandes avec statuts
3. Cliquer sur une commande pour voir les détails

## Maintenance

### Problèmes courants

**Accès refusé au portail**
- Vérifier que l'utilisateur a le groupe `Vendor Portal User`
- Vérifier les droits d'accès dans `security/ir.model.access.csv`

**Templates non chargés**
- Vérifier le fichier `__manifest__.py` contient `views/portal_templates.xml`
- Redémarrer le serveur Odoo

**Styles non appliqués**
- Vérifier que `portal.css` est dans `static/src/css/`
- Vérifier les assets dans `__manifest__.py`
- Vider le cache du navigateur

## Améliorations futures

- Édition des produits depuis le portail
- Historique complet des commandes
- Génération de factures
- Tableau de bord avec graphiques
- Système de messages directs
- Intégration des paiements
- Analyse des ventes
- Gestion des coupons vendeur

## Support

Pour toute question ou problème, consulter la documentation Odoo ou contacter le support ElysiumShop.
