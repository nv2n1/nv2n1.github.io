---
title: "text_length(3)"
name: "text_length"
section: "3"
letter: "t"
url: "/docs/linux/man/3-text_length/"
description: "text_length – Returns the length of a string in pixels. Allegro game programming library."
---

<p>text_length &#8211; Returns the length of a string in pixels. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int text_length(const FONT *f, const char *str);</code></pre>
<h2>Description</h2>
<p>Returns the length (in pixels) of a string in the specified font. Example: </p>
<pre><code>int width = text_length(font, &quot;I love spam&quot;);
... bmp = create_bitmap(width, height);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-text_height/">text_height</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
