---
title: "extend_dmalloc(1)"
name: "extend_dmalloc"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extend_dmalloc/"
description: "extend_dmalloc – Analyze return-addresses from dmalloc logfiles."
---

<h2 class="name">NAME</h2>
<p> extend_dmalloc &#8211; Analyze return-addresses from dmalloc logfiles. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>extend_dmalloc</code> [<i>dmalloc-log</i><code>binary</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>extend_dmalloc</code></p>
<dd>will run <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) to get information on the return-addresses from a <code><a href="/docs/linux/man/1-dmalloc/">dmalloc</a></code>(1) logfile. Specifically it will examine any ra= lines and try to get the corresponding line numbers </p>
<p> The argument <code>binary</code> must be the binary that generated the log dmalloc-log. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>NOTES</h2>
<p> You may wish to direct the output from <code>extend_dmalloc</code> to a file, since otherwise <code>gdb</code> seems to prompt for a return as if you are at the end of a page.</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
