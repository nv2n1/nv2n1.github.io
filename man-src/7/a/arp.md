---
title: "arp(7)"
name: "arp"
section: "7"
letter: "a"
url: "/docs/linux/man/7-arp/"
description: "arp – Linux ARP kernel module."
---

<p>arp &#8211; Linux ARP kernel module.</p>
<h2>Description</h2>
<p>This kernel protocol module implements the Address Resolution Protocol defined in RFC 826. It is used to convert between Layer2 hardware addresses and IPv4 protocol addresses on directly connected networks. The user normally doesn&#8217;t interact directly with this module except to configure it; instead it provides a service for other protocols in the kernel. A user process can receive ARP packets by using <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7) sockets. There is also a mechanism for managing the ARP cache in user-space by using <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) sockets. The ARP table can also be controlled via <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) on any <code>AF_INET</code> socket. The ARP module maintains a cache of mappings between hardware addresses and protocol addresses. The cache has a limited size so old and less frequently used entries are garbage-collected. Entries which are marked as permanent are never deleted by the garbage-collector. The cache can be directly manipulated by the use of ioctls and its behavior can be tuned by the <i>/proc</i> interfaces described below. When there is no positive feedback for an existing mapping after some time (see the <i>/proc</i> interfaces below), a neighbor cache entry is considered stale. Positive feedback can be gotten from a higher layer; for example from a successful TCP ACK. Other protocols can signal forward progress using the <code>MSG_CONFIRM</code> flag to <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). When there is no forward progress, ARP tries to reprobe. It first tries to ask a local arp daemon <code>app_solicit</code> times for an updated MAC address. If that fails and an old MAC address is known, a unicast probe is sent <code>ucast_solicit</code> times. If that fails too, it will broadcast a new ARP request to the network. Requests are sent only when there is data queued for sending. Linux will automatically add a nonpermanent proxy arp entry when it receives a request for an address it forwards to and proxy arp is enabled on the receiving interface. When there is a reject route for the target, no proxy arp entry is added.</p>
<h3>Ioctls</h3>
<p>Three ioctls are available on all <code>AF_INET</code> sockets. They take a pointer to a <i>struct arpreq</i> as their argument. </p>
<pre><code>struct arpreq {
    struct sockaddr arp_pa;      /* protocol address */
    struct sockaddr arp_ha;      /* hardware address */
    int arp_flags;               /* flags */
    struct sockaddr arp_netmask; /* netmask of protocol address */
    char arp_dev[16];
};</code></pre>
<p> <code>SIOCSARP</code>, <code>SIOCDARP</code> and <code>SIOCGARP</code> respectively set, delete and get an ARP mapping. Setting and deleting ARP maps are privileged operations and may be performed only by a process with the <code>CAP_NET_ADMIN</code> capability or an effective UID of 0. <i>arp_pa</i> must be an <code>AF_INET</code> address and <i>arp_ha</i> must have the same type as the device which is specified in <i>arp_dev</i>. <i>arp_dev</i> is a zero-terminated string which names a device.</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><i>arp_flags</i>
</td>
</tr>
<tr VALIGN=top>
<td>flag</td>
<td>meaning
</td>
</tr>
<tr VALIGN=top>
<td>ATF_COM</td>
<td>Lookup complete
</td>
</tr>
<tr VALIGN=top>
<td>ATF_PERM</td>
<td>Permanent entry
</td>
</tr>
<tr VALIGN=top>
<td>ATF_PUBL</td>
<td>Publish entry
</td>
</tr>
<tr VALIGN=top>
<td>ATF_USETRAILERS</td>
<td>Trailers requested
</td>
</tr>
<tr VALIGN=top>
<td>ATF_NETMASK</td>
<td>Use a netmask
</td>
</tr>
<tr VALIGN=top>
<td>ATF_DONTPUB</td>
<td>Don&#8217;t answer
</td>
</tr>
</table>
</dl>
<p> If the <code>ATF_NETMASK</code> flag is set, then <i>arp_netmask</i> should be valid. Linux 2.2 does not support proxy network ARP entries, so this should be set to 0xffffffff, or 0 to remove an existing proxy arp entry. <code>ATF_USETRAILERS</code> is obsolete and should not be used.</p>
<h3>/proc interfaces</h3>
<p>ARP supports a range of <i>/proc</i> interfaces to configure parameters on a global or per-interface basis. The interfaces can be accessed by reading or writing the <i>/proc/sys/net/ipv4/neigh/*/*</i> files. Each interface in the system has its own directory in <i>/proc/sys/net/ipv4/neigh/</i>. The setting in the &quot;default&quot; directory is used for all newly created devices. Unless otherwise specified, time-related interfaces are specified in seconds.</p>
<dl>
<dt><i>anycast_delay</i> (since Linux 2.2)</p>
<dd>The maximum number of jiffies to delay before replying to a IPv6 neighbor solicitation message. Anycast support is not yet implemented. Defaults to 1 second.</p>
<dt><i>app_solicit</i> (since Linux 2.2)</p>
<dd>The maximum number of probes to send to the user space ARP daemon via netlink before dropping back to multicast probes (see <i>mcast_solicit</i>). Defaults to 0.</p>
<dt><i>base_reachable_time</i> (since Linux 2.2)</p>
<dd>Once a neighbor has been found, the entry is considered to be valid for at least a random value between <i>base_reachable_time</i>/2 and 3*<i>base_reachable_time</i>/2. An entry&#8217;s validity will be extended if it receives positive feedback from higher level protocols. Defaults to 30 seconds. This file is now obsolete in favor of <i>base_reachable_time_ms</i>.</p>
<dt><i>base_reachable_time_ms</i> (since Linux 2.6.12)</p>
<dd>As for <i>base_reachable_time</i>, but measures time in milliseconds. Defaults to 30000 milliseconds.</p>
<dt><i>delay_first_probe_time</i> (since Linux 2.2)</p>
<dd>Delay before first probe after it has been decided that a neighbor is stale. Defaults to 5 seconds.</p>
<dt><i>gc_interval</i> (since Linux 2.2)</p>
<dd>How frequently the garbage collector for neighbor entries should attempt to run. Defaults to 30 seconds.</p>
<dt><i>gc_stale_time</i> (since Linux 2.2)</p>
<dd>Determines how often to check for stale neighbor entries. When a neighbor entry is considered stale, it is resolved again before sending data to it. Defaults to 60 seconds.</p>
<dt><i>gc_thresh1</i> (since Linux 2.2)</p>
<dd>The minimum number of entries to keep in the ARP cache. The garbage collector will not run if there are fewer than this number of entries in the cache. Defaults to 128.</p>
<dt><i>gc_thresh2</i> (since Linux 2.2)</p>
<dd>The soft maximum number of entries to keep in the ARP cache. The garbage collector will allow the number of entries to exceed this for 5 seconds before collection will be performed. Defaults to 512.</p>
<dt><i>gc_thresh3</i> (since Linux 2.2)</p>
<dd>The hard maximum number of entries to keep in the ARP cache. The garbage collector will always run if there are more than this number of entries in the cache. Defaults to 1024.</p>
<dt><i>locktime</i> (since Linux 2.2)</p>
<dd>The minimum number of jiffies to keep an ARP entry in the cache. This prevents ARP cache thrashing if there is more than one potential mapping (generally due to network misconfiguration). Defaults to 1 second.</p>
<dt><i>mcast_solicit</i> (since Linux 2.2)</p>
<dd>The maximum number of attempts to resolve an address by multicast/broadcast before marking the entry as unreachable. Defaults to 3.</p>
<dt><i>proxy_delay</i> (since Linux 2.2)</p>
<dd>When an ARP request for a known proxy-ARP address is received, delay up to <i>proxy_delay</i> jiffies before replying. This is used to prevent network flooding in some cases. Defaults to 0.8 seconds.</p>
<dt><i>proxy_qlen</i> (since Linux 2.2)</p>
<dd>The maximum number of packets which may be queued to proxy-ARP addresses. Defaults to 64.</p>
<dt><i>retrans_time</i> (since Linux 2.2)</p>
<dd>The number of jiffies to delay before retransmitting a request. Defaults to 1 second. This file is now obsolete in favor of <i>retrans_time_ms</i>.</p>
<dt><i>retrans_time_ms</i> (since Linux 2.6.12)</p>
<dd>The number of milliseconds to delay before retransmitting a request. Defaults to 1000 milliseconds.</p>
<dt><i>ucast_solicit</i> (since Linux 2.2)</p>
<dd>The maximum number of attempts to send unicast probes before asking the ARP daemon (see <i>app_solicit</i>). Defaults to 3.</p>
<dt><i>unres_qlen</i> (since Linux 2.2)</p>
<dd>The maximum number of packets which may be queued for each unresolved address by other network layers. Defaults to 3.</dl>
<h2>Versions</h2>
<p>The <i>struct arpreq</i> changed in Linux 2.0 to include the <i>arp_dev</i> member and the ioctl numbers changed at the same time. Support for the old ioctls was dropped in Linux 2.2. </p>
<p> Support for proxy arp entries for networks (netmask not equal 0xffffffff) was dropped in Linux 2.2. It is replaced by automatic proxy arp setup by the kernel for all reachable hosts on other interfaces (when forwarding and proxy arp is enabled for the interface). </p>
<p> The <i>neigh/*</i> interfaces did not exist before Linux 2.2.</p>
<h2>Bugs</h2>
<p>Some timer settings are specified in jiffies, which is architecture- and kernel version-dependent; see <code><a href="/docs/linux/man/7-time/">time</a></code>(7). </p>
<p> There is no way to signal positive feedback from user space. This means connection-oriented protocols implemented in user space will generate excessive ARP traffic, because ndisc will regularly reprobe the MAC address. The same problem applies for some kernel protocols (e.g., NFS over UDP). </p>
<p> This man page mashes together functionality that is IPv4-specific with functionality that is shared between IPv4 and IPv6.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/8-arpd/">arpd</a></code>(8) </p>
<p> RFC 826 for a description of ARP. RFC 2461 for a description of IPv6 neighbor discovery and the base algorithms used. Linux 2.2+ IPv4 ARP uses the IPv6 algorithms when applicable.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
