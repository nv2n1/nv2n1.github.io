---
title: "pcap-linktype(7)"
name: "pcap-linktype"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pcap-linktype/"
description: "pcap-linktype – link-layer header types supported by libpcap"
---

<p>pcap-linktype &#8211; link-layer header types supported by libpcap</p>
<h2>Description</h2>
<p>For a live capture or &#8220;savefile&#8221;, libpcap supplies, as the return value of the <code><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_datalink/">pcap_datalink</a></code>(3PCAP) routine, a value that indicates the type of link-layer header at the beginning of the packets it provides. This is not necessarily the type of link-layer header that the packets being captured have on the network from which they&#8217;re being captured; for example, packets from an IEEE 802.11 network might be provided by libpcap with Ethernet headers that the network adapter or the network adapter driver generates from the 802.11 headers. The names for those values begin with <code>DLT_</code>, so they are sometimes called &quot;DLT_ values&quot;. </p>
<p> The values stored in the link-layer header type field in the savefile header are, in most but not all cases, the same as the values returned by <code>pcap_datalink()</code>. The names for those values begin with <code>LINKTYPE_</code>. </p>
<p> The link-layer header types supported by libpcap are described at <a rel="nofollow" href="http://www.tcpdump.org/linktypes.html.">http://www.tcpdump.org/linktypes.html.</a></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_datalink/">pcap_datalink</a>(3PCAP) </p>
