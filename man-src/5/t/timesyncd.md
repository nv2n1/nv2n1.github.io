---
title: "timesyncd(5)"
name: "timesyncd"
section: "5"
letter: "t"
url: "/docs/linux/man/5-timesyncd/"
description: "timesyncd.conf – Network Time Synchronization configuration file"
---

<p>timesyncd.conf &#8211; Network Time Synchronization configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/timesyncd.conf</p>
<h2>Description</h2>
<p>When starting, systemd-timesyncd will read the configuration file timesyncd.conf. This configuration file controls NTP network time synchronization.</p>
<h2>Options</h2>
<p><i>NTP=</i></p>
<dl>
<dd>A space separated list of NTP servers host names or IP addresses. During runtime this list is combined with any per-interface NTP servers acquired from <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8). systemd-timesyncd will contact all configured system or per-interface servers in turn until one is found that responds. This setting defaults to the empty list.</dl>
<p> <i>FallbackNTP=</i></p>
<dl>
<dd>A space separated list of NTP server host names or IP addresses to be used as the fallback NTP servers. Any per-interface NTP servers obtained from <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) take precedence over this setting, as do any servers set via <i>NTP=</i> above. This setting is hence only used if no other NTP server information is known. If this option is not given, a compiled-in list of NTP servers is used instead.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) </p>
