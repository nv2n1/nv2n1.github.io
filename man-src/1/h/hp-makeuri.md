---
title: "hp-makeuri(1)"
name: "hp-makeuri"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-makeuri/"
description: "hp-makeuri – Device URI Creation Utility"
---

<h2 class="name">NAME</h2>
<p> hp-makeuri &#8211; Device URI Creation Utility </p>
<h2>DESCRIPTION</h2>
<p> Creates device URIs for local and network connected printers for use with CUPS.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-makeuri [OPTIONS] [SERIAL NO.|USB ID|IP|DEVNODE]</code></p>
<h2>SERIAL NO.|USB ID|IP|DEVNODE</h2>
<dl>
<dt>USB IDs (usb only):</dt>
<dd> &quot;xxx:yyy&quot; where xxx is the USB bus ID and yyy is the USB device ID. The &#8216;:&#8217; and all leading zeroes must be present. (Use the &#8216;lsusb&#8217; command to obtain this information. See Note 1.)</dd>
<dt>IPs (network only):</dt>
<dd> IPv4 address &quot;a.b.c.d&quot; or &quot;hostname&quot;</dd>
<dt>DEVNODE (parallel only):</dt>
<dd> &quot;/dev/parportX&quot;, X=0,1,2,&#8230;</dd>
<dt>SERIAL NO. (usb and parallel only):</dt>
<dd> &quot;serial no.&quot;</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>To specify the port on a multi-port JetDirect:</dt>
<dd> -p&lt;port&gt; or &#8211;port=&lt;port&gt; (Valid values are 1*, 2, and 3. *default)</dd>
<dt>Show the CUPS URI only (quiet mode):</dt>
<dd> -c or &#8211;cups</dd>
<dt>Show the SANE URI only (quiet mode):</dt>
<dd> -s or &#8211;sane</dd>
<dt>Show the HP Fax URI only (quiet mode):</dt>
<dd> -f or &#8211;fax</dd>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>USB:</dt>
<dd> $ hp-makeuri 001:002</dd>
<dt>Network:</dt>
<dd> $ hp-makeuri 66.35.250.209</dd>
<dt>Parallel:</dt>
<dd> $ hp-makeuri /dev/parport0</dd>
<dt>USB or parallel (using serial number):</dt>
<dd> $ hp-makeuri US123456789</dd></dl>
<h2>NOTES</h2>
<dl>
<dt>1. Example using &#8216;lsusb&#8217; to obtain USB bus ID and USB device ID (example only, the values you obtain will differ) :</dt>
<dd>
</dd><dt> $ lsusb</dt>
<dd>
</dd><dt> Bus 003 Device 011: ID 03f0:c202 Hewlett-Packard</dt>
<dd>
</dd><dt> $ hp-makeuri 003:011</dt>
<dd>
</dd><dt> (Note: You may have to run &#8216;lsusb&#8217; from /sbin or another location. Use &#8216;$ locate lsusb&#8217; to determine this.)</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> hp-setup</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
