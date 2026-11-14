---
title: "systemd-time-wait-sync-service(8)"
name: "systemd-time-wait-sync-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-time-wait-sync-service/"
description: "systemd-time-wait-sync.service, systemd-time-wait-sync – Wait until kernel time is synchronized"
---

<p>systemd-time-wait-sync.service, systemd-time-wait-sync &#8211; Wait until kernel time is synchronized</p>
<h2>Synopsis</h2>
<p>systemd-time-wait-sync.service </p>
<p> /lib/systemd/systemd-time-wait-sync</p>
<h2>Description</h2>
<p>systemd-time-wait-sync is a system service that delays the start of units that are ordered after time-sync.target (see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details) until the system time has been synchronized with an accurate remote reference time source by systemd-timesyncd.service. </p>
<p> systemd-timesyncd.service notifies systemd-time-wait-sync about successful synchronization. systemd-time-wait-sync also tries to detect when the kernel marks the system clock as synchronized, but this detection is not reliable and is intended only as a fallback for compatibility with alternative NTP services that can be used to synchronize time (e.g., ntpd, chronyd).</p>
<h2>Files</h2>
<p>/run/systemd/timesync/synchronized</p>
<dl>
<dd>The presence of this file indicates to this service that the system clock has been synchronized.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8), </p>
