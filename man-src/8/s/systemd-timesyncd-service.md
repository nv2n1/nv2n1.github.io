---
title: "systemd-timesyncd-service(8)"
name: "systemd-timesyncd-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-timesyncd-service/"
description: "systemd-timesyncd.service, systemd-timesyncd – Network Time Synchronization"
---

<p>systemd-timesyncd.service, systemd-timesyncd &#8211; Network Time Synchronization</p>
<h2>Synopsis</h2>
<p>systemd-timesyncd.service </p>
<p> /lib/systemd/systemd-timesyncd</p>
<h2>Description</h2>
<p>systemd-timesyncd is a system service that may be used to synchronize the local system clock with a remote Network Time Protocol (NTP) server. It also saves the local time to disk every time the clock has been synchronized and uses this to possibly advance the system realtime clock on subsequent reboots to ensure it (roughly) monotonically advances even if the system lacks a battery-buffered RTC chip. </p>
<p> The systemd-timesyncd service implements SNTP only. This minimalistic service will step the system clock for large offsets or slowly adjust it for smaller deltas. Complex use cases that require full NTP support (and where SNTP is not sufficient) are not covered by systemd-timesyncd. </p>
<p> The NTP servers contacted are determined from the global settings in <code><a href="/docs/linux/man/5-timesyncd-conf/">timesyncd.conf</a></code>(5), the per-link static settings in .network files, and the per-link dynamic settings received over DHCP. See <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) for further details. </p>
<p> <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1)&#8217;s <code>set-ntp</code> command may be used to enable and start, or disable and stop this service. </p>
<p> <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1)&#8217;s <code>timesync-status</code> or <code>show-timesync</code> command can be used to show the current status of this service. </p>
<p> systemd-timesyncd initialization delays the start of units that are ordered after time-set.target (see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details) until the local time has been updated from /var/lib/systemd/timesync/clock (see below) in order to make it roughly monotonic. It does not delay other units until synchronization with an accurate reference time sources has been reached. Use <code><a href="/docs/linux/man/8-systemd-time-wait-sync-service/">systemd-time-wait-sync.service</a></code>(8) to achieve that, which will delay start of units that are ordered after time-sync.target until synchronization to an accurate reference clock is reached.</p>
<h2>Files</h2>
<p>/var/lib/systemd/timesync/clock</p>
<dl>
<dd>The modification time (&quot;mtime&quot;) of this file indicates the timestamp of the last successful synchronization (or at least the systemd build date, in case synchronization was not possible). It is used to ensure that the system clock remains roughly monotonic across reboots, in case no local RTC is available.</dl>
<p> /run/systemd/timesync/synchronized</p>
<dl>
<dd>A file that is touched on each successful synchronization, to assist systemd-time-wait-sync and other applications to detecting synchronization with accurate reference clocks.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-timesyncd-conf/">timesyncd.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-time-wait-sync-service/">systemd-time-wait-sync.service</a></code>(8), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/1-timedatectl/">timedatectl</a></code>(1), <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) </p>
