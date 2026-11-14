---
title: "ipsec_spi(8)"
name: "ipsec_spi"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_spi/"
description: "ipsec_spi – manage IPSEC Security Associations"
---

<p>ipsec_spi &#8211; manage IPSEC Security Associations</p>
<h2>Synopsis</h2>
<p>Note: In the following,</p>
<dl>
<dt> <code>&lt;SA&gt;</code> <i>means:</i> &#8211;af <i>(inet | inet6)</i> &#8211;edst <i>daddr</i> &#8211;spi <i>spi</i> &#8211;proto <i>proto</i> <i>OR</i> &#8211;said <i>said,</i></p>
<dd><code>&lt;life&gt;</code> <i>means:</i> &#8211;life <i>(soft | hard)</i> allocations | <i>bytes</i> | <i>addtime</i> | <i>usetime</i> | <i>packets</i> | [value&#8230;] <code>&lt;SA&gt;</code> &#8211;src <i>src</i> &#8211;ah <i>(hmac-md5-96 | hmac-sha1-96)</i> [&#8211;replay_window&nbsp;<wbr><i>replayw</i>] [<i>&lt;life&gt;</i>] &#8211;authkey <i>akey</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;src <i>src</i> &#8211;esp <i>(3des | 3des-md5-96 | 3des-sha1-96)</i> [&#8211;replay_window&nbsp;<wbr><i>replayw</i>] [<i>&lt;life&gt;</i>] &#8211;enckey <i>ekey</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;src <i>src</i> &#8211;esp [&#8211;replay_window&nbsp;<wbr><i>replayw</i>] [<i>&lt;life&gt;</i>] &#8211;enckey <i>ekey</i> &#8211;authkey <i>akey</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;src <i>src</i> &#8211;comp <i>deflate</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;ip4 &#8211;src <i>encap-src</i> &#8211;dst <i>encap-dst</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;ip6 &#8211;src <i>encap-src</i> &#8211;dst <i>encap-dst</i></p>
<dd><i>ipsec</i> <i>spi</i> <i>&lt;SA&gt;</i> &#8211;del</p>
<dd><i>ipsec</i> <i>spi</i> &#8211;help</p>
<dd><i>ipsec</i> <i>spi</i> &#8211;version</p>
<dd><i>ipsec</i> <i>spi</i> &#8211;clear</p>
<dd>
<h2>Description</h2>
<p><i>Spi</i></p>
<dd>creates and deletes IPSEC Security Associations. A Security Association (SA) is a transform through which packet contents are to be processed before being forwarded. A transform can be an IPv4-in-IPv4 or an IPv6-in-IPv6 encapsulation, an IPSEC Authentication Header (authentication with no encryption), or an IPSEC Encapsulation Security Payload (encryption, possibly including authentication). </p>
<p> When a packet is passed from a higher networking layer through an IPSEC virtual interface, a search in the extended routing table (see <code><a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a></code>(8)) yields an effective destination address, a Security Parameters Index (SPI) and a IP protocol number. When an IPSEC packet arrives from the network, its ostensible destination, an SPI and an IP protocol specified by its outermost IPSEC header are used. The destination/SPI/protocol combination is used to select a relevant SA. (See <code><a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a></code>(8) for discussion of how multiple transforms are combined.) </p>
<p> The <i>af</i>, <i>daddr</i>, <i>spi</i> and <i>proto</i> arguments specify the SA to be created or deleted. <i>af</i> is the address family (inet for IPv4, inet6 for IPv6). <i>Daddr</i> is a destination address in dotted-decimal notation for IPv4 or in a coloned hex notation for IPv6. <i>Spi</i> is a number, preceded by &#8216;0x&#8217; for hexadecimal, between <code>0x100</code> and <code>0xffffffff</code>; values from <code>0x0</code> to <code>0xff</code> are reserved. <i>Proto</i> is an ASCII string, &quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot;, specifying the IP protocol. The protocol must agree with the algorithm selected. </p>
<p> Alternatively, the <i>said</i> argument can also specify an SA to be created or deleted. <i>Said</i> combines the three parameters above, such as: &quot;tun.101 [at] 1.2.3.4&quot; or &quot;tun:101@1:2::3:4&quot;, where the address family is specified by &quot;.&quot; for IPv4 and &quot;:&quot; for IPv6. The address family indicators substitute the &quot;0x&quot; for hexadecimal. </p>
<p> The source address, <i>src</i>, must also be provided for the inbound policy check to function. The source address does not need to be included if inbound policy checking has been disabled. </p>
<p> Keys vectors must be entered as hexadecimal or base64 numbers. They should be cryptographically strong random numbers. </p>
<p> All hexadecimal numbers are entered as strings of hexadecimal digits (0-9 and a-f), without spaces, preceded by &#8216;0x&#8217;, where each hexadecimal digit represents 4 bits. All base64 numbers are entered as strings of base64 digits (0-9, A-Z, a-z, &#8216;+&#8217; and &#8216;/&#8217;), without spaces, preceded by &#8216;0s&#8217;, where each hexadecimal digit represents 6 bits and &#8216;=&#8217; is used for padding. </p>
<p> The deletion of an SA which has been grouped will result in the entire chain being deleted. </p>
<p> The form with no additional arguments lists the contents of /proc/net/ipsec_spi. The format of /proc/net/ipsec_spi is discussed in <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5). </p>
<p> The lifetime severity of <code>soft</code> sets a limit when the key management daemons are asked to rekey the SA. The lifetime severity of <code>hard</code> sets a limit when the SA must expire. The lifetime type <code>allocations</code> tells the system when to expire the SA because it is being shared by too many eroutes (not currently used). The lifetime type of <code>bytes</code> tells the system to expire the SA after a certain number of bytes have been processed with that SA. The lifetime type of <code>addtime</code> tells the system to expire the SA a certain number of seconds after the SA was installed. The lifetime type of <code>usetime</code> tells the system to expire the SA a certain number of seconds after that SA has processed its first packet. The lifetime type of <code>packets</code> tells the system to expire the SA after a certain number of packets have been processed with that SA.</p>
<h2>Options</h2>
<p><code>&#8211;af</code></p>
<dl>
<dd>specifies the address family (inet for IPv4, inet6 for IPv6)</dl>
<p> <code>&#8211;edst</code></p>
<dl>
<dd>specifies the effective destination <i>daddr</i> of the Security Association</dl>
<p> <code>&#8211;spi</code></p>
<dl>
<dd>specifies the Security Parameters Index <i>spi</i> of the Security Association</dl>
<p> <code>&#8211;proto</code></p>
<dl>
<dd>specifies the IP protocol <i>proto</i> of the Security Association</dl>
<p> <code>&#8211;said</code></p>
<dl>
<dd>specifies the Security Association in monolithic format</dl>
<p> <code>&#8211;ah</code></p>
<dl>
<dd>add an SA for an IPSEC Authentication Header, specified by the following transform identifier (<code>hmac-md5-96</code> or <code>hmac-sha1-96</code>) (RFC2402, obsoletes RFC1826)</dl>
<p> <code>hmac-md5-96</code></p>
<dl>
<dd>transform following the HMAC and MD5 standards, using a 128-bit <i>key</i> to produce a 96-bit authenticator (RFC2403)</dl>
<p> <code>hmac-sha1-96</code></p>
<dl>
<dd>transform following the HMAC and SHA1 standards, using a 160-bit <i>key</i> to produce a 96-bit authenticator (RFC2404)</dl>
<p> <code>&#8211;esp</code></p>
<dl>
<dd>add an SA for an IPSEC Encapsulation Security Payload, specified by the following transform identifier (<code>3des</code>, or <code>3des-md5-96</code> (RFC2406, obsoletes RFC1827)</dl>
<p> <code>3des</code></p>
<dl>
<dd>encryption transform following the Triple-DES standard in Cipher-Block-Chaining mode using a 64-bit <i>iv</i> (internally generated) and a 192-bit 3DES <i>ekey</i> (RFC2451)</dl>
<p> <code>3des-md5-96</code></p>
<dl>
<dd>encryption transform following the Triple-DES standard in Cipher-Block-Chaining mode with authentication provided by HMAC and MD5 (96-bit authenticator), using a 64-bit <i>iv</i> (internally generated), a 192-bit 3DES <i>ekey</i> and a 128-bit HMAC-MD5 <i>akey</i> (RFC2451, RFC2403)</dl>
<p> <code>3des-sha1-96</code></p>
<dl>
<dd>encryption transform following the Triple-DES standard in Cipher-Block-Chaining mode with authentication provided by HMAC and SHA1 (96-bit authenticator), using a 64-bit <i>iv</i> (internally generated), a 192-bit 3DES <i>ekey</i> and a 160-bit HMAC-SHA1 <i>akey</i> (RFC2451, RFC2404)</dl>
<p> <code>&#8211;replay_window</code> replayw</p>
<dl>
<dd>sets the replay window size; valid values are decimal, 1 to 64</dl>
<p> <code>&#8211;life</code> life_param[,life_param]</p>
<dl>
<dd>sets the lifetime expiry; the format of <code>life_param</code> consists of a comma-separated list of lifetime specifications without spaces; a lifetime specification is comprised of a severity of <code>soft</code> or <code>hard</code> followed by a &#8216;-&#8216;, followed by a lifetime type of <code>allocations</code>, <code>bytes</code>, <code>addtime</code>, <code>usetime</code> or <code>packets</code> followed by an &#8216;=&#8217; and finally by a value</dl>
<p> <code>&#8211;comp</code></p>
<dl>
<dd>add an SA for IPSEC IP Compression, specified by the following transform identifier (<code>deflate</code>) (RFC2393)</dl>
<p> <code>deflate</code></p>
<dl>
<dd>compression transform following the patent-free Deflate compression algorithm (RFC2394)</dl>
<p> <code>&#8211;ip4</code></p>
<dl>
<dd>add an SA for an IPv4-in-IPv4 tunnel from <i>encap-src</i> to <i>encap-dst</i></dl>
<p> <code>&#8211;ip6</code></p>
<dl>
<dd>add an SA for an IPv6-in-IPv6 tunnel from <i>encap-src</i> to <i>encap-dst</i></dl>
<p> <code>&#8211;src</code></p>
<dl>
<dd>specify the source end of an IP-in-IP tunnel from <i>encap-src</i> to <i>encap-dst</i> and also specifies the source address of the Security Association to be used in inbound policy checking and must be the same address family as <i>af</i> and <i>edst</i></dl>
<p> <code>&#8211;dst</code></p>
<dl>
<dd>specify the destination end of an IP-in-IP tunnel from <i>encap-src</i> to <i>encap-dst</i></dl>
<p> <code>&#8211;del</code></p>
<dl>
<dd>delete the specified SA</dl>
<p> <code>&#8211;clear</code></p>
<dl>
<dd>clears the table of <code>SA</code>s</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>display synopsis</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>display version information</dl>
<h2>Examples</h2>
<p>To keep line lengths down and reduce clutter, some of the long keys in these examples have been abbreviated by replacing part of their text with &#8220;&#8230;&#8221;. Keys used when the programs are actually run must, of course, be the full length required for the particular algorithm. </p>
<p> <code>ipsec spi &#8211;af inet &#8211;edst gw2 &#8211;spi 0x125 &#8211;proto esp \</code><code> &#8211;src gw1 \</code><code> &#8211;esp 3des-md5-96 \</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;enckey 0x6630</code>&#8230;<code>97ce&nbsp;<wbr>\</code><code> &#8211;authkey 0x9941</code>&#8230;<code>71df</code> </p>
<p> sets up an SA from <code>gw1</code> to <code>gw2</code> with an SPI of <code>0x125</code> and protocol <code>ESP</code> (50) using <code>3DES</code> encryption with integral <code>MD5-96</code> authentication transform, using an encryption key of <code>0x6630</code>&#8230;<code>97ce</code> and an authentication key of <code>0x9941</code>&#8230;<code>71df</code> (see note above about abbreviated keys). </p>
<p> <code>ipsec spi &#8211;af inet6 &#8211;edst 3049:9::9000:3100 &#8211;spi 0x150 &#8211;proto ah \</code><code> &#8211;src 3049:9::9000:3101 \</code><code> &#8211;ah hmac-md5-96 \</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;authkey 0x1234</code>&#8230;<code>2eda&nbsp;<wbr>\</code> </p>
<p> sets up an SA from <code>3049:9::9000:3101</code> to <code>3049:9::9000:3100</code> with an SPI of <code>0x150</code> and protocol <code>AH</code> (50) using <code>MD5-96</code> authentication transform, using an authentication key of <code>0x1234</code>&#8230;<code>2eda</code> (see note above about abbreviated keys). </p>
<p> <code>ipsec spi &#8211;said tun.987 [at] 192.168.100.100 &#8211;del </code> </p>
<p> deletes an SA to 192.168.100.100 with an SPI of <code>0x987</code> and protocol <code>IPv4-in-IPv4</code> (4). </p>
<p> <code>ipsec spi &#8211;said tun:500 [at] 3049:9::1000:1 &#8211;del </code> </p>
<p> deletes an SA to <code>3049:9::1000:1</code> with an SPI of <code>0x500</code> and protocol <code>IPv6-in-IPv6</code> (4).</p>
<h2>Files</h2>
<p>/proc/net/ipsec_spi, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/8-ipsec_klipsdebug/">ipsec_klipsdebug</a>(8), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Bugs</h2>
<p>The syntax is messy and the transform naming needs work.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
