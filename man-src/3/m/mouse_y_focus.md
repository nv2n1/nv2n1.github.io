---
title: "mouse_y_focus(3)"
name: "mouse_y_focus"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mouse_y_focus/"
description: "mouse_sprite, mouse_x_focus, mouse_y_focus – Global variable with the mouse sprite and focus point. Allegro game programming library."
---

<p>mouse_sprite, mouse_x_focus, mouse_y_focus &#8211; Global variable with the mouse sprite and focus point. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern BITMAP *mouse_sprite;</code> </p>
<p> <code>extern int mouse_x_focus;</code> </p>
<p> <code>extern int mouse_y_focus;</code></p>
<h2>Description</h2>
<p>Global variables containing the current mouse sprite and the focus point. These are read-only, and only to be modified using the set_mouse_sprite() and set_mouse_sprite_focus() functions. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite_focus/">set_mouse_sprite_focus</a></code>(3)</p>
