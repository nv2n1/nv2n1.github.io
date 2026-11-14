---
title: "inotail(1)"
name: "inotail"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inotail/"
description: "inotail – A fast and lightweight version of tail using inotify"
---

<h2>NAME</h2>
<p> inotail &#8211; A fast and lightweight version of tail using inotify</p>
<h2>SYNOPSIS</h2>
<p> <code>inotail</code> [OPTION]&#8230; [FILE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>inotail</code> is a replacement for the &#8216;tail&#8217; program found in the base installation of every Linux/UNIX system. It makes use of the inotify infrastructure in recent versions of the Linux kernel to speed up tailing files in the follow mode (the &#8216;-f&#8217; option). Standard tail polls the file every second by default while inotail listens to special events sent by the kernel through the inotify API to determine whether a file needs to be reread. <i>Note:</i> inotail will not work on systems running a kernel without inotify. To enable inotify, please set CONFIG_INOTIFY=y in your Linux kernel configuration and recompile it. </p>
<p> Currently inotail is not fully compatible to neither POSIX or GNU tail but might be in the future.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>N</i>, <code>&#8211;bytes</code>=<i>N</i></p>
<dd> output the last N bytes. If the first character of N is a &#8216;+&#8217;, begin printing with the Nth character from the start of each file.</p>
<dt><code>-f, &#8211;follow</code></p>
<dd> keep the file(s) open and print appended data as the file grows</p>
<dt><code>-n </code><i>N</i>, <code>&#8211;lines</code>=<i>N</i></p>
<dd> output the last N lines (default: 10) If the first character of N is a &#8216;+&#8217;, begin printing with the Nth line from the start of each file.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> print headers with file names</p>
<dt><code>-h, &#8211;help</code></p>
<dd> show help and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd> show inotail version and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Tobias Klauser &lt;tklauser [at] distanz.ch&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tail/">tail</a>(1),</code> <code><a href="/docs/linux/man/7-inotify/">inotify</a>(7)</code> </p>
<h2>Index</h2>
