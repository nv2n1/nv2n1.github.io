---
title: "shorewall-notrack(5)"
name: "shorewall-notrack"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-notrack/"
description: "notrack – shorewall notrack file"
---

<p>notrack &#8211; shorewall notrack file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/notrack</code></dl>
<h2>Description</h2>
<dd>The notrack file is used to exempt certain traffic from Netfilter connection tracking. Traffic matching entries in this file will not be tracked. </p>
<p> The columns in the file are as follows. </p>
<p> SOURCE &#8211; {<i>zone</i>[:<i>interface</i>][:<i>address-list</i>]|COMMENT}</p>
<dl>
<dd>where <i>zone</i> is the name of a zone, <i>interface</i> is an interface to that zone, and <i>address-list</i> is a comma-separated list of addresses (may contain exclusion &#8211; see <i>shorewall-exclusion</i>[1] (5)). </p>
<p> Comments may be attached to Netfilter rules generated from entries in this file through the use of COMMENT lines. These lines begin with the word COMMENT; the remainder of the line is treated as a comment which is attached to subsequent rules until another COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line with only the word COMMENT.</dl>
<p> DEST &#8211; [<i>interface</i>|<i>address-list</i>]</p>
<dl>
<dd>where <i>interface</i> is the name of a network interface and <i>address-list</i> is a comma-separated list of addresses (may contain exclusion &#8211; see <i>shorewall-exclusion</i>[1] (5)). If an interface is given: </p>
<dl>
<dd>*It must be up and configured with an IPv4 address when Shorewall is started or restarted.</dl>
<dl>
<dd>*All routes out of the interface must be configured when Shorewall is started or restarted.</dl>
<dl>
<dd>*Default routes out of the interface will result in a warning message and will be ignored.</dl>
<dl>
<dd>These restrictions are because Netfilter doesn&#8217;t support NOTRACK rules that specify a destination interface (these rules are applied before packets are routed and hence the destination interface is unknown). Shorewall uses the routes out of the interface to replace the interface with an address list corresponding to the networks routed out of the named interface.</dl>
</dl>
<p> PROTO &#8211; <i>protocol-name-or-number</i></p>
<dl>
<dd>A protocol name from <i>/etc/protocols</i> or a protocol number.</dl>
<p> DEST PORT(S) &#8211; port-number/service-name-list</p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from <i>/etc/services</i>. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support.</dl>
<p> SOURCE PORT(S) &#8211; port-number/service-name-list</p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from <i>/etc/services</i>. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support.</dl>
<p> USER/GROUP &#8211; [<i>user</i>][:<i>group</i>]</p>
<dl>
<dd>May only be specified if the SOURCE <i>zone</i> is $FW. Specifies the effective user id and or group id of the process sending the traffic.</dl>
<h2>Files</h2>
<p>/etc/shorewall/notrack</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd>shorewall-exclusion.html</dl>
