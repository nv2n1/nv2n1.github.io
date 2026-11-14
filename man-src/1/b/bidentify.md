---
title: "bidentify(1)"
name: "bidentify"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bidentify/"
description: "bidentify – Barry Project’s program to identify BlackBerry handhelds"
---

<h2 class="name">NAME</h2>
<p> <code>bidentify</code> &#8211; Barry Project&#8217;s program to identify BlackBerry handhelds </p>
<h2>SYNOPSIS</h2>
<p> <code>bidentify</code> [-B busname][-N devname][-h][-v]</p>
<h2>DESCRIPTION</h2>
<p> <code>bidentify</code> scans the USB system for available BlackBerry devices and probes each one it finds, then sends the identifying information to stdout in a computer-friendly format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B busname</code></p>
<dd> Specify the USB bus to search for Blackberry devices on. This is the first number displayed in the output from the lsusb command, such as 002. If the busname is numeric on your system, 2 and 002 are equal. See also the -N option, which can be used together with this option to precisely select the device to work with.</p>
<dt><code>-N devname</code></p>
<dd> Specify the USB device name. This is the second number displayed in the output from the lsusb command, such as 005. If the device name is numeric on your system, 5 and 005 are equal. See also the -B option.</p>
<dt><code>-v</code></p>
<dd> Dump verbose protocol data during operation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>RETURN STATUS</h2>
<p> If <code>bidentify</code> detects a BlackBerry device, but cannot access it for some reason, it will write an error message to stderr describing the access problem, and return a count of the number of such failed devices as the error code. A return code of 0 means there were no BlackBerry devices found that could not be probed. </p>
<p> In the event of a fatal error, the message will be written to stderr, with an error code of 1. </p>
<h2>AUTHOR</h2>
<p> <code>bidentify</code> is part of the Barry project. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
