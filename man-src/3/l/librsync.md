---
title: "librsync(3)"
name: "librsync"
section: "3"
letter: "l"
url: "/docs/linux/man/3-librsync/"
description: "librsync – library for delta compression of streams"
---

<h2 class="name">NAME</h2>
<p> librsync &#8211; library for delta compression of streams </p>
<h2>SYNOPSYS</h2>
<p>&nbsp;<wbr>#include&nbsp;<wbr><code>&lt;stdio.h&gt;</code> </p>
<p>&nbsp;<wbr>#include&nbsp;<wbr><code>&lt;stdlib.h&gt;</code> </p>
<p>&nbsp;<wbr>#include&nbsp;<wbr><code>&lt;librsync.h&gt;</code> </p>
<p>&nbsp;<wbr>cc &#8230;&nbsp;<wbr><code>-lrsync</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>librsync</code> library implements network delta-compression of streams and files. The algorithm is similar to that used in the <code><a href="/docs/linux/man/1-rsync/">rsync</a>(1)</code> and <code><a href="/docs/linux/man/2-xdelta/">xdelta</a>(2)</code> programs, but specialized for transfer of arbitrary-length octet streams. Unlike most diff programs, <code>librsync</code> does not require access to both of the files on the same machine, but rather only a short &#8220;signature&#8221; of the old file and the complete contents of the new file. </p>
<p> The canonical use of <code>librsync</code> is in the <code><a href="/docs/linux/man/8-rproxy/">rproxy</a>(8)</code> reference implementation of the <i>rsync</i> proposed extension to HTTP. It may be useful to other programs which wish to do delta-compression in HTTP, or within their own protocol. There are HTTP-specific utility functions within <code>librsync</code>, but they need not be used. </p>
<p> A number of tools such as <code><a href="/docs/linux/man/1-rdiff/">rdiff</a>(1)</code> provide command-line and scriptable access to rsync functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rdiff/">rdiff</a></code>(1) </p>
<p> <i>rdiff and librsync Manual</i> </p>
<p> <i><a rel="nofollow" href="http://rproxy.sourceforge.net/">http://rproxy.sourceforge.net/</a></i>. </p>
<p> <i>draft-pool-rsync</i></p>
<h2>BUGS</h2>
<p> The rsync protocol is still evolving. There may be bugs in the implementation. The interface may change in the future, but it is becoming more stable. </p>
<p> Many routines will panic in case of error rather than returning an error code to the caller. Patches to fix this are welcome, but at the current state of development aborting seems as useful as trusting to possibly-incomplete checking in the client.</p>
<h2>AUTHOR</h2>
<p> Martin Pool &lt;mbp [at] samba.org&gt;, with Andrew Tridgell &lt;tridge [at] samba.org&gt;. </p>
<p> rdiff development has been supported by Linuxcare, Inc and VA Linux Systems. </p>
<h2>Index</h2>
