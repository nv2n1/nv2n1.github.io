---
title: "Upgrading Fedora with dnf system-upgrade: A Complete Guide"
date: 2018-03-24 08:21:39 +0000
layout: post
canonical: https://www.systutorials.com/how-to-upgrade-fedora-19-to-fedora-20-through-the-network/
---

Fedora upgrades are straightforward with `dnf system-upgrade`, the standard tool for network-based distribution upgrades. This replaces the older `fedup` tool and handles everything from downloading packages to managing the upgrade environment.

## Pre-Upgrade Checklist

Before starting any upgrade:

- **Update your current system**: `sudo dnf upgrade`
- **Back up critical data** — especially `/etc`, home directories, and application configs
- **Check the release notes** at <a href="https://docs.fedoraproject.org/en-US/docs/" rel="nofollow noopener" target="_blank">https://docs.fedoraproject.org/en-US/docs/</a>
- **Review the Fedora wiki** for known issues with your target release
- **Verify disk space**: at least 2-3 GB free in `/var` and `/usr`
- **Ensure stable network connectivity** — upgrades can be 1-2 GB depending on installed packages
- **Disable unnecessary services** that might interfere (optional but recommended)

## Handling Third-Party Repositories

Third-party repositories are a common source of upgrade failures. Before starting:

``` bash
sudo dnf repolist
```

Identify any non-standard repositories. You have two options:

**Option 1: Disable before upgrade**

``` bash
sudo dnf config-manager --set-disabled repo-id
```

**Option 2: Remove entirely**

``` bash
sudo dnf remove @repo-id  # if using module-based repos
```

Common problem repositories include those for proprietary software (Chrome, Nvidia drivers, multimedia codecs). Check their documentation for compatibility with your target Fedora version — many need reinstallation after major upgrades anyway.

## Preparation: Download Upgrade Packages

First, install the upgrade plugin if not present:

``` bash
sudo dnf install dnf-plugin-system-upgrade
```

Then download all packages for your target version without applying changes:

``` bash
sudo dnf system-upgrade download --releasever=42
```

Replace `42` with your target Fedora version. This step is safe to interrupt and resume — if your connection drops, just run the command again.

Watch for any dependency conflicts or unresolvable packages during download. Address these before proceeding. The download typically takes 10-30 minutes depending on your system and connection speed.

## Execute the Upgrade

Once the download completes successfully:

``` bash
sudo dnf system-upgrade reboot
```

Your system reboots into a special upgrade environment. The upgrade process runs automatically at boot and typically takes 15-30 minutes. **Do not interrupt this process** — a failed upgrade mid-transaction can leave your system in an inconsistent state.

Monitor progress by watching the boot messages. You’ll see package installation progress and any errors that occur.

## Post-Upgrade Tasks

After your system reboots normally back into the new Fedora version, complete the upgrade:

``` bash
sudo dnf distro-sync
sudo dnf autoremove
```

The `distro-sync` command ensures all installed packages match versions in your new release’s repositories. The `autoremove` command removes packages no longer needed by anything else on your system.

Verify the upgrade succeeded:

``` bash
cat /etc/fedora-release
rpm -qa | wc -l
```

Re-enable any third-party repositories you disabled earlier, but be prepared to reinstall some packages:

``` bash
sudo dnf config-manager --set-enabled repo-id
sudo dnf check-update
```

For proprietary software that doesn’t auto-update:

``` bash
sudo dnf remove google-chrome-*
sudo dnf install google-chrome-stable
```

## Troubleshooting Failed Upgrades

If the upgrade fails or gets stuck:

``` bash
sudo dnf system-upgrade clean
```

This cleans up partial downloads. Then retry:

``` bash
sudo dnf system-upgrade download --releasever=42
sudo dnf system-upgrade reboot
```

For detailed failure information, check the upgrade logs from your previous boot:

``` bash
sudo journalctl -b -1 -u dnf-system-upgrade
sudo journalctl -b -1 | grep -i error
```

Common issues and fixes:

- **Broken dependencies**: Run `sudo dnf install --best --allowerasing` before retrying the upgrade
- **Stuck packages**: Use `sudo dnf remove <package>` to uninstall problematic packages, then upgrade and reinstall them afterward
- **SELinux denials**: Check `/var/log/audit/audit.log` if you have SELinux in enforcing mode

For persistent problems, file a bug at <a href="https://bugzilla.redhat.com/" rel="nofollow noopener" target="_blank">https://bugzilla.redhat.com/</a> with your logs attached. Include output from `sudo dnf system-upgrade log` if available.

## Skipping Fedora Versions

You can technically skip multiple releases in one upgrade, but sequential upgrades are safer. Each Fedora release receives security updates for roughly 13 months. If you’re more than 2-3 releases behind, consider upgrading incrementally to catch any repository or package issues that might have been fixed in intermediate releases.
