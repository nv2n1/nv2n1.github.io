---
title: "hp-firmware(1)"
name: "hp-firmware"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-firmware/"
description: "hp-firmware – Firmware Download Utility"
---

<h2 class="name">NAME</h2>
<p> hp-firmware &#8211; Firmware Download Utility </p>
<h2>DESCRIPTION</h2>
<p> Download firmware to a device that requires downloaded firmware to function. (Note: Most printers do not require the use of this utility).</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-firmware [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
<h2>PRINTER|DEVICE-URI</h2>
<dl>
<dt>To specify a device-URI:</p>
<dd> -d&lt;device-uri&gt; or &#8211;device=&lt;device-uri&gt;</p>
<dt>To specify a CUPS printer:</p>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt;</dl>
<h2>MODE</h2>
<dl>
<dt>Run in interactive mode:</p>
<dd> -i or &#8211;interactive</p>
<dt>Run in non-interactive mode:</p>
<dd> -n or &#8211;non-interactive</dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</p>
<dt>Use USB IDs to specify printer:</p>
<dd> -s bbb:ddd, where bbb is the USB bus ID and ddd is the USB device ID. The &#8216;:&#8217; and all leading zeroes must be present.</p>
<dt>Seconds to delay before download:</p>
<dd> -y&lt;secs&gt; or &#8211;delay=&lt;secs&gt; (float value, e.g. 0.5)</dl>
<h2>SEE ALSO</h2>
<p> hp-plugin hp-toolbox</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
