---
title: "shorewall-tunnels(5)"
name: "shorewall-tunnels"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-tunnels/"
description: "tunnels – Shorewall VPN definition file"
---

<p>tunnels &#8211; Shorewall VPN definition file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/tunnels</code></dl>
<h2>Description</h2>
<dd>The tunnels file is used to define rules for encapsulated (usually encrypted) traffic to pass between the Shorewall system and a remote gateway. Traffic flowing through the tunnel is handled using the normal zone/policy/rule mechanism. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></code>m[]<font SIZE="-2">[1]</font> for details. The columns in the file are as follows. <code>TYPE</code> &#8211; {<code>ipsec</code>[<code>:{noah</code>|ah}]|<code>ipsecnat</code>|<code>ipip</code>|<code>gre</code>|l2tp|<code>pptpclient</code>|<code>pptpserver</code>|?COMMENT|{<code>openvpn</code>|<code>openvpnclient</code>|<code>openvpnserver</code>}[:{<code>tcp</code>|<code>udp</code>}]<code>[</code>:<i>port</i>]|<code>generic</code><code>:</code><i>protocol</i>[<code>:</code><i>port</i>]}</p>
<dl>
<dd>Types are as follows:</p>
<dl>
<dd>
<pre> <code>6to4</code> or <code>6in4</code> - 6to4 or 6in4 tunnel. The <code>6in4</code> synonym was added in 4.4.24.
 <code>ipsec</code> - IPv4 IPSEC
 <code>ipsecnat</code> - IPv4 IPSEC with NAT Traversal (UDP port 4500 encapsulation)
 <code>ipip</code> - IPv4 encapsulated in IPv4 (Protocol 4)
 <code>gre</code> - Generalized Routing Encapsulation (Protocol 47)
 <code>l2tp</code> - Layer 2 Tunneling Protocol (UDP port 1701)
 <code>pptpclient</code> - PPTP Client runs on the firewall
 <code>pptpserver</code> - PPTP Server runs on the firewall
 <code>openvpn</code> - OpenVPN in point-to-point mode
 <code>openvpnclient</code> - OpenVPN client runs on the firewall
 <code>openvpnserver</code> - OpenVPN server runs on the firewall
 <code>generic</code> - Other tunnel type
 <code>tinc</code> - TINC (added in Shorewall 4.6.6)</pre>
</dl>
<p> If the type is <code>ipsec</code>, it may be followed by <code>:ah</code> to indicate that the Authentication Headers protocol (51) is used by the tunnel (the default is <code>:noah</code> which means that protocol 51 is not used). NAT traversal is only supported with ESP (protocol 50) so <code>ipsecnat</code> tunnels don&#8217;t allow the <code>ah</code> option (<code>ipsecnat:noah</code> may be specified but is redundant). If type is <code>openvpn</code>, <code>openvpnclient</code> or <code>openvpnserver</code> it may optionally be followed by &quot;:&quot; and <code>tcp</code> or <code>udp</code> to specify the protocol to be used. If not specified, <code>udp</code> is assumed. If type is <code>openvpn</code>, <code>openvpnclient</code> or <code>openvpnserver</code> it may optionally be followed by &quot;:&quot; and the port number used by the tunnel. if no &quot;:&quot; and port number are included, then the default port of 1194 will be used. . Where both the protocol and port are specified, the protocol must be given first (e.g., openvpn:tcp:4444). If type is <code>generic</code>, it must be followed by &quot;:&quot; and a protocol name (from /etc/protocols) or a protocol number. If the protocol is <code>tcp</code> or <code>udp</code> (6 or 17), then it may optionally be followed by &quot;:&quot; and a port number. Comments may be attached to Netfilter rules generated from entries in this file through the use of /COMMENT lines. These lines begin with ?COMMENT; the remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line containing only ?COMMENT.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Beginning with Shorewall 4.5.11, ?COMMENT is a synonym for COMMENT and is preferred.  <code>ZONE</code> &#8211; <i>zone</i></p>
<dl>
<dd>The <i>zone</i> of the physical interface through which tunnel traffic passes. This is normally your internet zone.</dl>
<p> <code>GATEWAY</code>(S) (gateway or gateways) &#8211; <i>address-or-range</i> <code>[ , &#8230; ]</code></p>
<dl>
<dd>The IP address of the remote tunnel gateway. If the remote gateway has no fixed address (Road Warrior) then specify the gateway as <code>0.0.0.0/0</code>. May be specified as a network address and if your kernel and iptables include iprange match support then IP address ranges are also allowed. Beginning with Shorewall 4.5.3, a list of addresses or ranges may be given. Exclusion (m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[2]</font> (5) ) is not supported.</dl>
<p> <code>GATEWAY ZONES</code> (gateway_zone or gateway_zones) &#8211; [<i>zone</i>[<code>,</code><i>zone</i>]&#8230;]</p>
<dl>
<dd>Optional. If the gateway system specified in the third column is a standalone host then this column should contain a comma-separated list of the names of the zones that the host might be in. This column only applies to IPSEC tunnels where it enables ISAKMP traffic to flow through the tunnel to the remote gateway(s).</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>IPSec tunnel. </p>
<p> The remote gateway is 4.33.99.124 and the remote subnet is 192.168.9.0/24. The tunnel does not use the AH protocol </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY
 ipsec:noah net 4.33.99.124</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>Road Warrior (LapTop that may connect from anywhere) where the &quot;gw&quot; zone is used to represent the remote LapTop </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 ipsec net 0.0.0.0/0 gw</pre>
</dl>
</dl>
<p> Example 3:</p>
<dl>
<dd>Host 4.33.99.124 is a standalone system connected via an ipsec tunnel to the firewall system. The host is in zone gw. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 ipsec net 4.33.99.124 gw</pre>
</dl>
</dl>
<p> Example 4:</p>
<dl>
<dd>Road Warriors that may belong to zones vpn1, vpn2 or vpn3. The FreeS/Wan _updown script will add the host to the appropriate zone using the <code>shorewall add</code> command on connect and will remove the host from the zone at disconnect time. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 ipsec net 0.0.0.0/0 vpn1,vpn2,vpn3</pre>
</dl>
</dl>
<p> Example 5:</p>
<dl>
<dd>You run the Linux PPTP client on your firewall and connect to server 192.0.2.221. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 pptpclient net 192.0.2.221</pre>
</dl>
</dl>
<p> Example 6:</p>
<dl>
<dd>You run a PPTP server on your firewall. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 pptpserver net 0.0.0.0/0</pre>
</dl>
</dl>
<p> Example 7:</p>
<dl>
<dd>OPENVPN tunnel. The remote gateway is 4.33.99.124 and openvpn uses port 7777. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 openvpn:7777 net 4.33.99.124</pre>
</dl>
</dl>
<p> Example 8:</p>
<dl>
<dd>You have a tunnel that is not one of the supported types. Your tunnel uses UDP port 4444. The other end of the tunnel is 4.3.99.124. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 generic:udp:4444 net 4.3.99.124</pre>
</dl>
</dl>
<p> Example 9:</p>
<dl>
<dd>TINC tunnel where the remote gateways are not specified. If you wish to specify a list of gateways, you can do so in the GATEWAY column. </p>
<dl>
<dd>
<pre> #TYPE ZONE GATEWAY GATEWAY ZONES
 tinc net 0.0.0.0/0</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/tunnels</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/VPNBasics.html">http://www.shorewall.net/VPNBasics.html</a></dl>
<dt> 2.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
