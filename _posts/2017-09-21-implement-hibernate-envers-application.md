---
title: "Implementing Hibernate Envers for Entity Auditing"
date: 2017-09-21 03:50:03 +0000
modified: 2026-04-11 17:51:15 +0000
author: "Joseph Macwan"
layout: post
categories: [development-best-practices]
canonical: /implement-hibernate-envers-application/
---

Hibernate Envers is a proven auditing framework that automatically tracks changes to JPA entities without cluttering your domain model with logging code. It stores historical data in separate audit tables and lets you query entity states at any point in time.

## Why Use Hibernate Envers

Envers handles the mechanics of change tracking transparently:

- Audits all JPA mappings and Hibernate-specific extensions automatically
- Tracks changes per transaction with revision numbers and timestamps
- Stores audit data in separate tables with configurable naming conventions
- Queries historical states using an API similar to regular JPA queries
- Works across different database platforms without code changes
- Tracks which fields changed in each revision with `withModifiedFlag`

## Adding Dependencies

For Maven projects, add to `pom.xml`:

``` xml
<dependency>
    <groupId>org.hibernate.orm</groupId>
    <artifactId>hibernate-envers</artifactId>
    <version>6.8.0</version>
</dependency>
```

For Gradle:

``` gradle
implementation 'org.hibernate.orm:hibernate-envers:6.8.0'
```

## Marking Entities for Auditing

Apply `@Audited` at the class or field level:

``` java
@Entity
@Audited
public class Order {
    @Id
    private Long id;

    private String orderNumber;
    private BigDecimal totalAmount;

    @Audited(withModifiedFlag = true)
    private LocalDateTime createdAt;

    @NotAudited
    private String internalNotes;

    @ManyToOne
    @Audited
    private Customer customer;
}
```

Key annotation details:

- `@Audited` on the class audits all properties by default
- `@Audited` on individual fields audits only those specific fields
- `withModifiedFlag = true` tracks which fields changed in each revision — useful for identifying specific modifications
- `@NotAudited` excludes sensitive data or irrelevant fields from the audit trail
- Entity primary keys must be immutable (Long, UUID, String, etc.)
- Apply `@Audited` to `@ManyToOne` and `@OneToOne` relationships to track association changes

## Customizing Audit Table Names

Override default audit table naming (which appends `_AUD` suffix by default):

``` java
@Entity
@Audited
@AuditTable(value = "order_changes")
public class Order {
    // ...
}
```

For collection relationships, customize the join table audit names:

``` java
@ManyToMany
@AuditJoinTable(value = "order_items_audit")
private Set<Item> items;
```

Override auditing inheritance from mapped superclasses:

``` java
@Entity
@AuditingOverrides({
    @AuditingOverride(name = "createdBy", isAudited = false),
    @AuditingOverride(name = "lastModified", isAudited = true)
})
public class Order extends BaseEntity { }
```

## Setting Up a Revision Entity

Define a revision entity to track who changed what and when:

``` java
@Entity
@RevisionEntity(CustomRevisionListener.class)
public class RevisionLog {
    @Id
    @GeneratedValue
    @RevisionNumber
    private Long revisionNumber;

    @RevisionTimestamp
    private Long revisionTimestamp;

    private String modifiedBy;
    private String ipAddress;
}
```

The `@RevisionEntity` listener captures contextual information:

``` java
public class CustomRevisionListener implements RevisionListener {
    @Override
    public void newRevision(Object revisionEntity) {
        RevisionLog revLog = (RevisionLog) revisionEntity;
        revLog.setModifiedBy(getCurrentUser());
        revLog.setIpAddress(getClientIpAddress());
    }

    private String getCurrentUser() {
        // Get from SecurityContext, request context, etc.
        return "user-123";
    }

    private String getClientIpAddress() {
        HttpServletRequest request = ((ServletRequestAttributes) 
            RequestContextHolder.getRequestAttributes()).getRequest();
        return request.getRemoteAddr();
    }
}
```

## Configuration Properties

Set these in `application.properties` or `application.yml`:

```properties
# Audit table naming
hibernate.envers.audit_table_prefix=aud_
hibernate.envers.audit_table_suffix=_history

# Revision field names
hibernate.envers.revision_field_name=revision_id
hibernate.envers.revision_type_field_name=change_type

# Track which entities changed per revision (useful for analytics)
hibernate.envers.track_entities_changed_in_revision=true

# Store revision changes in a dedicated table
hibernate.envers.store_data_at_delete=true

# Auto-register Envers listeners (set false for conditional auditing)
hibernate.envers.autoRegisterListeners=true
```

## Querying Historical Data

Use `AuditReader` to retrieve entity states at specific points in time:

``` java
AuditReader auditReader = AuditReaderFactory.get(entityManager);

// Get entity state at a specific revision
Order orderAtRev5 = auditReader.find(Order.class, 42L, 5);

// Get all revision numbers where this entity changed
List<Number> revisions = auditReader.getRevisions(Order.class, 42L);

// Get revision metadata
RevisionLog revisionInfo = auditReader.findRevision(RevisionLog.class, 5);

// Query entities with conditions at a specific revision
AuditQuery query = auditReader.createQuery()
    .forEntitiesAtRevision(Order.class, 10)
    .add(AuditEntity.property("orderNumber").eq("ORD-001"))
    .add(AuditEntity.property("totalAmount").gt(BigDecimal.valueOf(1000)));
List<Order> results = query.getResultList();

// Get all entities modified in a specific revision
Set<String> modifiedEntities = auditReader.getModifiedEntityNames(10);

// Query between revisions
AuditQuery betweenQuery = auditReader.createQuery()
    .forEntitiesAtRevision(Order.class, 10)
    .forEntitiesModifiedAtRevision(Order.class, AuditEntity.RevisionType.MOD);
List<Order> modified = betweenQuery.getResultList();
```

## Conditional Auditing

Audit only specific entity types or based on business logic:

```properties
hibernate.envers.autoRegisterListeners=false
```

Create a conditional listener:

``` java
public class ConditionalAuditEventListener extends EnversPostInsertEventListenerImpl {
    @Override
    public void onPostInsert(PostInsertEvent event) {
        if (shouldAudit(event.getEntity())) {
            super.onPostInsert(event);
        }
    }

    private boolean shouldAudit(Object entity) {
        return entity instanceof Order || entity instanceof Invoice;
    }
}
```

Register via a custom integrator:

``` java
public class CustomEnversIntegrator extends EnversIntegrator {
    @Override
    public void integrate(Metadata metadata, SessionFactoryImpl sessionFactory, 
            ServiceRegistry serviceRegistry) {
        super.integrate(metadata, sessionFactory, serviceRegistry);

        EventListenerRegistry registry = 
            serviceRegistry.getService(EventListenerRegistry.class);
        registry.setListeners(PostInsertEventListener.class, 
            new ConditionalAuditEventListener());
        registry.setListeners(PostUpdateEventListener.class, 
            new ConditionalAuditEventListener());
        registry.setListeners(PostDeleteEventListener.class, 
            new ConditionalAuditEventListener());
    }

    @Override
    public int getPrecedence() {
        return 1; // High priority
    }
}
```

Register in `META-INF/services/org.hibernate.integrator.spi.Integrator`:

    com.example.CustomEnversIntegrator

## Tracking Modified Entities

Monitor which entity types changed in each revision:

```properties
hibernate.envers.track_entities_changed_in_revision=true
```

Or extend the default tracking entity:

``` java
@Entity
@RevisionEntity(CustomRevisionListener.class)
public class RevisionLog extends DefaultTrackingModifiedEntitiesRevisionEntity {
    @Id
    @GeneratedValue
    @RevisionNumber
    private Long revisionNumber;

    @RevisionTimestamp
    private Long revisionTimestamp;

    private String modifiedBy;
}
```

Query which entities changed:

``` java
AuditReader auditReader = AuditReaderFactory.get(entityManager);
Set<String> modifiedEntities = auditReader.getModifiedEntityNames(revisionNumber);

if (modifiedEntities.contains("Order")) {
    // Process order changes
}
```

## Complete Practical Example

``` java
@Entity
@Audited
public class Invoice {
    @Id
    private Long id;

    private String invoiceNumber;
    private BigDecimal amount;

    @ManyToOne
    @Audited
    private Customer customer;

    @Audited(withModifiedFlag = true)
    private InvoiceStatus status;

    @NotAudited
    private String internalNotes;

    private LocalDateTime createdAt;
}

// Usage in a service
@Service
public class InvoiceService {
    @Autowired
    private EntityManager em;

    public void auditInvoiceHistory(Long invoiceId) {
        AuditReader reader = AuditReaderFactory.get(em);

        // Get all revisions for this invoice
        List<Number> revisions = reader.getRevisions(Invoice.class, invoiceId);
        System.out.println("Total changes: " + revisions.size());

        // Inspect each revision
        for (Number rev : revisions) {
            Invoice invoiceState = reader.find(Invoice.class, invoiceId, rev);
            RevisionLog revLog = reader.findRevision(RevisionLog.class, rev.longValue());

            System.out.printf("Rev %d (%s): Status=%s, Amount=%s, By=%s%n",
                rev, 
                new Date(revLog.getRevisionTimestamp()),
                invoiceState.getStatus(),
                invoiceState.getAmount(),
                revLog.getModifiedBy()
            );
        }

        // Query invoices with amount > 5000 at revision 10
        AuditQuery query = reader.createQuery()
            .forEntitiesAtRevision(Invoice.class, 10)
            .add(AuditEntity.property("amount").gt(BigDecimal.valueOf(5000)));

        List<Invoice> largeInvoices = query.getResultList();
    }
}
```

## Best Practices

- Enable `withModifiedFlag` on fields that change frequently to identify specific modifications
- Use a `RevisionListener` to capture user context and IP addresses
- Index revision and entity ID columns in audit tables for query performance on large datasets
- Archive or purge old audit data using batch delete queries to manage table size
- Test audit queries regularly to ensure historical data is accurate
- Avoid auditing temporary or transient fields using `@NotAudited`
- Use Spring Security integration to automatically capture current user in revisions

Envers handles all schema creation and maintenance automatically. For most applications, basic configuration and `@Audited` annotations provide complete audit functionality without custom logic.
