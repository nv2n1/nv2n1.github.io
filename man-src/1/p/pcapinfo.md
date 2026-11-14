---
title: "pcapinfo(1)"
name: "pcapinfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcapinfo/"
description: "pcapinfo – Prints detailed information about the network devices"
---

<h2 class="name">NAME</h2>
<p> pcapinfo &#8211; Prints detailed information about the network devices </p>
<h2>SYNOPSIS</h2>
<pre>
    pcapinfo
</pre>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>DESCRIPTION</h2>
<p> <code>pcapinfo</code> prints detailed information about the network devices and Pcap library available on the current host. Here is an example: </p>
<pre><code>
Host information-- -- -- -- -- -- -- --Hostname : fangorn.maddingue.net
                                                      Aliases : fangorn.local fangorn
                                                                    Pcap version : libpcap version 0.8.3 Devices information-- -- -- -- -- -- -- -- -- -Device eth0(default)
                                                                                       Description : No description available
                                                                                                     Link type : Ethernet,
    no autonegotiation, 10baseT - HD, link ok Hardware address : 00 : 0c : 6e : 0a : c3 : ca Network address : 10.0.1.51 Network mask : 255.255.255.0 Flags : up running broadcast multicast Device eth1 Description : No description available Link type : Ethernet, no autonegotiation, 10baseT - HD, link ok Hardware address : 00 : 26 : 54 : 0a : d8 : 4d Network address : 192.168.1.51 Network mask : 255.255.255.0 Flags : up running broadcast multicast
</code></pre>
<p> The device marked as <tt>&quot;(default)&quot;</tt> is the one returned when calling <tt>&quot;Net::Pcap::lookupdev()&quot;</tt> </p>
<p> Some information like the link type can only be gathered with administrative privileges.</p>
<h2>AUTHOR</h2>
<p> Sebastien Aperghis-Tramoni, &lt;sebastien [at] aperghis.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005, 2006, 2007, 2008, 2009 Sebastien Aperghis-Tramoni. All rights reserved. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
