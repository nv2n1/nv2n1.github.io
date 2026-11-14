---
title: "putdata64(3)"
name: "putdata64"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putdata64/"
description: "putdata64 — write data to a dirfile database with largefile support"
---

<p>putdata64 &#8212; write data to a dirfile database with largefile support</p>
<h2>Synopsis</h2>
<pre><code>#define _LARGEFILE64_SOURCE
#include &lt;getdata.h&gt;

size_t putdata64(DIRFILE *dirfile, const char *field_code, off64_t

                                                               first_frame,
                 off64_t first_sample, size_t num_frames, size_t

                                                              num_samples,
                 gd_type_t data_type, const void *data_out);</code></pre>
<h2>Description</h2>
<dd>This version of <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3) uses a 64-bit offset type, even if <i>off_t</i> is a 32-bit type. It is only available if one defines <i>_LARGEFILE64_SOURCE</i>. If <i>off_t</i> is a 64-bit type (i.e. if <i>_FILE_OFFSET_BITS</i> is defined to be 64), this function will be called <code>putdata</code>(). Otherwise, <code>putdata</code>() will be a version of this function which uses a 32-bit <i>off_t</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7) </p>
