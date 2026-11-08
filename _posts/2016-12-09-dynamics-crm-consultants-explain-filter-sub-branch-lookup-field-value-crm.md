---
title: "Filter Dependent Lookup Fields in Dynamics 365 and Power Apps"
date: 2016-12-09 07:55:17 +0000
author: "jameswarner"
layout: post
canonical: https://www.systutorials.com/dynamics-crm-consultants-explain-filter-sub-branch-lookup-field-value-crm/
---

Filtering a dependent lookup field based on another lookup field’s value is a core requirement in Dynamics 365 and Power Apps. The classic example: a Lead entity with Branch and Sub Branch fields where Sub Branch options should only display records matching the selected Branch.

The form editor handles this natively—no plugins or JavaScript required.

## Set up the lookup entities

Start with two tables that support the hierarchical relationship:

1.  Create a Branch table (or use an existing one)
2.  Create a Sub Branch table with a lookup column pointing back to Branch

Populate with sample data:

**Branch table:**

- India
- United Kingdom
- Canada

**Sub Branch table:**

- Mumbai (linked to India)
- London (linked to United Kingdom)
- Toronto (linked to Canada)

Each Sub Branch record must have its parent Branch populated. Do this manually for small datasets or use bulk import for larger ones.

## Add the lookup fields to your main entity

Open your Lead table and add two lookup columns:

- **Branch** → references the Branch table
- **Sub Branch** → references the Sub Branch table

Add both to your Lead form and publish.

## Configure the dependent filter

Open the Lead form in the Form Designer:

1.  Select the Sub Branch field
2.  In the properties panel, scroll to **Filtering**
3.  Toggle **Filter based on a related table** to On
4.  Configure the filter:
    - **Related table:** Sub Branch
    - **Related column:** Main Branch (the lookup field on Sub Branch)
    - **Filter by:** Branch (the lookup field on your form)
5.  Ensure **Show search** is enabled
6.  Save and publish

This configuration displays only Sub Branch records where the Main Branch field matches the selected Branch value.

## Test the filter

Create a new Lead record and verify:

1.  Select “India” in the Branch field
2.  Open the Sub Branch dropdown
3.  Only “Mumbai” should appear
4.  Change Branch to “United Kingdom”—Sub Branch options should update immediately to show “London”

## Troubleshoot common issues

**Filter isn’t working:**

- Verify the Main Branch field on Sub Branch has values for all records
- Check both lookup fields are visible on the form (not hidden in collapsed sections)
- Confirm the filter is configured on Sub Branch, not Branch
- Publish the form (saving alone doesn’t apply changes)
- Clear browser cache and do a hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

**Wrong records appearing:**

- Check the relationship direction—Main Branch on Sub Branch must point to Branch
- Look for duplicate or misconfigured lookup fields
- Verify inactive records aren’t included in the filter results (filters apply regardless of record status)

**Lookup dialog is slow or unresponsive:**

- Check indexing on the Main Branch column in the Sub Branch table
- Use view filters to exclude inactive records
- Test with a smaller dataset first to isolate performance issues

## Handle multi-level hierarchies

For three or more levels (Branch → Sub Branch → Region):

1.  Create a Region lookup on Sub Branch pointing to a Region table
2.  Create a Region lookup on the next entity
3.  Filter Region based on the selected Sub Branch using the same method

Repeat this pattern for each additional level.

## Auto-clear dependent fields

When a user changes the Branch selection, any Sub Branch value that’s no longer valid should clear. Modern versions of Dynamics 365 and Power Apps handle this automatically in most cases. If you need custom behavior, configure a form script on the Branch field’s OnChange event to clear Sub Branch when Branch changes.

This filtering method works across all current Dynamics 365 versions and Power Apps. It’s the supported approach for dependent lookups without custom code, and it performs well even with large datasets when proper indexing is in place.
