---
title: "Renaming a Windows User Account in Local Users and Groups"
date: 2019-07-14 06:05:04 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-windows-user-name-on-windows-10-using-computer-management/
---

The Windows user account name can be changed through several methods, but Computer Management’s Local Users and Groups tool is the most reliable approach—its interface remains stable across Windows updates, unlike Settings which frequently changes.

## Open Local Users and Groups

Right-click the Windows Start button and select **Computer Management**. This opens the management console.

In the left navigation panel, navigate to:

- System Tools → Local Users and Groups → Users

You’ll see a list of all local user accounts on the system.

## Rename the User Account

Right-click the user account you want to rename and select **Rename** from the context menu. Type the new account name and press Enter.

**Important notes:**

- The new name takes effect on the next login
- Only administrators can rename user accounts
- You can rename any local user account, not just the current one
- This changes only the display name used in the user list, not the user’s home directory folder path (which remains unchanged)

## Alternative: Using Command Line

If you prefer the command line, you can rename an account using `net user`:

``` bash
net user "OldUsername" "NewUsername"
```

For example:

``` bash
net user "john" "john_smith"
```

Run Command Prompt as Administrator for this method. You’ll receive confirmation that the command executed successfully.

## Alternative: Using PowerShell

PowerShell offers more control:

``` powershell
Rename-LocalUser -Name "OldUsername" -NewName "NewUsername"
```

For example:

``` powershell
Rename-LocalUser -Name "john" -NewName "john_smith"
```

Run PowerShell as Administrator. This method provides error handling and is suitable for scripting bulk renames.

## When Home Directory Path Matters

If you need the home directory folder to match the new account name, you’ll need to manually rename the folder at `C:\Users\OldUsername` to `C:\Users\NewUsername`. Do this after renaming the account, then update the registry path at:

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

Find the registry key corresponding to your user’s Security Identifier (SID) and update the ProfilePath value. This is complex—only do this if necessary for specific applications.

## Considerations

- Avoid renaming the built-in Administrator account unnecessarily
- If applications store user-specific settings tied to the old account name, you may need to reconfigure them
- Network shares and permissions based on the old account name will still work—Windows tracks accounts by Security Identifier (SID), not the display name
- Domain accounts cannot be renamed through Local Users and Groups; use Active Directory Users and Computers instead

The Computer Management method remains the most straightforward approach for most users, requiring no command line knowledge and providing immediate visual confirmation.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
