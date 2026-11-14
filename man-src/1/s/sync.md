---
title: "sync(1)"
name: "sync"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sync/"
description: "sync – Synchronize cached writes to persistent storage"
---

<h2 class="name">NAME</h2>
<p> sync &#8211; Synchronize cached writes to persistent storage </p>
<h2>SYNOPSIS</h2>
<p> <code>sync</code> [<i>,OPTION/</i>] [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Synchronize cached writes to persistent storage </p>
<p> If one or more files are specified, sync only them, or their containing file systems.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;data</code></p>
<dd> sync only file data, no unneeded metadata</p>
<dt><code>-f</code>, <code>&#8211;file-system</code></p>
<dd> sync the file systems that contain the files</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>BUGS</h2>
<p> Persistence guarantees vary per system. See the system calls below for more details.</p>
<h2>AUTHOR</h2>
<p> Written by Jim Meyering and Giuseppe Scrivano.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-fdatasync/">fdatasync</a>(2), <a href="/docs/linux/man/2-fsync/">fsync</a>(2), <a href="/docs/linux/man/2-sync/">sync</a>(2), <a href="/docs/linux/man/2-syncfs/">syncfs</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/sync">https://www.gnu.org/software/coreutils/sync</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) sync invocation&#8217; </p>
<h2>Index</h2>
