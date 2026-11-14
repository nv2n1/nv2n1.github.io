---
title: "sync(8)"
name: "sync"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sync/"
description: "sync – synchronize data on disk with memory"
---

<p>sync &#8211; synchronize data on disk with memory</p>
<h2>Synopsis</h2>
<p><code>sync [&#8211;help] [&#8211;version]</code></p>
<h2>Description</h2>
<p><code>sync</code> writes any data buffered in memory out to disk. This can include (but is not limited to) modified superblocks, modified inodes, and delayed reads and writes. This must be implemented by the kernel; The <code>sync</code> program does nothing but exercise the <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) system call. </p>
<p> The kernel keeps data in memory to avoid doing (relatively slow) disk reads and writes. This improves performance, but if the computer crashes, data may be lost or the file system corrupted as a result. <code>sync</code> ensures that everything in memory is written to disk. </p>
<p> <code>sync</code> should be called before the processor is halted in an unusual manner (e.g., before causing a kernel panic when debugging new kernel code). In general, the processor should be halted using the <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) or <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8) or <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8) commands, which will attempt to put the system in a quiescent state before calling <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2). (Various implementations of these commands exist; consult your documentation; on some systems one should not call <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8) and <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8) directly.)</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print a usage message on standard output and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd>Print version information on standard output, then exit successfully.</p>
<dt><code>&#8212;</code></p>
<dd>Terminate option list.</dl>
<h2>Environment</h2>
<p>The variables <code>LANG</code>, <code>LC_ALL</code>, <code>LC_CTYPE</code>, and <code>LC_MESSAGES</code> have the usual meaning.</p>
<h2>Conforming To</h2>
<p>POSIX.2.</p>
<h2>Notes</h2>
<p>On Linux, <code>sync</code> is guaranteed only to schedule the dirty blocks for writing; it can actually take a short time before all the blocks are finally written. The <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8) and <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8) commands take this into account by sleeping for a few seconds after calling <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2). </p>
<p> This page describes <code>sync</code> as found in the fileutils-4.0 package; other versions may differ slightly.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8), <code><a href="/docs/linux/man/8-update/">update</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
