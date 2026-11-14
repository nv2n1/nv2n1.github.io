---
title: "hp-probe(1)"
name: "hp-probe"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-probe/"
description: "hp-probe – Printer Discovery Utility"
---

<h2 class="name">NAME</h2>
<p> hp-probe &#8211; Printer Discovery Utility </p>
<h2>DESCRIPTION</h2>
<p> Discover HPLIP supported USB, parallel, and network attached printers.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-probe [OPTIONS]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Bus to probe:</p>
<dd> -b&lt;bus&gt; or &#8211;bus=&lt;bus&gt; &lt;bus&gt;: cups, usb*, net, bt, fw, par (*default) (Note: bt and fw not supported in this release.)</p>
<dt>Set Time to Live (TTL):</p>
<dd> -t&lt;ttl&gt; or &#8211;ttl=&lt;ttl&gt; (Default is 4).</p>
<dt>Set timeout:</p>
<dd> -o&lt;timeout in secs.&gt; or &#8211;timeout=&lt;timeout is secs.&gt;</p>
<dt>Filter by functionality:</p>
<dd> -e&lt;filter list&gt; or &#8211;filter=&lt;filter list&gt; &lt;filter list&gt;: comma separated list of one or more of: scan, pcard, fax, copy, or none*. (*none is the default)</p>
<dt>Search:</p>
<dd> -s&lt;search re&gt; or &#8211;search=&lt;search re&gt; &lt;search re&gt; must be a valid regular expression (not case sensitive)</p>
<dt>Network discovery method:</p>
<dd> -m&lt;method&gt; or &#8211;method=&lt;method&gt;: &lt;method&gt; is &#8216;slp&#8217;* or &#8216;mdns&#8217;.</p>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Find all devices on the network:</p>
<dd> hp-probe -bnet</p>
<dt>Find all devices on USB that support scanning:</p>
<dd> hp-probe -busb -escan</p>
<dt>Find all networked devices that contain the name &#8216;lnx&#8217; and that support photo cards or scanning:</p>
<dd> hp-probe -bnet -slnx -escan,pcard</p>
<dt>Find all devices that have queues installed in CUPS:</p>
<dd> hp-probe -bcups</p>
<dt>Find all devices on the USB bus:</p>
<dd> hp-probe</dl>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
