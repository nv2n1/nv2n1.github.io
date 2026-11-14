---
title: "ipsec_spigrp(8)"
name: "ipsec_spigrp"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_spigrp/"
description: "ipsec_spigrp – group/ungroup IPSEC Security Associations"
---

<p>ipsec_spigrp &#8211; group/ungroup IPSEC Security Associations</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>spigrp</i></p>
<dd><i>ipsecspigrp</i> [&#8211;label&nbsp;<wbr><i>label</i>] <i>af1dst1spi1proto1</i> [<i>af2dst2spi2proto2</i>&nbsp;<wbr>[<i>af3dst3spi3proto3</i>&nbsp;<wbr>[<i>af4dst4spi4proto4</i>]]]</p>
<dd><i>ipsecspigrp</i> [&#8211;label&nbsp;<wbr><i>label</i>] &#8211;said <i>SA1</i> [<i>SA2</i>&nbsp;<wbr>[<i>SA3</i>&nbsp;<wbr>[<i>SA4</i>]]]</p>
<dd><i>ipsecspigrp</i> &#8211;help</p>
<dd><i>ipsecspigrp</i> &#8211;version</p>
<dd>
<h2>Obsolete</h2>
<dd>Note that spi is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. A replacement command still needs to be designed</p>
<h2>Description</h2>
<p><i>Spigrp</i> groups IPSEC Security Associations (SAs) together or ungroups previously grouped SAs. An entry in the IPSEC extended routing table can only point (via a destination address, a Security Parameters Index (SPI) and a protocol identifier) to one SA. If more than one transform must be applied to a given type of packet, this can be accomplished by setting up several SAs with the same destination address but potentially different SPIs and protocols, and grouping them with <i>spigrp</i>. </p>
<p> The SAs to be grouped, specified by destination address (DNS name lookup, IPv4 dotted quad or IPv6 coloned hex), SPI (&#8216;0x&#8217;-prefixed hexadecimal number) and protocol (&quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot;), are listed from the inside transform to the outside; in other words, the transforms are applied in the order of the command line and removed in the reverse order. The resulting SA group is referred to by its first SA (by <i>af1</i>, <i>dst1</i>, <i>spi1</i> and <i>proto1</i>). </p>
<p> The &#8211;said option indicates that the SA IDs are to be specified as one argument each, in the format &lt;proto&gt;&lt;af&gt;&lt;spi&gt;@&lt;dest&gt;. The SA IDs must all be specified as separate parameters without the &#8211;said option or all as monolithic parameters after the &#8211;said option. </p>
<p> The SAs must already exist and must not already be part of a group. </p>
<p> If <i>spigrp</i> is invoked with only one SA specification, it ungroups the previously-grouped set of SAs containing the SA specified. </p>
<p> The &#8211;label option identifies all responses from that command invocation with a user-supplied label, provided as an argument to the label option. This can be helpful for debugging one invocation of the command out of a large number. </p>
<p> The command form with no additional arguments lists the contents of /proc/net/ipsec_spigrp. The format of /proc/net/ipsec_spigrp is discussed in <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5).</p>
<h2>Examples</h2>
<p><code>ipsec spigrp inet gw2 0x113 tun inet gw2 0x115 esp inet gw2 0x116 ah</code></p>
<dl>
<dd>groups 3 SAs together, all destined for <code>gw2</code>, but with an IPv4-in-IPv4 tunnel SA applied first with SPI <code>0x113</code>, then an ESP header to encrypt the packet with SPI <code>0x115</code>, and finally an AH header to authenticate the packet with SPI <code>0x116</code>.</dl>
<p> <code>ipsec spigrp &#8211;said tun.113@gw2 esp.115@gw2 ah.116@gw2</code></p>
<dl>
<dd>groups 3 SAs together, all destined for <code>gw2</code>, but with an IPv4-in-IPv4 tunnel SA applied first with SPI <code>0x113</code>, then an ESP header to encrypt the packet with SPI <code>0x115</code>, and finally an AH header to authenticate the packet with SPI <code>0x116</code>.</dl>
<p> <code>ipsec spigrp &#8211;said tun:233 [at] 3049:1::1 esp:235 [at] 3049:1::1 ah:236 [at] 3049:1::1</code></p>
<dl>
<dd>groups 3 SAs together, all destined for <code>3049:1::1,</code> but with an IPv6-in-IPv6 tunnel SA applied first with SPI <code>0x233</code>, then an ESP header to encrypt the packet with SPI <code>0x235</code>, and finally an AH header to authenticate the packet with SPI <code>0x236</code>.</dl>
<p> <code>ipsec spigrp inet6 3049:1::1 0x233 tun inet6 3049:1::1 0x235 esp inet6 3049:1::1 0x236 ah</code></p>
<dl>
<dd>groups 3 SAs together, all destined for <code>3049:1::1,</code> but with an IPv6-in-IPv6 tunnel SA applied first with SPI <code>0x233</code>, then an ESP header to encrypt the packet with SPI <code>0x235</code>, and finally an AH header to authenticate the packet with SPI <code>0x236</code>.</dl>
<h2>Files</h2>
<p>/proc/net/ipsec_spigrp, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/8-ipsec_klipsdebug/">ipsec_klipsdebug</a>(8), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Bugs</h2>
<p>Yes, it really is limited to a maximum of four SAs, although admittedly it&#8217;s hard to see why you would need more.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
