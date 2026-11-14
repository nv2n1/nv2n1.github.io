---
title: "text_height(3)"
name: "text_height"
section: "3"
letter: "t"
url: "/docs/linux/man/3-text_height/"
description: "text_height – Returns the height of a font in pixels. Allegro game programming library."
---

<p>text_height &#8211; Returns the height of a font in pixels. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>int text_height(const FONT *f)</code></p>
<h2>Description</h2>
<p>Returns the height (in pixels) of the specified font. Example: </p>
<pre><code>int height = text_height(font);
... bmp = create_bitmap(width, height);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-text_length/">text_length</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exsyscur/">exsyscur</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
