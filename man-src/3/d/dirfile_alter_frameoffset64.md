---
title: "dirfile_alter_frameoffset64(3)"
name: "dirfile_alter_frameoffset64"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_alter_frameoffset64/"
description: "get_frameoffset64, dirfile_alter_frameoffset64 — report or change the frame offset of fields in a dirfile, with largefile support"
---

<h2>NAME</h2>
<p> get_frameoffset64, dirfile_alter_frameoffset64 &#8212; report or change the frame offset of fields in a dirfile, with largefile support</p>
<h2>SYNOPSIS</h2>
<p> <code>#define _LARGEFILE64_SOURCE</code> </p>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>off64_t get_frameoffset(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></p>
<dt> <code>int dirfile_alter_frameoffset64(DIRFILE *</code><i>dirfile</i><code>, off64_t </code><i>offset</i><code>,</code> <code>int </code><i>fragment_index</i><code>, int </code><i>move</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These version of <code><a href="/docs/linux/man/3-get_frameoffset/">get_frameoffset</a></code>(3) and <code><a href="/docs/linux/man/3-dirfile_alter_frameoffset/">dirfile_alter_frameoffset</a></code>(3) use a 64-bit offset type, even if <i>off_t</i> is a 32-bit type. They are only available if the caller defines <i>_LARGEFILE64_SOURCE </i> before including getdata.h. </p>
<p> If <i>off_t</i> is a 64-bit type (i.e. if <i>_FILE_OFFSET_BITS</i> is defined to be 64), these function will be called <code>get_frameoffset</code>() and <code>dirfile_alter_frameoffset</code>(). Otherwise, <code>get_frameoffset</code>() and <code>dirfile_alter_frameoffset</code>() will be versions of these functions which use a 32-bit <i>off_t</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_frameoffset/">dirfile_alter_frameoffset</a></code>(3), <code><a href="/docs/linux/man/3-get_frameoffset/">get_frameoffset</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7) </p>
<h2>Index</h2>
