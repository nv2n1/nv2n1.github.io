---
title: "pack_fopen_vtable(3)"
name: "pack_fopen_vtable"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fopen_vtable/"
description: "pack_fopen_vtable – Allegro game programming library."
---

<p>pack_fopen_vtable &#8211; Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>PACKFILE *pack_fopen_vtable(const PACKFILE_VTABLE *vtable, void *userdata);</code></p>
<h2>Description</h2>
<p>Creates a new packfile structure that uses the functions specified in the vtable instead of the standard functions. The data pointer by `vtable&#8217; and `userdata&#8217; must remain available for the lifetime of the created packfile. </p>
<p> While the created packfile structure can be used with other Allegro functions, there are two limitations. First, opening chunks using pack_fopen_chunk() on top of the returned packfile is not possible at this time. And packfile_password() does not have any effect on packfiles opened with pack_fopen_vtable().</p>
<h2>Return Value</h2>
<p>On success, it returns a pointer to a PACKFILE structure, and on error it returns NULL and stores an error code in `errno&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-packfile_password/">packfile_password</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
