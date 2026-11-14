---
title: "hal-disable-polling(1)"
name: "hal-disable-polling"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hal-disable-polling/"
description: "hal-disable-polling – disable polling on drives with removable media"
---

<h2>NAME</h2>
<p> hal-disable-polling &#8211; disable polling on drives with removable media</p>
<h2>SYNOPSIS</h2>
<p> <code>hal-disable-polling</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <i>hal-disable-polling</i> can be used to to disable and enable media detection on drives with removable storage. For more information about both the big picture and specific <code>HAL</code> properties, refer to the <i>HAL spec</i> which can be found in <i>/usr/share/doc/hal-0.5.13/spec/hal-spec.html</i> depending on the distribution. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;udi</i></p>
<dd> The UDI (<i>Unique Device Identifier</i>) of the device object.</p>
<dt><i>&#8211;device</i></p>
<dd> The device file of the drive.</p>
<dt><i>&#8211;enable-polling</i></p>
<dd> Enable polling instead of disabling it.</p>
<dt><i>&#8211;help</i></p>
<dd> Print out usage.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version. </p>
</dl>
<h2>NOTES</h2>
<p> This program requires super user privileges. </p>
<h2>RETURN VALUE</h2>
<p> If the requested operation was successful, this program will exit with exit code 0. </p>
<h2>HISTORY</h2>
<p> Polling a storage drive is a necessary evil to detect when the user inserts or removes media. Human computer interaction studies have shown that a broad class of users expect their system to react within a few seconds of this. Thus, the <i>hald</i> daemon polls through the <i>hald-addon-storage</i> addon (one instance for each drive with removable media). </p>
<p> The purpose of the <i>hald-addon-storage</i> addon is simply to open the special device file at a regular interval (either every 2 or every 16 seconds) to check for new media. This program tries to open the device file using the <code>O_EXCL</code> option which means that programs like <i><a href="/docs/linux/man/1-cdrecord/">cdrecord</a></i>(1) that uses <code>O_EXCL</code> automatically prevents the <i>hald-addon-storage</i> for interferring by continously opening the device file. In addition, if the drive is locked using HAL (see <i><a href="/docs/linux/man/1-hal-lock/">hal-lock</a></i>(1)) the addon also stops polling. </p>
<p> Unfortunately, polling a storage drive can have adverse side effects if the hardware and/or device driver for the hardware is malfunctioning. Additionally, the operating system kernel itself may offer multiple interfaces for the same device (e.g. <i>/dev/sg0</i> and <i>/dev/scd0</i>) so even <code>O_EXCL</code> won&#8217;t work. Also, polling a drive may decrease throughput in certain (odd and/or broken) configurations; for example, if two IDE drives shares the same host (master/slave), bus traffic and contention caused by polling e.g. the optical drive (slave) can reduce throughput to the hard disk (master) and/or interfere with CD burning on another optical drive (master). Finally, polling a drive incurs an overhead both in the host system (processes get woken up often, preventing the CPU to stay in a deep power saving states) and it may prevent the actual drive from reaching deep power states as well. As a result, more power is consumed and this affects battery life for laptops. </p>
<p> Despite the existence of support for asynchronous media change notification in recent MMC (Multi-Media Commands) specifications, virtually no optical drives are compliant with the specification. Fortunately newer SATA ATAPI hardware seems to support Asynchronous Notification (AN) and at this time of writing (March 2007) work is underway to make both the <i>Linux </i> operating system kernel and <i>HAL</i> take advantage of this. </p>
<p> It is the position of the <i>HAL</i> team that polling should be avoided at all costs as long as it doesn&#8217;t heavily impact the user experience in a negative way. This tool is provided as a stop-gap measure to use if a system is rendered useless due to bugs in drivers and/or hardware that is provoked by HAL polling the drive. If such a bug is encountered it should be reported (see the <code>BUGS</code> section below) so it can be fixed &#8211; historically <code>hald</code> have triggered a number of bugs in <i>Linux</i> storage drivers and related subsystems (such as USB) that have later been fixed. </p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the HAL mailing list, see <i><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></i> on how to subscribe. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-hald/">hald</a></i>(8), <i><a href="/docs/linux/man/1-lshal/">lshal</a></i>(1), <i><a href="/docs/linux/man/1-hal-lock/">hal-lock</a></i>(1), <i><a href="/docs/linux/man/2-open/">open</a></i>(2), <i><a rel="nofollow" href="http://www.t10.org/scsi-3.htm">http://www.t10.org/scsi-3.htm</a></i>, <i><a rel="nofollow" href="https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=halpolling">https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=halpolling</a></i> </p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others. </p>
<h2>Index</h2>
