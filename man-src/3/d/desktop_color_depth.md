---
title: "desktop_color_depth(3)"
name: "desktop_color_depth"
section: "3"
letter: "d"
url: "/docs/linux/man/3-desktop_color_depth/"
description: "desktop_color_depth – Finds out the desktop color depth. Allegro game programming library."
---

<h2>NAME</h2>
<p> desktop_color_depth &#8211; Finds out the desktop color depth. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int desktop_color_depth();</code></p>
<h2>DESCRIPTION</h2>
<p> Finds out the currently selected desktop color depth. You can use this information to make your program use the same color depth as the desktop, which will likely make it run faster because the graphic driver won&#8217;t be doing unnecessary color conversions behind your back. </p>
<p> Under some OSes, switching to a full screen graphics mode may automatically change the desktop color depth. You have, therefore, to call this function before setting any graphics mode in order to retrieve the real desktop color depth. Example: </p>
<pre><code>
allegro_init();
... if ((depth = desktop_color_depth()) != 0)
{
    set_color_depth(depth);
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the color depth or zero on platforms where this information is not available or does not apply. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_desktop_resolution/">get_desktop_resolution</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3) </p>
<h2>Index</h2>
