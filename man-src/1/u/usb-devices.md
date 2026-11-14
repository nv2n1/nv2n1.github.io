---
title: "usb-devices(1)"
name: "usb-devices"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usb-devices/"
description: "usb-devices – print USB device details"
---

<h2 class="name">NAME</h2>
<p> usb-devices &#8211; print USB device details </p>
<h2>SYNOPSIS</h2>
<p> <code>usb-devices</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>usb-devices</code> is a shell script that can be used to display details of USB buses in the system and the devices connected to them. </p>
<p> The output of the script is similar to the <i>usb/devices</i> file available either under <i>/proc/bus</i> (if usbfs is mounted), or under <i>/sys/kernel/debug</i> (if debugfs is mounted there). The script is primarily intended to be used if the file is not available. </p>
<p> In contrast to the <i>usb/devices</i> file, this script only lists <i>active</i> interfaces (those marked with a &quot;*&quot; in the <i>usb/devices</i> file) and their endpoints. </p>
<p> Be advised that there can be differences in the way information is sorted, as well as in the format of the output. </p>
<h2>RETURN VALUE</h2>
<p> If sysfs is not mounted, a non-zero exit code is returned. </p>
<h2>FILES</h2>
<dl>
<dt><code>/sys/bus/usb/devices/usb*</code></p>
<dd> The part of the sysfs tree the script walks through to assemble the printed information.</p>
<dt><code>/proc/bus/usb/devices</code></p>
<dd> Location where the <i>usb/devices</i> file can normally be found for Linux kernels before 2.6.31, if usbfs is mounted.</p>
<dt><code>/sys/kernel/debug/usb/devices</code></p>
<dd> Location where the <i>usb/devices</i> file can normally be found for Linux kernel 2.6.31 and later, if debugfs is mounted. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-lsusb/">lsusb</a></code>(8), <code><a href="/docs/linux/man/8-usbview/">usbview</a></code>(8). </p>
<h2>AUTHORS</h2>
<p> Greg Kroah-Hartman &lt;greg [at] kroah.com&gt; </p>
<p> Randy Dunlap &lt;rdunlap [at] xenotime.net&gt; </p>
<p> Frans Pop &lt;elendil [at] planet.nl&gt; </p>
<h2>Index</h2>
