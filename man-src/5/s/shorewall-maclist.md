---
title: "shorewall-maclist(5)"
name: "shorewall-maclist"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-maclist/"
description: "maclist – Shorewall MAC Verification file"
---

<p>maclist &#8211; Shorewall MAC Verification file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/maclist</code></dl>
<h2>Description</h2>
<dd>This file is used to define the MAC addresses and optionally their associated IP addresses to be allowed to use the specified interface. The feature is enabled by using the <code>maclist</code> option in the m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[1]</font>(5) or m[blue]<code>shorewall-hosts</code>m[]<font SIZE="-2">[2]</font>(5) configuration file. </p>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>DISPOSITION</code> &#8211; {<code>ACCEPT</code>|<code>DROP</code>|<code>REJECT</code>}[<code>:</code><i>log-level</i>]</p>
<dl>
<dd><code>ACCEPT</code> or <code>DROP</code> (if MACLIST_TABLE=filter in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[3]</font>(5), then REJECT is also allowed). If specified, the <i>log-level</i> causes packets matching the rule to be logged at that level.</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i></p>
<dl>
<dd>Network <i>interface</i> to a host.</dl>
<p> <code>MAC</code> &#8211; <i>address</i></p>
<dl>
<dd>MAC <i>address</i> of the host &#8212; you do not need to use the Shorewall format for MAC addresses here. If <code>IP ADDRESSES</code> is supplied then <code>MAC</code> can be supplied as a dash (<code>&#8211;</code>)</dl>
<p> <code>IP ADDRESSES</code> (addresses) &#8211; [<i>address</i>[<code>,</code><i>address</i>]&#8230;]</p>
<dl>
<dd>Optional &#8211; if specified, both the MAC and IP address must match. This column can contain a comma-separated list of host and/or subnet addresses. If your kernel and iptables have iprange match support then IP address ranges are also allowed. Similarly, if your kernel and iptables include ipset support than set names (prefixed by &quot;+&quot;) are also allowed.</dl>
<h2>Files</h2>
<p>/etc/shorewall/maclist</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-interfaces.html">http://www.shorewall.net/manpages/shorewall-interfaces.html</a></dl>
<dt> 2.</p>
<dd>shorewall-hosts</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-hosts.html">http://www.shorewall.net/manpages/shorewall-hosts.html</a></dl>
<dt> 3.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
