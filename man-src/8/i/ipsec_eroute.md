---
title: "ipsec_eroute(8)"
name: "ipsec_eroute"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_eroute/"
description: "ipsec_eroute – manipulate IPSEC extended routing tables"
---

<p>ipsec_eroute &#8211; manipulate IPSEC extended routing tables</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec eroute</code> <i>&#8211;add</i>&nbsp;<wbr><code>&#8211;eraf</code>&nbsp;<wbr><i>(inet | inet6)</i>&nbsp;<wbr><code>&#8211;src</code>&nbsp;<wbr><i>src/srcmaskbits|srcmask</i>&nbsp;<wbr><code>&#8211;dst</code>&nbsp;<wbr><i>dst/dstmaskbits|dstmask</i>&nbsp;<wbr>[[<code>&#8211;transport-proto</code>&nbsp;<wbr><i>transport-protocol</i>]]&nbsp;<wbr>[<code>&#8211;src-port&nbsp;<wbr></code><i>source-port</i>]&nbsp;<wbr>[<code>&#8211;dst-port&nbsp;<wbr></code><i>dest-port</i>]&nbsp;<wbr>[&lt;SAID&gt;]</p>
<dt> <code>ipsec eroute</code> <i>&#8211;replace</i>&nbsp;<wbr><code>&#8211;eraf</code>&nbsp;<wbr><i>(inet | inet6)</i>&nbsp;<wbr><code>&#8211;src</code>&nbsp;<wbr><i>src/srcmaskbits|srcmask</i>&nbsp;<wbr><code>&#8211;dst</code>&nbsp;<wbr><i>dst/dstmaskbits|dstmask</i>&nbsp;<wbr>[[<code>&#8211;transport-proto</code>&nbsp;<wbr><i>transport-protocol</i>]]&nbsp;<wbr>[<code>&#8211;src-port&nbsp;<wbr></code><i>source-port</i>]&nbsp;<wbr>[<code>&#8211;dst-port&nbsp;<wbr></code><i>dest-port</i>]&nbsp;<wbr>[&lt;SAID&gt;]</p>
<dt> <code>ipsec eroute</code> <i>&#8211;del</i>&#8211;del<code>&#8211;eraf</code>&nbsp;<wbr><i>(inet | inet6)</i>&nbsp;<wbr><code>&#8211;src</code><i>src/srcmaskbits|srcmask</i><code>&#8211;dst</code><i>dst/dstmaskbits|dstmask</i>&nbsp;<wbr>[[<code>&#8211;transport-proto</code>&nbsp;<wbr><i>transport-protocol</i>]]&nbsp;<wbr>[<code>&#8211;src-port&nbsp;<wbr></code><i>source-port</i>]&nbsp;<wbr>[<code>&#8211;dst-port&nbsp;<wbr></code><i>dest-port</i>]&nbsp;<wbr>[&lt;SAID&gt;]</p>
<dt> <code>ipsec eroute</code> &#8211;clear</p>
<dt> <code>ipsec eroute</code> &#8211;help</p>
<dt> <code>ipsec eroute</code> &#8211;version</dl>
<h2>Said Description</h2>
<dd>Where &lt;SAID&gt; is &#8211;af (inet | inet6) &#8211;edst edst &#8211;spi spi &#8211;proto proto OR &#8211;said said OR &#8211;said (%passthrough | %passthrough4 | %passthrough6 | %drop | %reject | %trap | %hold | %pass )</p>
<h2>Description</h2>
<p><i>Eroute</i> manages the IPSEC extended routing tables, which control what (if any) processing is applied to non-encrypted packets arriving for IPSEC processing and forwarding. The form with no additional arguments lists the contents of /proc/net/ipsec_eroute. The <code>&#8211;add</code> form adds a table entry, the <code>&#8211;replace</code> form replaces a table entry, while the <code>&#8211;del</code> form deletes one. The <code>&#8211;clear</code> form deletes the entire table. </p>
<p> A table entry consists of: </p>
<p> +</p>
<dl>
<dd>source and destination addresses, with masks, source and destination ports and protocol for selection of packets. The source and destination ports are only legal if the transport protocol is <code>TCP</code> or <code>UDP.</code> A port can be specified as either decimal, hexadecimal (leading 0x), octal (leading 0) or a name listed in the first column of /etc/services. A transport protocol can be specified as either decimal, hexadecimal (leading 0x), octal (leading 0) or a name listed in the first column of /etc/protocols. If a transport protocol or port is not specified then it defaults to 0 which means all protocols or all ports respectively.</dl>
<p> +</p>
<dl>
<dd>Security Association IDentifier, comprised of:</dl>
<p> +</p>
<dl>
<dd>protocol (<i>proto</i>), indicating (together with the effective destination and the security parameters index) which Security Association should be used to process the packet</dl>
<p> +</p>
<dl>
<dd>address family (<i>af</i>),</dl>
<p> +</p>
<dl>
<dd>Security Parameters Index (<i>spi</i>), indicating (together with the effective destination and protocol) which Security Association should be used to process the packet (must be larger than or equal to 0x100)</dl>
<p> +</p>
<dl>
<dd>effective destination (<i>edst</i>), where the packet should be forwarded after processing (normally the other security gateway)</dl>
<p> +</p>
<dl>
<dd>OR</dl>
<p> +</p>
<dl>
<dd>SAID (<i>said</i>), indicating which Security Association should be used to process the packet</dl>
<p> Addresses are written as IPv4 dotted quads or IPv6 coloned hex, protocol is one of &quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot; and SPIs are prefixed hexadecimal numbers where &#8216;.&#8217; represents IPv4 and &#8216;:&#8217; stands for IPv6. </p>
<p> SAIDs are written as &quot;protoafSPI [at] address&quot;. There are also 5 &quot;magic&quot; SAIDs which have special meaning: </p>
<p> +</p>
<dl>
<dd><code>%drop</code> means that matches are to be dropped</dl>
<p> +</p>
<dl>
<dd><code>%reject</code> means that matches are to be dropped and an ICMP returned, if possible to inform</dl>
<p> +</p>
<dl>
<dd><code>%trap</code> means that matches are to trigger an ACQUIRE message to the Key Management daemon(s) and a hold eroute will be put in place to prevent subsequent packets also triggering ACQUIRE messages.</dl>
<p> +</p>
<dl>
<dd><code>%hold</code> means that matches are to stored until the eroute is replaced or until that eroute gets reaped</dl>
<p> +</p>
<dl>
<dd><code>%pass</code> means that matches are to allowed to pass without IPSEC processing</dl>
<p> The format of /proc/net/ipsec_eroute is listed in <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5).</p>
<h2>Examples</h2>
<p><code>ipsec eroute &#8211;add &#8211;eraf inet &#8211;src 192.168.0.1/32 \</code><code> &#8211;dst 192.168.2.0/24 &#8211;af inet &#8211;edst 192.168.0.2 \</code><code> &#8211;spi 0x135 &#8211;proto tun</code> </p>
<p> sets up an <code>eroute</code> on a Security Gateway to protect traffic between the host 192.168.0.1 and the subnet 192.168.2.0 with 24 bits of subnet mask via Security Gateway 192.168.0.2 using the Security Association with address 192.168.0.2, Security Parameters Index <code>0x135</code> and protocol <code>tun</code> (50, IPPROTO_ESP). </p>
<p> <code>ipsec eroute &#8211;add &#8211;eraf inet6 &#8211;src 3049:1::1/128 \</code><code> &#8211;dst 3049:2::/64 &#8211;af inet6 &#8211;edst 3049:1::2 \</code><code> &#8211;spi 0x145 &#8211;proto tun</code> </p>
<p> sets up an <code>eroute</code> on a Security Gateway to protect traffic between the host <code>3049:1::1</code> and the subnet <code>3049:2::</code> with 64 bits of subnet mask via Security Gateway <code>3049:1::2</code> using the Security Association with address <code>3049:1::2</code>, Security Parameters Index <code>0x145</code> and protocol <code>tun</code> (50, IPPROTO_ESP). </p>
<p> <code>ipsec eroute &#8211;replace &#8211;eraf inet &#8211;src company.com/24 \</code><code> &#8211;dst <a href="ftp://ftp.ngo.org">ftp.ngo.org</a>/32 &#8211;said tun.135 [at] gw.ngo.org</code> </p>
<p> replaces an <code>eroute</code> on a Security Gateway to protect traffic between the subnet <code>company.com</code> with 24 bits of subnet mask and the host <code><a href="ftp://ftp.ngo.org">ftp.ngo.org</a></code> via Security Gateway <code>gw.ngo.org</code> using the Security Association with Security Association ID <code>tun0x135 [at] gw.ngo.org</code> </p>
<p> <code>ipsec eroute &#8211;del &#8211;eraf inet &#8211;src company.com/24 \</code><code> &#8211;dst <a rel="nofollow" href="http://www.ietf.org">www.ietf.org</a>/32 &#8211;said %passthrough4</code> </p>
<p> deletes an <code>eroute</code> on a Security Gateway that allowed traffic between the subnet <code>company.com</code> with 24 bits of subnet mask and the host <code><a rel="nofollow" href="http://www.ietf.org">www.ietf.org</a></code> to pass in the clear, unprocessed. </p>
<p> <code>ipsec eroute &#8211;add &#8211;eraf inet &#8211;src company.com/24 \</code><code> &#8211;dst mail.ngo.org/32 &#8211;transport-proto 6 \</code><code> &#8211;dst-port 110 &#8211;said tun.135 [at] mail.ngo.org</code> </p>
<p> sets up an <code>eroute</code> on on a Security Gateway to protect only TCP traffic on port 110 (pop3) between the subnet <code>company.com</code> with 24 bits of subnet mask and the host <code><a href="ftp://ftp.ngo.org">ftp.ngo.org</a></code> via Security Gateway <code>mail.ngo.org</code> using the Security Association with Security Association ID <code>tun0x135 [at] mail.ngo.org.</code> Note that any other traffic bound for <code>mail.ngo.org</code> that is routed via the ipsec device will be dropped. If you wish to allow other traffic to pass through then you must add a %pass rule. For example the following rule when combined with the above will ensure that POP3 messages read from <code>mail.ngo.org</code> will be encrypted but all other traffic to/from <code>mail.ngo.org</code> will be in clear text. </p>
<p> <code>ipsec eroute &#8211;add &#8211;eraf inet &#8211;src company.com/24 \</code><code> &#8211;dst mail.ngo.org/32 &#8211;said %pass</code></p>
<h2>Files</h2>
<p>/proc/net/ipsec_eroute, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a>(8), <a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a>(8), <a href="/docs/linux/man/8-ipsec_spigrp/">ipsec_spigrp</a>(8), <a href="/docs/linux/man/8-ipsec_klipsdebug/">ipsec_klipsdebug</a>(8), <a href="/docs/linux/man/5-ipsec_eroute/">ipsec_eroute</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
