---
title: "gui_menu_draw_menu_item(3)"
name: "gui_menu_draw_menu_item"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gui_menu_draw_menu_item/"
description: "gui_menu_draw_menu, gui_menu_draw_menu_item – Hooks to modify the appearance of menus. Allegro game programming library."
---

<h2>NAME</h2>
<p> gui_menu_draw_menu, gui_menu_draw_menu_item &#8211; Hooks to modify the appearance of menus. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*gui_menu_draw_menu)(int x, int y, int w, int h);</code> </p>
<p> <code>extern void (*gui_menu_draw_menu_item)(MENU *m, int x, int y, int w,</code> </p>
<p> <code>int h, int bar, int sel);</code></p>
<h2>DESCRIPTION</h2>
<p> If set, these functions will be called whenever a menu needs to be drawn, so you can change how menus look. </p>
<p> gui_menu_draw_menu() is passed the position and size of the menu. It should draw the background of the menu onto screen. </p>
<p> gui_menu_draw_menu_item() is called once for each menu item that is to be drawn. bar will be set if the item is part of a top-level horizontal menu bar, and sel will be set if the menu item is selected. It should also draw onto screen. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
