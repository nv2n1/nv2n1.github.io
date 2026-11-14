---
title: "hp-makecopies(1)"
name: "hp-makecopies"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-makecopies/"
description: "hp-makecopies – Make Copies Utility"
---

<h2 class="name">NAME</h2>
<p> hp-makecopies &#8211; Make Copies Utility </p>
<h2>DESCRIPTION</h2>
<p> PC initiated make copies function on supported HP AiO and MFP devices. (Note: Currently unsupported in Qt4.)</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-makecopies [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
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
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</p>
<dt>Number of copies:</p>
<dd> -m&lt;num_copies&gt; or &#8211;copies=&lt;num_copies&gt; or &#8211;num=&lt;num_copies&gt; (1-99)</p>
<dt>Reduction/enlargement:</p>
<dd> -r&lt;%&gt; or &#8211;reduction=&lt;%&gt; or &#8211;enlargement=&lt;%&gt; (25-400%)</p>
<dt>Quality:</p>
<dd> -q&lt;quality&gt; or &#8211;quality=&lt;quality&gt; (where quality is: &#8216;fast&#8217;, &#8216;draft&#8217;, &#8216;normal&#8217;, &#8216;presentation&#8217;, or &#8216;best&#8217;)</p>
<dt>Contrast:</p>
<dd> -c&lt;contrast&gt; or &#8211;contrast=&lt;contrast&gt; (-5 to +5)</p>
<dt>Fit to page (flatbed only):</p>
<dd> -f or &#8211;fittopage or &#8211;fit (overrides reduction/enlargement)</dl>
<h2>AUTHOR</h2>
<p> HPLIP (Hewlett-Packard Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-13 Hewlett-Packard Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
