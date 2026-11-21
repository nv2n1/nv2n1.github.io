---

title: "hp-clean(1)"
name: "hp-clean"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-clean/"
description: "hp-clean – Printer Printhead Cleaning Utility"
---

<p> hp-clean &#8211; Printer Printhead Cleaning Utility </p>
<h2>DESCRIPTION</h2>
<p> Printhead cleaning utility for HPLIP supported inkjet printers.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-clean [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
<h2>PRINTER|DEVICE-URI</h2>
<dl>
<dt>To specify a device-URI:</dt>
<dd> -d&lt;device-uri&gt; or &#8211;device=&lt;device-uri&gt;</dd>
<dt>To specify a CUPS printer:</dt>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt;</dd></dl>
<h2>MODE</h2>
<dl>
<dt>Run in interactive mode:</dt>
<dd> -i or &#8211;interactive</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd></dl>
<h2>SEE ALSO</h2>
<p> hp-align hp-clean hp-linefeedcal hp-pqdiag</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
