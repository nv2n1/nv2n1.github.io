---
title: "do_menu(3)"
name: "do_menu"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_menu/"
description: "do_menu – Displays an animates a popup menu. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_menu &#8211; Displays an animates a popup menu. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int do_menu(MENU *menu, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Displays and animates a popup menu at the specified screen coordinates (these will be adjusted if the menu does not entirely fit on the screen). Returns the index of the menu item that was selected, or -1 if the menu was cancelled. Note that the return value cannot indicate selection from child menus, so you will have to use the callback functions if you want multi-level menus. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-d_menu_proc/">d_menu_proc</a></code>(3), <code><a href="/docs/linux/man/3-active_menu/">active_menu</a></code>(3), <code><a href="/docs/linux/man/3-gui_menu_draw_menu/">gui_menu_draw_menu</a></code>(3), <code><a href="/docs/linux/man/3-update_menu/">update_menu</a></code>(3) </p>
<h2>Index</h2>
