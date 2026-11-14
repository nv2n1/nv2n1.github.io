---
title: "pack_fclose(3)"
name: "pack_fclose"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fclose/"
description: "pack_fclose – Closes a stream previously opened. Allegro game programming library."
---

<p>pack_fclose &#8211; Closes a stream previously opened. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_fclose(PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Closes the stream `f&#8217; previously opened with pack_fopen() or pack_fopen_vtable(). After you have closed the stream, performing operations on it will yield errors in your application (e.g. crash it) or even block your OS.</p>
<h2>Return Value</h2>
<p>Returns zero on success. On error, returns an error code which is also stored in `errno&#8217;. This function can fail only when writing to files: if the file was opened in read mode, it will always succeed. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3), <code><a href="/docs/linux/man/3-packfile_password/">packfile_password</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
