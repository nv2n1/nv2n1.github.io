---
title: "retrace_count(3)"
name: "retrace_count"
section: "3"
letter: "r"
url: "/docs/linux/man/3-retrace_count/"
description: "retrace_count – Retrace count simulator. Allegro game programming library."
---

<p>retrace_count &#8211; Retrace count simulator. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern volatile int retrace_count;</code></p>
<h2>Description</h2>
<p>If the retrace simulator is installed, this count is incremented on each vertical retrace; otherwise, if the refresh rate is known, the count is incremented at the same rate (ignoring retraces); otherwise, it is incremented 70 times a second. This provides a way of controlling the speed of your program without installing user timer functions. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-exdbuf/">exdbuf</a></code>(3), <code><a href="/docs/linux/man/3-exflip/">exflip</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3) </p>
