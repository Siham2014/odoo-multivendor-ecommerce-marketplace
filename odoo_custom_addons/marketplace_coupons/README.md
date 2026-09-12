# Marketplace Coupons Module

## Overview

The **Marketplace Coupons** module extends the Odoo 16 marketplace with comprehensive coupon and dynamic pricing management capabilities. It allows vendors to create and manage discount coupons, while providing administrators with tools to implement dynamic pricing strategies.

## Features

### 1. Coupon Management
- **Create Coupons**: Generate discount coupons with multiple types (percentage, fixed amount, free shipping)
- **Code Generation**: Unique coupon codes with automatic prefix/padding
- **Validity Control**: Set date ranges and usage limits
- **Usage Tracking**: Monitor coupon usage with automated increment
- **Vendor Association**: Link coupons to specific vendors
- **Status Management**: Activate/deactivate coupons

### 2. Dynamic Pricing Rules
- **Strategy Configuration**: Multiple pricing strategies (cost-plus, demand-based, manual override)
- **Margin Control**: Set min/max margin constraints per vendor
- **Recommended Pricing**: Placeholder for price calculation algorithms
- **Vendor-Specific Rules**: Configure pricing strategies per vendor

### 3. Security
- **Role-Based Access**:
  - Coupon Users: Read-only access to coupons and pricing rules
  - Coupon Managers: Full CRUD access on all coupon and pricing data
  - Administrators: Full access (inherited from base.group_system)

## Installation

### Prerequisites
- Odoo 16.0 or later
- `marketplace_vendor` module installed

### Steps
1. Copy the `marketplace_coupons` directory to your Odoo addons folder:
   ```bash
   cp -r marketplace_coupons /path/to/odoo/addons/
   ```

2. Restart Odoo server:
   ```bash
   # If using Docker
   docker-compose restart odoo
   
   # If running standalone
   sudo systemctl restart odoo
   ```

3. Update module list in Odoo:
   - Go to **Apps** → **Update Apps List**
   - Search for "marketplace_coupons"
   - Click **Install**

## Models

### marketplace.coupon

**Fields:**
- `name` (Char): Coupon display name
- `code` (Char): Unique coupon code (automatically generated with sequence)
- `coupon_type` (Selection): Type of discount
  - `percentage`: Percentage discount
  - `fixed_amount`: Fixed amount discount
  - `free_shipping`: Free shipping coupon
- `amount` (Float): Discount amount or percentage
- `vendor_id` (Many2One): Associated vendor
- `valid_from` (Date): Coupon start date
- `valid_to` (Date): Coupon expiration date
- `usage_limit` (Integer): Maximum number of uses (0 = unlimited)
- `usage_count` (Integer): Current usage count
- `active` (Boolean): Enable/disable coupon
- `notes` (Text): Internal notes
- `is_valid` (Computed): Boolean indicating if coupon is currently valid

**Methods:**
- `action_increment_usage()`: Increment usage count and check limits
- `_check_dates()`: Constraint to validate date ranges
- `_check_amount()`: Constraint to validate amount values

### marketplace.dynamic.pricing

**Fields:**
- `vendor_id` (Many2One): Associated vendor
- `strategy` (Selection): Pricing strategy
  - `cost_plus`: Cost-plus markup
  - `demand_based`: Demand-based pricing
  - `manual_override`: Manual pricing override
- `min_margin_percent` (Float): Minimum margin percentage
- `max_margin_percent` (Float): Maximum margin percentage
- `active` (Boolean): Enable/disable pricing rule
- `recommended_price` (Computed): Suggested price based on strategy

**Methods:**
- `_check_margin_range()`: Constraint to validate margin values
- `_check_margin_order()`: Constraint to ensure min < max

## Views

### Coupon Views
- **Tree View**: List all coupons with key information
- **Form View**: Detailed coupon editor with usage tracking button
- **Search View**: Filter by code, vendor, type, status, and validity
- **Kanban View**: Card-based coupon view with status indicators
- **Pivot View**: Analyze coupon usage by type and vendor
- **Graph View**: Visualize coupon discount amounts

### Dynamic Pricing Views
- **Tree View**: List pricing strategies by vendor
- **Form View**: Configure margin constraints per vendor
- **Search View**: Filter by vendor and strategy

## Menu Structure

```
Coupons & Pricing (Independent Root Menu)
├── All Coupons          → marketplace.coupon
└── Dynamic Pricing      → marketplace.dynamic.pricing
```

**Note**: This module creates its own independent root menu in the sidebar. It does NOT depend on other modules' menus.

## Security Groups

- **group_coupon_user**: Read-only access to coupon and pricing data
- **group_coupon_manager**: Full CRUD access on coupons and pricing rules

## Data

### Sequences
- **Coupon Code Sequence**: `COUPON/YYYY/00001`
  - Prefix: `COUPON/`
  - Year: `%(y)s` (2-digit year)
  - Padding: 5 digits with leading zeros
  - Example: `COUPON/24/00001`

## XML Files Reference

| File | Purpose | Load Order |
|------|---------|-----------|
| `security/coupon_security.xml` | Security groups definition | 1 |
| `security/ir.model.access.csv` | Access control rules | 2 |
| `data/coupon_sequence.xml` | Coupon code sequence | 3 |
| `views/coupon_views.xml` | Coupon view definitions | 4 |
| `views/dynamic_pricing_views.xml` | Pricing view definitions | 4 |
| `views/coupon_actions.xml` | Action window definitions | 5 |
| `views/coupon_menus.xml` | Menu structure | 6 |

## Manifest Dependencies

```python
'depends': [
    'base',               # Odoo core
    'marketplace_vendor', # Marketplace vendor module
],
```

## File Structure

```
marketplace_coupons/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── coupon.py
│   └── dynamic_pricing.py
├── views/
│   ├── coupon_views.xml
│   ├── dynamic_pricing_views.xml
│   ├── coupon_actions.xml
│   └── coupon_menus.xml
├── security/
│   ├── coupon_security.xml
│   └── ir.model.access.csv
├── data/
│   └── coupon_sequence.xml
└── static/
    └── description/
```

## SAFE MODE Compliance

This module adheres to SAFE MODE standards:

✅ **No modifications** to existing modules  
✅ **Proper XML separation** - records, menus, and data in separate files  
✅ **Correct load order** - security → data → views → actions → menus  
✅ **Unique XML IDs** - all prefixed with `marketplace_coupons_`  
✅ **Valid references** - only references existing external IDs  
✅ **Placeholder implementations** - computed fields and constraints use safe patterns  

## Testing Checklist

- [ ] Module installs without errors
- [ ] Coupon menu appears under ElysiumShop
- [ ] Can create new coupons
- [ ] Coupon code auto-generates with correct format
- [ ] Date validation works correctly
- [ ] Usage count increments properly
- [ ] Dynamic pricing rules can be configured
- [ ] Security groups restrict access appropriately
- [ ] All views load correctly

## Troubleshooting

### Module won't install
1. Check that `marketplace_vendor` module is installed first
2. Verify XML files are well-formed (no syntax errors)
3. Check Odoo log for specific error messages

### Views not displaying
1. Clear browser cache (Ctrl+Shift+Delete)
2. Restart Odoo server
3. Verify all view IDs match in coupon_actions.xml

### Coupons not appearing in menu
1. Verify coupon_menus.xml references correct action IDs
2. Check that current user is in appropriate security group
3. Ensure parent menu `elysiumshop_core.marketplace_menu_root` exists

## Future Enhancements

- Integrate with sales order workflow
- Coupon redemption tracking
- Performance-based pricing algorithms
- Bulk coupon generation
- Coupon analytics dashboard

## Support & Contribution

For issues or improvements, please contact the development team.

---

**Module Version**: 1.0  
**Odoo Version**: 16.0  
**Last Updated**: 2024
