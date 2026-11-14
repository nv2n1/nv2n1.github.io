---
title: "interface-order(5)"
name: "interface-order"
section: "5"
letter: "i"
url: "/docs/linux/man/5-interface-order/"
description: "interface-order – resolvconf configuration file"
---

<p>interface-order &#8211; resolvconf configuration file</p>
<h2>Description</h2>
<p>The file <i>/etc/resolvconf/interface-order</i> is used to control the order in which resolvconf nameserver information records are processed by those resolvconf update scripts that consult this file. (The name of the file is apt because a resolvconf nameserver information record is named after the interface with which it is associated.) </p>
<p> The file contains a sequence of shell glob patterns, one per line. The position of a record in the order is the point at which its name first matches a pattern. </p>
<p> Patterns may not contain whitespace, slashes or initial dots or tildes. Blank lines and lines beginning with a &#8216;#&#8217; are ignored. </p>
<p> Resolvconf update scripts in <i>/etc/resolvconf/update.d/</i> that consult this file include the current default versions of <i>dnsmasq</i>, <i>pdnsd</i> and <i>libc</i>. (Actually they don&#8217;t read the file directly; they call the utility program <i>/lib/resolvconf/list-records</i> which lists records in the specified order and omits the names of empty records.)</p>
<h2>Example</h2>
<pre># /etc/resolvconf/interface-order
# Use nameservers on the loopback interface first.
lo*
# Next use records for Ethernet interfaces
eth*
# Next use records for Wi-Fi interfaces
wlan*
# Next use records for PPP interfaces
ppp*
# Last use other interfaces
*</pre>
<h2>Author</h2>
<p>Resolvconf was written by Thomas Hood &lt;jdthood [at] gmail.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2011 Thomas Hood<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8) </p>
