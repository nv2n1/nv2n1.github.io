---
title: "lock_variable(3)"
name: "lock_variable"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lock_variable/"
description: "LOCK_VARIABLE – Locks the memory of a variable used by a timer. Allegro game programming library."
---

<p>LOCK_VARIABLE &#8211; Locks the memory of a variable used by a timer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Macro LOCK_VARIABLE(variable_name);</code></p>
<h2>Description</h2>
<p>Due to interrupts, you are required to lock all the memory used by your timer routines. See the description of install_int_ex() for a more detailed explanation and usage example. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_int/">install_int</a></code>(3), <code><a href="/docs/linux/man/3-install_int_ex/">install_int_ex</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-extimer/">extimer</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3)</p>
