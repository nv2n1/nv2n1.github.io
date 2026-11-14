---
title: "cpu_vendor(3)"
name: "cpu_vendor"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpu_vendor/"
description: "cpu_vendor – Contains the CPU vendor name. Allegro game programming library."
---

<h2>NAME</h2>
<p> cpu_vendor &#8211; Contains the CPU vendor name. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern char cpu_vendor[];</code></p>
<h2>DESCRIPTION</h2>
<p> On Intel PCs, contains the CPU vendor name if known. On Mac OSX systems this contains the PPC subtype name. On other platforms, this may be an empty string. You can read this variable after you have called check_cpu() (which is automatically called by allegro_init()). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-check_cpu/">check_cpu</a></code>(3), <code><a href="/docs/linux/man/3-cpu_family/">cpu_family</a></code>(3), <code><a href="/docs/linux/man/3-cpu_model/">cpu_model</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3) </p>
<h2>Index</h2>
