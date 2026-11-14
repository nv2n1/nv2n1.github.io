---
title: "libnutclient_general(3)"
name: "libnutclient_general"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_general/"
description: "libnutclient_general, nutclient_destroy, strarr_alloc, strarr_free – General and utility functions in Network UPS Tools high-level client access library"
---

<h2 class="name">NAME</h2>
<p> libnutclient_general, nutclient_destroy, strarr_alloc, strarr_free &#8211; General and utility functions in Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef void* NUTCLIENT_t;
</pre>
<p>void nutclient_destroy(NUTCLIENT_t client);</p>
<pre>
typedef char** strarr;
</pre>
<pre><code>
strarr strarr_alloc(unsigned short count);
void strarr_free(strarr arr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>nutclient_destroy()</code> function destroys a <i>NUTCLIENT_t</i> or derived (like <i>NUTCLIENT_TCP_t</i>) connection object, and frees allocated memory. </p>
<p> The <code>strarr</code> type represents an array of C strings (array of char pointer). The array must always be terminated by a NULL pointer. Pointed strings must be allocated by (x)calloc or (x)strdup. </p>
<p> The <code>strarr_alloc()</code> function allocates a <i>strarr</i> array with the specified number of (non-initialized) string pointers. Another additional pointer set to 0 is added at the end of the array. </p>
<p> The <code>strarr_free</code> function frees a <i>strarr</i> array. It also frees all pointed strings. </p>
<p> <i>dev</i> is the device name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) </p>
<h2>Index</h2>
