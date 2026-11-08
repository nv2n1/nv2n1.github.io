---
title: "Applying Email Sort Order to All Folders in Evolution"
date: 2018-03-24 11:55:00 +0000
author: "Eric Ma"
layout: post
categories: [functional-programming]
canonical: /how-to-apply-the-email-sort-order-to-all-folders-in-evolution/
---

Evolution stores sort preferences individually per folder by default. If you want emails consistently sorted across your entire mailbox, you need to set a global default.

## Steps

1.  Open Evolution and navigate to **Edit → Preferences**
2.  Go to **Mail Preferences → General**
3.  Locate the **Default Sorting** section
4.  Choose your preferred **Sort by** option (Date Received, Subject, Sender, etc.)
5.  Select your **Sort order** (Ascending or Descending)
6.  Click **Close** to apply

This sets the default sort behavior, but Evolution will still remember individual folder customizations if you’ve already modified them. To reset a folder to use the global default, right-click the folder, select **Properties**, and choose **Use Default Sort Order** if available, or manually reapply your preferred sort in that folder’s view menu.

## Understanding Folder-Specific Overrides

Even after setting a global default, Evolution allows per-folder sort overrides. This is useful when you want most folders sorted by Date but need a specific archive folder sorted by Subject. However, if you want uniform sorting everywhere:

- Right-click any folder and check its **Properties**
- If you’ve previously set a custom sort for that folder, Evolution prioritizes it over the global default
- Change the sort setting in the folder’s toolbar (via **View → Sort**)

## Performance Considerations

Modern mailboxes often contain hundreds of thousands of emails. Evolution uses SQLite for local indexing, which handles large-scale sorting efficiently. However:

- Sorting by Date Received is fastest since it’s indexed
- Sorting by Subject or Sender requires additional database operations
- If you notice slowdowns with deeply nested folder structures, consolidate folders or archive older mail to a separate Evolution profile

## Alternative: Using Search Instead of Sort

For large mailboxes, instead of relying on folder sort order, use Evolution’s search functionality:

- Press **Ctrl+F** to open the search bar
- Filter by sender, date range, or keywords
- Save frequent searches as **Search Folders** (right-click **Search Folders** → **New Search**)

Search Folders act as virtual folders showing results across multiple locations, which is often more efficient than manually sorting through folders when dealing with tens of thousands of emails.

## Resetting All Sort Preferences

If you want to completely reset Evolution’s sort configuration:

1.  Close Evolution

2.  Remove the sort preferences database:

    ``` bash
    rm ~/.local/share/evolution/mail/local/system/
    ```

3.  Reopen Evolution — all folders will revert to the default sort order

This is a nuclear option and will reset all folder-specific customizations, so use it only when necessary.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
