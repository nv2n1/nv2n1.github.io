---
title: "iftab(5)"
name: "iftab"
section: "5"
letter: "i"
url: "/docs/linux/man/5-iftab/"
description: "iftab – static information about the network interfaces"
---

<p>iftab &#8211; static information about the network interfaces</p>
<h2>Description</h2>
<p>The file <code>/etc/iftab</code> contains descriptive information about the various network interfaces. <code>iftab</code> is only used by the program <i><a href="/docs/linux/man/8-ifrename/">ifrename</a></i>(8) to assign a consistent network interface name to each network interface. </p>
<p> <code>/etc/iftab</code> defines a set of <i>mappings</i>. Each mapping contains an interface name and a set of selectors. The selectors allow <code>ifrename</code> to identify each network interface on the system. If a network interface matches all descriptors of a mapping, <code>ifrename</code> attempt to change the name of the interface to the interface name given by the mapping.</p>
<h2>Mappings</h2>
<p>Each mapping is described on a separate line, it starts with an <i>interface name</i>, and contains a set of <i>descriptors</i>, separated by space or tabs. </p>
<p> The relationship between descriptors of a mapping is a <i>logical and</i>. A mapping matches a network interface only is all the descriptors match. If a network interface doesn&#8217;t support a specific descriptor, it won&#8217;t match any mappings using this descriptor. </p>
<p> If you want to use alternate descriptors for an interface name (logical or), specify two different mappings with the same interface name (one on each line). <code>Ifrename</code> always use the first matching mapping starting from the <i>end</i> of <code>iftab</code>, therefore more restrictive mapping should be specified last.</p>
<h2>Interface Name</h2>
<p>The first part of each mapping is an interface name. If a network interface matches all descriptors of a mapping, <code>ifrename</code> attempt to change the name of the interface to the interface name given by the mapping. </p>
<p> The interface name of a mapping is either a plain interface name (such as <i>eth2</i> or <i>wlan1</i>) or a interface name pattern containing a single wildcard (such as <i>eth*</i> or <i>wlan*</i>). In case of wildcard, the kernel replace the &#8216;*&#8217; with the lowest available integer making this interface name unique. Note that wildcard is only supported for kernel 2.6.1 and 2.4.30 and later. </p>
<p> It is discouraged to try to map interfaces to default interfaces names such as <i>eth0</i>, <i>wlan0</i> or <i>ppp0</i>. The kernel use those as the default name for any new interface, therefore most likely an interface will already use this name and prevent ifrename to use it. Even if you use takeover, the interface may already be up in some cases. Not using those name will allow you to immediately spot unconfigured or new interfaces.<br />
 Good names are either totally unique and meaningfull, such as <i>mydsl</i> or <i>privatehub</i>, or use larger integer, such as <i>eth5</i> or <i>wlan5</i>. The second type is usually easier to integrate in various network utilities.</p>
<h2>Descriptors</h2>
<p>Each descriptor is composed of a descriptor name and descriptor value. Descriptors specify a static attribute of a network interface, the goal is to uniquely identify each piece of hardware. </p>
<p> Most users will only use the <code>mac</code> selector despite its potential problems, other selectors are for more specialised setup. Most selectors accept a &#8216;*&#8217; in the selector value for wilcard matching, and most selectors are case insensitive.</p>
<dl>
<dt><code>mac</code><i> mac address</i></p>
<dd>Matches the MAC Address of the interface with the specified MAC address. The MAC address of the interface can be shown using <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8) or <i><a href="/docs/linux/man/8-ip/">ip</a></i>(8).<br />
 This is the most common selector, as most interfaces have a unique MAC address allowing to identify network interfaces without ambiguity. However, some interfaces don&#8217;t have a valid MAC address until they are brought up, in such case using this selector is tricky or impossible.</p>
<dt><code>arp</code><i> arp type</i></p>
<dd>Matches the ARP Type (also called Link Type) of the interface with the specified ARP type as a number. The ARP Type of the interface can be shown using <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8) or <i><a href="/docs/linux/man/8-ip/">ip</a></i>(8), the <code>link/ether</code> type correspond to <code>1</code> and the <code>link/ieee802.11</code> type correspond to <code>801</code>.<br />
 This selector is useful when a driver create multiple network interfaces for a single network card.</p>
<dt><code>driver</code><i> driver name</i></p>
<dd>Matches the Driver Name of the interface with the specified driver name. The Driver Name of the interface can be shown using <i>ethtool <a href="/docs/linux/man/8--i/">-i</a></i>(8).</p>
<dt><code>businfo</code><i> bus information</i></p>
<dd>Matches the Bus Information of the interface with the specified bus information. The Bus Information of the interface can be shown using <i>ethtool <a href="/docs/linux/man/8--i/">-i</a></i>(8).</p>
<dt><code>firmware</code><i> firmware revision</i></p>
<dd>Matches the Firmware Revision of the interface with the firmware revision information. The Firmware Revision of the interface can be shown using <i>ethtool <a href="/docs/linux/man/8--i/">-i</a></i>(8).</p>
<dt><code>baseaddress</code><i> base address</i></p>
<dd>Matches the Base Address of the interface with the specified base address. The Base Address of the interface can be shown using <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8).<br />
 Because most cards use dynamic allocation of the Base Address, this selector is only useful for ISA and EISA cards.</p>
<dt><code>irq</code><i> irq line</i></p>
<dd>Matches the IRQ Line (interrupt) of the interface with the specified IRQ line. The IRQ Line of the interface can be shown using <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8).<br />
 Because there are IRQ Lines may be shared, this selector is usually not sufficient to uniquely identify an interface.</p>
<dt><code>iwproto</code><i> wireless protocol</i></p>
<dd>Matches the Wireless Protocol of the interface with the specified wireless protocol. The Wireless Protocol of the interface can be shown using <i><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></i>(8) or <i><a href="/docs/linux/man/8-iwgetid/">iwgetid</a></i>(8).<br />
 This selector is only supported on wireless interfaces and is not sufficient to uniquely identify an interface.</p>
<dt><code>pcmciaslot</code><i> pcmcia slot</i></p>
<dd>Matches the Pcmcia Socket number of the interface with the specified slot number. Pcmcia Socket number of the interface can be shown using <i>cardctl <a href="/docs/linux/man/8-ident/">ident</a></i>(8).<br />
 This selector is usually only supported on 16 bits cards, for 32 bits cards it is advised to use the selector <code>businfo</code>.</p>
<dt><code>prevname</code><i> previous interface name</i></p>
<dd>Matches the name of the interface prior to renaming with the specified oldname.<br />
 This selector should be avoided as the previous interface name may vary depending on various condition. A system/kernel/driver update may change the original name. Then, ifrename or another tool may rename it prior to the execution of this selector.</p>
<dt><code>SYSFS{</code><i>filename</i><code>}</code><i> value</i></p>
<dd>Matches the content the sysfs attribute given by filename to the specified value. For symlinks and parents directories, match the actual directory name of the sysfs attribute given by filename to the specified value.<br />
 A list of the most useful sysfs attributes is given in the next section.</dl>
<h2>Sysfs Descriptors</h2>
<p>Sysfs attributes for a specific interface are located on most systems in the directory named after that interface at <i>/sys/class/net/</i>. Most sysfs attribute are files, and their values can be read using <i><a href="/docs/linux/man/1-cat/">cat</a></i>(1) or <i><a href="/docs/linux/man/1-more/">more</a></i>(1). It is also possible to match attributes in subdirectories. </p>
<p> Some sysfs attributes are symlinks, pointing to another directory in sysfs. If the attribute filename is a symlink the sysfs attribute resolves to the name of the directory pointed by the symlink using <i><a href="/docs/linux/man/1-readlink/">readlink</a></i>(1). The location is a directory in the sysfs tree is also important. If the attribute filename ends with <i>/..</i>, the sysfs attribute resolves to the real name of the parent directory using <i><a href="/docs/linux/man/1-pwd/">pwd</a></i>(1). </p>
<p> The sysfs filesystem is only supported with 2.6.X kernel and need to be mounted (usually in <i>/sys</i>). sysfs selectors are not as efficient as other selectors, therefore they should be avoided for maximum performance. </p>
<p> These are common sysfs attributes and their corresponding ifrename descriptors.</p>
<dl>
<dt><code>SYSFS{address}</code><i> value</i></p>
<dd>Same as the <code>mac</code> descriptor.</p>
<dt><code>SYSFS{type}</code><i> value</i></p>
<dd>Same as the <code>arp</code> descriptor.</p>
<dt><code>SYSFS{device}</code><i> value</i></p>
<dd>Valid only up to kernel 2.6.20. Same as the <code>businfo</code> descriptor.</p>
<dt><code>SYSFS{..}</code><i> value</i></p>
<dd>Valid only from kernel 2.6.21. Same as the <code>businfo</code> descriptor.</p>
<dt><code>SYSFS{device/driver}</code><i> value</i></p>
<dd>Valid only up to kernel 2.6.20. Same as the <code>driver</code> descriptor.</p>
<dt><code>SYSFS{../driver}</code><i> value</i></p>
<dd>Valid only from kernel 2.6.21. Same as the <code>driver</code> descriptor.</p>
<dt><code>SYSFS{device/irq}</code><i> value</i></p>
<dd>Valid only up to kernel 2.6.20. Same as the <code>irq</code> descriptor.</p>
<dt><code>SYSFS{../irq}</code><i> value</i></p>
<dd>Valid only from kernel 2.6.21. Same as the <code>irq</code> descriptor.</dl>
<h2>Examples</h2>
<p># This is a comment<br />
 eth2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mac 08:00:09:DE:82:0E</p>
<p> eth3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>driver wavelan interrupt 15 baseaddress 0x390</p>
<p> eth4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>driver pcnet32 businfo 0000:02:05.0</p>
<p> air*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mac 00:07:0E:* arp 1</p>
<p> myvpn<tt>&nbsp;<wbr>&nbsp;<wbr></tt>SYSFS{address} 00:10:83:* SYSFS{type} 1</p>
<p> bcm*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SYSFS{device} 0000:03:00.0 SYSFS{device/driver} bcm43xx</p>
<p> bcm*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SYSFS{..} 0000:03:00.0 SYSFS{../driver} bcm43xx</p>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/etc/iftab</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifrename/">ifrename</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ethtool/">ethtool</a></code>(8), <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8). </p>
