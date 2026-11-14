---
title: "systemd-hostnamed-service(8)"
name: "systemd-hostnamed-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-hostnamed-service/"
description: "systemd-hostnamed.service, systemd-hostnamed – Daemon to control system hostname from programs"
---

<p>systemd-hostnamed.service, systemd-hostnamed &#8211; Daemon to control system hostname from programs</p>
<h2>Synopsis</h2>
<p>systemd-hostnamed.service </p>
<p> /lib/systemd/systemd-hostnamed</p>
<h2>Description</h2>
<p>systemd-hostnamed.service is a system service that may be used to change the system&#8217;s hostname and related machine metadata from user programs. It is automatically activated on request and terminates itself when unused. </p>
<p> It currently offers access to five variables: </p>
<dl>
<dd>&bull; The current hostname (Example: &quot;dhcp-192-168-47-11&quot;)</dl>
<dl>
<dd>&bull; The static (configured) hostname (Example: &quot;lennarts-computer&quot;)</dl>
<dl>
<dd>&bull; The pretty hostname (Example: &quot;Lennart&#8217;s Computer&quot;)</dl>
<dl>
<dd>&bull; A suitable icon name for the local host (Example: &quot;computer-laptop&quot;)</dl>
<dl>
<dd>&bull; A chassis type (Example: &quot;tablet&quot;)</dl>
<p> The static hostname is stored in /etc/hostname, see <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5) for more information. The pretty hostname, chassis type, and icon name are stored in /etc/machine-info, see <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5). </p>
<p> The tool <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1) is a command line client to this service. </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-hostname1/">org.freedesktop.hostname1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for a description of the D-Bus API.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5), <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1), <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) </p>
