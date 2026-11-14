---
title: "get_framenum_subset64(3)"
name: "get_framenum_subset64"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_framenum_subset64/"
description: "get_framenum_subset64 — perform a reverse look-up on a monotonic dirfile field"
---

<h2>NAME</h2>
<p> get_framenum_subset64 &#8212; perform a reverse look-up on a monotonic dirfile field</p>
<h2>SYNOPSIS</h2>
<p> <code>#define _LARGEFILE64_SOURCE</code> </p>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>double get_framenum_subset64(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>field_code</i><code>, double </code><i>value</i><code>, off64_t </code><i>field_start</i><code>,</code> <code>off64_t </code><i>field_end</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This version of <code><a href="/docs/linux/man/3-get_framenum_subset/">get_framenum_subset</a></code>(3) uses a 64-bit offset type, even if <i>off_t</i> is a 32-bit type. It is only available if one defines <i>_LARGEFILE64_SOURCE</i>. If <i>off_t</i> is a 64-bit type (i.e. if <i>_FILE_OFFSET_BITS</i> is defined to be 64), this function will be called <code>get_framenum_subset</code>(). Otherwise, <code>get_framenum_subset</code>() will be a version of this function which uses a 32-bit <i>off_t</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_framenum_subset/">get_framenum_subset</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7) </p>
<h2>Index</h2>
