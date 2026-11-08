---
title: "Printing Text Files from Linux Terminal with lp and CUPS"
date: 2018-03-24 08:21:12 +0000
modified: 2026-04-11 16:03:47 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-print-a-plain-text-file-to-printers-from-a-terminal-in-linux/
---

The `lp` command is the standard tool for printing from the Linux command line. It interfaces with CUPS (Common Unix Printing System), the printing backbone on virtually all modern Linux distributions.

## Basic Printing

Send a file to your default printer:

``` bash
lp text-file.txt
```

Specify a particular printer:

``` bash
lp -d printer-name text-file.txt
```

List available printers and identify the default:

``` bash
lpstat -p -d
```

## Formatting Options

Use the `-o` flag to control paper size, density, and margins. Margins are in points (72 points = 1 inch):

``` bash
lp -o media=a4 -o cpi=12 -o lpi=7.2 \
   -o page-left=48 -o page-right=48 \
   -o page-top=48 -o page-bottom=48 text-file.txt
```

Common options:

- `media=a4|letter|legal` — paper size
- `cpi=10|12|17` — characters per inch
- `lpi=6|8|7.2` — lines per inch
- `page-left|right|top|bottom=N` — margins in points
- `sides=one-sided|two-sided-long-edge|two-sided-short-edge` — duplex printing
- `number-up=2|4|6|9|16` — multiple logical pages per sheet

Print on both sides with 2-up layout:

``` bash
lp -o sides=two-sided-long-edge -o number-up=2 text-file.txt
```

## Print Queue Management

View the current print queue:

``` bash
lpstat -o
```

Cancel a specific job:

``` bash
cancel job-id
```

Cancel all jobs for a printer:

``` bash
cancel -a printer-name
```

## Piping and Redirection

Print command output directly without creating a file:

``` bash
cat text-file.txt | lp
ps aux | lp
dmesg | lp -o media=letter
```

## Using enscript for Advanced Formatting

For more sophisticated text-to-print conversion, `enscript` preprocesses files before sending to the printer. It supports syntax highlighting, headers/footers, and complex layouts:

``` bash
# Print with syntax highlighting (no header banner)
enscript -B -E text-file.txt

# Print 2 logical pages per physical sheet
enscript -B -2 text-file.txt

# Output to PostScript file first, then print
enscript -B text-file.txt -p output.ps
lp output.ps
```

Common `enscript` options:

- `-B` — suppress header banner
- `-2` — print 2 logical pages per physical page
- `-4` — print 4 logical pages per physical page
- `-E` — enable syntax highlighting for C, C++, and Python
- `-p <file>` — write PostScript to file (use `-p -` for stdout)
- `-f fontname` — change font
- `-M <margins>` — set margins (format: top:bottom:left:right)

Pipe directly to printer:

``` bash
enscript -B -E - | lp
```

## Creating a Print Wrapper Script

For repeated printing with consistent formatting, write a shell script:

``` bash
#!/bin/bash
# save as ~/bin/print-formatted
# usage: print-formatted [printer] <file>

PRINTER="${1:-default}"
FILE="${2}"

if [ ! -f "$FILE" ]; then
    echo "Error: file '$FILE' not found"
    exit 1
fi

if [ "$PRINTER" = "default" ] && [ -z "$2" ]; then
    FILE="$1"
fi

lp -d "$PRINTER" \
    -o media=a4 \
    -o cpi=12 \
    -o lpi=7.2 \
    -o page-left=48 \
    -o page-right=48 \
    -o page-top=48 \
    -o page-bottom=48 \
    "$FILE"
```

Make it executable:

``` bash
chmod +x ~/bin/print-formatted
```

Use it:

``` bash
print-formatted myfile.txt
print-formatted my-printer myfile.txt
```

## Installation and Troubleshooting

If `lp` is unavailable, install CUPS:

**Debian/Ubuntu:**

``` bash
sudo apt install cups cups-client
```

**RHEL/Fedora/Rocky/CentOS:**

``` bash
sudo dnf install cups cups-client
```

Start the CUPS daemon if it’s not running:

``` bash
sudo systemctl enable cups
sudo systemctl start cups
sudo systemctl status cups
```

### Access Denied Errors

If you can’t print, you may lack permission to access the printer. Add your user to the `lpadmin` group:

``` bash
sudo usermod -aG lpadmin $USER
```

Log out and back in, or start a new shell session:

``` bash
su - $USER
```

Verify group membership:

``` bash
groups
```

### Check CUPS Socket and Permissions

If the `lpadmin` group addition doesn’t resolve the issue, check that the CUPS socket is accessible:

``` bash
ls -l /run/cups/cups.sock
```

The socket should have group `lpadmin` with read/write permissions. If permissions are wrong, CUPS may not have started properly—restart it:

``` bash
sudo systemctl restart cups
```
