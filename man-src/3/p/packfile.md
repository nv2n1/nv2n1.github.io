---
title: "packfile(3)"
name: "packfile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packfile/"
description: "PACKFILE – Packfile structure, similar to the libc FILE structure. Allegro game programming library."
---

<p>PACKFILE &#8211; Packfile structure, similar to the libc FILE structure. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct PACKFILE</code></p>
<h2>Description</h2>
<p>A packfile structure, similar to the libc FILE structure. Read chapter &quot;File and compression routines&quot; for a description on how to obtain/use this structure. Note that prior to version 4.1.18, some internal fields were accidentally documented &#8211; but PACKFILE should be treated as an opaque structure, just like the libc FILE type. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3)</p>
