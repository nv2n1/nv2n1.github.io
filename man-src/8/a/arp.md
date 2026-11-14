---
title: "arp(8)"
name: "arp"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arp/"
description: "arp – manipulate the system ARP cache"
---

<p>arp &#8211; manipulate the system ARP cache</p>
<h2>Synopsis</h2>
<p><code>arp</code> [<code>-vn</code>] [<code>-H</code> <i>type</i>] [<code>-i</code> <i>if</i>] [<code>-ae</code>] [<i>hostname</i>] <code>arp</code> [<code>-v</code>] [<code>-i</code> <i>if</i>] <code>-d</code> <i>hostname</i> [<code>pub</code>] <code>arp</code> [<code>-v</code>] [<code>-H</code> <i>type</i>] [<code>-i</code> <i>if</i>] <code>-s</code> <i>hostname hw_addr</i> [<code>temp</code>] <code>arp</code> [<code>-v</code>] [<code>-H</code> <i>type</i>] [<code>-i</code> <i>if</i>] <code>-s</code> <i>hostname hw_addr</i> [<code>netmask</code> <i>nm</i>] <code>pub</code> <code>arp</code> [<code>-v</code>] [<code>-H</code> <i>type</i>] [<code>-i</code> <i>if</i>] <code>-Ds</code> <i>hostname</i> <i>ifname</i> [<code>netmask</code> <i>nm</i>] <code>pub</code> <code>arp</code> [<code>-vnD</code>] [<code>-H</code> <i>type</i>] [<code>-i</code> <i>if</i>] <code>-f</code> [<i>filename</i>] </p>
<h2>Description</h2>
<p><code>Arp</code> manipulates or displays the kernel&#8217;s IPv4 network neighbour cache. It can add entries to the table, delete one or display the current content. </p>
<p> <code>ARP</code> stands for Address Resolution Protocol, which is used to find the media access control address of a network neighbour for a given IPv4 Address.</p>
<h2>Modes</h2>
<p><code>arp</code> with no mode specifier will print the current content of the table. It is possible to limit the number of entries printed, by specifying an hardware address type, interface name or host address. </p>
<p> <code>arp -d</code> <i>address</i> will delete a ARP table entry. Root or netadmin privilege is required to do this. The entry is found by IP address. If a hostname is given, it will be resolved before looking up the entry in the ARP table. </p>
<p> <code>arp -s</code> <i>address hw_addr</i> is used to set up a new table entry. The format of the <i>hw_addr</i> parameter is dependent on the hardware class, but for most classes one can assume that the usual presentation can be used. For the Ethernet class, this is 6 bytes in hexadecimal, separated by colons. When adding proxy arp entries (that is those with the <code>pub</code>lish flag set) a <code>netmask</code> may be specified to proxy arp for entire subnets. This is not good practice, but is supported by older kernels because it can be useful. If the <code>temp</code> flag is not supplied entries will be permanent stored into the ARP cache. To simplify setting up entries for one of your own network interfaces, you can use the <code>arp -Ds</code> <i>address ifname</i> form. In that case the hardware address is taken from the interface with the specified name.</p>
<h2>Options</h2>
<dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Tell the user what is going on by being verbose.</p>
<dt><code>-n, &#8211;numeric</code></p>
<dd>shows numerical addresses instead of trying to determine symbolic host, port or user names.</p>
<dt><code>-H</code><i> type</i>, <code>&#8211;hw-type</code><i> type</i>, <code>-t</code><i> type</i></p>
<dd>When setting or reading the ARP cache, this optional parameter tells <code>arp</code> which class of entries it should check for. The default value of this parameter is <code>ether</code> (i.e. hardware code 0x01 for IEEE 802.3 10Mbps Ethernet). Other values might include network technologies such as ARCnet (<code>arcnet</code>) , PROnet (<code>pronet</code>) , AX.25 (<code>ax25</code>) and NET/ROM (<code>netrom</code>).</p>
<dt><code>-a</code></p>
<dd>Use alternate BSD style output format (with no fixed columns).</p>
<dt><code>-e</code></p>
<dd>Use default Linux style output format (with fixed columns).</p>
<dt><code>-D, &#8211;use-device</code></p>
<dd>Instead of a hw_addr, the given argument is the name of an interface. <code>arp</code> will use the MAC address of that interface for the table entry. This is usually the best option to set up a proxy ARP entry to yourself.</p>
<dt><code>-i</code><i> If</i>, <code>&#8211;device</code><i> If</i></p>
<dd>Select an interface. When dumping the ARP cache only entries matching the specified interface will be printed. When setting a permanent or <code>temp</code> ARP entry this interface will be associated with the entry; if this option is not used, the kernel will guess based on the routing table. For <code>pub</code> entries the specified interface is the interface on which ARP requests will be answered.<br />
 <code>NOTE:</code> This has to be different from the interface to which the IP datagrams will be routed. <code>NOTE:</code> As of kernel 2.2.0 it is no longer possible to set an ARP entry for an entire subnet. Linux instead does automagic proxy arp when a route exists and it is forwarding. See <code><a href="/docs/linux/man/7-arp/">arp</a></code>(7) for details. Also the <code>dontpub</code> option which is available for delete and set operations cannot be used with 2.4 and newer kernels.</p>
<dt><code>-f</code><i> filename</i>, <code>&#8211;file</code><i> filename</i></p>
<dd>Similar to the <code>-s</code> option, only this time the address info is taken from file <i>filename</i>. This can be used if ARP entries for a lot of hosts have to be set up. The name of the data file is very often <i>/etc/ethers</i>, but this is not official. If no filename is specified <i>/etc/ethers</i> is used as default. </p>
<p> The format of the file is simple; it only contains ASCII text lines with a hostname, and a hardware address separated by whitespace. Additionally the <code>pub</code>,<code> temp</code> and<code> netmask</code> flags can be used.</dl>
<p> In all places where a <code>hostname</code> is expected, one can also enter an <code>IP address</code> in dotted-decimal notation. </p>
<p> As a special case for compatibility the order of the hostname and the hardware address can be exchanged. </p>
<p> Each complete entry in the ARP cache will be marked with the <code>C</code> flag. Permanent entries are marked with <code>M</code> and published entries have the <code>P</code> flag.</p>
<h2>Examples</h2>
<p><code>/usr/sbin/arp -i eth0 -Ds 10.0.0.2 eth1 pub</code> </p>
<p> This will answer ARP requests for 10.0.0.2 on eth0 with the MAC address for eth1. </p>
<p> <code>/usr/sbin/arp -i eth1 -d 10.0.0.1</code> </p>
<p> Delete the ARP table entry for 10.0.0.1 on interface eth1. This will match published proxy ARP entries and permanent entries.</p>
<h2>Files</h2>
<p><i>/proc/net/arp</i><br />
 <i>/etc/networks</i><br />
 <i>/etc/hosts</i><br />
 <i>/etc/ethers</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-rarp/">rarp</a>(8), <a href="/docs/linux/man/8-route/">route</a>(8), <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8), <a href="/docs/linux/man/8-netstat/">netstat</a>(8)</p>
<h2>Authors</h2>
<p>Fred N. van Kempen &lt;waltje [at] uwalt.nl.mugnet.org&gt;, Bernd Eckenfels &lt;net-tools [at] lina.inka.de&gt;.</p>
