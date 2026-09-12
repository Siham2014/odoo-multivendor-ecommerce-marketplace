# Marketplace Vendor Portal - Guide de déploiement

## 🚀 Déploiement en production

### Prérequis

- Serveur Odoo 16.0 opérationnel
- Accès SSH ou FTP au serveur
- Permissions administrateur Odoo
- Modules dépendants installés:
  - base
  - website
  - sale
  - product
  - marketplace_delivery
  - marketplace_sav
  - marketplace_notifications

### Étapes de déploiement

#### 1. Copier le module

```bash
# Via SCP (depuis votre machine locale)
scp -r marketplace_vendor_portal/ user@server:/path/to/addons/

# Ou via FTP
ftp://server.com/addons/marketplace_vendor_portal/
```

#### 2. Mettre à jour les addons

```bash
# Dans l'interface Odoo
1. Aller à Apps
2. Cliquer sur "Update Apps List"
3. Attendre la mise à jour
```

#### 3. Installer le module

```bash
# Via l'interface Odoo
1. Aller à Apps
2. Rechercher "Marketplace Vendor Portal"
3. Cliquer sur "Install"
4. Valider les dépendances manquantes
```

#### 4. Configurer les accès

```bash
# Via l'interface Odoo
1. Aller à Settings → Users & Companies → Users
2. Sélectionner un utilisateur
3. Ajouter le groupe "Vendor Portal User"
4. Sauvegarder
```

#### 5. Vérifier l'installation

```bash
# Vérifier l'installation
1. Accéder à /vendor/portal
2. Vérifier que le portail s'affiche
3. Vérifier les redirections
4. Tester les routes
```

---

## 📋 Checklist de déploiement

- [ ] Backup du serveur effectué
- [ ] Module copié au bon emplacement
- [ ] Permissions fichiers correctes (755)
- [ ] Module visible dans la liste des apps
- [ ] Module installé sans erreurs
- [ ] Groupe de sécurité créé
- [ ] Utilisateurs assignés au groupe
- [ ] Routes accessibles
- [ ] Templates chargées
- [ ] Styles appliqués
- [ ] Tests fonctionnels validés
- [ ] Permissions testées

---

## 🔧 Configuration avancée

### Paramètres optionnels

```xml
<!-- Dans portal_controller.py, vous pouvez ajouter: -->
<constant name="PORTAL_ITEMS_PER_PAGE" value="20"/>
<constant name="PORTAL_CACHE_TIMEOUT" value="3600"/>
<constant name="PORTAL_MAX_UPLOAD_SIZE" value="10485760"/>
```

### Personnalisation des templates

```xml
<!-- Modifier les couleurs dans portal_templates.xml -->
<div style="background: #VOTRE_COULEUR;">
    <!-- Contenu -->
</div>
```

### Styles personnalisés

```css
/* Ajouter dans portal.css */
:root {
    --custom-color: #VOTRE_COULEUR;
}
```

---

## 🐛 Troubleshooting

### Problème: Module n'apparaît pas

**Solution:**
```bash
# Redémarrer Odoo
sudo systemctl restart odoo

# Ou via docker
docker restart odoo-server
```

### Problème: Routes 404

**Solution:**
```bash
# Vérifier les droits d'accès
1. Vérifier le groupe "vendor_portal_user"
2. Vérifier les permissions utilisateur
3. Redémarrer le serveur
```

### Problème: Styles non appliqués

**Solution:**
```bash
# Vider le cache navigateur (Ctrl+Shift+Del)
# Ou:
1. Aller à Settings → Technical → Views
2. Filtrer par "portal"
3. Cliquer sur "Reset View"
```

### Problème: Permission denied

**Solution:**
```bash
# Vérifier les permissions des fichiers
chmod 755 /path/to/marketplace_vendor_portal/
chmod 644 /path/to/marketplace_vendor_portal/*.py
```

---

## 📊 Monitoring post-déploiement

### Logs à vérifier

```bash
# Logs Odoo
tail -f /var/log/odoo/odoo-server.log

# Chercher les erreurs du module
grep -i "vendor_portal" /var/log/odoo/odoo-server.log

# Erreurs d'import
grep -i "ImportError" /var/log/odoo/odoo-server.log
```

### Performance

```bash
# Vérifier les requêtes SQL lentes
1. Aller à Settings → Technical → Database Structure → Models
2. Filtrer par "marketplace.vendor"
3. Vérifier les indexes
```

### Utilisation des utilisateurs

```bash
# Via l'interface Odoo
1. Aller à Reporting → Portal Usage
2. Vérifier le nombre d'utilisateurs actifs
3. Vérifier les pages les plus visitées
```

---

## 🔐 Sécurité post-déploiement

### Vérifications de sécurité

- [ ] HTTPS activé sur le serveur
- [ ] Certificats SSL valides
- [ ] Firewall configuré
- [ ] Rate limiting activé
- [ ] Authentification 2FA (recommandé)
- [ ] Logs audités régulièrement
- [ ] Backups automatisés

### Configuration HTTPS

```bash
# Forcer HTTPS
1. Aller à Settings → Technical → System Parameters
2. Ajouter: web.base.url = https://domain.com
```

---

## 🔄 Maintenance régulière

### Tâches hebdomadaires
- [ ] Vérifier les logs d'erreurs
- [ ] Vérifier l'espace disque
- [ ] Vérifier les performances

### Tâches mensuelles
- [ ] Nettoyer les anciens logs
- [ ] Optimiser la base de données
- [ ] Mettre à jour les modules dépendants

### Tâches trimestrielles
- [ ] Audit de sécurité
- [ ] Sauvegarde archivée
- [ ] Rapport d'utilisation

---

## 📈 Rollback en cas de problème

### Rollback rapide

```bash
# 1. Désinstaller le module
# Interface Odoo → Apps → Marketplace Vendor Portal → Désinstaller

# 2. Supprimer le module
rm -rf /path/to/marketplace_vendor_portal/

# 3. Redémarrer Odoo
sudo systemctl restart odoo

# 4. Restaurer depuis backup si nécessaire
```

### Rollback base de données

```bash
# Via backup
1. Aller à Settings → Database Tools
2. Cliquer sur "Restore Database"
3. Sélectionner le backup pré-déploiement
4. Attendre la restauration
```

---

## 📞 Support et assistance

### Contacts
- Support Odoo: support@odoo.com
- ElysiumShop: support@elysiumshop.com
- Documentation: https://www.odoo.com/documentation/

### Ressources
- [Odoo Developer Documentation](https://www.odoo.com/documentation/16.0/)
- [GitHub Repository](https://github.com/odoo/odoo)
- [Community Forums](https://www.odoo.com/forum/)

---

## ✅ Validation finale

Une fois le module en production:

1. **Vérifier l'accès**: Accéder à `/vendor/portal`
2. **Tester les routes**: Parcourir toutes les pages
3. **Tester les formulaires**: Soumettre un produit test
4. **Vérifier les permissions**: Test avec différents rôles
5. **Documenter les problèmes**: Créer des tickets de support

---

**Déploiement validé le:** 6 décembre 2025
**Module:** marketplace_vendor_portal v16.0.1.0.0
**Statut:** PRODUCTION-READY ✓
