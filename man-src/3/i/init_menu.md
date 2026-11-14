---
title: "init_menu(3)"
name: "init_menu"
section: "3"
letter: "i"
url: "/docs/linux/man/3-init_menu/"
description: "init_menu – Low level initialisation of a menu. Allegro game programming library."
---

<h2>NAME</h2>
<p> init_menu &#8211; Low level initialisation of a menu. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>MENU_PLAYER *init_menu(MENU *menu, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> This function provides lower level access to the same functionality as do_menu(), but allows you to combine a popup menu with your own program control structures. It initialises a menu, returning a pointer to a menu player object that can be used with update_menu() and shutdown_menu(). With these functions, you could implement your own version of do_menu() with the lines: </p>
<pre><code>
MENU_PLAYER *player = init_menu(menu, x, y);

while (update_menu(player))
    ;

return shutdown_menu(player);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-update_menu/">update_menu</a></code>(3), <code><a href="/docs/linux/man/3-shutdown_menu/">shutdown_menu</a></code>(3), <code><a href="/docs/linux/man/3-do_menu/">do_menu</a></code>(3) </p>
<h2>Index</h2>
