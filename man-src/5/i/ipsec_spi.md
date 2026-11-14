---
title: "ipsec_spi(5)"
name: "ipsec_spi"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_spi/"
description: "ipsec_spi – list IPSEC Security Associations"
---

<p>ipsec_spi &#8211; list IPSEC Security Associations</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>spi</i></p>
<dd><i>cat/proc/net/ipsec_spi</i></p>
<dd>
<h2>Obsolete</h2>
<dd>Note that eroute is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. A replacement command still needs to be designed</p>
<h2>Description</h2>
<p>/proc/net/ipsec_spi is a read-only file that lists the current IPSEC Security Associations. A Security Association (SA) is a transform through which packet contents are to be processed before being forwarded. A transform can be an IPv4-in-IPv4 or IPv6-in-IPv6 encapsulation, an IPSEC Authentication Header (authentication with no encryption), or an IPSEC Encapsulation Security Payload (encryption, possibly including authentication). </p>
<p> When a packet is passed from a higher networking layer through an IPSEC virtual interface, a search in the extended routing table (see <code><a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a></code>(5)) yields a IP protocol number , a Security Parameters Index (SPI) and an effective destination address When an IPSEC packet arrives from the network, its ostensible destination, an SPI and an IP protocol specified by its outermost IPSEC header are used. The destination/SPI/protocol combination is used to select a relevant SA. (See <code><a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a></code>(5) for discussion of how multiple transforms are combined.) </p>
<p> An <i>spi</i>, <i>proto</i>, <i>daddr</i> and <i>address_family</i> arguments specify an SAID. <i>Proto</i> is an ASCII string, &quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot;, specifying the IP protocol. <i>Spi</i> is a number, preceded by &#8216;.&#8217; indicating hexadecimal and IPv4 or by &#8216;:&#8217; indicating hexadecimal and IPv6, where each hexadecimal digit represents 4 bits, between <code>0x100</code> and <code>0xffffffff</code>; values from <code>0x0</code> to <code>0xff</code> are reserved. <i>Daddr</i> is a dotted-decimal IPv4 destination address or a coloned hex IPv6 destination address. </p>
<p> An <i>SAID</i> combines the three parameters above, such as: &quot;tun.101 [at] 1.2.3.4&quot; for IPv4 or &quot;tun:101 [at] 3049:1::1&quot; for IPv6 </p>
<p> A table entry consists of: </p>
<p> +</p>
<dl>
<dd><code>SAID</code></dl>
<p> +</p>
<dl>
<dd>&lt;transform name (proto,encalg,authalg)&gt;:</dl>
<p> +</p>
<dl>
<dd>direction (dir=)</dl>
<p> +</p>
<dl>
<dd>source address (src=)</dl>
<p> +</p>
<dl>
<dd>source and destination addresses and masks for inner header policy check addresses (policy=), as dotted-quads or coloned hex, separated by &#8216;-&gt;&#8217;, for IPv4-in-IPv4 or IPv6-in-IPv6 SAs only</dl>
<p> +</p>
<dl>
<dd>initialisation vector length and value (iv_bits=, iv=) if non-zero</dl>
<p> +</p>
<dl>
<dd>out-of-order window size, number of out-of-order errors, sequence number, recently received packet bitmask, maximum difference between sequence numbers (ooowin=, ooo_errs=, seq=, bit=, max_seq_diff=) if SA is AH or ESP and if individual items are non-zero</dl>
<p> +</p>
<dl>
<dd>extra flags (flags=) if any are set</dl>
<p> +</p>
<dl>
<dd>authenticator length in bits (alen=) if non-zero</dl>
<p> +</p>
<dl>
<dd>authentication key length in bits (aklen=) if non-zero</dl>
<p> +</p>
<dl>
<dd>authentication errors (auth_errs=) if non-zero</dl>
<p> +</p>
<dl>
<dd>encryption key length in bits (eklen=) if non-zero</dl>
<p> +</p>
<dl>
<dd>encryption size errors (encr_size_errs=) if non-zero</dl>
<p> +</p>
<dl>
<dd>encryption padding error warnings (encr_pad_errs=) if non-zero</dl>
<p> +</p>
<dl>
<dd>lifetimes legend, c=Current status, s=Soft limit when exceeded will initiate rekeying, h=Hard limit will cause termination of SA (life(c,s,h)=)</dl>
<p> +</p>
<dl>
<dd>number of connections to which the SA is allocated (c), that will cause a rekey (s), that will cause an expiry (h) (alloc=), if any value is non-zero</dl>
<p> +</p>
<dl>
<dd>number of bytes processesd by this SA (c), that will cause a rekey (s), that will cause an expiry (h) (bytes=), if any value is non-zero</dl>
<p> +</p>
<dl>
<dd>time since the SA was added (c), until rekey (s), until expiry (h), in seconds (add=)</dl>
<p> +</p>
<dl>
<dd>time since the SA was first used (c), until rekey (s), until expiry (h), in seconds (used=), if any value is non-zero</dl>
<p> +</p>
<dl>
<dd>number of packets processesd by this SA (c), that will cause a rekey (s), that will cause an expiry (h) (packets=), if any value is non-zero</dl>
<p> +</p>
<dl>
<dd>time since the last packet was processed, in seconds (idle=), if SA has been used </p>
<p> average compression ratio (ratio=)</dl>
<h2>Examples</h2>
<p><code>tun.12a [at] 192.168.43.1 IPIP: dir=out src=192.168.43.2</code><code> life(c,s,h)=bytes(14073,0,0)add(269,0,0)</code><code> use(149,0,0)packets(14,0,0)</code><code> idle=23</code> </p>
<p> is an outbound IPv4-in-IPv4 (protocol 4) tunnel-mode SA set up between machines 192.168.43.2 and 192.168.43.1 with an SPI of 12a in hexadecimal that has passed about 14 kilobytes of traffic in 14 packets since it was created, 269 seconds ago, first used 149 seconds ago and has been idle for 23 seconds. </p>
<p> <code>esp:9a35fc02 [at] 3049:1::1 ESP_3DES_HMAC_MD5:</code><code> dir=in src=9a35fc02 [at] 3049:1::2</code><code> ooowin=32 seq=7149 bit=0xffffffff</code><code> alen=128 aklen=128 eklen=192</code><code> life(c,s,h)=bytes(1222304,0,0)add(4593,0,0)</code><code> use(3858,0,0)packets(7149,0,0)</code><code> idle=23</code> </p>
<p> is an inbound Encapsulating Security Payload (protocol 50) SA on machine 3049:1::1 with an SPI of 9a35fc02 that uses 3DES as the encryption cipher, HMAC MD5 as the authentication algorithm, an out-of-order window of 32 packets, a present sequence number of 7149, every one of the last 32 sequence numbers was received, the authenticator length and keys is 128 bits, the encryption key is 192 bits (actually 168 for 3DES since 1 of 8 bits is a parity bit), has passed 1.2 Mbytes of data in 7149 packets, was added 4593 seconds ago, first used 3858 seconds ago and has been idle for 23 seconds.</p>
<h2>Files</h2>
<p>/proc/net/ipsec_spi, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_manual/">ipsec_manual</a>(8), <a href="/docs/linux/man/5-ipsec_tncfg/">ipsec_tncfg</a>(5), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Bugs</h2>
<p>The add and use times are awkward, displayed in seconds since machine start. It would be better to display them in seconds before now for human readability.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
