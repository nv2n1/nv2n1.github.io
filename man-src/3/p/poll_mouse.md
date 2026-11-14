---
title: "poll_mouse(3)"
name: "poll_mouse"
section: "3"
letter: "p"
url: "/docs/linux/man/3-poll_mouse/"
description: "poll_mouse – Polls the mouse. Allegro game programming library."
---

<p>poll_mouse &#8211; Polls the mouse. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int poll_mouse();</code></pre>
<h2>Description</h2>
<p>Wherever possible, Allegro will read the mouse input asynchronously (ie. from inside an interrupt handler), but on some platforms that may not be possible, in which case you must call this routine at regular intervals to update the mouse state variables. To help you test your mouse polling code even if you are programming on a platform that doesn&#8217;t require it, after the first time that you call this function Allegro will switch into polling mode, so from that point onwards you will have to call this routine in order to get any mouse input at all, regardless of whether the current driver actually needs to be polled or not.</p>
<h2>Return Value</h2>
<p>Returns zero on success, or a negative number on failure (ie. no mouse driver installed). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mouse_needs_poll/">mouse_needs_poll</a></code>(3), <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-mouse_x/">mouse_x</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
