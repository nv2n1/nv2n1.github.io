---
title: "shorewall6-routes(5)"
name: "shorewall6-routes"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-routes/"
description: "routes – Shorewall6 file"
---

<p>routes &#8211; Shorewall6 file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/routes</code></dl>
<h2>Description</h2>
<dd>This file was added in Shorewall 4.4.15 and is used to define routes to be added to provider routing tables. </p>
<p> The columns in the file are as follows. </p>
<p> <code>PROVIDER</code></p>
<dl>
<dd>The name or number of a provider defined in m[blue]<code>shorewall6-providers</code>m[]<font SIZE="-2">[1]</font> (5). Beginning with Shorewall 4.5.14, you may also enter <code>main</code> in this column to add routes to the main routing table.</dl>
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
<dd>Specifies the device route. If neither DEVICE nor GATEWAY is given, then the INTERFACE specified for the PROVIDER in m[blue]<code>shorewall6-providers</code>m[]<font SIZE="-2">[1]</font> (5).This column must be omitted if <code>blackhole</code>, <code>prohibit</code> or <code>unreachable</code> is specified in the GATEWAY column.</dl>
<p> <code>OPTIONS</code> (Optional)</p>
<dl>
<dd>Added in Shorewall 5.0.2. </p>
<p> Allowed options are: </p>
<p> <code>persistent</code></p>
<dl>
<dd>If specified, the route remains in the provider&#8217;s routing table even when the provider is disabled.</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/routes</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-providers</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-providers.html">http://www.shorewall.net/manpages6/shorewall6-providers.html</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
