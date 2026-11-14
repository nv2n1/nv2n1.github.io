---
title: "hp-config_usb_printer(1)"
name: "hp-config_usb_printer"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-config_usb_printer/"
description: "hp-config_usb_printer – HP device config using USB"
---

<h2 class="name">NAME</h2>
<p> hp-config_usb_printer &#8211; HP device config using USB </p>
<h2>DESCRIPTION</h2>
<p> Udev invokes this tool. Tool detects the plugin, Smart Install (C/DVD-ROM) issues and notifies to logged-in user. Tool also downloads firmware to the device.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-config_usb_printer [OPTIONS] [USB bus:device]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</dl>
<h2>USB BUSDEVICE</h2>
<dl>
<dt>USB bus:device :</p>
<dd> &quot;xxx:yyy&quot; where &#8216;xxx&#8217; is the USB bus and &#8216;yyy&#8217; is the USB device. (Note: The &#8216;:&#8217; and all leading zeros must be present.) Use the &#8216;lsusb&#8217; command to obtain this information.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>USB, IDs specified:</p>
<dd> $hp-config_usb_printer 001:002</dl>
<h2>NOTES</h2>
<dl>
<dt>1. Using &#8216;lsusb&#8217; to obtain USB IDs: (example)</p>
<dd>
<dt> $ lsusb</p>
<dd>
<dt> Bus 003 Device 011: ID 03f0:c202 Hewlett-Packard</p>
<dd>
<dt> $ hp-config_usb_printer 003:011</p>
<dd>
<dt> (Note: You may have to run &#8216;lsusb&#8217; from /sbin or another location. Use &#8216;$ locate lsusb&#8217; to determine this.)</p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
