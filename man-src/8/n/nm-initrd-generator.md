---
title: "nm-initrd-generator(8)"
name: "nm-initrd-generator"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nm-initrd-generator/"
description: "nm-initrd-generator – early boot NetworkManager configuration generator"
---

<p>nm-initrd-generator &#8211; early boot NetworkManager configuration generator</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nm-initrd-generator</code> [<i>OPTIONS</i>&#8230;] &#8212; [<i>CMDLINE</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>nm-initrd-generator</code></p>
<dd>scans the command line for options relevant to network configuration and creates configuration files for an early instance of NetworkManager run from the initial ramdisk during early boot.</p>
<h2>Options</h2>
<p><code>-c</code> | <code>&#8211;connections-dir</code> <i>path</i></p>
<dl>
<dd>Output connection directory.</dl>
<p> <code>-p</code> | <code>&#8211;persistent-connections-dir</code> <i>path</i></p>
<dl>
<dd>Persistent connection directory. If it exists, rd.neednet will not cause a default connection to be generated in absence of other options.</dl>
<p> <code>-i</code> | <code>&#8211;initrd-data-dir</code> <i>path</i></p>
<dl>
<dd>Output directory for initrd data (e.g. hostname).</dl>
<p> <code>-d</code> | <code>&#8211;sysfs-dir</code> <i>path</i></p>
<dl>
<dd>The sysfs mount point.</dl>
<p> <code>-r</code> | <code>&#8211;run-config-dir</code> <i>path</i></p>
<dl>
<dd>Output directory for config files.</dl>
<p> <code>-s</code> | <code>&#8211;stdout</code></p>
<dl>
<dd>Dump connections to standard output. Useful for debugging.</dl>
<p> <i>CMDLINE</i></p>
<dl>
<dd>The options that appear on the kernel command line. The following options are recognized:</p>
<dl>
<dd><code>ip</code></dl>
<dl>
<dd><code>rd.route</code></dl>
<dl>
<dd><code>bridge</code></dl>
<dl>
<dd><code>bond</code></dl>
<dl>
<dd><code>team</code></dl>
<dl>
<dd><code>vlan</code></dl>
<dl>
<dd><code>ib.pkey</code></dl>
<dl>
<dd><code>bootdev</code></dl>
<dl>
<dd><code>nameserver</code></dl>
<dl>
<dd><code>rd.peerdns</code></dl>
<dl>
<dd><code>rd.bootif</code></dl>
<dl>
<dd><code>rd.ethtool</code></dl>
<dl>
<dd><code>rd.net.timeout.dhcp</code></dl>
<dl>
<dd><code>rd.net.timeout.carrier</code></dl>
<dl>
<dd><code>rd.znet</code></dl>
<dl>
<dd><code>rd.znet_ifnames</code></dl>
<dl>
<dd><code>BOOTIF</code></dl>
<p> Please consult the <code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7) manual for the documentation of the precise format of the values supported.</dl>
<h2>Differences From The Network-Legacy Dracut Module</h2>
<p><code>nm-initrd-generator</code> generates a set of connections that are then configured by the NetworkManager instance running in the initrd. There are some differences in behavior compared to the network-legacy dracut module: </p>
<dl>
<dd>&bull; When an interface is configured with a static address and a gateway, the network-legacy module waits that the gateway responds to arping requests before proceeding, while NetworkManager doesn&#8217;t.</dl>
<dl>
<dd>&bull; network-legacy configures interfaces one by one in the order in which they are announced by udev. If multiple interfaces specify a hostname (from command line or from DHCP), the one from the last interface activated wins. With NetworkManager, hostnames from command line have higher precedence over ones from DHCP, and the last that appears in the command line wins.</dl>
<dl>
<dd>&bull; NetworkManager supports the <code>ib.pkey</code>=<i>PARENT</i>.<i>PKEY</i> argument to set up an Infiniband partition on IPoIB parent device <i>PARENT</i> using the specified partition key <i>PKEY</i>. The partition key must be in hexadecimal notation without leading &quot;0x&quot;, for example &quot;ib.pkey=ib0.8004&quot;.</dl>
<dl>
<dd>&bull; NetworkManager supports the <code>rd.ethtool</code>=<i>INTERFACE</i>:<i>AUTONEG</i>:<i>SPEED</i> kernel command line option to set up ethtool NIC configuration parameters <i>AUTONEG</i> and <i>SPEED</i>. The <i>INTERFACE</i> being configured must be specified, and the other parameters are optional and can be left blank. When <i>SPEED</i> is set, duplex mode is automatically set to &#8216;full&#8217;. <i>INTERFACE</i> accepts string values, <i>AUTONEG</i> accepts boolean values (true and false / on or off / 0 or 1), and <i>SPEED</i> accepts positive integer values.</dl>
<h2>Exit Status</h2>
<p><code>nm-initrd-generator</code> exits with status 0. It ignores unrecognized options and prints an error message if it encounters a malformed option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a></code>(7), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8). </p>
