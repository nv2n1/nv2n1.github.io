---
title: "systemd-networkd(8)"
name: "systemd-networkd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-networkd/"
description: "systemd-networkd.service, systemd-networkd – Network manager"
---

<p>systemd-networkd.service, systemd-networkd &#8211; Network manager</p>
<h2>Synopsis</h2>
<p>systemd-networkd.service </p>
<p> /lib/systemd/systemd-networkd</p>
<h2>Description</h2>
<p><code>systemd-networkd</code> is a system service that manages networks. It detects and configures network devices as they appear, as well as creating virtual network devices. </p>
<p> To configure low-level link settings independently of networks, see <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5). </p>
<p> <code>systemd-networkd</code> will create network devices based on the configuration in <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5) files, respecting the [Match] sections in those files. </p>
<p> <code>systemd-networkd</code> will manage network addresses and routes for any link for which it finds a .network file with an appropriate [Match] section, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). For those links, it will flush existing network addresses and routes when bringing up the device. Any links not matched by one of the .network files will be ignored. It is also possible to explicitly tell systemd-networkd to ignore a link by using <i>Unmanaged=yes</i> option, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). </p>
<p> When systemd-networkd exits, it generally leaves existing network devices and configuration intact. This makes it possible to transition from the initramfs and to restart the service without breaking connectivity. This also means that when configuration is updated and systemd-networkd is restarted, netdev interfaces for which configuration was removed will not be dropped, and may need to be cleaned up manually. </p>
<p> <code>systemd-networkd</code> may be introspected and controlled at runtime using <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1).</p>
<h2>Configuration Files</h2>
<p>The configuration files are read from the files located in the system network directory /lib/systemd/network, the volatile runtime network directory /run/systemd/network and the local administration network directory /etc/systemd/network. </p>
<p> Networks are configured in .network files, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), and virtual network devices are configured in .netdev files, see <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-wait-online-service/">systemd-networkd-wait-online.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-network-generator-service/">systemd-network-generator.service</a></code>(8) </p>
