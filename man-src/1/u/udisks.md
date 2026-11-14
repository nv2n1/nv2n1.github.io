---
title: "udisks(1)"
name: "udisks"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udisks/"
description: "udisks – udisks command line tool"
---

<h2 class="name">NAME</h2>
<p> udisks &#8211; udisks command line tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>udisks</code> [<code>OPTIONS</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <i>udisks</i></p>
<dd>is a simple command line client for the <code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7) system bus service.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;dump</code></p>
<dl>
<dt>
<dd> Dump all information about all devices. Please include this when filing bugs.</dl>
<p> <code>&#8211;enumerate</code></p>
<dl>
<dt>
<dd> Lists all object paths of devices know to the daemon.</dl>
<p> <code>&#8211;enumerate-device-files</code></p>
<dl>
<dt>
<dd> Lists all device files of devices know to the daemon.</dl>
<p> <code>&#8211;monitor</code></p>
<dl>
<dt>
<dd> Connect to the daemon and print a line every time an event happens.</dl>
<p> <code>&#8211;monitor-detail</code></p>
<dl>
<dt>
<dd> Like <code>&#8211;monitor</code> but prints the full details of the device whenever an event happens.</dl>
<p> <code>&#8211;show-info</code> <i>device_file</i></p>
<dl>
<dt>
<dd> Shows information about <i>device_file</i>.</dl>
<p> <code>&#8211;inhibit-polling</code> <i>device_file</i> [<code>&#8212; program arg &#8230;</code>]</p>
<dl>
<dt>
<dd> Inhibits polling on <i>device_file</i>. If no program is given, polling is inhibited until Ctrl+C is pressed. Otherwise the program is spawned and the polling is only inhibited until the program terminates.</dl>
<p> <code>&#8211;poll-for-media</code> <i>device_file</i></p>
<dl>
<dt>
<dd> Polls <i>device_file</i> to perform media detection.</dl>
<p> <code>&#8211;inhibit-all-polling</code> [<code>&#8212; program arg &#8230;</code>]</p>
<dl>
<dt>
<dd> Inhibits polling on all devices. If no program is given, polling is inhibited until Ctrl+C is pressed. Otherwise the program is spawned and the polling is only inhibited until the program terminates.</dl>
<p> <code>&#8211;mount</code> <i>device_file</i> [<code>&#8211;mount-fstype</code>&nbsp;<wbr><i>fstype</i>] [<code>&#8211;mount-options</code>&nbsp;<wbr><i>options</i>]</p>
<dl>
<dt>
<dd> Mounts the device represented by <i>device_file</i> using the file system <i>fstype</i> and a comma-separated list of <i>options</i>.</dl>
<p> <code>&#8211;unmount</code> <i>device_file</i> [<code>&#8211;unmount-options</code>&nbsp;<wbr><i>options</i>]</p>
<dl>
<dt>
<dd> Unmounts the device represented by <i>device_file</i> using a comma-separated list of <i>options</i>.</dl>
<p> <code>&#8211;detach</code> <i>device_file</i> [<code>&#8211;detach-options</code>&nbsp;<wbr><i>options</i>]</p>
<dl>
<dt>
<dd> Detaches (e.g. powering down the physical port the device is connected to) the device represented by <i>device_file</i> using a comma-separated list of <i>options</i>.</dl>
<p> <code>&#8211;eject</code> <i>device_file</i> [<code>&#8211;eject-options</code>&nbsp;<wbr><i>options</i>]</p>
<dl>
<dt>
<dd> Ejects media from the device represented by <i>device_file</i> using a comma-separated list of <i>options</i>.</dl>
<p> <code>&#8211;ata-smart-refresh</code> <i>device_file</i> [<code>&#8211;ata-smart-wakeup</code>]</p>
<dl>
<dt>
<dd> Refreshes ATA SMART data for <i>device_file</i>. If the disk is sleeping it will not be woken up unless <code>&#8211;ata-smart-wakeup</code> is passed. will be used.</dl>
<p> <code>&#8211;ata-smart-refresh</code> <i>device_file</i> <code>&#8211;ata-smart-simulate</code> <i>blob</i></p>
<dl>
<dt>
<dd> Read ATA SMART data from <i>blob</i> for <i>device_file</i>. This can only be done by the super user and is typically used for testing that clients relying on the ATA SMART data provided by udisks behave correctly. The libatasmart git repository at m[blue]<code><a rel="nofollow" href="http://git.0pointer.de/?p=libatasmart.git;a=summary">http://git.0pointer.de/?p=libatasmart.git;a=summary</a></code>m[] contains a collection of blobs from failing disks.</dl>
<p> <code>&#8211;inhibit</code> [<code>&#8212; program arg &#8230;</code>]</p>
<dl>
<dt>
<dd> Inhibits clients from invoking methods on the daemon that require authorization (all methods will return the org.freedesktop.UDisks.Error.Inhibited error) if the caller is not the super user. This is typically used by OS installers and other programs that expects full control of the system, specifically to avoid automounting devices. Only the super user can do this. </p>
<p> If no program is given, the daemon is inhibited until Ctrl+C is pressed. Otherwise the program is spawned and the daemon is only inhibited until the program terminates.</dl>
<p> <code>&#8211;set-spindown</code> <i>device_file</i> <code>&#8211;spindown-timeout</code> <i>seconds</i> [<code>&#8212; program arg &#8230;</code>]</p>
<dl>
<dt>
<dd> Configures disk spindown timeout on <i>device_file</i> to <i>seconds</i>. See the section called &#8220;SPINNING DOWN DISKS&#8221; for important information before using this option. </p>
<p> If no program is given, the spindown time will be used until Ctrl+C is pressed. Otherwise the program is spawned and the the spindown timeout will only be used until the program terminates.</dl>
<p> <code>&#8211;set-spindown-all</code> <code>&#8211;spindown-timeout</code> <i>seconds</i> [<code>&#8212; program arg &#8230;</code>]</p>
<dl>
<dt>
<dd> Configures disk spindown timeout on all disks that can be spun down to <i>seconds</i>. See the section called &#8220;SPINNING DOWN DISKS&#8221; for important information before using this option. </p>
<p> If no program is given, the spindown time will be used until Ctrl+C is pressed. Otherwise the program is spawned and the the spindown timeout will only be used until the program terminates.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options.</dl>
<h2>SPINNING DOWN DISKS</h2>
<p> Caution should be exercised when configuring disk spin down timeouts. </p>
<p> Note that every time a disk is spun down, the &#8220;start-stop-count&#8221; ATA SMART attribute will increase by 1 and most disks are only good for a limited number (typically 50,000 but it varies by manufacturer and model). In addition, the drive may take as long as 30 seconds to respond to subsequent disk access &#8211; most drives are typically faster, see the &#8220;spin-up-time&#8221; ATA SMART attribute. </p>
<p> On the other hand, cautious use (e.g. using conservative timeouts) of the ability to spin down disks, can be a good way to trade power consumption (typically 8 vs 1 Watts for 3.5&quot; drives) and heat emission for a slightly higher latency.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="http://bugs.freedesktop.org/enter_bug.cgi?product=udisks">http://bugs.freedesktop.org/enter_bug.cgi?product=udisks</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-udisks-daemon/">udisks-daemon</a></code>(8), <code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7), </p>
<h2>Index</h2>
