---
title: "ipsec_eroute(5)"
name: "ipsec_eroute"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec_eroute/"
description: "ipsec_eroute – list of existing eroutes"
---

<p>ipsec_eroute &#8211; list of existing eroutes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>eroute</i></p>
<dd><i>cat/proc/net/ipsec_eroute</i></dl>
<h2>Obsolete</h2>
<dd>Note that eroute is only supported on the classic KLIPS stack. It is not supported on any other stack and will be completely removed in future versions. On the <code>mast</code> stack, use <i>ipsec policy</i>, on the <code>netkey</code> stack, use <i>ip xfrm</i></p>
<h2>Description</h2>
<p>/proc/net/ipsec_eroute lists the IPSEC extended routing tables, which control what (if any) processing is applied to non-encrypted packets arriving for IPSEC processing and forwarding. At this point it is a read-only file. </p>
<p> A table entry consists of: </p>
<p> +</p>
<dl>
<dd>packet count,</dl>
<p> +</p>
<dl>
<dd>source address with mask and source port (0 if all ports or not applicable)</dl>
<p> +</p>
<dl>
<dd>a &#8216;-&gt;&#8217; separator for visual and automated parsing between src and dst</dl>
<p> +</p>
<dl>
<dd>destination address with mask and destination port (0 if all ports or not applicable)</dl>
<p> +</p>
<dl>
<dd>a &#8216;=&gt;&#8217; separator for visual and automated parsing between selection criteria and SAID to use</dl>
<p> +</p>
<dl>
<dd>SAID (Security Association IDentifier), comprised of:</dl>
<p> +</p>
<dl>
<dd>protocol (<i>proto</i>),</dl>
<p> +</p>
<dl>
<dd>address family (<i>af</i>), where &#8216;.&#8217; stands for IPv4 and &#8216;:&#8217; for IPv6</dl>
<p> +</p>
<dl>
<dd>Security Parameters Index (<i>SPI</i>),</dl>
<p> +</p>
<dl>
<dd>effective destination (<i>edst</i>), where the packet should be forwarded after processing (normally the other security gateway) together indicate which Security Association should be used to process the packet,</dl>
<p> +</p>
<dl>
<dd>a &#8216;:&#8217; separating the SAID from the transport protocol (0 if all protocols)</dl>
<p> +</p>
<dl>
<dd>source identity text string with no whitespace, in parens,</dl>
<p> +</p>
<dl>
<dd>destination identity text string with no whitespace, in parens</dl>
<p> Addresses are written as IPv4 dotted quads or IPv6 coloned hex, protocol is one of &quot;ah&quot;, &quot;esp&quot;, &quot;comp&quot; or &quot;tun&quot; and SPIs are prefixed hexadecimal numbers where the prefix &#8216;.&#8217; is for IPv4 and the prefix &#8216;:&#8217; is for IPv6 </p>
<p> SAIDs are written as &quot;protoafSPI [at] edst&quot;. There are also 5 &quot;magic&quot; SAIDs which have special meaning: </p>
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
<h2>Examples</h2>
<p><code>1867 172.31.252.0/24:0 -&gt; 0.0.0.0/0:0 =&gt; tun0x130 [at] 192.168.43.1:0 </code><code> () ()</code> </p>
<p> means that 1,867 packets have been sent to an <code>eroute</code> that has been set up to protect traffic between the subnet 172.31.252.0 with a subnet mask of 24 bits and the default address/mask represented by an address of 0.0.0.0 with a subnet mask of 0 bits using the local machine as a security gateway on this end of the tunnel and the machine 192.168.43.1 on the other end of the tunnel with a Security Association IDentifier of <code>tun0x130 [at] 192.168.43.1</code> which means that it is a tunnel mode connection (4, IPPROTO_IPIP) with a Security Parameters Index of 130 in hexadecimal with no identies defined for either end. </p>
<p> <code>746 192.168.2.110/32:0 -&gt; 192.168.2.120/32:25 =&gt; esp0x130 [at] 192.168.2.120:6 </code><code> () ()</code> </p>
<p> means that 746 packets have been sent to an <code>eroute</code> that has been set up to protect traffic sent from any port on the host 192.168.2.110 to the SMTP (TCP, port 25) port on the host 192.168.2.120 with a Security Association IDentifier of <code>tun0x130 [at] 192.168.2.120</code> which means that it is a transport mode connection with a Security Parameters Index of 130 in hexadecimal with no identies defined for either end. </p>
<p> <code>125 3049:1::/64 -&gt; 0:0/0 =&gt; tun:130 [at] 3058:4::5 () ()</code> </p>
<p> means that 125 packets have been sent to an <code>eroute</code> that has been set up to protect traffic between the subnet <code>3049:1::</code> with a subnet mask of 64 bits and the default address/mask represented by an address of <code>0:0</code> with a subnet mask of 0 bits using the local machine as a security gateway on this end of the tunnel and the machine <code>3058:4::5</code> on the other end of the tunnel with a Security Association IDentifier of <code>tun:130 [at] 3058:4::5</code> which means that it is a tunnel mode connection with a Security Parameters Index of 130 in hexadecimal with no identies defined for either end. </p>
<p> <code>42 192.168.6.0/24:0 -&gt; 192.168.7.0/24:0 =&gt; %passthrough</code> </p>
<p> means that 42 packets have been sent to an <code>eroute</code> that has been set up to pass the traffic from the subnet 192.168.6.0 with a subnet mask of 24 bits and to subnet 192.168.7.0 with a subnet mask of 24 bits without any IPSEC processing with no identies defined for either end. </p>
<p> <code>2112 192.168.8.55/32:0 -&gt; 192.168.9.47/24:0 =&gt; %hold (east) ()</code> </p>
<p> means that 2112 packets have been sent to an <code>eroute</code> that has been set up to hold the traffic from the host 192.168.8.55 and to host 192.168.9.47 until a key exchange from a Key Management daemon succeeds and puts in an SA or fails and puts in a pass or drop eroute depending on the default configuration with the local client defined as &quot;east&quot; and no identy defined for the remote end. </p>
<p> <code>2001 192.168.2.110/32:0 -&gt; 192.168.2.120/32:0 =&gt; </code><code> esp0xe6de [at] 192.168.2.120:0 () ()</code> </p>
<p> means that 2001 packets have been sent to an <code>eroute</code> that has been set up to protect traffic between the host 192.168.2.110 and the host 192.168.2.120 using 192.168.2.110 as a security gateway on this end of the connection and the machine 192.168.2.120 on the other end of the connection with a Security Association IDentifier of <code>esp0xe6de [at] 192.168.2.120</code> which means that it is a transport mode connection with a Security Parameters Index of <code>e6de</code> in hexadecimal using Encapsuation Security Payload protocol (50, IPPROTO_ESP) with no identies defined for either end. </p>
<p> <code>1984 3049:1::110/128 -&gt; 3049:1::120/128 =&gt; </code><code> ah:f5ed [at] 3049:1::120 () ()</code> </p>
<p> means that 1984 packets have been sent to an <code>eroute</code> that has been set up to authenticate traffic between the host <code>3049:1::110</code> and the host <code>3049:1::120</code> using <code>3049:1::110</code> as a security gateway on this end of the connection and the machine <code>3049:1::120</code> on the other end of the connection with a Security Association IDentifier of <code>ah:f5ed [at] 3049:1::120</code> which means that it is a transport mode connection with a Security Parameters Index of <code>f5ed</code> in hexadecimal using Authentication Header protocol (51, IPPROTO_AH) with no identies defined for either end.</p>
<h2>Files</h2>
<p>/proc/net/ipsec_eroute, /usr/local/bin/ipsec</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipsec/">ipsec</a>(8), <a href="/docs/linux/man/5-ipsec_tncfg/">ipsec_tncfg</a>(5), <a href="/docs/linux/man/5-ipsec_spi/">ipsec_spi</a>(5), <a href="/docs/linux/man/5-ipsec_spigrp/">ipsec_spigrp</a>(5), <a href="/docs/linux/man/5-ipsec_klipsdebug/">ipsec_klipsdebug</a>(5), <a href="/docs/linux/man/8-ipsec_eroute/">ipsec_eroute</a>(8), <a href="/docs/linux/man/5-ipsec_version/">ipsec_version</a>(5), <a href="/docs/linux/man/5-ipsec_pf_key/">ipsec_pf_key</a>(5)</p>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Richard Guy Briggs.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
