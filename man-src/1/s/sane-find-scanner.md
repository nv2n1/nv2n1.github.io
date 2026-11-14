---
title: "sane-find-scanner(1)"
name: "sane-find-scanner"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sane-find-scanner/"
description: "sane-find-scanner – find SCSI and USB scanners and their device files"
---

<h2 class="name">NAME</h2>
<p> sane-find-scanner &#8211; find SCSI and USB scanners and their device files </p>
<h2>SYNOPSIS</h2>
<p> <code>sane-find-scanner</code> [<code>-?</code>|<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>] [<code>-q</code>] [<code>-p</code>] [<code>-f</code>] [<code>-F</code> <i>filename</i>] [<i>devname</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>sane-find-scanner</code> is a command-line tool to find SCSI and USB scanners and determine their UNIX device files. Its primary aim is to make sure that scanners can be detected by SANE backends. </p>
<p> For <code>SCSI</code> scanners, it checks the default generic SCSI device files (e.g., <i>/dev/sg0</i>) and <i>/dev/scanner</i>. The test is done by sending a SCSI inquiry command and looking for a device type of &quot;scanner&quot; or &quot;processor&quot; (some old HP scanners seem to send &quot;processor&quot;). So <code>sane-find-scanner</code> will find any SCSI scanner connected to those default device files even if it isn&#8217;t supported by any SANE backend. </p>
<p> For <code>USB</code> scanners, first the USB kernel scanner device files (e.g. <i>/dev/usb/scanner0</i>, <i>/dev/usb/scanner</i>, and <i>/dev/usbscanner</i>) are tested. The files are opened and the vendor and device ids are determined, if the operating system supports this feature. Currently USB scanners are only found this way if they are supported by the Linux scanner module or the FreeBSD or OpenBSD uscanner driver. After that test, <code>sane-find-scanner</code> tries to scan for USB devices found by the USB library libusb (if available). There is no special USB class for scanners, so the heuristics used to distinguish scanners from other USB devices is not perfect. <code>sane-find-scanner</code> also tries to find out the type of USB chip used in the scanner. If detected, it will be printed after the vendor and product ids. <code>sane-find-scanner</code> will even find USB scanners, that are not supported by any SANE backend. </p>
<p> <code>sane-find-scanner</code> won&#8217;t find most parallel port scanners, or scanners connected to proprietary ports. Some <code>parallel port</code> scanners may be detected by <i>sane-find-scanner -p .</i> At the time of writing this will only detect Mustek parallel port scanners. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Prints a short usage message.</p>
<dt><code>-v</code></p>
<dd> Verbose output. If used once, <code>sane-find-scanner</code> shows every device name and the test result. If used twice, SCSI inquiry information and the USB device descriptors are also printed.</p>
<dt><code>-q</code></p>
<dd> Be quiet. Print only the devices, no comments.</p>
<dt><code>-p</code></p>
<dd> Probe parallel port scanners.</p>
<dt><code>-f</code></p>
<dd> Force opening all explicitly given devices as SCSI and USB devices. That&#8217;s useful if <code>sane-find-scanner</code> is wrong in determining the device type.</p>
<dt><code>-F filename</code></p>
<dd> filename is a file that contains USB descriptors in the format of /proc/bus/usb/devices as used by Linux. <code>sane-find-scanner</code> tries to identify the chipset(s) of all USB scanners found in such a file. This option is useful for developers when the output of <i>cat /proc/bus/usb/devices</i> is available but the scanner itself isn&#8217;t.</p>
<dt><code>devname</code></p>
<dd> Test device file &quot;devname&quot;. No other devices are checked if devname is given.</dl>
<h2>EXAMPLE</h2>
<p> <i>sane-find-scanner -v</i><br />
 Check all SCSI and USB devices for available scanners and print a line for every device file. </p>
<p> <i>sane-find-scanner /dev/scanner</i><br />
 Look for a (SCSI) scanner only at /dev/scanner and print the result. </p>
<p> <i>sane-find-scanner -p</i><br />
 Probe for parallel port scanners.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Oliver Rauch, Henning Meier-Geinitz and others</p>
<h2>SUPPORTED PLATFORMS</h2>
<p> USB support is limited to Linux (kernel, libusb), FreeBSD (kernel, libusb), NetBSD (libusb), OpenBSD (kernel, libusb). Detecting the vendor and device ids only works with Linux or libusb. </p>
<p> SCSI support is available on Irix, EMX, Linux, Next, AIX, Solaris, FreeBSD, NetBSD, OpenBSD, and HP-UX. </p>
<h2>BUGS</h2>
<p> No support for most parallel port scanners yet.<br />
 Detection of USB chipsets is limited to a few chipsets. </p>
<h2>Index</h2>
