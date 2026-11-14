---
title: "shorewall6-tunnels(5)"
name: "shorewall6-tunnels"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-tunnels/"
description: "tunnels – Shorewall6 VPN definition file"
---

<p>tunnels &#8211; Shorewall6 VPN definition file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/tunnels</code></dl>
<h2>Description</h2>
<dd>The tunnels file is used to define rules for encapsulated (usually encrypted) traffic to pass between the Shorewall6 system and a remote gateway. Traffic flowing through the tunnel is handled using the normal zone/policy/rule mechanism. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></code>m[]<font SIZE="-2">[1]</font> for details. </p>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>TYPE</code> &#8211; {<code>ipsec</code>[<code>:{noah</code>|ah}]|<code>ipsecnat</code>|<code>gre</code>|l2tp|<code>pptpclient</code>|<code>pptpserver</code>|?COMMENT|{<code>openvpn</code>|<code>openvpnclient</code>|<code>openvpnserver</code>}[:{<code>tcp</code>|<code>udp</code>}]<code>[</code>:<i>port</i>]|<code>generic</code><code>:</code><i>protocol</i>[<code>:</code><i>port</i>]}</p>
<dl>
<dd>Types are as follows: </p>
<dl>
<dd>
<pre> <code>ipsec</code> - IPv6 IPSEC
 <code>ipsecnat</code> - IPv6 IPSEC with NAT Traversal (UDP port 4500 encapsulation)
 <code>gre</code> - Generalized Routing Encapsulation (Protocol 47)
 <code>l2tp</code> - Layer 2 Tunneling Protocol (UDP port 1701)
 <code>openvpn</code> - OpenVPN in point-to-point mode
 <code>openvpnclient</code> - OpenVPN client runs on the firewall
 <code>openvpnserver</code> - OpenVPN server runs on the firewall
 <code>generic</code> - Other tunnel type
 <code>tinc</code> - TINC (added in Shorewall 4.6.6)</pre>
</dl>
<p> If the type is <code>ipsec</code>, it may be followed by <code>:ah</code> to indicate that the Authentication Headers protocol (51) is used by the tunnel (the default is <code>:noah</code> which means that protocol 51 is not used). NAT traversal is only supported with ESP (protocol 50) so <code>ipsecnat</code> tunnels don&#8217;t allow the <code>ah</code> option (<code>ipsecnat:noah</code> may be specified but is redundant). </p>
<p> If type is <code>openvpn</code>, <code>openvpnclient</code> or <code>openvpnserver</code> it may optionally be followed by &quot;:&quot; and <code>tcp</code> or <code>udp</code> to specify the protocol to be used. If not specified, <code>udp</code> is assumed. Note: At this writing, OpenVPN does not support IPv6. </p>
<p> If type is <code>openvpn</code>, <code>openvpnclient</code> or <code>openvpnserver</code> it may optionally be followed by &quot;:&quot; and the port number used by the tunnel. if no &quot;:&quot; and port number are included, then the default port of 1194 will be used. . Where both the protocol and port are specified, the protocol must be given first (e.g., openvpn:tcp:4444). </p>
<p> If type is <code>generic</code>, it must be followed by &quot;:&quot; and a protocol name (from /etc/protocols) or a protocol number. If the protocol is <code>tcp</code> or <code>udp</code> (6 or 17), then it may optionally be followed by &quot;:&quot; and a port number. </p>
<p> Comments may be attached to Netfilter rules generated from entries in this file through the use of ?COMMENT lines. These lines begin with the word ?COMMENT; the remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line with only the word ?COMMENT.</dl>
<p> <code>ZONE</code> &#8211; <i>zone</i></p>
<dl>
<dd>The <i>zone</i> of the physical interface through which tunnel traffic passes. This is normally your internet zone.</dl>
<p> <code>GATEWAY</code>(S) (gateway or gateways) &#8211; <i>address-or-range</i> <code>[ , &#8230; ]</code></p>
<dl>
<dd>The IP address of the remote tunnel gateway. If the remote gateway has no fixed address (Road Warrior) then specify the gateway as <code>::/0</code>. May be specified as a network address and if your kernel and ip6tables include iprange match support then IP address ranges are also allowed. </p>
<p> Beginning with Shorewall 4.5.3, a list of addresses or ranges may be given. Exclusion (m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[2]</font> (5) ) is not supported.</dl>
<p> <code>GATEWAY ZONE(S)</code> (gateway_zone or gateway_zones) &#8211; [<i>zone</i>[<code>,</code><i>zone</i>]&#8230;]</p>
<dl>
<dd>Optional. If the gateway system specified in the third column is a standalone host then this column should contain a comma-separated list of the names of the zones that the host might be in. This column only applies to IPSEC tunnels where it enables ISAKMP traffic to flow through the tunnel to the remote gateway(s).</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>IPSec tunnel. </p>
<p> The remote gateway is 2001:cec792b4:1::44. The tunnel does not use the AH protocol </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY
 ipsec:noah net 2002:cec792b4:1::44</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>Road Warrior (LapTop that may connect from anywhere) where the &quot;gw&quot; zone is used to represent the remote LapTop </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 ipsec net ::/0 gw</pre>
</dl>
</dl>
<p> Example 3:</p>
<dl>
<dd>Host 2001:cec792b4:1::44 is a standalone system connected via an ipsec tunnel to the firewall system. The host is in zone gw. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 ipsec net 2001:cec792b4:1::44 gw</pre>
</dl>
</dl>
<p> Example 4:</p>
<dl>
<dd>OPENVPN tunnel. The remote gateway is 2001:cec792b4:1::44 and openvpn uses port 7777. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 openvpn:7777 net 2001:cec792b4:1::44</pre>
</dl>
</dl>
<p> Example 8:</p>
<dl>
<dd>You have a tunnel that is not one of the supported types. Your tunnel uses UDP port 4444. The other end of the tunnel is 2001:cec792b4:1::44. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 generic:udp:4444 net 2001:cec792b4:1::44</pre>
</dl>
</dl>
<p> Example 9:</p>
<dl>
<dd>TINC tunnel where the remote gateways are not specified. If you wish to specify a list of gateways, you can do so in the GATEWAY column. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 tinc net ::/0</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/tunnels</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
