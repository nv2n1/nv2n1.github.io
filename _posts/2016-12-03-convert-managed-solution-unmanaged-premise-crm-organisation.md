---
title: "Converting Managed Solutions to Unmanaged in Dynamics CRM"
date: 2016-12-03 06:01:37 +0000
modified: 2026-04-11 17:15:58 +0000
author: "jameswarner"
layout: post
categories: [algorithms-data-structures]
canonical: /convert-managed-solution-unmanaged-premise-crm-organisation/
---

Converting a managed solution to unmanaged in on-premise Dynamics CRM requires direct database modification. You’ll need this when customizing third-party solutions that the publisher hasn’t provided in unmanaged form, or when you need to export and modify components before deployment.

## Prerequisites

- Full database backup (this modifies system tables — non-negotiable)
- SQL Server Management Studio or equivalent query tool with direct database access
- The managed solution already imported into your organization
- The solution’s unique name from Settings \> Solutions (not the display name)
- A test environment for validation before production work

## Back Up Your Database

Before running any SQL, take a full backup:

``` powershell
sqlcmd -S <SERVER> -U <USERNAME> -P <PASSWORD> -Q "BACKUP DATABASE [OrganizationName_MSCRM] TO DISK = 'D:\Backups\PreUnmanage_$(Get-Date -Format yyyyMMdd_HHmmss).bak'"
```

This is mandatory. Database modifications can’t be undone without a backup.

## Run the Conversion Script

Connect to your CRM database and execute this T-SQL script. Replace `YOUR_SOLUTION_UNIQUE_NAME` with your actual solution’s unique name (case-sensitive):

``` sql
DECLARE @solutionId UNIQUEIDENTIFIER
DECLARE @systemSolutionId UNIQUEIDENTIFIER

-- Replace with your managed solution's unique name
SELECT @solutionId = solutionid
FROM SolutionBase
WHERE UniqueName = 'YOUR_SOLUTION_UNIQUE_NAME'

-- Verify the solution exists
IF @solutionId IS NULL
BEGIN
  RAISERROR('Solution not found. Verify the unique name and try again.', 16, 1)
  RETURN
END

PRINT 'Found solution: ' + CAST(@solutionId AS NVARCHAR(100))

-- Get the Active solution ID
SELECT @systemSolutionId = solutionid
FROM SolutionBase
WHERE UniqueName = 'Active'

-- Unlock the publisher
UPDATE PublisherBase SET IsReadonly = 0
WHERE PublisherId IN (SELECT PublisherId FROM SolutionBase WHERE SolutionId = @solutionId)

PRINT 'Unlocked publisher'

DECLARE @tables TABLE (
  id INT IDENTITY,
  NAME NVARCHAR(100),
  ismanaged BIT,
  issolution BIT
)

DECLARE @count INT, @currentTable NVARCHAR(100), @currentM BIT, @currentS BIT, @sql NVARCHAR(max)

-- Find all tables with IsManaged column
INSERT INTO @tables (NAME, ismanaged, issolution)
SELECT NAME, 1, 0
FROM sysobjects
WHERE id IN (SELECT id FROM syscolumns WHERE NAME = 'IsManaged')
AND type = 'U'
ORDER BY NAME

-- Find all tables with SolutionId column (except SolutionComponentBase)
INSERT INTO @tables (NAME, ismanaged, issolution)
SELECT NAME, 0, 1
FROM sysobjects
WHERE id IN (SELECT id FROM syscolumns WHERE NAME = 'SolutionId')
AND type = 'U'
AND NAME NOT IN ('SolutionComponentBase')
ORDER BY NAME

SELECT @count = COUNT(*)
FROM @tables

-- Process each table
WHILE (@count > 0)
BEGIN
  SELECT @currentTable = NAME, @currentM = ismanaged, @currentS = issolution
  FROM @tables
  WHERE id = @count

  IF (@currentM = 1)
  BEGIN
    SELECT @sql = 'UPDATE ' + @currentTable + ' SET IsManaged = 0 WHERE SolutionId = N''' + CAST(@solutionId AS NVARCHAR(100)) + ''''
    EXEC (@sql)
    PRINT 'Updated IsManaged to 0 on: ' + @currentTable
  END

  IF (@currentS = 1)
  BEGIN
    SELECT @sql = 'UPDATE ' + @currentTable + ' SET SolutionId = N''' + CAST(@systemSolutionId AS NVARCHAR(100)) + ''' WHERE SolutionId = N''' + CAST(@solutionId AS NVARCHAR(100)) + ''''
    EXEC (@sql)
    PRINT 'Updated SolutionId on: ' + @currentTable
  END

  SELECT @count = @count - 1, @currentTable = NULL
END

PRINT 'Conversion complete'
```

The script performs three operations:

1.  Locates your managed solution in the database
2.  Unlocks the publisher (sets `IsReadonly = 0`)
3.  Iterates through all solution component tables, flipping `IsManaged` from 1 to 0 and reassigning components to the Active solution

## Extract and Clean Solution XML

After the SQL script completes, export the solution and modify the package:

Export the solution through the CRM UI (**Settings \> Solutions \> your solution \> Export**).

Extract the ZIP archive:

``` bash
unzip solution.zip -d solution_extracted/
cd solution_extracted
```

Edit `solution.xml` and remove all `<MissingDependency>` elements:

``` bash
grep -n "MissingDependency" solution.xml
nano solution.xml
```

Look for and delete these blocks entirely:

``` xml
<MissingDependency>
 <Required solution="SomeSolution" />
</MissingDependency>
```

Missing dependencies can cause import failures if those solutions aren’t actually installed. Only remove them if you’re certain the referenced solutions will be available in your deployment environment.

Repackage the solution:

``` bash
zip -r ../solution_modified.zip *
cd ..
```

Import the modified solution back into CRM (**Settings \> Solutions \> Import**).

## Verify the Conversion

Confirm the solution is now unmanaged:

- Open the solution in CRM and attempt to edit a component (button, field, form, etc.)
- Export the solution again — managed solutions cannot be exported
- Check that no read-only warnings appear when publishing customizations
- Query the database to verify the flag changed:

``` sql
SELECT UniqueName, IsManaged FROM SolutionBase WHERE UniqueName = 'YOUR_SOLUTION_UNIQUE_NAME'
```

This should return `IsManaged = 0`.

## Critical Warnings

**Cloud/Online environments:** This only works on on-premise Dynamics CRM. Microsoft Dynamics 365 online uses managed identity and licensing models that prevent this approach entirely.

**MissingDependency elements:** Removing these tags is risky. These dependencies exist because the solution references features from other solutions. If you remove the tag but the dependency is actually needed, your customizations will fail at runtime. Only remove them if you’re certain those solutions will be available in your target environment.

**Licensing restrictions:** Some publishers restrict unmanaging in their licensing agreements. Premium solutions may have contractual restrictions on modification. Check your agreement before proceeding.

**Always test first:** A broken solution in production can take down critical business processes. Run this entire procedure in a test environment and verify functionality before touching anything live.

**The Active solution is permanent:** Once you’ve reassigned components to the Active solution, you cannot convert them back to a managed solution without re-creating the entire solution package.

**Use as a last resort:** Only use this approach when you genuinely need to modify a third-party solution and cannot obtain an unmanaged version from the publisher.
