---
title: "get_desktop_resolution(3)"
name: "get_desktop_resolution"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_desktop_resolution/"
description: "get_desktop_resolution – Finds out the desktop resolution. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_desktop_resolution &#8211; Finds out the desktop resolution. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_desktop_resolution(int *width, int *height);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds out the currently selected desktop resolution. You can use this information to avoid creating windows bigger than the current resolution. This is especially important for some windowed drivers which are unable to create windows bigger than the desktop. Each parameter is a pointer to an integer where one dimension of the screen will be stored. </p>
<p> Under some OSes, switching to a full screen graphics mode may automatically change the desktop resolution. You have, therefore, to call this function before setting any graphics mode in order to retrieve the real desktop resolution. Example: </p>
<pre><code>
int width, height;

allegro_init();
... if (get_desktop_resolution(&amp;width, &amp;height) == 0)
{
    /* Got the resolution correctly */
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number if this information is not available or does not apply, in which case the values stored in the variables you provided for `width&#8217; and `height&#8217; are undefined. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-desktop_color_depth/">desktop_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3) </p>
<h2>Index</h2>
