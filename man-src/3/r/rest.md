---
title: "rest(3)"
name: "rest"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rest/"
description: "rest – Waits a specified number of milliseconds or yields CPU. Allegro game programming library."
---

<p>rest &#8211; Waits a specified number of milliseconds or yields CPU. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void rest(unsigned int time);</code></pre>
<h2>Description</h2>
<p>This function waits for the specified number of milliseconds. Passing 0 as parameter will not wait, but just yield. This can be useful in order to &quot;play nice&quot; with other processes. Other values will cause CPU time to be dropped on most platforms. This will look better to users, and also does things like saving battery power and making fans less noisy. Note that calling this inside your active game loop is a bad idea, as you never know when the OS will give you the CPU back, so you could end up missing the vertical retrace and skipping frames. On the other hand, on multitasking operating systems it is good form to give up the CPU for a while if you will not be using it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-rest_callback/">rest_callback</a></code>(3), <code><a href="/docs/linux/man/3-vsync/">vsync</a></code>(3), <code><a href="/docs/linux/man/3-d_yield_proc/">d_yield_proc</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-extimer/">extimer</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
