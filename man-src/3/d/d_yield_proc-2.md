---
title: "d_yield_proc-2(3)"
name: "d_yield_proc-2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_yield_proc-2/"
description: "d_yield_proc – Invisible dialog procedure that yields CPU time slices. Allegro game programming library."
---

<p>d_yield_proc &#8211; Invisible dialog procedure that yields CPU time slices. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_yield_proc(int msg, DIALOG *d, int c);</code></p>
<h2>Description</h2>
<p>An invisible helper object that yields time slices for the scheduler (if the system supports it) when the GUI has nothing to do but waiting for user actions. You should put one instance of this object in each dialog array because it may be needed on systems with an unusual scheduling algorithm (for instance QNX) in order to make the GUI fully responsive. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rest/">rest</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3)</p>
