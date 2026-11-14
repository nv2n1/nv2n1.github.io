---
title: "gcore(1)"
name: "gcore"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcore/"
description: "gcore – Generate core files for running processes"
---

<h2 class="name">NAME</h2>
<p> gcore &#8211; Generate core files for running processes </p>
<h2>SYNOPSIS</h2>
<p> <code>gcore</code> [-a] [-o <i>filename</i>] <i>pid[s]</i></p>
<h2>DESCRIPTION</h2>
<p> gcore generates a core file for the process(es) specified by process IDs, <i>pid[s]</i>. By default, each core file is written to core.<i>pid</i>, in the current directory.</p>
<dl>
<dt><code>-a</code></p>
<dd> (Linux only) ignore /proc/PID/coredump_filter and also dump memory mappings marked with the &#8216;VM_DONTDUMP&#8217; flag. See info node Core File Generation for longer explanation.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> write core file to <i>filename</i> if one PID, or <i>filename.pid</i> if multiple PIDs, instead of default core.<i>pid</i></dl>
<h2>COPYING</h2>
<p> Copyright &#169; 2003, 2005, 2007, 2008, 2018, 2020 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/5-core/">core</a></code>(5) </p>
<h2>Index</h2>
