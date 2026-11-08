---
title: "Where Windows 10 Stores Metro App Data"
date: 2018-03-24 11:50:30 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /where-are-the-data-of-metro-apps-stored-in-windows-10/
---

Modern Universal Windows Platform (UWP) apps store their data in protected user-specific directories. Understanding this structure is essential if you need to back up app settings, troubleshoot issues, or migrate data between systems.

## Default Data Location

UWP app data lives here:

    C:\Users\<YourUsername>\AppData\Local\Packages\<AppPackageName>\

The `<AppPackageName>` is a unique identifier assigned by Windows—typically a long alphanumeric string like `Microsoft.WindowsCalculator_8wekyb3d8bbwe`. This naming convention ensures apps from different publishers don’t collide.

## Directory Structure Within Packages

Inside each package folder, you’ll typically find:

- **LocalState/** — app settings, caches, and local data
- **RoamingState/** — data that syncs across devices (if the app supports it)
- **AC/** — application cache
- **TempState/** — temporary files (safe to delete)

Some apps create additional subdirectories for specific data types (databases, logs, etc.).

## Accessing Protected Folders

These directories are permission-locked by default. File Explorer will show “Access Denied” errors. To browse them:

**Option 1: Take Ownership via Properties**

Right-click the folder → Properties → Security → Advanced → Change Owner → type your username → Check Names → OK. Then edit permissions to grant yourself full control.

**Option 2: Use Command Line as Administrator**

``` bash
takeown /F "C:\Users\<YourUsername>\AppData\Local\Packages\<AppPackageName>" /R /D Y
icacls "C:\Users\<YourUsername>\AppData\Local\Packages\<AppPackageName>" /grant:r "%USERNAME%:F" /T
```

This recursively takes ownership and grants full permissions.

**Option 3: PowerShell One-Liner**

``` powershell
Get-ChildItem -Path "C:\Users\$env:USERNAME\AppData\Local\Packages" | Where-Object {$_.PSChildName -like "*Calculator*"} | Select-Object FullName
```

Replace `Calculator` with the app name you’re looking for. This helps locate the exact package folder if you’re unsure of the full package name.

## Finding Your App’s Package Name

If you don’t know the exact package name, use PowerShell:

``` powershell
Get-AppxPackage | Where-Object {$_.Name -like "*YourAppName*"} | Select-Object Name, PackageFullName
```

This lists all installed packages matching your search term with their full names.

## Backup and Restore

To back up an app’s data:

``` bash
robocopy "C:\Users\<YourUsername>\AppData\Local\Packages\<AppPackageName>" "D:\backup\<AppPackageName>" /E /COPYALL
```

The `/E` flag copies all subdirectories (including empty ones), and `/COPYALL` preserves permissions and attributes.

To restore, reverse the source and destination:

``` bash
robocopy "D:\backup\<AppPackageName>" "C:\Users\<YourUsername>\AppData\Local\Packages\<AppPackageName>" /E /COPYALL
```

## Cleaning Up

Old or uninstalled app data may remain. To safely remove orphaned package folders after uninstalling an app:

``` powershell
$packagePath = "C:\Users\$env:USERNAME\AppData\Local\Packages\<AppPackageName>"
Remove-Item -Path $packagePath -Recurse -Force
```

**Caution:** Only remove packages you’ve verified are uninstalled. Removing active app data breaks the app.

## Important Notes

- Windows 11 uses the same structure as Windows 10, so these paths remain consistent
- Some enterprise-managed systems may have different permissions or storage policies
- OneDrive integration can sync some app data; check app settings for cloud backup options
- Portable or sideloaded apps may store data differently—check their documentation

## 2026 Best Practices and Advanced Techniques

For Where Windows 10 Stores Metro App Data, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
