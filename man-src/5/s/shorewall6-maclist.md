---
title: "shorewall6-maclist(5)"
name: "shorewall6-maclist"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-maclist/"
---

maclist - shorewall6 MAC Verification file

<h2>Synopsis</h2>

<dl><dt> <b>/etc/shorewall6/maclist</b></dt></dl>

<h2>Description</h2>

<dd>This file is used to define the MAC addresses and optionally their associated IPv6 addresses to be allowed to use the specified interface. The feature is enabled by using the <b>maclist</b> option in the m[blue]<b>shorewall6-interfaces</b>m[][1](5) or m[blue]<b>shorewall6-hosts</b>m[][2](5) configuration file. 

 The columns in the file are as follows. 

 <b>DISPOSITION</b> - {<b>ACCEPT</b>|<b>DROP</b>|<b>REJECT</b>}[<b>:</b><i>log-level</i>]
</dd><dl><dd><b>ACCEPT</b> or <b>DROP</b> (if MACLIST_TABLE=filter in m[blue]<b>shorewall6.conf</b>m[][3](5), then REJECT is also allowed). If specified, the <i>log-level</i> causes packets matching the rule to be logged at that level.</dd></dl>
 

 <b>INTERFACE</b> - <i>interface</i>
<dl><dd>Network <i>interface</i> to a host.</dd></dl>
 

 <b>MAC</b> - <i>address</i>
<dl><dd>MAC <i>address</i> of the host -- you do not need to use the shorewall6 format for MAC addresses here. If <b>IP ADDRESSES</b> is supplied then <b>MAC</b> can be supplied as a dash (<b>-</b>)</dd></dl>
 

 <b>IP ADDRESSES</b> (Optional) - [<i>address</i>[<b>,</b><i>address</i>]...]
<dl><dd>If specified, both the MAC and IP address must match. This column can contain a comma-separated list of host and/or subnet addresses. If your kernel and ip6tables have iprange match support then IP address ranges are also allowed. Similarly, if your kernel and ip6tables include ipset support than set names (prefixed by &quot;+&quot;) are also allowed.</dd></dl>

<h2>Files</h2>

/etc/shorewall6/maclist

<h2>See Also</h2>

m[blue]<b><a rel="nofollow" HREF="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a></b>m[][4] 

 m[blue]<b><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></b>m[][5] 

 <a HREF="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a HREF="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a HREF="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), shorewall6-blacklist(5), <a HREF="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a HREF="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a HREF="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a HREF="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a HREF="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a HREF="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a HREF="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), shorewall6-routestopped(5), <a HREF="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a HREF="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a HREF="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a HREF="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), shorewall6-tos(5), <a HREF="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a HREF="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)

<h2>Notes</h2>

<dl><dt> 1.
</dt><dd>shorewall6-interfaces
</dd><dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a></dd></dl><dt> 2.
</dt><dd>shorewall6-hosts
</dd><dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/manpages6/shorewall6-hosts.html">http://www.shorewall.net/manpages6/shorewall6-hosts.html</a></dd></dl><dt> 3.
</dt><dd>shorewall6.conf
</dd><dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dd></dl><dt> 4.
</dt><dd><a rel="nofollow" HREF="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a>
</dd><dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/MAC_Validation.html">http://www.shorewall.net/MAC_Validation.html</a></dd></dl><dt> 5.
</dt><dd><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a>
</dd><dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dd></dl>
 
</dl>