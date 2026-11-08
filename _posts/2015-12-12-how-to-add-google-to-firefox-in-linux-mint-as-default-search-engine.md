---
title: "Set Google as Default Search in Firefox on Linux Mint"
date: 2015-12-12 08:13:12 +0000
modified: 2026-04-12 16:08:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-add-google-to-firefox-in-linux-mint-as-default-search-engine/
---

Firefox on Linux Mint doesn’t include Google in its default search engine list. Linux Mint deliberately curates search engines based on revenue-sharing agreements — only search engines that share ad revenue with Linux Mint appear by default. Google doesn’t participate in this arrangement, so you need to add it manually if you prefer it over the included options.

## Adding Google to Firefox

The fastest way is to use the Linux Mint Search Engines page, which hosts searchable shortcuts for popular engines.

1.  Open Firefox and navigate to `https://linuxmint.com/searchengines.php`
2.  Locate the Google option and click it
3.  Firefox will display a dropdown or popup prompting you to add Google
4.  Click **“Add Google”** to confirm

You’ll see a small green plus icon appear in the Firefox search bar once the engine is added successfully.

## Setting Google as Default

After adding Google, make it your default search engine:

1.  Open Firefox preferences in a new tab: `about:preferences#search`
2.  Under **“Default Search Engine,”** select **Google** from the dropdown menu
3.  Your changes save automatically

## Alternative: Manual Search Engine Addition

If you prefer not to use the Linux Mint page, you can add Google directly:

1.  Visit `https://www.google.com` in Firefox
2.  Right-click the address bar and select **“Add Search Engine”**
3.  Firefox will prompt you to confirm — click **Add**

This works for any website with a searchable interface. Google will then appear in your search engine list.

## Verify the Change

To confirm Google is now your default:

1.  Click the search bar in a new tab — it should show the Google logo
2.  Type a search term and press Enter — results should come from Google

## Why Remove Other Search Engines?

Linux Mint’s defaults include DuckDuckGo, Ecosia, and others. If you want to clean up your search engine list and only keep Google:

1.  Go to `about:preferences#search` again
2.  Hover over unwanted engines — a trash icon appears
3.  Click the trash icon to remove them

## Note on Linux Mint’s Philosophy

Linux Mint prioritizes search engines that contribute revenue back to the project. This funds development and keeps the distribution free. If you’re comfortable with alternatives like DuckDuckGo (privacy-focused) or Ecosia (environmental), consider keeping them in rotation. However, Google remains fully functional and available in Linux Mint’s Firefox — there’s no restriction preventing its use.

Your choice of search engine doesn’t affect Firefox’s performance or Linux Mint’s functionality either way.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
