---
title: "tc-tunnel_key(8)"
name: "tc-tunnel_key"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-tunnel_key/"
description: "tunnel_key – Tunnel metadata manipulation"
---

<p>tunnel_key &#8211; Tunnel metadata manipulation</p>
<h2>Synopsis</h2>
<pre><code>tc ... action tunnel_key { unset |

    SET }
SET :=

set src_ip

ADDRESS

dst_ip

ADDRESS

id KEY_ID

dst_port UDP_PORT

tos TOS

ttl TTL

[ csum | nocsum ]
</code></pre>
<h2>Description</h2>
<p>The <code>tunnel_key</code> action combined with a shared IP tunnel device, allows to perform IP tunnel en- or decapsulation on a packet, reflected by the operation modes <i>UNSET</i> and <i>SET</i>. The <i>UNSET</i> mode is optional &#8211; even without using it, the metadata information will be released automatically when packet processing will be finished. <i>UNSET</i> function could be used in cases when traffic is forwarded between two tunnels, where the metadata from the first tunnel will be used for encapsulation done by the second tunnel. <i>SET</i> mode requires the source and destination ip <i>ADDRESS</i> and the tunnel key id <i>KEY_ID</i> which will be used by the ip tunnel shared device to create the tunnel header. The <code>tunnel_key</code> action is useful only in combination with a <code>mirred redirect</code> action to a shared IP tunnel device which will use the metadata (for <i>SET</i> ) and unset the metadata created by it (for <i>UNSET</i> ). </p>
<h2>Options</h2>
<dl>
<dt><code>unset</code></p>
<dd>Unset the tunnel metadata created by the IP tunnel device. This function is not mandatory and might be used only in some specific use cases (as explained above).</p>
<dt><code>set</code></p>
<dd>Set tunnel metadata to be used by the IP tunnel device. Requires <code>src_ip</code> and <code>dst_ip</code> options. <code>id</code> , <code>dst_port</code> , <code>geneve_opts</code> , <code>vxlan_opts</code> and <code>erspan_opts</code> are optional.</p>
<dl>
<dd>
<dl>
<dt><code>id</code></p>
<dd>Tunnel ID (for example VNI in VXLAN tunnel)</p>
<dt><code>src_ip</code></p>
<dd>Outer header source IP address (IPv4 or IPv6)</p>
<dt><code>dst_ip</code></p>
<dd>Outer header destination IP address (IPv4 or IPv6)</p>
<dt><code>dst_port</code></p>
<dd>Outer header destination UDP port</p>
<dt><code>geneve_opts</code></p>
<dd>Geneve variable length options. <code>geneve_opts</code> is specified in the form CLASS:TYPE:DATA, where CLASS is represented as a 16bit hexadecimal value, TYPE as an 8bit hexadecimal value and DATA as a variable length hexadecimal value. Additionally multiple options may be listed using a comma delimiter.</p>
<dt><code>vxlan_opts</code></p>
<dd>Vxlan metadata options. <code>vxlan_opts</code> is specified in the form GBP, as a 32bit number. Multiple options is not supported.</p>
<dt><code>erspan_opts</code></p>
<dd>Erspan metadata options. <code>erspan_opts</code> is specified in the form VERSION:INDEX:DIR:HWID, where VERSION is represented as a 8bit number, INDEX as an 32bit number, DIR and HWID as a 8bit number. Multiple options is not supported. Note INDEX is used when VERSION is 1, and DIR and HWID are used when VERSION is 2.</p>
<dt><code>tos</code></p>
<dd>Outer header TOS</p>
<dt><code>ttl</code></p>
<dd>Outer header TTL</p>
<dt>[<code>no</code>]<code>csum</code></p>
<dd>Controls outer UDP checksum. When set to <code>csum</code> (which is default), the outer UDP checksum is calculated and included in the packets. When set to <code>nocsum</code>, outer UDP checksum is zero. Note that when using zero UDP checksums with IPv6, the other tunnel endpoint must be configured to accept such packets. In Linux, this would be the <code>udp6zerocsumrx</code> option for the VXLAN tunnel interface.</p>
<dd>If using <code>nocsum</code> with IPv6, be sure you know what you are doing. Zero UDP checksums provide weaker protection against corrupted packets. See RFC6935 for details.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>The following example encapsulates incoming ICMP packets on eth0 into a vxlan tunnel, by setting metadata to VNI 11, source IP 11.11.0.1 and destination IP 11.11.0.2, and by redirecting the packet with the metadata to device vxlan0, which will do the actual encapsulation using the metadata:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev eth0 protocol ip parent ffff: \<br />
&nbsp;<wbr>&nbsp;flower&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ip_proto icmp&nbsp;\<br />
&nbsp;<wbr>&nbsp;action tunnel_key set&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;src_ip 11.11.0.1&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dst_ip 11.11.0.2&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id 11&nbsp;\<br />
&nbsp;<wbr>&nbsp;action mirred egress redirect dev vxlan0</dl>
<p> Here is an example of the <code>unset</code> function: Incoming VXLAN traffic with outer IP&#8217;s and VNI 11 is decapsulated by vxlan0 and metadata is unset before redirecting to tunl1 device:</p>
<dl>
<dd>#tc qdisc add dev eth0 handle ffff: ingress #tc filter add dev vxlan0 protocol ip parent ffff:<br />
&nbsp;<wbr>&nbsp;flower&nbsp;\ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> enc_src_ip 11.11.0.2 enc_dst_ip 11.11.0.1 enc_key_id 11 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action tunnel_key unset action mirred egress redirect dev tunl1
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
