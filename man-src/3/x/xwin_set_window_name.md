---
title: "xwin_set_window_name(3)"
name: "xwin_set_window_name"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwin_set_window_name/"
description: "xwin_set_window_name – Specify the window name and group (or class). Allegro game programming library."
---

<p>xwin_set_window_name &#8211; Specify the window name and group (or class). Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void xwin_set_window_name(const char *name, const char *group);</code></pre>
<h2>Description</h2>
<p>This function is only available under X. It lets you to specify the window name and group (or class). They are important because they allow the window manager to remember the window attributes (position, layer, etc). Note that the name and the title of the window are two different things: the title is what appears in the title bar of the window, but usually has no other effects on the behaviour of the application. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_window_title/">set_window_title</a></code>(3) </p>
