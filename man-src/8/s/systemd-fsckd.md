---
title: "systemd-fsckd(8)"
name: "systemd-fsckd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-fsckd/"
description: "systemd-fsckd.service, systemd-fsckd.socket, systemd-fsckd – File system check progress reporting"
---

<p>systemd-fsckd.service, systemd-fsckd.socket, systemd-fsckd &#8211; File system check progress reporting</p>
<h2>Synopsis</h2>
<p>systemd-fsckd.service </p>
<p> systemd-fsckd.socket </p>
<p> /lib/systemd/systemd-fsckd</p>
<h2>Description</h2>
<p>systemd-fsckd.service is a service responsible for receiving file system check progress, and communicating some consolidated data to console and plymouth (if running). It also handles possible check cancellations. </p>
<p> <code>systemd-fsckd</code> receives messages about file system check progress from <code>fsck</code> through an UNIX domain socket. It can display the progress of the least advanced fsck as well as the total number of devices being checked in parallel to the console. It will also send progress messages to plymouth. Both the raw data and translated messages are sent, so compiled plymouth themes can use the raw data to display custom messages, and scripted themes, not supporting i18n, can display the translated versions. </p>
<p> <code>systemd-fsckd</code> will instruct plymouth to grab Control+C keypresses. When the key is pressed, running checks will be terminated. It will also cancel any newly connected fsck instances for the lifetime of systemd-fsckd.</p>
<h2>Protocol For Communication With Plymouth</h2>
<p>systemd-fsckd passes the following messages to the theme: </p>
<p> Progress update, sent as a plymouth update message: &quot;fsckd:&lt;num_devices&gt;:&lt;progress&gt;:&lt;string&gt;&quot; </p>
<p> &quot;&lt;num_devices&gt;&quot;</p>
<dl>
<dd>the current number of devices being checked (int)</dl>
<p> &quot;&lt;progress&gt;&quot;</p>
<dl>
<dd>the current minimum percentage of all devices being checking (float, from 0 to 100)</dl>
<p> &quot;&lt;string&gt;&quot;</p>
<dl>
<dd>a translated message ready to be displayed by the plymouth theme displaying the data above. It can be overridden by themes supporting i18n.</dl>
<p> Cancel message, sent as a traditional plymouth message: &quot;fsckd-cancel-msg:&lt;string&gt;&quot; </p>
<p> &quot;&lt;strings&gt;&quot;</p>
<dl>
<dd>a translated string ready to be displayed by the plymouth theme indicating that Control+C can be used to cancel current checks. It can be overridden (matching only &quot;fsckd-cancel-msg&quot; prefix) by themes supporting i18n.</dl>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise. Note that the daemon stays idle for a while to accept new fsck connections before exiting.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-fsck/">systemd-fsck</a></code>(8), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-systemd-quotacheck-service/">systemd-quotacheck.service</a></code>(8), <code><a href="/docs/linux/man/8-fsck-btrfs/">fsck.btrfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-cramfs/">fsck.cramfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ext4/">fsck.ext4</a></code>(8), <code><a href="/docs/linux/man/8-fsck-fat/">fsck.fat</a></code>(8), <code><a href="/docs/linux/man/8-fsck-hfsplus/">fsck.hfsplus</a></code>(8), <code><a href="/docs/linux/man/8-fsck-minix/">fsck.minix</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ntfs/">fsck.ntfs</a></code>(8), <code><a href="/docs/linux/man/8-fsck-xfs/">fsck.xfs</a></code>(8) </p>
