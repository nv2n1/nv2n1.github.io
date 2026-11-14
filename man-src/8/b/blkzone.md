---
title: "blkzone(8)"
name: "blkzone"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkzone/"
description: "blkzone – run zone command on a device"
---

<p>blkzone &#8211; run zone command on a device</p>
<h2>Synopsis</h2>
<p><code>blkzone</code> <i>command</i> [options] <i>device</i></p>
<h2>Description</h2>
<p><code>blkzone</code> is used to run zone command on device that support the Zoned Block Commands (ZBC) or Zoned-device ATA Commands (ZAC). The zones to operate on can be specified using the offset, count and length options. </p>
<p> The <i>device</i> argument is the pathname of the block device.</p>
<h2>Commands</h2>
<h3>report</h3>
<p>The command <code>blkzone report</code> is used to report device zone information. </p>
<p> By default, the command will report all zones from the start of the block device. Options may be used to modify this behavior, changing the starting zone or the size of the report, as explained below. </p>
<p> Report output: </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> start </td>
<td>
<p> Zone start sector
</td>
</tr>
<tr VALIGN=top>
<td>
<p> len </td>
<td>
<p> Zone length in number of sectors
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cap </td>
<td>
<p> Zone capacity in number of sectors
</td>
</tr>
<tr VALIGN=top>
<td>
<p> wptr </td>
<td>
<p> Zone write pointer position
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reset </td>
<td>
<p> Reset write pointer recommended
</td>
</tr>
<tr VALIGN=top>
<td>
<p> non-seq </td>
<td>
<p> Non-sequential write resources active
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cond </td>
<td>
<p> Zone condition
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> Zone type
</td>
</tr>
</table>
<p> Zone conditions: </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> cl </td>
<td>
<p> Closed
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nw </td>
<td>
<p> Not write pointer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> em </td>
<td>
<p> Empty
</td>
</tr>
<tr VALIGN=top>
<td>
<p> fu </td>
<td>
<p> Full
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oe </td>
<td>
<p> Explicitly opened
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oi </td>
<td>
<p> Implicitly opened
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ol </td>
<td>
<p> Offline
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ro </td>
<td>
<p> Read only
</td>
</tr>
<tr VALIGN=top>
<td>
<p> x? </td>
<td>
<p> Reserved conditions (should not be reported)
</td>
</tr>
</table>
<h3>capacity</h3>
<p>The command <code>blkzone capacity</code> is used to report device capacity information. </p>
<p> By default, the command will report the sum, in number of sectors, of all zone capacities on the device. Options may be used to modify this behavior, changing the starting zone or the size of the report, as explained below.</p>
<h3>reset</h3>
<p>The command <code>blkzone reset</code> is used to reset one or more zones. Unlike <code><a href="/docs/linux/man/8-sg_reset_wp/">sg_reset_wp</a></code>(8), this command operates from the block layer and can reset a range of zones.</p>
<h3>open</h3>
<p>The command <code>blkzone open</code> is used to explicitly open one or more zones. Unlike <code><a href="/docs/linux/man/8-sg_zone/">sg_zone</a></code>(8), open action, this command operates from the block layer and can open a range of zones.</p>
<h3>close</h3>
<p>The command <code>blkzone close</code> is used to close one or more zones. Unlike <code><a href="/docs/linux/man/8-sg_zone/">sg_zone</a></code>(8), close action, this command operates from the block layer and can close a range of zones.</p>
<h3>finish</h3>
<p>The command <code>blkzone finish</code> is used to finish (transition to full condition) one or more zones. Unlike <code><a href="/docs/linux/man/8-sg_zone/">sg_zone</a></code>(8), finish action, this command operates from the block layer and can finish a range of zones. </p>
<p> By default, the reset, open, close and finish commands will operate from the zone at device sector 0 and operate on all zones. Options may be used to modify this behavior as explained below.</p>
<h2>Options</h2>
<p>The <i>offset</i> and <i>length</i> option arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. Additionally, the 0x prefix can be used to specify <i>offset</i> and <i>length</i> in hex. </p>
<p> <code>-o</code>, <code>&#8211;offset</code> <i>sector</i></p>
<dl>
<dd>The starting zone specified as a sector offset. The provided offset in sector units (512 bytes) should match the start of a zone. The default value is zero.</dl>
<p> <code>-l</code>, <code>&#8211;length</code> <i>sectors</i></p>
<dl>
<dd>The maximum number of sectors the command should operate on. The default value is the number of sectors remaining after <i>offset</i>. This option cannot be used together with the option <code>&#8211;count</code>.</dl>
<p> <code>-c</code>, <code>&#8211;count</code> <i>count</i></p>
<dl>
<dd>The maximum number of zones the command should operate on. The default value is the number of zones starting from <i>offset</i>. This option cannot be used together with the option <code>&#8211;length</code>.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Enforce commands to change zone status on block devices used by the system.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Display the number of zones returned in the report or the range of sectors reset.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_rep_zones/">sg_rep_zones</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>blkzone</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
