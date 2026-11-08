---
title: "Generate and Store HTML Forms from Database Data"
date: 2018-03-24 08:18:51 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /html-form-generation-from-the-database-and-store-value-into-the-database/
---

When you need to store form submissions where different form types have different attributes, you’re essentially implementing an Entity-Attribute-Value (EAV) model. This is a common pattern for flexible schemas, but it requires careful design.

### The Core Problem

You have multiple form types (Laptop, Mobile, Tablet) with different fields. A naive approach is a wide table with all possible columns, but that wastes storage and becomes unwieldy at scale. The alternative is a normalized schema that handles variable attributes per form type.

### Recommended Schema Design

Use a three-table approach: one for the items being submitted, one for the attribute definitions, and one to store the actual values.

**items table** — stores one row per form submission

``` sql
CREATE TABLE items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    form_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (form_id) REFERENCES forms(form_id)
);
```

**forms table** — defines available form types

``` sql
CREATE TABLE forms (
    form_id INT PRIMARY KEY AUTO_INCREMENT,
    form_name VARCHAR(100),
    description TEXT
);
```

**form_attributes table** — junction table connecting forms to available attributes

``` sql
CREATE TABLE form_attributes (
    form_id INT NOT NULL,
    attribute_id INT NOT NULL,
    PRIMARY KEY (form_id, attribute_id),
    FOREIGN KEY (form_id) REFERENCES forms(form_id),
    FOREIGN KEY (attribute_id) REFERENCES attributes(attribute_id)
);
```

**attributes table** — defines the attribute names and their data types

``` sql
CREATE TABLE attributes (
    attribute_id INT PRIMARY KEY AUTO_INCREMENT,
    attribute_name VARCHAR(100),
    data_type ENUM('string', 'integer', 'decimal', 'date')
);
```

**item_attributes table** — stores the actual values submitted by users

``` sql
CREATE TABLE item_attributes (
    item_id INT NOT NULL,
    attribute_id INT NOT NULL,
    attribute_value VARCHAR(500),
    PRIMARY KEY (item_id, attribute_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (attribute_id) REFERENCES attributes(attribute_id)
);
```

### Sample Data

Start with your attribute definitions:

``` sql
INSERT INTO attributes (attribute_name, data_type) VALUES
('Model', 'string'),
('Screen Size', 'decimal'),
('OS', 'string'),
('CD Player', 'string');

INSERT INTO forms (form_name, description) VALUES
(1, 'Laptop', 'Possible attributes: Model, Screen Size, OS, CD Player'),
(2, 'Mobile', 'Possible attributes: Model, OS'),
(3, 'Tablet', 'Possible attributes: Model, Screen Size, OS');

INSERT INTO form_attributes (form_id, attribute_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4),
(2, 1), (2, 3),
(3, 1), (3, 2), (3, 3);
```

When a user submits a Laptop form with values:

``` sql
INSERT INTO items (form_id) VALUES (1);
-- Assume item_id 9 was generated

INSERT INTO item_attributes (item_id, attribute_id, attribute_value) VALUES
(9, 1, 'HP Pavilion 15'),
(9, 2, '15.6'),
(9, 3, 'Windows 11'),
(9, 4, 'Yes');
```

### Retrieving and Filtering Data

To fetch a specific item with all its attributes:

``` sql
SELECT 
    a.attribute_name,
    ia.attribute_value
FROM item_attributes ia
JOIN attributes a ON ia.attribute_id = a.attribute_id
WHERE ia.item_id = 9;
```

To filter items by a range (e.g., laptops with screen size 14 to 16):

``` sql
SELECT DISTINCT
    i.item_id,
    f.form_name
FROM items i
JOIN item_attributes ia ON i.item_id = ia.item_id
JOIN attributes a ON ia.attribute_id = a.attribute_id
JOIN forms f ON i.form_id = f.form_id
WHERE i.form_id = 1  -- Laptops only
AND a.attribute_id = 2  -- Screen Size
AND CAST(ia.attribute_value AS DECIMAL(5,2)) BETWEEN 14 AND 16;
```

For multiple filter conditions (e.g., screen size AND OS):

``` sql
SELECT DISTINCT
    i.item_id,
    f.form_name
FROM items i
JOIN forms f ON i.form_id = f.form_id
WHERE i.form_id = 1
AND i.item_id IN (
    SELECT ia1.item_id
    FROM item_attributes ia1
    JOIN attributes a1 ON ia1.attribute_id = a1.attribute_id
    WHERE a1.attribute_id = 2 
    AND CAST(ia1.attribute_value AS DECIMAL(5,2)) BETWEEN 14 AND 16
)
AND i.item_id IN (
    SELECT ia2.item_id
    FROM item_attributes ia2
    JOIN attributes a2 ON ia2.attribute_id = a2.attribute_id
    WHERE a2.attribute_id = 3 
    AND ia2.attribute_value = 'Linux'
);
```

### HTML Form Generation

When displaying a form, query the allowed attributes for that form type:

``` sql
SELECT a.attribute_id, a.attribute_name, a.data_type
FROM attributes a
JOIN form_attributes fa ON a.attribute_id = fa.attribute_id
WHERE fa.form_id = ?;
```

Then dynamically generate input fields based on the data_type. Use the attribute_id as the field name or data attribute to map submissions back to the attribute definitions.

### Trade-offs

This normalized approach scales well with 40+ form types and 15+ attributes per form. Storage is minimal because you only store actual values. Query complexity increases with multiple filters, but this is manageable with proper indexing on item_id and attribute_id.

For high-volume filtering, consider denormalizing specific frequently-queried attributes (like Screen Size) into the items table, keeping the EAV structure for less-common fields. Add indexes on `item_attributes(attribute_id, attribute_value)` and `items(form_id, created_at)` to optimize common queries.
