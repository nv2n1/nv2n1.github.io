---

title: "hp-config_usb_printer(1)"
name: "hp-config_usb_printer"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-config_usb_printer/"
description: "hp-config_usb_printer – HP device config using USB"
---

<p> Udev invokes this tool. Tool detects the plugin, Smart Install (C/DVD-ROM) issues and notifies to logged-in user. Tool also downloads firmware to the device.</p>
<p> <code>hp-config_usb_printer [OPTIONS] [USB bus:device]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd></dl>
<h2>USB BUSDEVICE</h2>
<dl>
<dt>USB bus:device :</dt>
<dd> &quot;xxx:yyy&quot; where &#8216;xxx&#8217; is the USB bus and &#8216;yyy&#8217; is the USB device. (Note: The &#8216;:&#8217; and all leading zeros must be present.) Use the &#8216;lsusb&#8217; command to obtain this information.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>USB, IDs specified:</dt>
<dd> $hp-config_usb_printer 001:002</dd></dl>
<h2>NOTES</h2>
<dl>
<dt>1. Using &#8216;lsusb&#8217; to obtain USB IDs: (example)</dt>
<dd>
</dd><dt> $ lsusb</dt>
<dd>
</dd><dt> Bus 003 Device 011: ID 03f0:c202 Hewlett-Packard</dt>
<dd>
</dd><dt> $ hp-config_usb_printer 003:011</dt>
<dd>
</dd><dt> (Note: You may have to run &#8216;lsusb&#8217; from /sbin or another location. Use &#8216;$ locate lsusb&#8217; to determine this.)</dt>
<dd>
</dd></dl>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
