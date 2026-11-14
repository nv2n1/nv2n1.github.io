---
title: "verify_blkparse(1)"
name: "verify_blkparse"
section: "1"
letter: "v"
url: "/docs/linux/man/1-verify_blkparse/"
description: "verify_blkparse – verifies an output file produced by blkparse"
---

<h2 class="name">NAME</h2>
<p> verify_blkparse &#8211; verifies an output file produced by blkparse </p>
<h2>SYNOPSIS</h2>
<p> <code>verify_blkparse &lt;</code><i>filename</i>&gt; </p>
<h2>DESCRIPTION</h2>
<p> Verifies an output file from blkparse. All it does is check if the events in the file are correctly time ordered. If an entry is found that isn&#8217;t ordered, it&#8217;s dumped to stdout. </p>
<h2>AUTHORS</h2>
<p> <i>blkparse</i> was written by Jens Axboe, Alan D. Brunelle and Nathan Scott. This man page was created from the <i>blktrace</i> documentation by Bas Zoetekouw. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 Jens Axboe, Alan D. Brunelle and Nathan Scott.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2. </p>
<h2>SEE ALSO</h2>
<p> btrace (8), blktrace (8), blkparse (1), blkrawverify (1), btt (1) </p>
<h2>Index</h2>
