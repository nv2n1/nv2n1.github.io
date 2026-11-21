---
title: "hp-info(1)"
name: "hp-info"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-info/"
description: "hp-info – Device Information Utility"
---

<h2 class="name">NAME</h2>
<p> hp-info &#8211; Device Information Utility </p>
<h2>DESCRIPTION</h2>
<p> Query a printer for static model information, dynamic status information, and CUPS printer queue settings.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-info [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
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
<dd> -h or &#8211;help</dd>
<dt>Device ID mode:</dt>
<dd> &#8211;id (prints device ID only and exits.) (interactive (-i) mode only.)</dd>
<dt>Allow device URIs of uninstalled printers:</dt>
<dd> -x (interactive (-i) mode only.)</dd></dl>
<h2>SEE ALSO</h2>
<p> hp-toolbox</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
