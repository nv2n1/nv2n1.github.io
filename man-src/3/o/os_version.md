---
title: "os_version(3)"
name: "os_version"
section: "3"
letter: "o"
url: "/docs/linux/man/3-os_version/"
description: "os_version, os_revision – Version of the OS currently running. Allegro game programming library."
---

<p>os_version, os_revision &#8211; Version of the OS currently running. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern int os_version;</code> <code>extern int os_revision;</code></p>
<h2>Description</h2>
<p>The major and minor version of the Operating System currently running. Set by allegro_init(). If Allegro for some reason was not able to retrieve the version of the Operating System, os_version and os_revision will be set to -1. For example: Under Win98 SE (v4.10.2222) os_version will be set to 4 and os_revision to 10. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-os_type/">os_type</a></code>(3), <code><a href="/docs/linux/man/3-os_multitasking/">os_multitasking</a></code>(3) </p>
