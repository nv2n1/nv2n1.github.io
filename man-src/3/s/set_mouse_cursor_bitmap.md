---
title: "set_mouse_cursor_bitmap(3)"
name: "set_mouse_cursor_bitmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_mouse_cursor_bitmap/"
description: "set_mouse_cursor_bitmap – Changes the image Allegro uses for mouse cursors."
---

<p>set_mouse_cursor_bitmap &#8211; Changes the image Allegro uses for mouse cursors.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_mouse_cursor_bitmap(int cursor, BITMAP *bmp);</code></p>
<h2>Description</h2>
<p> This function changes the cursor image Allegro uses if select_mouse_cursor() is called but no native operating system cursor can be used, e.g. because you did not call enable_hardware_cursor(). </p>
<p> The cursor argument can be one of: </p>
<p> <code>MOUSE_CURSOR_ALLEGRO</code> <code>MOUSE_CURSOR_ARROW</code> <code>MOUSE_CURSOR_BUSY</code> <code>MOUSE_CURSOR_QUESTION</code> <code>MOUSE_CURSOR_EDIT</code> </p>
<p> but not MOUSE_CURSOR_NONE. </p>
<p> The bmp argument can either point to a valid bitmap or it can be NULL. Passing a bitmap makes Allegro use that image in place of its own default substitution (should the operating system&#8217;s native cursor be unavailable). The bitmap must remain available for the duration in which it could be used. Passing NULL lets Allegro revert to its default substitutions. </p>
<p> The effect of this function will not be apparent until show_mouse() is called. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-enable_hardware_cursor/">enable_hardware_cursor</a></code>(3), <code><a href="/docs/linux/man/3-show_os_cursor/">show_os_cursor</a></code>(3)</p>
