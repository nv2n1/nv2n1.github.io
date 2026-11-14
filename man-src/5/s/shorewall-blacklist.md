---
title: "shorewall-blacklist(5)"
name: "shorewall-blacklist"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-blacklist/"
description: "blacklist – Shorewall Blacklist file"
---

<p>blacklist &#8211; Shorewall Blacklist file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/blacklist</code></dl>
<h2>Description</h2>
<dd>The blacklist file is used to perform static blacklisting. You can blacklist by source address (IP or MAC), or by application. </p>
<p> The columns in the file are as follows. </p>
<p> <code>ADDRESS/SUBNET</code> &#8211; {<code>&#8211;</code>|<code>~</code><i>mac-address</i>|<i>ip-address</i>|<i>address-range</i>|<code>+</code><i>ipset</i>}</p>
<dl>
<dd>Host address, network address, MAC address, IP address range (if your kernel and iptables contain iprange match support) or ipset name prefaced by &quot;+&quot; (if your kernel supports ipset match). </p>
<p> MAC addresses must be prefixed with &quot;~&quot; and use &quot;-&quot; as a separator. </p>
<p> Example: ~00-A0-C9-15-39-78 </p>
<p> A dash (&quot;-&quot;) in this column means that any source address will match. This is useful if you want to blacklist a particular application using entries in the PROTOCOL and PORTS columns.</dl>
<p> <code>PROTOCOL</code> (Optional) &#8211; {<code>&#8211;</code>|[!]<i>protocol-number</i>|[!]<i>protocol-name</i>}</p>
<dl>
<dd>If specified, must be a protocol number or a protocol name from <a href="/docs/linux/man/5-protocols/">protocols</a>(5).</dl>
<p> <code>PORTS</code> (Optional) &#8211; {<code>&#8211;</code>|[!]<i>port-name-or-number</i>[,<i>port-name-or-number</i>]&#8230;}</p>
<dl>
<dd>May only be specified if the protocol is TCP (6) or UDP (17). A comma-separated list of destination port numbers or service names from <a href="/docs/linux/man/5-services/">services</a>(5).</dl>
<p> When a packet arrives on an interface that has the <code>blacklist</code> option specified in <i>shorewall-interfaces</i>[1](5), its source IP address and MAC address is checked against this file and disposed of according to the <code>BLACKLIST_DISPOSITION</code> and <code>BLACKLIST_LOGLEVEL</code> variables in <i>shorewall.conf</i>[2](5). If <code>PROTOCOL</code> or <code>PROTOCOL</code> and <code>PORTS</code> are supplied, only packets matching the protocol (and one of the ports if <code>PORTS</code> supplied) are blocked.</p>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>To block DNS queries from address 192.0.2.126: </p>
<dl>
<dd>
<pre> #ADDRESS/SUBNET PROTOCOL PORT
 192.0.2.126 udp 53</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>To block some of the nuisance applications: </p>
<dl>
<dd>
<pre> #ADDRESS/SUBNET PROTOCOL PORT
 - udp 1024:1033,1434
 - tcp 57,1433,1434,2401,2745,3127,3306,3410,4899,5554,6101,8081,9898</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/blacklist</p>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://shorewall.net/blacklisting_support.htm">http://shorewall.net/blacklisting_support.htm</a></i> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd>shorewall-interfaces.html</dl>
<dt> 2.</p>
<dd>shorewall.conf</p>
<dl>
<dd>shorewall.conf.html</dl>
