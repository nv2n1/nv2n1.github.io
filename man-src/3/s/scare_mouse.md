---
title: "scare_mouse(3)"
name: "scare_mouse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scare_mouse/"
description: "scare_mouse – Helper for hiding the mouse pointer before drawing. Allegro game programming library."
---

<p>scare_mouse &#8211; Helper for hiding the mouse pointer before drawing. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void scare_mouse();</code></pre>
<h2>Description</h2>
<p>Helper for hiding the mouse pointer prior to a drawing operation. This will temporarily get rid of the pointer, but only if that is really required (ie. the mouse is visible, and is displayed on the physical screen rather than some other memory surface, and it is not a hardware or OS cursor). The previous mouse state is stored for subsequent calls to unscare_mouse(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-unscare_mouse/">unscare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-scare_mouse_area/">scare_mouse_area</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3) </p>
