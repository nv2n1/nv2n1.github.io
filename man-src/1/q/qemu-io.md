---
title: "qemu-io(1)"
name: "qemu-io"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-io/"
description: "qemu-io – QEMU Disk exerciser"
---

<h2>SYNOPSIS</h2>
<p> <code>qemu-io [-h] [-V] [-rsnm] [-c cmd] &#8230; [file]</code></p>
<h2>DESCRIPTION</h2>
<p> qemu-io is a command line utility to exercise the QEMU I/O path.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c, &#8211;cmd&nbsp;&lt;cmd&gt;</code></dt>
<dd> Command to execute</dd>
<dt><code>-r, &#8211;read-only</code></dt>
<dd> Export read-only</dd>
<dt><code>-s, &#8211;snapshot</code></dt>
<dd> Use snapshot file</dd>
<dt><code>-n, &#8211;nocache</code></dt>
<dd> Disable host cache</dd>
<dt><code>-g, &#8211;growable</code></dt>
<dd> Allow file to grow (only applies to protocols)</dd>
<dt><code>-m, &#8211;misalign</code></dt>
<dd> Misalign allocations for O_DIRECT</dd>
<dt><code>-k, &#8211;native-aio</code></dt>
<dd> Use kernel AIO implementation (on Linux only)</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help and exit</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Output version information and exit</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></code>(1), <code><a href="/docs/linux/man/8-qemu-nbd/">qemu-nbd</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> QEMU project </p>
<p> This manual page was written by Asias He &lt;asias.hejun [at] gmail.com&gt;, for the Debian project (and may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the Creative Commons Attribution-Share Alike 3.0 United States License. (See <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/3.0/us/legalcode)">http://creativecommons.org/licenses/by-sa/3.0/us/legalcode)</a> </p>
