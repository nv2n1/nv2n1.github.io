---
title: "pcap-config(1)"
name: "pcap-config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcap-config/"
description: "pcap-config – write libpcap compiler and linker flags to standard output"
---

<h2>NAME</h2>
<p> pcap-config &#8211; write libpcap compiler and linker flags to standard output</p>
<h2>SYNOPSIS</h2>
<p> <code>pcap-config</code> [ <code>&#8211;static</code> ] [ <code>&#8211;cflags | &#8211;libs | &#8211;additional-libs</code> ]</p>
<h2>DESCRIPTION</h2>
<p> When run with the <code>&#8211;cflags</code> option, <i>pcap-config</i> writes to the standard output the <code>-I</code> compiler flags required to include libpcap&#8217;s header files. When run with the <code>&#8211;libs</code> option, <i>pcap-config</i> writes to the standard output the <code>-L</code> and <code>-l</code> linker flags required to link with libpcap, including <code>-l</code> flags for libraries required by libpcap. When run with the <code>&#8211;additional-libs</code> option, <i>pcap-config</i> writes to the standard output the <code>-L</code> and <code>-l</code> flags for libraries required by libpcap, but not the <code>-lpcap</code> flag to link with libpcap itself. </p>
<p> By default, it writes flags appropriate for compiling with a dynamically-linked version of libpcap; the <code>&#8211;static</code> flag causes it to write flags appropriate for compiling with a statically-linked version of libpcap.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap/">pcap</a>(3PCAP) </p>
<h2>Index</h2>
