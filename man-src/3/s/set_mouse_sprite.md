---
title: "set_mouse_sprite(3)"
name: "set_mouse_sprite"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_mouse_sprite/"
description: "set_mouse_sprite – Sets the mouse sprite. Allegro game programming library."
---

<p>set_mouse_sprite &#8211; Sets the mouse sprite. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_mouse_sprite(BITMAP *sprite);</code></p>
<h2>Description</h2>
<p> You don&#8217;t like Allegro&#8217;s mouse pointer? No problem. Use this function to supply an alternative of your own. If you change the pointer and then want to get Allegro&#8217;s lovely arrow back again, call set_mouse_sprite(NULL). </p>
<p> As a bonus, set_mouse_sprite(NULL) uses the current palette in choosing colors for the arrow. So if your arrow mouse sprite looks ugly after changing the palette, call set_mouse_sprite(NULL). </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite_focus/">set_mouse_sprite_focus</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3)</p>
