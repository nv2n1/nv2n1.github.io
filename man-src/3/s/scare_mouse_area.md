---
title: "scare_mouse_area(3)"
name: "scare_mouse_area"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scare_mouse_area/"
description: "scare_mouse_area – Helper for hiding the mouse cursor before drawing in an area. Allegro game programming library."
---

<p>scare_mouse_area &#8211; Helper for hiding the mouse cursor before drawing in an area. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void scare_mouse_area(int x, int y, int w, int h);</code></pre>
<h2>Description</h2>
<p>Like scare_mouse(), but will only hide the cursor if it is inside the specified rectangle. Otherwise the cursor will simply be frozen in place until you call unscare_mouse(), so it cannot interfere with your drawing. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-unscare_mouse/">unscare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-scare_mouse/">scare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3) </p>
