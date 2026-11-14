---
title: "ipsec_spigrp(5)"
name: "ipsec_spigrp"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_spigrp/"
description: "ipsec_spigrp – list IPSEC Security Association groupings"
---

<p>ipsec_spigrp &#8211; list IPSEC Security Association groupings</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>spigrp</i></p>
<dd><i>cat/proc/net/ipsec_spigrp</i></p>
<dd>
<h2>Obsolete</h2>
<dd>Note that spigrp is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. A replacement command still needs to be designed</p>
<h2>Description</h2>
<p>/proc/net/ipsec_spigrp is a read-only file that lists groups of IPSEC Security Associations (SAs). </p>
<p> An entry in the IPSEC extended routing table can only point (via an SAID) to one SA. If more than one transform must be applied to a given type of packet, this can be accomplished by setting up several SAs with the same destination address but potentially different SPIs and protocols, and grouping them with <i><a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8)</i>. </p>
<p> The SA groups are listed, one line per connection/group, as a sequence of SAs to be applied (or that should have been applied, in the case of an incoming packet) from inside to outside the packet. An SA is identified by its SAID, which consists of protocol (&quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot;), SPI (with &#8216;.&#8217; for IPv4 or &#8216;:&#8217; for IPv6 prefixed hexadecimal number ) and destination address (IPv4 dotted quad or IPv6 coloned hex) prefixed by &#8216;@&#8217;, in the format &lt;proto&gt;&lt;af&gt;&lt;spi&gt;@&lt;dest&gt;.</p>
<h2>Examples</h2>
<p><code>tun.3d0 [at] 192.168.2.110</code></p>
<dl>
<dd><code>comp.3d0 [at] 192.168.2.110</code><code>esp.187a101b [at] 192.168.2.110</code><code>ah.187a101a [at] 192.168.2.110</code></dl>
<p> is a group of 3 SAs, destined for 192.168.2.110 with an IPv4-in-IPv4 tunnel SA applied first with an SPI of <code>3d0</code> in hexadecimal, followed by a Deflate compression header to compress the packet with CPI of <code>3d0</code> in hexadecimal, followed by an Encapsulating Security Payload header to encrypt the packet with SPI <code>187a101b</code> in hexadecimal, followed by an Authentication Header to authenticate the packet with SPI <code>187a101a</code> in hexadecimal, applied from inside to outside the packet. This could be an incoming or outgoing group, depending on the address of the local machine. </p>
<p> <code>tun:3d0 [at] 3049:1::2</code></p>
<dl>
<dd><code>comp:3d0 [at] 3049:1::2</code><code>esp:187a101b [at] 3049:1::2</code><code>ah:187a101a [at] 3049:1::2</code></dl>
<p> is a group of 3 SAs, destined for <code>3049:1::2</code> with an IPv6-in-IPv6 tunnel SA applied first with an SPI of <code>3d0</code> in hexadecimal, followed by a Deflate compression header to compress the packet with CPI of <code>3d0</code> in hexadecimal, followed by an Encapsulating Security Payload header to encrypt the packet with SPI <code>187a101b</code> in hexadecimal, followed by an Authentication Header to authenticate the packet with SPI <code>187a101a</code> in hexadecimal, applied from inside to outside the packet. This could be an incoming or outgoing group, depending on the address of the local machine.</p>
<h2>Files</h2>
<p>/proc/net/ipsec_spigrp, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/5-ipsec_tncfg/">ipsec_tncfg</a>(5), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Bugs</h2>
<p>:-)</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
