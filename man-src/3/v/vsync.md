---
title: "vsync(3)"
name: "vsync"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vsync/"
description: "vsync – Waits for a vertical retrace to begin. Allegro game programming library."
---

<p>vsync &#8211; Waits for a vertical retrace to begin. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void vsync();</code></pre>
<h2>Description</h2>
<p>Waits for a vertical retrace to begin. The retrace happens when the electron beam in your monitor has reached the bottom of the screen and is moving back to the top ready for another scan. During this short period the graphics card isn&#8217;t sending any data to the monitor, so you can do things to it that aren&#8217;t possible at other times, such as altering the palette without causing flickering (snow). Allegro will automatically wait for a retrace before altering the palette or doing any hardware scrolling, though, so you don&#8217;t normally need to bother with this function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3) </p>
