---
title: "Conditional Dropdown Filtering in Dynamics 365: Filter Salutation by Gender"
date: 2016-12-15 11:02:30 +0000
layout: post
canonical: https://www.systutorials.com/filter-salutation-microsoft-dynamics-crm/
---

Filtering dependent fields based on parent field values is a common requirement in Dynamics 365 CRM. This guide walks through implementing conditional filtering so the salutation dropdown only shows values relevant to the selected gender.

## Prerequisites

- Access to a Dynamics 365 environment (2016 or later) with customization rights
- Basic understanding of option sets and form events
- Familiarity with JavaScript and the Xrm client API
- Admin access to publish customizations

## Create the Option Set Fields

Navigate to **Settings \> Customization \> Customize the System** and select the Contact entity.

Create the Gender field:

- **Name**: new_gender
- **Display Name**: Gender
- **Type**: Option Set
- **Options**: Male, Female, Other

Create the Salutation field:

- **Name**: new_salutation
- **Display Name**: Salutation
- **Type**: Option Set
- **Options**: Mr, Mrs, Ms, Dr, Prof

Document the numeric values assigned to each option—these are environment-specific and needed for the filtering logic. You’ll find these values in the option set configuration.

## Add Fields to the Form

Open the Contact form in the form editor, drag both the Gender and Salutation fields to your desired layout, then save and publish.

## Create the JavaScript Web Resource

Create a new JavaScript web resource with the filtering logic. This script runs when the gender field changes and updates available salutation options.

``` javascript
function filterSalutationByGender() {
    var formContext = Xrm.getFormContext();
    var genderValue = formContext.getAttribute("new_gender").getValue();
    var salutationControl = formContext.getControl("new_salutation");

    if (salutationControl === null) {
        console.warn("Salutation control not found on form");
        return;
    }

    var salutationAttribute = formContext.getAttribute("new_salutation");

    // Clear current salutation value when gender changes
    salutationAttribute.setValue(null);

    // Define salutation options based on gender
    var salutationOptions = [];

    if (genderValue === 1) { // Male
        salutationOptions = [
            { value: 1, text: "Mr" },
            { value: 4, text: "Dr" },
            { value: 5, text: "Prof" }
        ];
    } else if (genderValue === 2) { // Female
        salutationOptions = [
            { value: 2, text: "Mrs" },
            { value: 3, text: "Ms" },
            { value: 4, text: "Dr" },
            { value: 5, text: "Prof" }
        ];
    } else if (genderValue === 3) { // Other
        salutationOptions = [
            { value: 1, text: "Mr" },
            { value: 2, text: "Mrs" },
            { value: 3, text: "Ms" },
            { value: 4, text: "Dr" },
            { value: 5, text: "Prof" }
        ];
    }

    // Clear and repopulate the salutation dropdown
    salutationControl.clearOptions();
    salutationOptions.forEach(function(option) {
        salutationControl.addOption(option);
    });
}
```

This uses `Xrm.getFormContext()` for modern Dynamics 365 compatibility and works across cloud and on-premises deployments.

## Register the Web Resource

Navigate to **Settings \> Customization \> Web Resources** and click **New**.

Fill in:

- **Name**: new_SalutationFilter
- **Display Name**: Salutation Filter
- **Type**: Script (JavaScript)
- **Upload** your JavaScript file

Save and publish the web resource.

## Add the Event Handler

Open the Contact form in the form editor and select the Gender field.

In the **Events** tab:

1.  Under **Form Libraries**, click **Add** and select the new_SalutationFilter web resource
2.  Click **Add** under **Event Handlers**
3.  Configure:
    - **Event**: OnChange
    - **Library**: new_SalutationFilter
    - **Function**: filterSalutationByGender
    - **Enabled**: Yes

Save and publish the form.

## Testing

1.  Create or open a Contact record
2.  Select a value in the Gender field
3.  Verify the Salutation dropdown updates to show only relevant options
4.  Switch between different gender values and confirm filtering works
5.  Confirm that changing gender clears any previously selected salutation

## Troubleshooting

**Filtering doesn’t work**: Verify option set values match your JavaScript. Open each option set field and confirm the numeric values—these are environment-specific.

**JavaScript errors**: Press F12 to open browser developer tools and check the console for errors. Look for null reference errors or missing function names.

**Changes don’t take effect**: Web resource changes require publishing. Verify the web resource status is published and clear your browser cache (Ctrl+Shift+Delete).

**Event handler not firing**: Open the form editor and confirm the OnChange handler for the Gender field is set to **Enabled: Yes**.

## Using Global Option Sets

For better maintainability, use Global Option Sets instead of local ones. This allows updates in a single location to propagate across all forms using those options. The JavaScript logic remains identical—only the configuration differs.

## Dynamic Salutation Options

If your salutations need to be fetched from the server rather than hardcoded, enhance the script to use the Web API:

``` javascript
function filterSalutationByGenderDynamic() {
    var formContext = Xrm.getFormContext();
    var genderValue = formContext.getAttribute("new_gender").getValue();
    var salutationControl = formContext.getControl("new_salutation");

    if (!salutationControl || !genderValue) {
        return;
    }

    formContext.getAttribute("new_salutation").setValue(null);

    // Fetch filtered options from the server
    var fetchXml = "?$filter=new_genderfilter eq " + genderValue;

    formContext.webAPI.retrieveMultipleRecords("new_salutationoption", fetchXml)
        .then(function(result) {
            salutationControl.clearOptions();
            result.records.forEach(function(record) {
                salutationControl.addOption({
                    value: record.new_salutationoptionid,
                    text: record.new_name
                });
            });
        })
        .catch(function(error) {
            console.error("Failed to retrieve salutation options: " + error.message);
        });
}
```

This approach works well when salutation rules change frequently or are stored in custom tables.
