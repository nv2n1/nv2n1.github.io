---
title: "udplite(7)"
name: "udplite"
section: "7"
letter: "u"
url: "/docs/linux/man/7-udplite/"
description: "udplite – Lightweight User Datagram Protocol"
---

<p>udplite &#8211; Lightweight User Datagram Protocol</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;
sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE);</code></pre>
<h2>Description</h2>
<p>This is an implementation of the Lightweight User Datagram Protocol (UDP-Lite), as described in RFC 3828. </p>
<p> UDP-Lite is an extension of UDP (RFC 768) to support variable-length checksums. This has advantages for some types of multimedia transport that may be able to make use of slightly damaged datagrams, rather than having them discarded by lower-layer protocols. </p>
<p> The variable-length checksum coverage is set via a <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) option. If this option is not set, the only difference from UDP is in using a different IP protocol identifier (IANA number 136). </p>
<p> The UDP-Lite implementation is a full extension of <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7)&#8212;that is, it shares the same API and API behavior, and in addition offers two socket options to control the checksum coverage.</p>
<h3>Address format</h3>
<p>UDP-Litev4 uses the <i>sockaddr_in</i> address format described in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). UDP-Litev6 uses the <i>sockaddr_in6</i> address format described in <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7).</p>
<h3>Socket options</h3>
<p>To set or get a UDP-Lite socket option, call <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to write the option with the option level argument set to <code>IPPROTO_UDPLITE</code>. In addition, all <code>IPPROTO_UDP</code> socket options are valid on a UDP-Lite socket. See <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7) for more information. </p>
<p> The following two options are specific to UDP-Lite.</p>
<dl>
<dt><code>UDPLITE_SEND_CSCOV</code></p>
<dd>This option sets the sender checksum coverage and takes an <i>int</i> as argument, with a checksum coverage value in the range 0..2^16-1.</p>
<dd>A value of 0 means that the entire datagram is always covered. Values from 1-7 are illegal (RFC 3828, 3.1) and are rounded up to the minimum coverage of 8.</p>
<dd>With regard to IPv6 jumbograms (RFC 2675), the UDP-Litev6 checksum coverage is limited to the first 2^16-1 octets, as per RFC 3828, 3.5. Higher values are therefore silently truncated to 2^16-1. If in doubt, the current coverage value can always be queried using <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2).</p>
<dt><code>UDPLITE_RECV_CSCOV</code></p>
<dd>This is the receiver-side analogue and uses the same argument format and value range as <code>UDPLITE_SEND_CSCOV</code>. This option is not required to enable traffic with partial checksum coverage. Its function is that of a traffic filter: when enabled, it instructs the kernel to drop all packets which have a coverage <i>less</i> than the specified coverage value.</p>
<dd>When the value of <code>UDPLITE_RECV_CSCOV</code> exceeds the actual packet coverage, incoming packets are silently dropped, but may generate a warning message in the system log.</dl>
<h2>Errors</h2>
<p>All errors documented for <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7) may be returned. UDP-Lite does not add further errors.</p>
<h2>Files</h2>
<dl>
<dt><i>/proc/net/snmp</i></p>
<dd>Basic UDP-Litev4 statistics counters.</p>
<dt><i>/proc/net/snmp6</i></p>
<dd>Basic UDP-Litev6 statistics counters.</dl>
<h2>Versions</h2>
<p>UDP-Litev4/v6 first appeared in Linux 2.6.20.</p>
<h2>Bugs</h2>
<p>Where glibc support is missing, the following definitions are needed: </p>
<pre><code>#define IPPROTO_UDPLITE     136

#define UDPLITE_SEND_CSCOV  10
#define UDPLITE_RECV_CSCOV  11</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7) </p>
<p> RFC 3828 for the Lightweight User Datagram Protocol (UDP-Lite). </p>
<p> <i>Documentation/networking/udplite.txt</i> in the Linux kernel source tree</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
