# Marketplace - Service Après Vente (SAV)

Complete Service Après Vente (SAV) / After-Sales Service Management module for Odoo 16.

## Features

- **Complete SAV Ticket Management**: Create, manage, and track customer claims
- **Multiple Views**: Tree, Form, Kanban, Calendar, Graph, Pivot, and Search views
- **Workflow States**: Draft → Submitted → Assigned → In Progress → Approved/Rejected → Refunded/Closed
- **Security Groups**: SAV User (read-only) and SAV Manager (full access with approval rights)
- **Chatter Integration**: Mail and activity tracking for all tickets
- **Analysis Views**:
  - **Kanban**: Visual workflow by status
  - **Calendar**: Timeline view by creation date
  - **Graph**: Bar chart analysis by reason and state
  - **Pivot**: Multi-dimensional analysis
  - **Search**: Advanced filtering and grouping

## Installation

```bash
odoo -d test_db -i marketplace_sav
```

## Module Structure

```
marketplace_sav/
├── __init__.py                  # Package init
├── __manifest__.py              # Module metadata
├── models/
│   ├── __init__.py
│   └── sav_ticket.py           # Main SAV Ticket model
├── security/
│   ├── ir.model.access.csv     # Access control rules
│   └── sav_security.xml        # Groups and sequences
├── views/
│   ├── sav_ticket_views.xml    # Tree, Form, Kanban views
│   ├── sav_ticket_search.xml   # Search view
│   ├── sav_ticket_calendar.xml # Calendar view
│   ├── sav_ticket_graph.xml    # Graph view
│   ├── sav_ticket_pivot.xml    # Pivot view
│   ├── actions.xml             # Action window
│   └── menu.xml                # Menu items
├── static/
│   └── description/
│       └── icon.png            # Module icon
└── README.md                    # This file

```

## Fields

### Main Fields
- **Ticket Number**: Auto-generated with sequence (SAV/YYYY/00001)
- **Sales Order**: Link to original sale order
- **Product**: Product being claimed
- **Customer**: Customer who submitted the claim
- **Reason**: Defect, Damaged, Missing Parts, Wrong Item, Not Working, Quality Issue, Other
- **Description**: Detailed description of the issue
- **Image**: Image of the defected product
- **Status**: Workflow state
- **Responsible**: SAV manager assigned to handle the ticket
- **Resolution Notes**: Notes on resolution or rejection reason
- **Days Since Creation**: Automatically calculated

## Workflow States

1. **Draft**: Initial state when ticket is created
2. **Submitted**: Ticket submitted by customer
3. **Assigned**: Assigned to a manager
4. **In Progress**: Manager is investigating
5. **Approved**: Claim approved by manager
6. **Rejected**: Claim rejected by manager
7. **Refunded**: Refund issued to customer
8. **Closed**: Ticket closed

## Buttons & Permissions

- **Submit**: Anyone can submit a draft ticket
- **Assign**: Assign ticket to a manager
- **Start**: Manager starts processing assigned ticket
- **Approve Claim**: SAV Manager only - approves the claim
- **Reject Claim**: SAV Manager only - rejects the claim
- **Refund Customer**: SAV Manager only - issues refund for approved claims
- **Close Ticket**: Anyone can close resolved tickets

## Security

### Groups
- **SAV User**: Can view and create tickets (read-only access to most fields)
- **SAV Manager**: Full access including approval, rejection, and refund operations

### Access Control
```csv
SAV User: Read + Create
SAV Manager: Read + Write + Create + Delete
```

## Views Available

### Tree View
- Columns: Name, Customer, Product, Order, State, Responsible, Creation Date
- Color coding: Danger (Rejected), Success (Refunded), Warning (In Progress)

### Form View
- Complete ticket information
- Workflow buttons with proper state transitions
- Chatter for communication
- Tabs: Claim Details, Resolution
- Image upload support

### Kanban View
- Grouped by state by default
- Quick card view with key information
- Shows customer, product, days since creation
- Manager avatar

### Calendar View
- Event-based view using creation date
- Color-coded by state
- Drag-and-drop support

### Graph View
- Bar chart analysis
- Reason vs. State breakdown
- Quick visual analytics

### Pivot View
- Multi-dimensional analysis
- Count by State and Reason
- Flexible data exploration

### Search View
- Filter by status (Draft, Submitted, Assigned, In Progress, Approved, Rejected, Refunded, Closed)
- Filter by reason
- Quick filters (My Tickets)
- Group by: State, Reason, Customer, Product, Responsible, Creation Date

## Dependencies

- **base**: Odoo base module
- **mail**: For chatter and notifications
- **sale**: For sales order linking
- **product**: For product reference

## Usage

### Creating a SAV Ticket
1. Navigate to Service Après Vente → SAV Tickets
2. Click Create
3. Select the Sales Order (customer auto-populated)
4. Select the Product
5. Choose the Reason
6. Add Description and Image
7. Click Submit

### Processing a Ticket
1. As SAV Manager, click Assign and select yourself
2. Click Start to begin investigation
3. Add investigation notes in Resolution tab
4. Click Approve or Reject based on findings
5. If approved, click Refund Customer to issue refund
6. Close the ticket when complete

## Notes

- Module is independent and does not require vendor or delivery modules
- All views are fully functional with demonstration data
- Sequences auto-generate ticket numbers
- Chatter integration for team communication
- Activity tracking for management oversight

## Support

For questions or issues, please refer to the module documentation or contact the development team.
