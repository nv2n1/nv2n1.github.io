---
title: "menu(3)"
name: "menu"
section: "3"
letter: "m"
url: "/docs/linux/man/3-menu/"
description: "MENU – Stores the entries of a menu. Allegro game programming library."
---

<p>MENU &#8211; Stores the entries of a menu. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct MENU</code></p>
<h2>Description</h2>
<pre> char *text; - the text to display for the menu item
 int (*proc)(void); - called when the menu item is clicked
 struct MENU *child; - nested child menu
 int flags; - disabled or checked state
 void *dp; - pointer to any data you need</pre>
<p>Structure used to hold an entry of a menu. Read chapter &quot;GUI routines&quot;, section &quot;GUI menus&quot; for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-do_menu/">do_menu</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3)</p>
