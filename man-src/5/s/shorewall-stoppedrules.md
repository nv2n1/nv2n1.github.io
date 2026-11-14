---
title: "shorewall-stoppedrules(5)"
name: "shorewall-stoppedrules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-stoppedrules/"
description: "stoppedrules – The Shorewall file that governs what traffic flows through the firewall while it is in the ‘stopped’ state."
---

<p>stoppedrules &#8211; The Shorewall file that governs what traffic flows through the firewall while it is in the &#8216;stopped&#8217; state.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/stoppedrules</code></dl>
<h2>Description</h2>
<dd>This file is used to define the hosts that are accessible when the firewall is stopped or is being stopped.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Changes to this file do not take effect until after the next <code>shorewall start</code>, <code>shorewall reload</code>, <code>shorewall restart</code>, or <code>shorewall compile</code> command.  The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>ACTION</code> &#8211; <code>ACCEPT|NOTRACK|DROP</code></p>
<dl>
<dd>Determines the disposition of the packet. <code>ACCEPT</code> means that the packet will be accepted. <code>NOTRACK</code> indicates that no conntrack entry should be created for the packet. <code>NOTRACK</code> does not imply <code>ACCEPT</code>. <code>DROP</code> was added in Shorewall 4.6.0 and causes the packet to be dropped in the raw table&#8217;s PREROUTING chain.</dl>
<p> <code>SOURCE</code> &#8211; [<code>&#8211;</code>|[$FW|<i>interface</i>]|[{$FW|interface}[<i>:address</i>[,<i>address</i>]&#8230;]]|[<i>address</i>[,<i>address</i>]&#8230;]</p>
<dl>
<dd><code>$FW</code> matches packets originating on the firewall itself, while <i>interface</i> specifies packets arriving on the named interface. This column may also include a comma-separated list of IP/subnet addresses. If your kernel and iptables include iprange match support, IP address ranges are also allowed. Ipsets and exclusion are also supported. When <code>$FW</code> or interface are specified, the list must be preceded by a colon (&quot;:&quot;). If left empty or supplied as &quot;-&quot;, 0.0.0.0/0 is assumed.</dl>
<p> <code>DEST</code> &#8211; [<code>&#8211;</code>|[$FW|<i>interface</i>]|[{$FW|interface}[<i>:address</i>[,<i>address</i>]&#8230;]]|[<i>address</i>[,<i>address</i>]&#8230;]</p>
<dl>
<dd><code>$FW</code> matches packets addressed the firewall itself, while <i>interface</i> specifies packets arriving on the named interface. Neither may be specified if the target is <code>NOTRACK</code> or <code>DROP</code>. This column may also include a comma-separated list of IP/subnet addresses. If your kernel and iptables include iprange match support, IP address ranges are also allowed. Ipsets and exclusion are also supported. When <code>$FW</code> or interface are specified, the list must be preceded by a colon (&quot;:&quot;). If left empty or supplied as &quot;-&quot;, 0.0.0.0/0 is assumed.</dl>
<p> <code>PROTO (Optional)</code> &#8211; <i>protocol-name-or-number</i>[,&#8230;]</p>
<dl>
<dd>Protocol. Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols.</dl>
<p> <code>DPORT</code> &#8211; <i>service-name/port-number-list</i></p>
<dl>
<dd>Optional. A comma-separated list of port numbers and/or service names from /etc/services. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support. This column was formerly labelled DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; <i>service-name/port-number-list</i></p>
<dl>
<dd>Optional. A comma-separated list of port numbers and/or service names from /etc/services. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support. Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DEST PORTS(S). Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel. This column was formerly labelled SOURCE PORT(S).</dl>
<h2>Files</h2>
<p>/etc/shorewall/stoppedrules</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></code>m[]<font SIZE="-2">[1]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
