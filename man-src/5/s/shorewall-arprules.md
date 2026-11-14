---
title: "shorewall-arprules(5)"
name: "shorewall-arprules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-arprules/"
description: "arprules – Shorewall ARP rules file"
---

<p>arprules &#8211; Shorewall ARP rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/arprules</code></dl>
<h2>Description</h2>
<dd>This file was added in Shorewall 4.5.12 and is used to describe low-level rules managed by arptables (8). These rules only affect Address Resolution Protocol (ARP), Reverse Address Resolution Protocol (RARP) and Dynamic Reverse Address Resolution Protocol (DRARP) frames. The columns in the file are as shown below. MAC addresses are specified normally (6 hexadecimal numbers separated by colons). <code>ACTION</code></p>
<dl>
<dd>Describes the action to take when a frame matches the criteria in the other columns. Possible values are: <code>ACCEPT</code></p>
<dl>
<dd>This is the default action if no rules matches a frame; it lets the frame go through.</dl>
<p> <code>DROP</code></p>
<dl>
<dd>Causes the frame to be dropped.</dl>
<p> <code>SNAT:</code><i>ip-address</i></p>
<dl>
<dd>Modifies the source IP address to the specified <i>ip-address</i>.</dl>
<p> <code>DNAT:</code><i>ip-address</i></p>
<dl>
<dd>Modifies the destination IP address to the specified <i>ip-address</i>.</dl>
<p> <code>SMAT:</code><i>mac-address</i></p>
<dl>
<dd>Modifies the source MAC address to the specified <i>mac-address</i>.</dl>
<p> <code>DMAT:</code><i>mac-address</i></p>
<dl>
<dd>Modifies the destination MAC address to the specified <i>mac-address</i>.</dl>
<p> <code>SNATC:</code><i>ip-address</i></p>
<dl>
<dd>Like SNAT except that the frame is then passed to the next rule.</dl>
<p> <code>DNATC:</code><i>ip-address</i></p>
<dl>
<dd>Like DNAT except that the frame is then passed to the next rule.</dl>
<p> <code>SMATC:</code><i>mac-address</i></p>
<dl>
<dd>Like SMAT except that the frame is then passed to the next rule.</dl>
<p> <code>DMATC:</code><i>mac-address</i></p>
<dl>
<dd>Like DMAT except that the frame is then passed to the next rule.</dl>
</dl>
<p> <code>SOURCE</code> &#8211; <code>[</code><i>interface</i><code>[:[!]</code><i>ipaddress</i><code>[/ip</code><i>mask</i><code>][:[!]</code><i>macaddress</i><code>[/</code><i>macmask</i><code>]]]]</code></p>
<dl>
<dd>Where <i>interface</i></p>
<dl>
<dd>Is an interface defined in <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5).</dl>
<p> <i>ipaddress</i></p>
<dl>
<dd>is an IPv4 address. DNS names are not allowed.</dl>
<p> <i>ipmask</i></p>
<dl>
<dd>specifies a mask to be applied to <i>ipaddress</i>.</dl>
<p> <i>macaddress</i></p>
<dl>
<dd>The source MAC address.</dl>
<p> <i>macmask</i></p>
<dl>
<dd>Mask for MAC address; must be specified as 6 hexadecimal numbers separated by colons.</dl>
<p> When &#8216;!&#8217; is specified, the test is inverted. If not specified, matches only frames originating on the firewall itself.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Either SOURCE or DEST must be specified.  <code>DEST</code> &#8211; <code>[</code><i>interface</i><code>[:[!]</code><i>ipaddress</i><code>[/ip</code><i>mask</i><code>][:[!]</code><i>macaddress</i><code>[/</code><i>macmask</i><code>]]]]</code></p>
<dl>
<dd>Where <i>interface</i></p>
<dl>
<dd>Is an interface defined in <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5).</dl>
<p> <i>ipaddress</i></p>
<dl>
<dd>is an IPv4 address. DNS Names are not allowed.</dl>
<p> <i>ipmask</i></p>
<dl>
<dd>specifies a mask to be applied to frame addresses.</dl>
<p> <i>macaddress</i></p>
<dl>
<dd>The destination MAC address.</dl>
<p> <i>macmask</i></p>
<dl>
<dd>Mask for MAC address; must be specified as 6 hexadecimal numbers separated by colons.</dl>
<p> When &#8216;!&#8217; is specified, the test is inverted and the rule matches frames which do not match the specified address/mask. If not specified, matches only frames originating on the firewall itself. If both SOURCE and DEST are specified, then both interfaces must be bridge ports on the same bridge.</p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 Either SOURCE or DEST must be specified.  OPCODE &#8211; [[!]<i>opcode</i>]</p>
<dl>
<dd>Optional. Describes the type of frame. Possible <i>opcode</i> values are: 1</p>
<dl>
<dd>ARP Request</dl>
<p> 2</p>
<dl>
<dd>ARP Reply</dl>
<p> 3</p>
<dl>
<dd>RARP Request</dl>
<p> 4</p>
<dl>
<dd>RARP Reply</dl>
<p> 5</p>
<dl>
<dd>Dynamic RARP Request</dl>
<p> 6</p>
<dl>
<dd>Dynamic RARP Reply</dl>
<p> 7</p>
<dl>
<dd>Dynamic RARP Error</dl>
<p> 8</p>
<dl>
<dd>InARP Request</dl>
<p> 9</p>
<dl>
<dd>ARP NAK</dl>
<p> When &#8216;!&#8217; is specified, the test is inverted and the rule matches frames which do not match the specified <i>opcode</i>.</dl>
<h2>Example</h2>
<p>The eth1 interface has both a public IP address and a private address (10.1.10.11/24). When sending ARP requests to 10.1.10.0/24, use the private address as the IP source: </p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST ARP OPCODE
SNAT:10.1.10.11 - eth1:10.1.10.0/24 1</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/arprules</p>
