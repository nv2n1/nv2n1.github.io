---
title: "dnswasher(1)"
name: "dnswasher"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnswasher/"
description: "dnswasher – A PowerDNS nameserver debugging tool"
---

<h2>NAME</h2>
<p> dnswasher &#8211; A PowerDNS nameserver debugging tool</p>
<h2>SYNOPSIS</h2>
<p> <code>dnswasher </code><i>[infile]</i> <i>[outfile]</i></p>
<h2>DESCRIPTION</h2>
<p> dnswasher takes an <i>infile</i> in PCAP format and writtes out <i>outfile</i> also in PCAP format. It copies all network traffic found in <i>infile</i> to <i>outfile</i> except for non DNS traffic. This might be handy when creating bug reports or test cases for DNS software e.g. PowerDNS.</p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap/">pcap</a>(3PCAP), <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8)</p>
<h2>AUTHORS</h2>
<p> This manpage was written by Joerg Jungermann (jj+debian At borkum.net) for the Debian Project and the PowerDNS versatile DNS server. </p>
<h2>Index</h2>
