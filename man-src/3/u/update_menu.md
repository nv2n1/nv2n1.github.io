---
title: "update_menu(3)"
name: "update_menu"
section: "3"
letter: "u"
url: "/docs/linux/man/3-update_menu/"
description: "update_menu – Low level function to update a menu player. Allegro game programming library."
---

<p>update_menu &#8211; Low level function to update a menu player. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int update_menu(MENU_PLAYER *player);</code></pre>
<h2>Description</h2>
<p>Updates the status of a menu object returned by init_menu(). Returns TRUE if the menu is still active, or FALSE if it has terminated. Upon a return value of FALSE, it is up to you to call shutdown_menu() or to continue execution. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-init_menu/">init_menu</a></code>(3), <code><a href="/docs/linux/man/3-shutdown_menu/">shutdown_menu</a></code>(3), <code><a href="/docs/linux/man/3-do_menu/">do_menu</a></code>(3) </p>
