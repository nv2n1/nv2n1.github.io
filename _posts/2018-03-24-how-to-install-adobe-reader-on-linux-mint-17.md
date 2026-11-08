---
title: "Installing and Configuring a PDF Reader on Linux Mint"
date: 2018-03-24 11:42:35 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-adobe-reader-on-linux-mint-17/
---

Adobe Reader (acroread) is rarely the best choice for Linux users anymore. It’s unmaintained, doesn’t receive security updates, and performs poorly compared to modern alternatives. This guide covers better options and how to set up a functional PDF viewer on Linux Mint.

## Why Not Adobe Reader?

Adobe stopped supporting Reader for Linux in 2013. The acroread package available in older repositories is outdated and no longer receives security patches. Using it exposes you to known vulnerabilities. Modern alternatives are lighter, faster, and actively maintained.

## Recommended PDF Viewers

### Evince (GNOME Documents Viewer)

Evince is lightweight, reliable, and included by default on most Linux distributions. It handles PDFs efficiently without unnecessary bloat.

``` bash
sudo apt update
sudo apt install evince
```

Set it as the default:

``` bash
xdg-mime default evince.desktop application/pdf
```

### Okular

Okular is feature-rich with support for annotations, form filling, and advanced search. It’s ideal if you work with PDFs frequently.

``` bash
sudo apt install okular
```

Set as default:

``` bash
xdg-mime default okularApplication_pdf.desktop application/pdf
```

### Firefox

If you prefer an in-browser experience, Firefox’s built-in PDF viewer works well for most use cases:

``` bash
sudo apt install firefox
xdg-mime default firefox.desktop application/pdf
```

## Installation Steps for Any Viewer

1.  **Update package lists:**

    ``` bash
    sudo apt update
    ```

2.  **Install your chosen viewer** (example: Evince):

    ``` bash
    sudo apt install evince
    ```

3.  **Verify installation:**

    ``` bash
    which evince
    ```

4.  **Set as default PDF handler:**

    ``` bash
    xdg-mime default evince.desktop application/pdf
    ```

5.  **Test it by opening a PDF:**

    ``` bash
    evince /path/to/file.pdf
    ```

## Check and Change Default PDF Viewer

View your current default handler:

``` bash
xdg-mime query default application/pdf
```

List all available PDF viewer desktop files:

``` bash
ls /usr/share/applications/ | grep -i pdf
```

Change the default by specifying the correct `.desktop` file name:

``` bash
xdg-mime default <viewer-name>.desktop application/pdf
```

## Advanced: Install from Flatseal or Snap

For the latest versions of these applications with automatic updates:

``` bash
sudo snap install okular
# or
sudo snap install evince
```

## Troubleshooting

If PDFs won’t open with your chosen viewer:

- Verify the `.desktop` file exists: `ls /usr/share/applications/ | grep viewer-name`
- Reset to system defaults: `xdg-mime query default application/pdf`
- Test from the command line: `evince file.pdf` (or your chosen viewer)
- Check file permissions: `ls -l /path/to/file.pdf`

For Mint-specific issues, ensure your desktop environment’s file manager is configured to use the system’s default handler (usually Files/Caja).

## Conclusion

Modern PDF viewers are faster, more secure, and better maintained than Adobe Reader. Evince and Okular are solid choices for most workflows. Test whichever feels fastest on your system and set it as your default.

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
