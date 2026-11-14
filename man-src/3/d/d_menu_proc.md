---
title: "d_menu_proc(3)"
name: "d_menu_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_menu_proc/"
description: "d_menu_proc – Dialog procedure implementing a menu bar object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_menu_proc &#8211; Dialog procedure implementing a menu bar object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_menu_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> This object is a menu bar which will drop down child menus when it is clicked or if an alt+key corresponding to one of the shortcuts in the menu is pressed. It ignores a lot of the fields in the dialog structure, in particular the color is taken from the gui_*_color variables, and the width and height are calculated automatically (the w and h fields from the DIALOG are only used as a minimum size.) The dp field points to an array of menu structures: see do_menu() for more information. The top level menu will be displayed as a horizontal bar, but when child menus drop down from it they will be in the normal vertical format used by do_menu(). When a menu item is selected, the return value from the menu callback function is passed back to the dialog manager, so your callbacks should return D_O_K, D_REDRAW, or D_CLOSE. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-active_menu/">active_menu</a></code>(3), <code><a href="/docs/linux/man/3-gui_menu_draw_menu/">gui_menu_draw_menu</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
