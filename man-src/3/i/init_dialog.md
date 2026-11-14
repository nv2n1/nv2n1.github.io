---
title: "init_dialog(3)"
name: "init_dialog"
section: "3"
letter: "i"
url: "/docs/linux/man/3-init_dialog/"
description: "init_dialog – Low level initialisation of a dialog. Allegro game programming library."
---

<h2>NAME</h2>
<p> init_dialog &#8211; Low level initialisation of a dialog. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DIALOG_PLAYER *init_dialog(DIALOG *dialog, int focus_obj);</code></p>
<h2>DESCRIPTION</h2>
<p> This function provides lower level access to the same functionality as do_dialog(), but allows you to combine a dialog box with your own program control structures. It initialises a dialog, returning a pointer to a player object that can be used with update_dialog() and shutdown_dialog(). With these functions, you could implement your own version of do_dialog() with the lines: </p>
<pre><code>
DIALOG_PLAYER *player = init_dialog(dialog, focus_obj);

while (update_dialog(player))
    ;

return shutdown_dialog(player);
</code></pre>
<p> Note that you are responsible for showing and hiding the mouse cursor, which do_dialog would otherwise do for you, or saving and restoring the screen contents, as popup_dialog would do for you. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-update_dialog/">update_dialog</a></code>(3), <code><a href="/docs/linux/man/3-shutdown_dialog/">shutdown_dialog</a></code>(3), <code><a href="/docs/linux/man/3-do_dialog/">do_dialog</a></code>(3) </p>
<h2>Index</h2>
