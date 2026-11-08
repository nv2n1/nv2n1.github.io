---
title: "Preventing dnf/yum from Updating Specific Packages"
date: 2013-07-12 16:32:07 +0000
layout: post
canonical: https://www.systutorials.com/making-dnf-yum-not-update-certain-packages/
---

You may need to prevent certain packages from being updated during system maintenance—the kernel on production servers, or specific library versions you’ve carefully tuned. When you run `dnf update` or `yum update`, you want those packages skipped entirely.

The solution is straightforward: add an exclusion to DNF or YUM’s configuration file.

## Configuration Syntax

Add this line to the appropriate config file:

    exclude=package_names package_name_pattern

Package names are space-separated. Shell globbing with `*` and `?` wildcards works:

    exclude=kernel* nss nss-* mysql-community-server

This example excludes:

- All kernel packages (`kernel*`)
- The `nss` package exactly
- All nss-related packages (`nss-*`)
- The mysql-community-server package

## Configuration Files

### DNF (Fedora, RHEL 9+, CentOS Stream)

Edit `/etc/dnf/dnf.conf`:

``` ini
[main]
gpgcheck=1
installonly_limit=3
exclude=kernel* nss nss-* mysql-server*
```

Add the `exclude` line under the `[main]` section if it doesn’t exist.

### YUM (Legacy RHEL/CentOS systems)

Edit `/etc/yum.conf`:

``` ini
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
exclude=kernel* nss nss-*
```

## Verification

Test your exclusions before a full system update:

``` bash
dnf check-update | grep -i kernel
```

This shows which kernel updates would be applied. If your exclusion works, nothing kernel-related appears.

Run the dry-run:

``` bash
dnf update --assumeno
```

Review the output to confirm excluded packages are skipped.

## Per-Command Exclusion

For one-off updates without modifying config:

``` bash
dnf update --exclude='kernel*' --exclude='mysql-server*'
```

Or with yum:

``` bash
yum update --exclude='kernel*'
```

## Excluding Installonly Packages

The kernel and some other packages use DNF’s `installonly_limit` setting—they’re designed to keep multiple versions installed. These packages don’t remove old versions during updates; they install alongside.

Check which packages are treated as installonly:

``` bash
grep -i installonlychanges /etc/dnf/dnf.conf
```

For most systems, kernel is already handled specially. If you want to prevent kernel installation entirely (rare, but sometimes needed for testing), exclude it as shown above.

## Re-enabling Updates

To remove an exclusion, either:

1.  Edit the config file and delete the `exclude` line
2.  Use `dnf config-manager` to modify it:

``` bash
dnf config-manager --save-config --set-enabled=* 
```

Then manually edit `/etc/dnf/dnf.conf` to remove the `exclude` directive.

## Important Considerations

**Security updates**: Excluding packages may leave you vulnerable to security fixes. Review excluded packages regularly and allow security updates even if you skip minor version bumps.

**Dependency conflicts**: Excluding packages can cause dependency resolution failures during updates. Test updates in a staging environment first.

**Multiple exclusion lines**: Only the last `exclude=` line is used. Put all exclusions on one line or use commas:

    exclude=kernel*,nss,nss-*,mysql-server*

**Repositories**: Exclusions apply system-wide. If you need per-repository exclusions, use repository-specific configuration in `/etc/dnf/repos.d/`:

``` ini
[fedora]
name=Fedora $releasever - $basearch
exclude=kernel*
```

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
