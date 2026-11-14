---
title: "ares_dup(3)"
name: "ares_dup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_dup/"
description: "ares_dup – Duplicate a resolver channel"
---

<h2>NAME</h2>
<p> ares_dup &#8211; Duplicate a resolver channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_dup(ares_channel *dest, ares_channel source)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3)</code> function duplicates an existing communications channel for name service lookups. If it returns successfully, <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3)</code> will set the variable pointed to by <i>dest</i> to a handle used to identify the name service channel. The caller should invoke <i><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a>(3)</i> on the handle when the channel is no longer needed. </p>
<p> The <code>ares_dup_options</code> function also initializes a name service channel, with additional options set exactly as the <i>source</i> channel has them configured.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_destroy/">ares_destroy</a>(3),</code> <code><a href="/docs/linux/man/3-ares_init/">ares_init</a>(3),</code> <code><a href="/docs/linux/man/3-ares_library_init/">ares_library_init</a>(3)</code></p>
<h2>AVAILABILITY</h2>
<p> <a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3) was added in c-ares 1.6.0</p>
<h2>AUTHOR</h2>
<p> Daniel Stenberg </p>
<h2>Index</h2>
