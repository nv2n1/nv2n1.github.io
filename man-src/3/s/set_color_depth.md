---
title: "set_color_depth(3)"
name: "set_color_depth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_color_depth/"
description: "set_color_depth – Sets the global pixel color depth. Allegro game programming library."
---

<p>set_color_depth &#8211; Sets the global pixel color depth. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_color_depth(int depth);</code></pre>
<h2>Description</h2>
<p>Sets the pixel format to be used by subsequent calls to set_gfx_mode() and create_bitmap(). Valid depths are 8 (the default), 15, 16, 24, and 32 bits. Example: </p>
<pre> set_color_depth(32);
 if (set_gfx_mode(GFX_AUTODETECT, 640, 480, 0, 0) != 0) {
 abort_on_error(&quot;Couldn't set a 32 bit color resolution&quot;);
 }</pre>
<p>Note that the screen color depth won&#8217;t change until the next successful call to set_gfx_mode(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_color_depth/">get_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-getr/">getr</a></code>(3), <code><a href="/docs/linux/man/3-desktop_color_depth/">desktop_color_depth</a></code>(3) </p>
