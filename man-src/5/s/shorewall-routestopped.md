---
title: "shorewall-routestopped(5)"
name: "shorewall-routestopped"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-routestopped/"
description: "routestopped – The Shorewall file that governs what traffic flows through the firewall while it is in the ‘stopped’ state."
---

<p>routestopped &#8211; The Shorewall file that governs what traffic flows through the firewall while it is in the &#8216;stopped&#8217; state.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/routestopped</code></dl>
<h2>Description</h2>
<dd>This file is used to define the hosts that are accessible when the firewall is stopped or is being stopped. </p>
<p> Warning </p>
<p> Changes to this file do not take effect until after the next <code>shorewall start</code> or <code>shorewall restart</code> command. </p>
<p> The columns in the file are as follows. </p>
<p> <code>INTERFACE</code> &#8211; <i>interface</i></p>
<dl>
<dd>Interface through which host(s) communicate with the firewall</dl>
<p> <code>HOST(S)</code> (Optional) &#8211; [<code>&#8211;</code>|<i>address</i>[,<i>address</i>]&#8230;]</p>
<dl>
<dd>Comma-separated list of IP/subnet addresses. If your kernel and iptables include iprange match support, IP address ranges are also allowed. </p>
<p> If left empty or supplied as &quot;-&quot;, 0.0.0.0/0 is assumed.</dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<code>&#8211;</code>|<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options. The order of the options is not important but the list can contain no embedded whitespace. The currently-supported options are: </p>
<p> <code>routeback</code></p>
<dl>
<dd>Set up a rule to ACCEPT traffic from these hosts back to themselves. Beginning with Shorewall 4.4.9, this option is automatically set if <code>routeback</code> is specified in <i>shorewall-interfaces</i>[1] (5) or if the rules compiler detects that the interface is a bridge.</dl>
<p> <code>source</code></p>
<dl>
<dd>Allow traffic from these hosts to ANY destination. Without this option or the <code>dest</code> option, only traffic from this host to other listed hosts (and the firewall) is allowed. If <code>source</code> is specified then <code>routeback</code> is redundant.</dl>
<p> <code>dest</code></p>
<dl>
<dd>Allow traffic to these hosts from ANY source. Without this option or the <code>source</code> option, only traffic from this host to other listed hosts (and the firewall) is allowed. If <code>dest</code> is specified then <code>routeback</code> is redundant.</dl>
<p> notrack</p>
<dl>
<dd>The traffic will be exempted from conntection tracking.</dl>
</dl>
<p> PROTO (Optional) &#8211; <i>protocol-name-or-number</i></p>
<dl>
<dd>Protocol.</dl>
<p> DEST PORT(S) (Optional) &#8211; <i>service-name/port-number-list</i></p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from <i>/etc/services</i>. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support.</dl>
<p> SOURCE PORT(S) (Optional) &#8211; <i>service-name/port-number-list</i></p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from <i>/etc/services</i>. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support.</dl>
<p> Note </p>
<p> The <code>source</code> and <code>dest</code> options work best when used in conjunction with ADMINISABSENTMINDED=Yes in <i>shorewall.conf</i>[2](5).</p>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>
<dl>
<dd>
<pre> #INTERFACE HOST(S) OPTIONS PROTO DEST SOURCE
 # PORT(S) PORT(S)
 eth2 192.168.1.0/24
 eth0 192.0.2.44
 br0 - routeback
 eth3 - source
 eth4 - notrack 41</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/routestopped</p>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://shorewall.net/starting_and_stopping_shorewall.htm">http://shorewall.net/starting_and_stopping_shorewall.htm</a></i> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
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
