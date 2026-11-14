---
title: "tc-csum(8)"
name: "tc-csum"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-csum/"
description: "csum – checksum update action"
---

<p>csum &#8211; checksum update action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action csum</code> <i>UPDATE</i> </p>
<pre><code>UPDATE := TARGET [ UPDATE ]
TARGET := {

    ip4h |

    icmp |

    igmp |

    tcp |

    udp |

    udplite |

    sctp |

    SWEETS }
SWEETS := {

    and | or | + }</code></pre>
<h2>Description</h2>
<p>The <code>csum</code> action triggers checksum recalculation of specified packet headers. It is commonly used to fix incorrect checksums after the <code>pedit</code> action has modified the packet content.</p>
<h2>Options</h2>
<dl>
<dt><i>TARGET</i></p>
<dd>Specify which headers to update: IPv4 header (<code>ip4h</code>), ICMP header (<code>icmp</code>), IGMP header (<code>igmp</code>), TCP header (<code>tcp</code>), UDP header (<code>udp</code>), UDPLite header (<code>udplite</code>) or SCTP header (<code>sctp</code>).</p>
<dt><code>SWEETS</code></p>
<dd>These are merely syntactic sugar and ignored internally.</dl>
<h2>Examples</h2>
<p>The following performs stateless NAT for incoming packets from 192.0.2.100 to new destination 198.51.100.1. Assuming these are UDP packets, both IP and UDP checksums have to be recalculated:</p>
<dl>
<dd># tc qdisc add dev eth0 ingress handle ffff: # tc filter add dev eth0 prio 1 protocol ip parent ffff: \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip src 192.0.2.100/32 flowid :1 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit munge ip dst set 198.51.100.1 pipe \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>csum ip and udp
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-pedit/">tc-pedit</a></code>(8) </p>
