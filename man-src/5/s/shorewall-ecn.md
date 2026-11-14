---
title: "shorewall-ecn(5)"
name: "shorewall-ecn"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-ecn/"
description: "ecn – Shorewall ECN file"
---

<p>ecn &#8211; Shorewall ECN file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/ecn</code></dl>
<h2>Description</h2>
<dd>Use this file to list the destinations for which you want to disable ECN (Explicit Congestion Notification). </p>
<p> The columns in the file are as follows. </p>
<p> <code>INTERFACE</code> &#8211; <i>interface</i></p>
<dl>
<dd>Interface through which host(s) communicate with the firewall</dl>
<p> <code>HOST(S)</code> (Optional) &#8211; [<code>&#8211;</code>|<i>address-or-address-range</i>[<code>,</code><i>address-or-address-range</i>]&#8230;]</p>
<dl>
<dd>Comma-separated list of host and/or network addresses. If left empty or supplied as &quot;-&quot;, 0.0.0.0/0 is assumed. If your kernel and iptables include iprange match support then IP address ranges are also permitted.</dl>
<h2>Files</h2>
<p>/etc/shorewall/ecn</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5) </p>
