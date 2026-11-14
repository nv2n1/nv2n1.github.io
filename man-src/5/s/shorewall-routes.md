---
title: "shorewall-routes(5)"
name: "shorewall-routes"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-routes/"
description: "routes – Shorewall file"
---

<p>routes &#8211; Shorewall file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/routes</code></dl>
<h2>Description</h2>
<dd>This file was added in Shorewall 4.4.15 and is used to define routes to be added to provider routing tables. </p>
<p> The columns in the file are as follows. </p>
<p> <code>PROVIDER</code></p>
<dl>
<dd>The name or number of a provider defined in m[blue]<code>shorewall-providers</code>m[]<font SIZE="-2">[1]</font> (5). Beginning with Shorewall 4.5.14, you may also enter <code>main</code> in this column to add routes to the main routing table.</dl>
<p> <code>DEST</code></p>
<dl>
<dd>Destination host address or network address.</dl>
<p> <code>GATEWAY</code> (Optional)</p>
<dl>
<dd>If specified, gives the IP address of the gateway to the DEST. </p>
<p> Beginning with Shorewall 4.5.14, you may specify <code>blackhole</code> in this column to create a blackhole route. </p>
<p> Beginning with Shorewall 4.5.15, you may specify <code>prohibit</code> or <code>unreachable</code> in this column to create a prohibit or unreachable route respectively.</dl>
<p> <code>DEVICE</code> (Optional)</p>
<dl>
<dd>Specifies the device route. If neither DEVICE nor GATEWAY is given, then the INTERFACE specified for the PROVIDER in m[blue]<code>shorewall-providers</code>m[]<font SIZE="-2">[1]</font> (5). This column must be omitted if <code>blackhole</code>, <code>prohibit</code> or <code>unreachable</code> is specified in the GATEWAY column.</dl>
<p> <code>OPTIONS</code> (Optional)</p>
<dl>
<dd>Added in Shorewall 5.0.2. </p>
<p> Allowed options are: </p>
<p> <code>persistent</code></p>
<dl>
<dd>If specified, the route remains in the provider&#8217;s routing table even when the provider is disabled.</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/routes</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-providers</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-providers.html">http://www.shorewall.net/manpages/shorewall-providers.html</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
