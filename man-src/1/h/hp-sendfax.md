---
title: "hp-sendfax(1)"
name: "hp-sendfax"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-sendfax/"
description: "hp-sendfax – PC Sendfax Utility"
---

<h2 class="name">NAME</h2>
<p> hp-sendfax &#8211; PC Sendfax Utility </p>
<h2>DESCRIPTION</h2>
<p> PC send fax for HPLIP supported multifunction printers.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-sendfax [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
<h2>PRINTER|DEVICE-URI</h2>
<dl>
<dt>To specify a device-URI:</p>
<dd> -d&lt;device-uri&gt; or &#8211;device=&lt;device-uri&gt;</p>
<dt>To specify a CUPS printer:</p>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt;</dl>
<h2>MODE</h2>
<dl>
<dt>Run in non-interactive mode:</p>
<dd> -n or &#8211;non-interactive</dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</p>
<dt>Specify the fax number(s):</p>
<dd> -f&lt;number(s)&gt; or &#8211;faxnum=&lt;number(s)&gt; or &#8211;fax-num=&lt;number(s)&gt; or &#8211;num=&lt;number(s)&gt;(-n only)</p>
<dt>Specify the recipient(s):</p>
<dd> -r&lt;recipient(s)&gt; or &#8211;recipient=&lt;recipient(s)&gt; (-n only)</p>
<dt>Specify the groups(s):</p>
<dd> &#8211;group=&lt;group(s)&gt; or &#8211;groups=&lt;group(s)&gt; (-n only)</dl>
<h2>SEE ALSO</h2>
<p> hp-faxsetup hp-fab</p>
<h2>AUTHOR</h2>
<p> HPLIP (Hewlett-Packard Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-13 Hewlett-Packard Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
