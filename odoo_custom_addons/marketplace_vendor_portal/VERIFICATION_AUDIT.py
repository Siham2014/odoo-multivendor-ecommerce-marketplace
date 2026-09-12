#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Marketplace Vendor Portal - Vérification complète du module
===========================================================

Ce script effectue un audit complet du module marketplace_vendor_portal
pour vérifier l'intégrité et la configuration.
"""

import os
import sys
import io

# Force UTF-8 output encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_files():
    """Vérifier la présence de tous les fichiers nécessaires"""
    print("=" * 60)
    print("VÉRIFICATION DES FICHIERS")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    required_files = {
        '__init__.py': 'Module init',
        '__manifest__.py': 'Manifeste',
        'README.md': 'Documentation',
        'controllers/__init__.py': 'Controllers init',
        'controllers/portal_controller.py': 'Contrôleur principal',
        'security/portal_groups.xml': 'Groupes de sécurité',
        'security/ir.model.access.csv': 'Matrice d\'accès',
        'static/src/css/portal.css': 'Styles CSS',
        'views/portal_templates.xml': 'Templates QWeb',
    }
    
    missing_files = []
    for file_path, description in required_files.items():
        full_path = os.path.join(base_path, file_path)
        if os.path.exists(full_path):
            size = os.path.getsize(full_path)
            print(f"✓ {file_path:<40} ({size:>6} bytes) - {description}")
        else:
            print(f"✗ {file_path:<40} MANQUANT - {description}")
            missing_files.append(file_path)
    
    return len(missing_files) == 0


def check_manifest():
    """Vérifier la configuration du manifeste"""
    print("\n" + "=" * 60)
    print("VÉRIFICATION DU MANIFESTE")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    manifest_path = os.path.join(base_path, '__manifest__.py')
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier les clés importantes
        required_keys = [
            'name',
            'version',
            'category',
            'summary',
            'author',
            'license',
            'depends',
            'data',
            'assets',
        ]
        
        manifest_ok = True
        for key in required_keys:
            if f"'{key}'" in content or f'"{key}"' in content:
                print(f"✓ Clé '{key}' trouvée")
            else:
                print(f"✗ Clé '{key}' MANQUANTE")
                manifest_ok = False
        
        # Vérifier les dépendances
        print("\nDépendances attendues:")
        expected_deps = [
            'base',
            'website',
            'sale',
            'product',
            'marketplace_delivery',
            'marketplace_sav',
            'marketplace_notifications',
        ]
        
        for dep in expected_deps:
            if f"'{dep}'" in content:
                print(f"✓ Dépendance '{dep}' trouvée")
            else:
                print(f"✗ Dépendance '{dep}' MANQUANTE")
                manifest_ok = False
        
        return manifest_ok
        
    except Exception as e:
        print(f"✗ Erreur lors de la lecture du manifeste: {e}")
        return False


def check_controller():
    """Vérifier la présence des routes"""
    print("\n" + "=" * 60)
    print("VÉRIFICATION DU CONTRÔLEUR")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    controller_path = os.path.join(base_path, 'controllers', 'portal_controller.py')
    
    try:
        with open(controller_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_routes = [
            '/vendor/portal',
            '/vendor/products',
            '/vendor/add-product',
            '/vendor/orders',
            '/vendor/delivery',
            '/vendor/sav',
            '/vendor/notifications',
        ]
        
        routes_ok = True
        print("Routes définies:")
        for route in required_routes:
            if f"'{route}'" in content:
                print(f"✓ Route '{route}' trouvée")
            else:
                print(f"✗ Route '{route}' MANQUANTE")
                routes_ok = False
        
        # Vérifier les méthodes utilitaires
        print("\nMéthodes utilitaires:")
        utilities = [
            '_get_current_vendor',
            '_check_vendor_access',
        ]
        
        for utility in utilities:
            if f"def {utility}" in content:
                print(f"✓ Méthode '{utility}' trouvée")
            else:
                print(f"✗ Méthode '{utility}' MANQUANTE")
                routes_ok = False
        
        return routes_ok
        
    except Exception as e:
        print(f"✗ Erreur lors de la lecture du contrôleur: {e}")
        return False


def check_templates():
    """Vérifier la présence de tous les templates"""
    print("\n" + "=" * 60)
    print("VÉRIFICATION DES TEMPLATES")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    templates_path = os.path.join(base_path, 'views', 'portal_templates.xml')
    
    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_templates = [
            'portal_dashboard',
            'portal_products',
            'portal_add_product',
            'portal_orders',
            'portal_delivery',
            'portal_sav',
            'portal_notifications',
        ]
        
        templates_ok = True
        print("Templates définis:")
        for template in required_templates:
            if f'id="{template}"' in content:
                print(f"✓ Template '{template}' trouvé")
            else:
                print(f"✗ Template '{template}' MANQUANT")
                templates_ok = False
        
        return templates_ok
        
    except Exception as e:
        print(f"✗ Erreur lors de la lecture des templates: {e}")
        return False


def check_security():
    """Vérifier la configuration de sécurité"""
    print("\n" + "=" * 60)
    print("VÉRIFICATION DE LA SÉCURITÉ")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    
    # Vérifier groups.xml
    groups_path = os.path.join(base_path, 'security', 'portal_groups.xml')
    print("\nGroupes de sécurité:")
    try:
        with open(groups_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'vendor_portal_user' in content:
            print(f"✓ Groupe 'vendor_portal_user' trouvé")
        else:
            print(f"✗ Groupe 'vendor_portal_user' MANQUANT")
            return False
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False
    
    # Vérifier access.csv
    access_path = os.path.join(base_path, 'security', 'ir.model.access.csv')
    print("\nMatrice d'accès:")
    try:
        with open(access_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        models = [
            'marketplace_delivery.model_marketplace_delivery_task',
            'marketplace_sav.model_marketplace_sav_ticket',
        ]
        
        security_ok = True
        for model in models:
            if model in content:
                print(f"✓ Accès pour '{model}' configuré")
            else:
                print(f"✗ Accès pour '{model}' MANQUANT")
                security_ok = False
        
        return security_ok
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False


def check_styles():
    """Vérifier la présence des styles"""
    print("\n" + "=" * 60)
    print("VÉRIFICATION DES STYLES")
    print("=" * 60)
    
    base_path = os.path.dirname(__file__)
    css_path = os.path.join(base_path, 'static', 'src', 'css', 'portal.css')
    
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier les variables CSS
        print("Variables CSS ElysiumShop:")
        colors = [
            '--color-primary',
            '--color-secondary',
            '--color-accent',
            '--color-success',
        ]
        
        styles_ok = True
        for color in colors:
            if color in content:
                print(f"✓ Variable '{color}' trouvée")
            else:
                print(f"✗ Variable '{color}' MANQUANTE")
                styles_ok = False
        
        # Vérifier les sections principales
        print("\nSections CSS:")
        sections = [
            'Cards',
            'Buttons',
            'Tables',
            'Forms',
            'Responsive Design',
        ]
        
        for section in sections:
            if section in content:
                print(f"✓ Section '{section}' trouvée")
            else:
                print(f"✗ Section '{section}' MANQUANTE")
                styles_ok = False
        
        return styles_ok
        
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False


def main():
    """Exécuter la vérification complète"""
    print("\n")
    print("█" * 60)
    print("AUDIT DU MODULE MARKETPLACE_VENDOR_PORTAL")
    print("█" * 60)
    print("\n")
    
    results = {
        'Files': check_files(),
        'Manifest': check_manifest(),
        'Controller': check_controller(),
        'Templates': check_templates(),
        'Security': check_security(),
        'Styles': check_styles(),
    }
    
    print("\n" + "=" * 60)
    print("RÉSUMÉ DE L'AUDIT")
    print("=" * 60)
    
    all_ok = True
    for check_name, status in results.items():
        status_text = "✓ PASS" if status else "✗ FAIL"
        print(f"{check_name:<20} {status_text}")
        if not status:
            all_ok = False
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✓ AUDIT RÉUSSI - Le module est correctement configuré")
        print("=" * 60)
        return 0
    else:
        print("✗ AUDIT ÉCHOUÉ - Des vérifications ont échoué")
        print("=" * 60)
        return 1


if __name__ == '__main__':
    sys.exit(main())
