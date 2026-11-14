---
title: "blkrawverify(1)"
name: "blkrawverify"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blkrawverify/"
description: "blkrawverify – verifies an output file produced by blkparse"
---

<h2 class="name">NAME</h2>
<p> blkrawverify &#8211; verifies an output file produced by blkparse </p>
<h2>SYNOPSIS</h2>
<p> <code>blkrawverify &lt;</code><i>dev</i>&gt; [&lt;<i>dev</i>&gt;&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The <i>blkrawverify</i> utility can be used to verify data retrieved via <i>blktrace</i>. It will check for valid event formats, forward progressing sequence numbers and time stamps, also does reasonable checks for other potential issues within individual events. </p>
<p> Errors found will be tracked in &lt;<i>dev</i>&gt;.verify.out. </p>
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
<p> btrace (8), blktrace (8), blkparse (1), verify_blkparse (1), btt (1) </p>
<h2>Index</h2>
