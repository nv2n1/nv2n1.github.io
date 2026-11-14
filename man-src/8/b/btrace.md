---
title: "btrace(8)"
name: "btrace"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btrace/"
description: "btrace – perform live tracing for block devices"
---

<p>btrace &#8211; perform live tracing for block devices </p>
<h2>Synopsis</h2>
<p><code>btrace [-s] [-t] [-w </code><i>N</i>] [-n <i>N</i>] [-b <i>N</i>] [-r <i>&lt;dbg mnt&gt;</i>] [-a &lt;<i>trace</i>&gt;&#8230;] &lt;<i>dev</i>&gt;&#8230; </p>
<h2>Description</h2>
<p>The <i>btrace</i> script provides a quick and easy way to do live tracing of block devices. It calls <i>blktrace</i> on the specified devices and pipes the output through <i>blkparse</i> for formatting. See blktrace (8) for more in-depth information about how <i>blktrace</i> works. </p>
<h2>Options</h2>
<dl>
<dt> <code>-s</code></p>
<dd>Displays data sorted by program (see <i>blkparse</i> (1)). </p>
<dt> <code>-t </code></p>
<dd>Displays time deltas per IO (see <i>blkparse</i> (1)). </p>
<dt> <code>-w </code><i>N</i></p>
<dd>Sets run time to the number of seconds specified (see <i>blktrace</i> (8)). </p>
<dt> <code>-n </code><i>N</i></p>
<dd>Specifies the number of buffers to use (see <i>blktrace</i> (8)). </p>
<dt> <code>-b </code><i>N</i></p>
<dd>Specifies buffer size for event extraction (scaled by 1024) (see <i>blktrace</i> (8)). </p>
<dt> <code>-r </code><i>&lt;dbg mnt&gt;</i></p>
<dd>Specifies the debugfs mountpoint. </p>
<dt> <code>-a &lt;</code><i>trace</i>&gt;&#8230;</p>
<dd>Adds mask to current filter (see <i>blktrace</i> (8)). </p>
<dt> <code>&lt;</code><i>dev</i>&gt;</p>
<dd>Specifies the device to trace. </p>
</dl>
<h2>Example</h2>
<p>Simply running<br />
&nbsp;<wbr>%&nbsp;<wbr>btrace&nbsp;<wbr>/dev/sda will show a trace of the device <i>/dev/sda</i>. </p>
<h2>Authors</h2>
<p><i>blkparse</i> was written by Jens Axboe, Alan D. Brunelle and Nathan Scott. This man page was created from the <i>blktrace</i> documentation by Bas Zoetekouw.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2.</p>
<h2>See Also</h2>
<p>blktrace (8), blkparse (1), verify_blkparse (1), blkrawverify (1), btt (1) </p>
