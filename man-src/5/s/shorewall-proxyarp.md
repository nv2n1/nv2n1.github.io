---
title: "shorewall-proxyarp(5)"
name: "shorewall-proxyarp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-proxyarp/"
description: "proxyarp – Shorewall Proxy ARP file"
---

<p>proxyarp &#8211; Shorewall Proxy ARP file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/proxyarp</code></dl>
<h2>Description</h2>
<dd>This file is used to define Proxy ARP. There is one entry in this file for each IP address to be proxied. </p>
<p> The columns in the file are as follows. </p>
<p> <code>ADDRESS</code> &#8211; <i>address</i></p>
<dl>
<dd>IP Address.</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i> (Optional as of Shorewall 4.4.16)</p>
<dl>
<dd>Local interface where system with the ip address in ADDRESS is connected. This column is only required when HAVEROUTE is set to <code>No</code> (<code>no</code>) or is left empty.</dl>
<p> <code>EXTERNAL</code> &#8211; <i>interface</i></p>
<dl>
<dd>External Interface to be used to access this system from the Internet.</dl>
<p> <code>HAVEROUTE</code> &#8211; [<code>&#8211;</code>|<code>Yes</code>|<code>No</code>]</p>
<dl>
<dd>If there is already a route from the firewall to the host whose address is given, enter <code>Yes</code> or <code>yes</code> in this column. Otherwise, enter <code>no</code> or <code>No</code> or leave the column empty and Shorewall will add the route for you. If Shorewall adds the route, its persistence depends on the value of the<code>PERSISTENT</code> column contains <code>Yes</code>; otherwise, <code>shorewall stop</code> or <code>shorewall clear</code> will delete the route.</dl>
<p> <code>PERSISTENT</code> &#8211; [<code>&#8211;</code>|<code>Yes</code>|<code>No</code>]</p>
<dl>
<dd>If HAVEROUTE is <code>No</code> or <code>no</code>, then the value of this column determines if the route added by Shorewall persists after a <code>shorewall stop</code> or a <code>shorewall clear</code>. If this column contains <code>Yes</code> or <code>yes</code> then the route persists; If the column is empty or contains <code>No</code> or <code>no</code> then the route is deleted by <code>shorewall stop</code> or <code>shorewall clear</code>.</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Host with IP 155.186.235.6 is connected to interface eth1 and we want hosts attached via eth0 to be able to access it using that address. </p>
<dl>
<dd>
<pre> #ADDRESS INTERFACE EXTERNAL
 155.186.235.6 eth1 eth0</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/proxyarp</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/ProxyARP.htm">http://www.shorewall.net/ProxyARP.htm</a></code>m[]<font SIZE="-2">[1]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/ProxyARP.htm">http://www.shorewall.net/ProxyARP.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/ProxyARP.htm">http://www.shorewall.net/ProxyARP.htm</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
