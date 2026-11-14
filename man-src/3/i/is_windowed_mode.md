---
title: "is_windowed_mode(3)"
name: "is_windowed_mode"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_windowed_mode/"
description: "is_windowed_mode – Tells if you are running in windowed mode. Allegro game programming library."
---

<h2>NAME</h2>
<p> is_windowed_mode &#8211; Tells if you are running in windowed mode. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int is_windowed_mode(void);</code></p>
<h2>DESCRIPTION</h2>
<p> This function can be used to detect whether or not set_gfx_mode() selected a windowed mode. Example: </p>
<pre><code>
if (set_gfx_mode(GFX_AUTODETECT, 640, 480, 0, 0) != 0)
    abort_on_error("Couldn't set graphic mode!");
if (is_windowed_mode()) {
    /* Windowed mode stuff. */
} else {
    /* Fullscreen mode stuff. */
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns true if the current graphics mode is a windowed mode, or zero if it is a fullscreen mode. You should not call this function if you are not in graphics mode. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3) </p>
<h2>Index</h2>
