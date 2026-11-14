---
title: "find_dialog_focus(3)"
name: "find_dialog_focus"
section: "3"
letter: "f"
url: "/docs/linux/man/3-find_dialog_focus/"
description: "find_dialog_focus – Searches the dialog for the object which has the input focus. Allegro game programming library."
---

<h2>NAME</h2>
<p> find_dialog_focus &#8211; Searches the dialog for the object which has the input focus. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int find_dialog_focus(DIALOG *dialog);</code></p>
<h2>DESCRIPTION</h2>
<p> Searches the dialog for the object which has the input focus, returning an index or -1 if the focus is not set. This is useful if you are calling do_dialog() several times in a row and want to leave the focus in the same place it was when the dialog was last displayed, as you can call do_dialog(dlg, find_dialog_focus(dlg)); </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-do_dialog/">do_dialog</a></code>(3), <code><a href="/docs/linux/man/3-init_dialog/">init_dialog</a></code>(3), <code><a href="/docs/linux/man/3-offer_focus/">offer_focus</a></code>(3) </p>
<h2>Index</h2>
