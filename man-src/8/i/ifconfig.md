---
title: "ifconfig(8)"
name: "ifconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifconfig/"
description: "ifconfig – configure a network interface"
---

<p>ifconfig &#8211; configure a network interface</p>
<h2>Synopsis</h2>
<p><code>ifconfig [-v] [-a] [-s] [interface]</code><br />
 <code>ifconfig [-v] interface [aftype] options | address &#8230;</code></p>
<h2>Description</h2>
<p><code>Ifconfig</code> is used to configure the kernel-resident network interfaces. It is used at boot time to set up interfaces as necessary. After that, it is usually only needed when debugging or when system tuning is needed. If no arguments are given, <code>ifconfig</code> displays the status of the currently active interfaces. If a single <code>interface</code> argument is given, it displays the status of the given interface only; if a single <code>-a</code> argument is given, it displays the status of all interfaces, even those that are down. Otherwise, it configures an interface. </p>
<h2>Address Families</h2>
<p>If the first argument after the interface name is recognized as the name of a supported address family, that address family is used for decoding and displaying all protocol addresses. Currently supported address families include <code>inet</code> (TCP/IP, default), <code>inet6</code> (IPv6), <code>ax25</code> (AMPR Packet Radio), <code>ddp</code> (Appletalk Phase 2), <code>ipx</code> (Novell IPX) and <code>netrom</code> (AMPR Packet radio). All numbers supplied as parts in IPv4 dotted decimal notation may be decimal, octal, or hexadecimal, as specified in the ISO C standard (that is, a leading 0x or 0X implies hexadecimal; otherwise, a leading &#8216;0&#8217; implies octal; otherwise, the number is interpreted as decimal). Use of hexadecimal and octal numbers is not RFC-compliant and therefore its use is discouraged.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>display all interfaces which are currently available, even if down</p>
<dt><code>-s</code></p>
<dd>display a short list (like netstat -i)</p>
<dt><code>-v</code></p>
<dd>be more verbose for some error conditions</p>
<dt><code>interface</code></p>
<dd>The name of the interface. This is usually a driver name followed by a unit number, for example <code>eth0</code> for the first Ethernet interface. If your kernel supports alias interfaces, you can specify them with syntax like <code>eth0:0</code> for the first alias of eth0. You can use them to assign more addresses. To delete an alias interface use <code>ifconfig eth0:0 down</code>. Note: for every scope (i.e. same net with address/netmask combination) all aliases are deleted, if you delete the first (primary).</p>
<dt><code>up</code></p>
<dd>This flag causes the interface to be activated. It is implicitly specified if an address is assigned to the interface; you can suppress this behavior when using an alias interface by appending an <code>&#8211;</code> to the alias (e.g. <code>eth0:0-</code>). It is also suppressed when using the IPv4 0.0.0.0 address as the kernel will use this to implicitly delete alias interfaces.</p>
<dt><code>down</code></p>
<dd>This flag causes the driver for this interface to be shut down.</p>
<dt><code>[-]arp</code></p>
<dd>Enable or disable the use of the ARP protocol on this interface.</p>
<dt><code>[-]promisc</code></p>
<dd>Enable or disable the <code>promiscuous</code> mode of the interface. If selected, all packets on the network will be received by the interface.</p>
<dt><code>[-]allmulti</code></p>
<dd>Enable or disable <code>all-multicast</code> mode. If selected, all multicast packets on the network will be received by the interface.</p>
<dt><code>mtu N</code></p>
<dd>This parameter sets the Maximum Transfer Unit (MTU) of an interface.</p>
<dt><code>dstaddr addr</code></p>
<dd>Set the remote IP address for a point-to-point link (such as PPP). This keyword is now obsolete; use the <code>pointopoint</code> keyword instead.</p>
<dt><code>netmask addr</code></p>
<dd>Set the IP network mask for this interface. This value defaults to the usual class A, B or C network mask (as derived from the interface IP address), but it can be set to any value.</p>
<dt><code>add addr/prefixlen</code></p>
<dd>Add an IPv6 address to an interface.</p>
<dt><code>del addr/prefixlen</code></p>
<dd>Remove an IPv6 address from an interface.</p>
<dt><code>tunnel ::aa.bb.cc.dd</code></p>
<dd>Create a new SIT (IPv6-in-IPv4) device, tunnelling to the given destination.</p>
<dt><code>irq addr</code></p>
<dd>Set the interrupt line used by this device. Not all devices can dynamically change their IRQ setting.</p>
<dt><code>io_addr addr</code></p>
<dd>Set the start address in I/O space for this device.</p>
<dt><code>mem_start addr</code></p>
<dd>Set the start address for shared memory used by this device. Only a few devices need this.</p>
<dt><code>media type</code></p>
<dd>Set the physical port or medium type to be used by the device. Not all devices can change this setting, and those that can vary in what values they support. Typical values for <code>type</code> are <code>10base2</code> (thin Ethernet), <code>10baseT</code> (twisted-pair 10Mbps Ethernet), <code>AUI </code> (external transceiver) and so on. The special medium type of <code>auto</code> can be used to tell the driver to auto-sense the media. Again, not all drivers can do this.</p>
<dt><code>[-]broadcast [addr]</code></p>
<dd>If the address argument is given, set the protocol broadcast address for this interface. Otherwise, set (or clear) the <code>IFF_BROADCAST</code> flag for the interface.</p>
<dt><code>[-]pointopoint [addr]</code></p>
<dd>This keyword enables the <code>point-to-point</code> mode of an interface, meaning that it is a direct link between two machines with nobody else listening on it.<br />
 If the address argument is also given, set the protocol address of the other side of the link, just like the obsolete <code>dstaddr</code> keyword does. Otherwise, set or clear the <code>IFF_POINTOPOINT</code> flag for the interface.</p>
<dt><code>hw class address</code></p>
<dd>Set the hardware address of this interface, if the device driver supports this operation. The keyword must be followed by the name of the hardware class and the printable ASCII equivalent of the hardware address. Hardware classes currently supported include <code>ether</code> (Ethernet), <code>ax25</code> (AMPR AX.25), <code>ARCnet</code> and <code>netrom</code> (AMPR NET/ROM).</p>
<dt><code>multicast</code></p>
<dd>Set the multicast flag on the interface. This should not normally be needed as the drivers set the flag correctly themselves.</p>
<dt><code>address</code></p>
<dd>The IP address to be assigned to this interface.</p>
<dt><code>txqueuelen length</code></p>
<dd>Set the length of the transmit queue of the device. It is useful to set this to small values for slower devices with a high latency (modem links, ISDN) to prevent fast bulk transfers from disturbing interactive traffic like telnet too much.</dl>
<h2>Notes</h2>
<p>Since kernel release 2.2 there are no explicit interface statistics for alias interfaces anymore. The statistics printed for the original address are shared with all alias addresses on the same device. If you want per-address statistics you should add explicit accounting rules for the address using the <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) command. </p>
<p> Interrupt problems with Ethernet device drivers fail with EAGAIN <i>(SIOCSIIFLAGS: Resource temporarily unavailable)</i> it is most likely a interrupt conflict. See <i><a rel="nofollow" href="http://www.scyld.com/expert/irq-conflict.html">http://www.scyld.com/expert/irq-conflict.html</a></i> for more information.</p>
<h2>Files</h2>
<p><i>/proc/net/dev</i><br />
 <i>/proc/net/if_inet6</i></p>
<h2>Bugs</h2>
<p>Ifconfig uses the ioctl access method to get the full address information, which limits hardware addresses to 8 bytes. Because Infiniband hardware address has 20 bytes, only the first 8 bytes are displayed correctly. Please use <code>ip link</code> command from <code>iproute2</code> package to display link layer informations including the hardware address. </p>
<p> While appletalk DDP and IPX addresses will be displayed they cannot be altered by this command.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-route/">route</a>(8), <a href="/docs/linux/man/8-netstat/">netstat</a>(8), <a href="/docs/linux/man/8-arp/">arp</a>(8), <a href="/docs/linux/man/8-rarp/">rarp</a>(8), <a href="/docs/linux/man/8-iptables/">iptables</a>(8), <a href="/docs/linux/man/8-ifup/">ifup</a>(8), <a href="/docs/linux/man/5-interfaces/">interfaces</a>(5).<br />
 <a rel="nofollow" href="http://physics.nist.gov/cuu/Units/binary.html">http://physics.nist.gov/cuu/Units/binary.html</a> &#8211; Prefixes for binary multiples</p>
<h2>Authors</h2>
<p>Fred N. van Kempen, &lt;waltje [at] uwalt.nl.mugnet.org&gt;<br />
 Alan Cox, &lt;Alan.Cox [at] linux.org&gt;<br />
 Phil Blundell, &lt;Philip.Blundell [at] pobox.com&gt;<br />
 Andi Kleen<br />
 Bernd Eckenfels, &lt;net-tools [at] lina.inka.de&gt;</p>
