---
title: "bno_plot(1)"
name: "bno_plot"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bno_plot/"
description: "bno_plot – generate interactive 3D plot of IO blocks and sizes"
---

<h2 class="name">NAME</h2>
<p> bno_plot &#8211; generate interactive 3D plot of IO blocks and sizes </p>
<h2>SYNOPSIS</h2>
<p> <code>bno_plot</code> [ -h | &#8211;help ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>-v | &#8211;verbose&nbsp;<wbr>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>-K | &#8211;keys-below&nbsp;<wbr>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&lt;file&#8230;&gt;&nbsp;<wbr>] </p>
<h2>DESCRIPTION</h2>
<p> bno_plot is a visualization tool for the block layer IO tracing tool called <a href="/docs/linux/man/8-blktrace/">blktrace</a>(8). As noted in its documentation, blktrace is a block layer IO tracing mechanism which provides detailed information about request queue operations up to user space. </p>
<p> bno_plot utilizes gnuplot to generate a 3D plot of the block number output from btt. If no <i>&lt;files&gt;</i> are specified, it will utilize all files generated after btt was run with <i>-B blknos</i> (meaning: all files of the form <i>blknos*[rw].dat</i>). </p>
<p> The <i>-K</i> option forces bno_plot to put the keys below the graph. If it is not specified, all keys for input files are put in the upper right corner of the graph. If the number of devices exceed 10, then bno_plot will automatically push the keys under the graph. </p>
<p> To use this utility, the gnuplot package needs to be installed. </p>
<p> To exit the plotter, enter &#8216;quit&#8217; or ^D at the &#8216;gnuplot&gt; &#8216; prompt. </p>
<h2>AUTHORS</h2>
<p> <i>bno_plot</i> was written by Alan D. Brunelle. This man page was created from the <i>blktrace</i> documentation by Bas Zoetekouw. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;linux-btrace [at] vger.kernel.org&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Hewlett-Packard Development Company, L.P.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page was created for Debian by Bas Zoetekouw. It was derived from the documentation provided by the authors and it may be used, distributed and modified under the terms of the GNU General Public License, version 2.<br />
 On Debian systems, the text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2. </p>
<h2>SEE ALSO</h2>
<p> btt (1), gnuplot (1), blktrace (8), blkparse (1), verify_blkparse (1), blkrawverify (1) </p>
<h2>Index</h2>
