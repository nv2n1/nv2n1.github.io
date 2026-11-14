---
title: "hp-setup(1)"
name: "hp-setup"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-setup/"
description: "hp-setup – Printer/Fax Setup Utility"
---

<h2 class="name">NAME</h2>
<p> hp-setup &#8211; Printer/Fax Setup Utility </p>
<h2>DESCRIPTION</h2>
<p> Installs HPLIP printers and faxes in the CUPS spooler. Tries to automatically determine the correct PPD file to use. Allows the printing of a testpage. Performs basic fax parameter setup.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-setup [MODE] [OPTIONS] [SERIAL NO.|USB bus:device|IP|DEVNODE]</code></p>
<h2>MODE</h2>
<dl>
<dt>Run in graphical UI mode:</p>
<dd> -u or &#8211;gui (Default)</p>
<dt>Run in interactive mode:</p>
<dd> -i or &#8211;interactive</dl>
<h2>OPTIONS</h2>
<dl>
<dt>Automatic mode:</p>
<dd> -a or &#8211;auto (-i mode only)</p>
<dt>To specify the port on a multi-port JetDirect:</p>
<dd> &#8211;port=&lt;port&gt; (Valid values are 1*, 2, and 3. *default)</p>
<dt>No testpage in automatic mode:</p>
<dd> -x (-i mode only)</p>
<dt>To specify a CUPS printer queue name:</p>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt; (-i mode only)</p>
<dt>To specify a CUPS fax queue name:</p>
<dd> -f&lt;fax&gt; or &#8211;fax=&lt;fax&gt; (-i mode only)</p>
<dt>Type of queue(s) to install:</p>
<dd> -t&lt;typelist&gt; or &#8211;type=&lt;typelist&gt;. &lt;typelist&gt;: print*, fax* (*default) (-i mode only)</p>
<dt>To specify the device URI to install:</p>
<dd> -d&lt;device&gt; or &#8211;device=&lt;device&gt; (&#8211;qt4 mode only)</p>
<dt>Remove printers or faxes instead of setting-up:</p>
<dd> -r or &#8211;rm or &#8211;remove</p>
<dt>Set the language:</p>
<dd> &#8211;loc=&lt;lang&gt; or &#8211;lang=&lt;lang&gt;. Use &#8211;loc=? or &#8211;lang=? to see a list of available language codes.</p>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</dl>
<h2>SERIAL NO.|USB ID|IP|DEVNODE</h2>
<dl>
<dt>USB bus:device (usb only):</p>
<dd> &quot;xxx:yyy&quot; where &#8216;xxx&#8217; is the USB bus and &#8216;yyy&#8217; is the USB device. (Note: The &#8216;:&#8217; and all leading zeros must be present.) Use the &#8216;lsusb&#8217; command to obtain this information.</p>
<dt>IPs (network only):</p>
<dd> IPv4 address &quot;a.b.c.d&quot; or &quot;hostname&quot;</p>
<dt>DEVNODE (parallel only):</p>
<dd> &quot;/dev/parportX&quot;, X=0,1,2,&#8230;</p>
<dt>SERIAL NO. (usb and parallel only):</p>
<dd> &quot;serial no.&quot;</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Setup using GUI mode:</p>
<dd> $ hp-setup</p>
<dt>Setup using GUI mode, specifying usb:</p>
<dd> $ hp-setup -b usb</p>
<dt>Setup using GUI mode, specifying an IP:</p>
<dd> $ hp-setup 192.168.0.101</p>
<dt>One USB printer attached, automatic:</p>
<dd> $ hp-setup -i -a</p>
<dt>USB, IDs specified:</p>
<dd> $ hp-setup -i 001:002</p>
<dt>Network:</p>
<dd> $ hp-setup -i 66.35.250.209</p>
<dt>Network, Jetdirect port 2:</p>
<dd> $ hp-setup -i &#8211;port=2 66.35.250.209</p>
<dt>Parallel:</p>
<dd> $ hp-setup -i /dev/parport0</p>
<dt>USB or parallel, using serial number:</p>
<dd> $ hp-setup -i US12345678A</p>
<dt>USB, automatic:</p>
<dd> $ hp-setup -i &#8211;auto 001:002</p>
<dt>Parallel, automatic, no testpage:</p>
<dd> $ hp-setup -i -a -x /dev/parport0</p>
<dt>Parallel, choose device:</p>
<dd> $ hp-setup -i -b par</dl>
<h2>NOTES</h2>
<dl>
<dt>1. If no serial number, USB ID, IP, or device node is specified, the USB and parallel busses will be probed for devices.</p>
<dd>
<dt>2. Using &#8216;lsusb&#8217; to obtain USB IDs: (example)</p>
<dd>
<dt> $ lsusb</p>
<dd>
<dt> Bus 003 Device 011: ID 03f0:c202 Hewlett-Packard</p>
<dd>
<dt> $ hp-setup &#8211;auto 003:011</p>
<dd>
<dt> (Note: You may have to run &#8216;lsusb&#8217; from /sbin or another location. Use &#8216;$ locate lsusb&#8217; to determine this.)</p>
<dd>
<dt>3. Parameters -a, -f, -p, or -t are not valid in GUI (-u) mode.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> hp-makeuri hp-probe</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
