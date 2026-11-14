---
title: "systemd-network-generator-service(8)"
name: "systemd-network-generator-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-network-generator-service/"
description: "systemd-network-generator.service, systemd-network-generator – Generate network configuration from the kernel command line"
---

<p>systemd-network-generator.service, systemd-network-generator &#8211; Generate network configuration from the kernel command line</p>
<h2>Synopsis</h2>
<p>systemd-network-generator.service </p>
<p> /lib/systemd/systemd-network-generator</p>
<h2>Description</h2>
<p>systemd-network-generator.service is a system service that translates <i>ip=</i> and the related settings on the kernel command line (see below) into <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), and <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5) configuration files understood by <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) and <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8). </p>
<p> Files are generated in /run/systemd/network/.</p>
<h2>Kernel Command Line Options</h2>
<p>This tool understands the following options: </p>
<p> <i>ip=</i>, <i>rd.route=</i>, <i>rd.peerdns=</i></p>
<dl>
<dd>&#8212; translated into <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) files.</dl>
<p> <i>ifname=</i></p>
<dl>
<dd>&#8212; translated into <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5) files.</dl>
<p> <i>vlan=</i>, <i>bond=</i>, <i>bridge=</i>, <i>bootdev=</i></p>
<dl>
<dd>&#8212; translated into <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5) files.</dl>
<p> See <code><a href="/docs/linux/man/7-dracut-kernel/">dracut.kernel</a></code>(7) for option syntax and details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
