---
title: "Extract Files from a .deb Package Without Installing"
date: 2018-03-24 11:43:56 +0000
modified: 2026-04-12 07:57:19 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-list-all-files-from-a-deb-package/
---

\[md\]
When you need to inspect what files a .deb package contains or will install, `dpkg` is your primary tool. This is useful for understanding package contents before installation, checking what files a package added to your system, or troubleshooting file conflicts.

\## Listing Files in an Installed Package

If the package is already installed on your system:

```wp-block-code
dpkg -L package-name
```

This lists all files the package owns, including configuration files, binaries, libraries, and documentation. For example:

```wp-block-code
dpkg -L curl | head -20
```

\## Listing Files in a .deb File (Not Installed)

To inspect a .deb file before installing it:

```wp-block-code
dpkg-deb -c package.deb
```

This shows the file listing with permissions, ownership, and size — similar to `tar -tvf` output. The format shows:

– File permissions (drwxr-xr-x for directories, -rw-r–r– for files)
– Owner and group
– File size
– Full installation path

To see just the file names without metadata:

```wp-block-code
dpkg-deb -c package.deb | awk '{print $NF}'
```

\## Using apt-file for Remote Packages

If you don’t have the .deb file downloaded and the package isn’t installed:

```wp-block-code
sudo apt install apt-file
sudo apt-file update
apt-file list package-name
```

This queries the package repository database to show what files the package would install. It works for any package in your configured repositories, even if you haven’t installed it.

\## Using ar and tar for Manual Extraction

A .deb file is actually an `ar` archive. You can manually extract and inspect it:

```wp-block-code
# Extract the .deb archive
ar x package.deb

# This creates three files:
# debian-binary  - format version
# control.tar.*  - package metadata and install scripts
# data.tar.*     - actual files to be installed

# List files in the data archive
tar -tzf data.tar.gz     # gzip compressed
tar -tJf data.tar.xz     # xz compressed
tar -tjf data.tar.bz2    # bzip2 compressed
```

To extract just the data files to a temporary directory for inspection:

```wp-block-code
mkdir /tmp/pkg-inspect
tar -xzf data.tar.gz -C /tmp/pkg-inspect
find /tmp/pkg-inspect -type f
```

\## Inspecting Package Metadata

The control archive contains useful metadata:

```wp-block-code
# Extract control information
ar x package.deb
tar -xzf control.tar.gz ./control

# View package metadata
cat control
```

This shows the package name, version, dependencies, maintainer, description, and other metadata that `dpkg` uses.

\## Find Which Package Owns a File

If you have a file on your system and want to know which package installed it:

```wp-block-code
dpkg -S /path/to/file
```

Examples:

```wp-block-code
dpkg -S /usr/bin/curl        # curl: /usr/bin/curl
dpkg -S /etc/nginx/nginx.conf  # nginx-common: /etc/nginx/nginx.conf
```

You can also search by filename pattern:

```wp-block-code
dpkg -S '*/bin/curl'
```

\## Common Use Cases

\*\*Check what a package will install before installing:\*\*

```wp-block-code
apt-file list nginx
```

\*\*Verify all files from an installed package are intact:\*\*

```wp-block-code
dpkg -V package-name
```

This checks file checksums against the package database and reports any modifications.

\*\*List only configuration files:\*\*

```wp-block-code
dpkg -L package-name | grep /etc/
```

\*\*List only executables:\*\*

```wp-block-code
dpkg -L package-name | grep bin/
```

\## One-Command Summary

Quick reference for the most common operations:

– `dpkg -L pkg` — list files from installed package
– `dpkg-deb -c file.deb` — list files in .deb archive
– `dpkg -S /path` — find which package owns a file
– `dpkg -V pkg` — verify installed files
– `apt-file list pkg` — list files from remote package
