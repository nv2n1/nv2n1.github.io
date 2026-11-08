---
title: "Merging Multiple PDFs on Linux"
date: 2018-03-24 11:45:36 +0000
layout: post
canonical: https://www.systutorials.com/how-to-merge-multiple-pdf-files-to-a-pdf-on-linux/
---

Merging PDFs on Linux is straightforward with several tools available, each suited to different needs. Whether you need a quick command-line merge or want to reorder pages visually, here’s what works best.

## pdfunite: The Simplest Approach

The fastest way to merge PDFs is with `pdfunite` from poppler-utils:

``` bash
pdfunite file1.pdf file2.pdf file3.pdf output.pdf
```

Install it if needed:

``` bash
# Debian/Ubuntu
sudo apt-get install poppler-utils

# RHEL/CentOS/Fedora
sudo dnf install poppler-utils
```

Files are merged in the order you specify. This is ideal when you just need a basic concatenation without fussing with compression or metadata.

## qpdf: Control and Compression

For more control over the output, use `qpdf`:

``` bash
qpdf --empty --pages file1.pdf file2.pdf file3.pdf -- output.pdf
```

qpdf lets you reorder or extract specific page ranges:

``` bash
# Merge pages 1-5 from file1.pdf with all pages from file2.pdf
qpdf --empty --pages file1.pdf 1-5 file2.pdf -- output.pdf
```

You can also compress the output to reduce file size:

``` bash
qpdf --compress-streams=y file1.pdf file2.pdf output.pdf
```

Install qpdf:

``` bash
# Debian/Ubuntu
sudo apt-get install qpdf

# RHEL/CentOS/Fedora
sudo dnf install qpdf
```

## pdfjam: Advanced Merging and Layout

If you need to adjust page layout, scale, or create booklets, `pdfjam` is powerful:

``` bash
pdfjam file1.pdf file2.pdf -o output.pdf
```

Merge with scaling (useful for different page sizes):

``` bash
pdfjam --nup 2x1 file1.pdf file2.pdf -o output.pdf
```

Install it:

``` bash
# Debian/Ubuntu
sudo apt-get install pdfjam

# RHEL/CentOS/Fedora
sudo dnf install pdfjam
```

## PDF Arranger: Graphical Interface

For a visual approach without the command line, use PDF Arranger:

``` bash
# Debian/Ubuntu
sudo apt-get install pdf-arranger

# Fedora
sudo dnf install pdf-arranger
```

Launch it with `pdf-arranger` and drag-and-drop pages from multiple files into a single document. You can reorder, rotate, delete, or extract pages before saving.

## Batch Merging with a Script

To merge multiple pairs of PDFs or handle many files:

``` bash
#!/bin/bash
# Merge all PDFs in a directory into one file

pdfunite *.pdf merged_output.pdf
```

Or merge files matching a pattern:

``` bash
#!/bin/bash
for dir in */; do
    pdfunite "$dir"/*.pdf "$dir/merged.pdf"
done
```

## Comparing the Tools

| Tool | Speed | Features | Use Case |
|----|----|----|----|
| pdfunite | Very fast | Basic merge | Quick concatenation |
| qpdf | Fast | Compression, page ranges, encryption | Production workflows |
| pdfjam | Moderate | Layout control, scaling, booklets | Complex arrangements |
| PDF Arranger | N/A | Visual reordering, batch processing | Interactive, no CLI |

Choose `pdfunite` for simplicity, `qpdf` for control and compression, `pdfjam` for layout flexibility, and PDF Arranger if you prefer a GUI. All are lightweight and reliable for most document management tasks.

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
