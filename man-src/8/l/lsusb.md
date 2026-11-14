---
title: "lsusb(8)"
name: "lsusb"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsusb/"
description: "lsusb – list USB devices"
---

<p>lsusb &#8211; list USB devices</p>
<h2>Synopsis</h2>
<p><code>lsusb</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p><code>lsusb</code> is a utility for displaying information about USB buses in the system and the devices connected to them. It uses udev&#8217;s hardware database to associate a full human-readable name to the vendor ID and the product ID. </p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Tells <i>lsusb</i> to be verbose and display detailed information about the devices shown. This includes configuration descriptors for the device&#8217;s current speed. Class descriptors will be shown, when available, for USB device classes including hub, audio, HID, communications, and chipcard. Can be used with the <code>t</code> option.</p>
<dt><code>-s</code> [[<i>bus</i>]<code>:</code>][<i>devnum</i>]</p>
<dd>Show only devices in specified <i>bus</i> and/or <i>devnum</i>. Both IDs are given in decimal and may be omitted.</p>
<dt><code>-d</code> [<i>vendor</i>]<code>:</code>[<i>product</i>]</p>
<dd>Show only devices with the specified vendor and product ID. Both IDs are given in hexadecimal.</p>
<dt><code>-D </code><i>device</i></p>
<dd>Do not scan the /dev/bus/usb directory, instead display only information about the device whose device file is given. The device file should be something like /dev/bus/usb/001/001. This option displays detailed information like the <code>v</code> option; you must be root to do this.</p>
<dt><code>-t</code>, <code>&#8211;tree</code></p>
<dd>Tells <i>lsusb</i> to dump the physical USB device hierarchy as a tree. Verbosity can be increased twice with the <code>v</code> option.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information on standard output, then exit successfully. </p>
</dl>
<h2>Return Value</h2>
<p>If the specified device is not found, a non-zero exit code is returned. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-usbview/">usbview</a></code>(8). </p>
<h2>Author</h2>
<p>Thomas Sailer, &lt;sailer [at] ife.ee.ethz.ch&gt;.</p>
