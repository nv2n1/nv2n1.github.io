---
title: "shorewall-hosts(5)"
name: "shorewall-hosts"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-hosts/"
description: "hosts – Shorewall file"
---

<p>hosts &#8211; Shorewall file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/hosts</code></dl>
<h2>Description</h2>
<dd>This file is used to define zones in terms of subnets and/or individual IP addresses. Most simple setups don&#8217;t need to (should not) place anything in this file. The order of entries in this file is not significant in determining zone composition. Rather, the order that the zones are declared in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5) determines the order in which the records in this file are interpreted.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 The only time that you need this file is when you have more than one zone connected through a single interface. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If you have an entry for a zone and interface in m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) then do not include any entries in this file for that same (zone, interface) pair.  The columns in the file are as follows. <code>ZONE</code> &#8211; <i>zone-name</i></p>
<dl>
<dd>The name of a zone declared in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5). You may not list the firewall zone in this column.</dl>
<p> <code>HOST(S)</code> &#8211; <i>interface</i>:{[{<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;|<code>+</code><i>ipset</i>|<code>dynamic</code>}[<i>exclusion</i>]</p>
<dl>
<dd>The name of an interface defined in the m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) file followed by a colon (&quot;:&quot;) and a comma-separated list whose elements are either:</p>
<dl>
<dd>1. The IP <i>address</i> of a host.</dl>
<dl>
<dd>2. A network in CIDR format.</dl>
<dl>
<dd>3. An IP address range of the form <i>low.address</i>&#8211;<i>high.address</i>. Your kernel and iptables must have iprange match support.</dl>
<dl>
<dd>4. The name of an <i>ipset</i>.</dl>
<dl>
<dd>5. The word <code>dynamic</code> which makes the zone dynamic in that you can use the <code>shorewall add</code> and <code>shorewall delete</code> commands to change to composition of the zone.</dl>
<p> You may also exclude certain hosts through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[3]</font>(5).</dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options from the following list. The order in which you list the options is not significant but the list must have no embedded white-space. <code>blacklist</code></p>
<dl>
<dd>Check packets arriving on this port against the m[blue]<code>shorewall-blacklist</code>m[]<font SIZE="-2">[4]</font>(5) file.</dl>
<p> <code>broadcast</code></p>
<dl>
<dd>Used when you want to include limited broadcasts (destination IP address 255.255.255.255) from the firewall to this zone. Only necessary when:</p>
<dl>
<dd>1. The network specified in the HOST(S) column does not include 255.255.255.255.</dl>
<dl>
<dd>2. The zone does not have an entry for this interface in m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
</dl>
<p> <code>destonly</code></p>
<dl>
<dd>Normally used with the Multi-cast IP address range (224.0.0.0/4). Specifies that traffic will be sent to the specified net(s) but that no traffic will be received from the net(s).</dl>
<p> <code>ipsec</code></p>
<dl>
<dd>The zone is accessed via a kernel 2.6 ipsec SA. Note that if the zone named in the ZONE column is specified as an IPSEC zone in the m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5) file then you do NOT need to specify the &#8216;ipsec&#8217; option here.</dl>
<p> <code>maclist</code></p>
<dl>
<dd>Connection requests from these hosts are compared against the contents of m[blue]<code>shorewall-maclist</code>m[]<font SIZE="-2">[5]</font>(5). If this option is specified, the interface must be an Ethernet NIC or equivalent and must be up before Shorewall is started.</dl>
<p> <code>mss</code>=<i>mss</i></p>
<dl>
<dd>Added in Shorewall 4.5.2. When present, causes the TCP mss for new connections to/from the hosts given in the HOST(S) column to be clamped at the specified <i>mss</i>.</dl>
<p> <code>nosmurfs</code></p>
<dl>
<dd>This option only makes sense for ports on a bridge. Filter packets for smurfs (packets with a broadcast address as the source). Smurfs will be optionally logged based on the setting of SMURF_LOG_LEVEL in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[6]</font>(5). After logging, the packets are dropped.</dl>
<p> <code>routeback</code></p>
<dl>
<dd>Shorewall should set up the infrastructure to pass packets from this/these address(es) back to themselves. This is necessary if hosts in this group use the services of a transparent proxy that is a member of the group or if DNAT is used to send requests originating from this group to a server in the group.</dl>
<p> <code>tcpflags</code></p>
<dl>
<dd>Packets arriving from these hosts are checked for certain illegal combinations of TCP flags. Packets found to have such a combination of flags are handled according to the setting of TCP_FLAGS_DISPOSITION after having been logged according to the setting of TCP_FLAGS_LOG_LEVEL.</dl>
</dl>
<h2>Examples</h2>
<p>Example 1</p>
<dl>
<dd>The firewall runs a PPTP server which creates a ppp interface for each remote client. The clients are assigned IP addresses in the network 192.168.3.0/24 and in a zone named &#8216;vpn&#8217;. </p>
<dl>
<dd>
<pre>#ZONE HOST(S) OPTIONS
vpn ppp+:192.168.3.0/24</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/hosts</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[7]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-nesting/">shorewall-nesting</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-zones.html">http://www.shorewall.net/manpages/shorewall-zones.html</a></dl>
<dt> 2.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-interfaces.html">http://www.shorewall.net/manpages/shorewall-interfaces.html</a></dl>
<dt> 3.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 4.</p>
<dd>shorewall-blacklist</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-blacklist.html">http://www.shorewall.net/manpages/shorewall-blacklist.html</a></dl>
<dt> 5.</p>
<dd>shorewall-maclist</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-maclist.html">http://www.shorewall.net/manpages/shorewall-maclist.html</a></dl>
<dt> 6.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 7.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
