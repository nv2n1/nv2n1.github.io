---
title: "shorewall6-netmap(5)"
name: "shorewall6-netmap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-netmap/"
description: "netmap – Shorewall6 NETMAP definition file"
---

<p>netmap &#8211; Shorewall6 NETMAP definition file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/netmap</code></dl>
<h2>Description</h2>
<dd>This file is used to map addresses in one network to corresponding addresses in a second network. It was added in Shorewall6 4.4.23.3.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 To use this file, your kernel and ip6tables must have RAWPOST table support included.  The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>TYPE</code> &#8211; <code>{DNAT</code>|<code>SNAT}:{P|O|T}</code></p>
<dl>
<dd>Must be DNAT or SNAT followed by :P, :O or :T to perform stateless NAT. Stateless NAT requires Rawpost Table support in your kernel and iptables (see the output of <code>shorewall6 show capabilities</code>). If DNAT:P, traffic entering INTERFACE and addressed to NET1 has its destination address rewritten to the corresponding address in NET2. If SNAT:T, traffic leaving INTERFACE with a source address in NET1 has it&#8217;s source address rewritten to the corresponding address in NET2. If DNAT:O, traffic originating on the firewall and leaving via INTERFACE and addressed to NET1 has its destination address rewritten to the corresponding address in NET2. If DNAT:P, traffic entering via INTERFACE and addressed to NET1 has its destination address rewritten to the corresponding address in NET2. If SNAT:P, traffic entering via INTERFACE with a destination address in NET1 has it&#8217;s source address rewritten to the corresponding address in NET2. If SNAT:O, traffic originating on the firewall and leaving via INTERFACE with a source address in NET1 has it&#8217;s source address rewritten to the corresponding address in NET2.</dl>
<p> <code>NET1</code> &#8211; <i>network-address</i></p>
<dl>
<dd>Network in CIDR format (e.g., 2001:470:b:227/64). Beginning in Shorewall6 4.4.24, m[blue]<code>exclusion</code>m[]<font SIZE="-2">[1]</font> is supported.</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i></p>
<dl>
<dd>The name of a network interface. The interface must be defined in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[2]</font>(5). Shorewall allows loose matches to wildcard entries in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[2]</font>(5). For example, ppp0 in this file will match a m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) entry that defines ppp+.</dl>
<p> <code>NET2</code> &#8211; <i>network-address</i></p>
<dl>
<dd>Network in CIDR format</dl>
<p> <code>NET3</code> &#8211; <i>network-address</i></p>
<dl>
<dd>Optional &#8211; added in Shorewall 4.4.11. If specified, qualifies INTERFACE. It specifies a SOURCE network for DNAT rules and a DESTINATION network for SNAT rules.</dl>
<p> <code>PROTO (Optional</code> &#8211; <i>protocol-number-or-name</i></p>
<dl>
<dd>Only packets specifying this protocol will have their IP header modified.</dl>
<p> <code>DPORT</code> &#8211; <i>port-number-or-name-list</i></p>
<dl>
<dd>Destination Ports. An optional comma-separated list of Port names (from <a href="/docs/linux/man/5-services/">services</a>(5)), <i>port number</i>s or <i>port range</i>s; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). ICMP types may be specified as a numeric type, a numeric type and code separated by a slash (e.g., 3/4), or a typename. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></code>m[]<font SIZE="-2">[3]</font>. If the protocol is <code>ipp2p</code>, this column is interpreted as an ipp2p option without the leading &quot;&#8211;&quot; (example <code>bit</code> for bit-torrent). If no PORT is given, <code>ipp2p</code> is assumed. An entry in this field requires that the PROTO column specify icmp (1), tcp (6), udp (17), sctp (132) or udplite (136). Use &#8216;-&#8216; if any of the following field is supplied. This column was formerly labelled DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; <i>port-number-or-name-list</i></p>
<dl>
<dd>Optional source port(s). If omitted, any source port is acceptable. Specified as a comma-separated list of port names, port numbers or port ranges. An entry in this field requires that the PROTO column specify tcp (6), udp (17), sctp (132) or udplite (136). Use &#8216;-&#8216; if any of the following fields is supplied. This column was formerly labelled SOURCE PORT(S).</dl>
<h2>Files</h2>
<p>/etc/shorewall/netmap</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/netmap.html">http://www.shorewall.net/netmap.html</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[5]</font></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/netmap.html">http://www.shorewall.net/netmap.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/netmap.html">http://www.shorewall.net/netmap.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
