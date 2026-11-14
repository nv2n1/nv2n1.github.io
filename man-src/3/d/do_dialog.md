---
title: "do_dialog(3)"
name: "do_dialog"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_dialog/"
description: "do_dialog – Basic dialog manager function. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_dialog &#8211; Basic dialog manager function. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int do_dialog(DIALOG *dialog, int focus_obj);</code></p>
<h2>DESCRIPTION</h2>
<p> The basic dialog manager function. This displays a dialog (an array of dialog objects, terminated by one with a NULL dialog procedure), and sets the input focus to the focus_obj (-1 if you don&#8217;t want anything to have the focus). It interprets user input and dispatches messages as they are required, until one of the dialog procedures tells it to close the dialog, at which point it returns the index of the object that caused it to exit, or until ESC is pressed, at which point it returns -1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-popup_dialog/">popup_dialog</a></code>(3), <code><a href="/docs/linux/man/3-init_dialog/">init_dialog</a></code>(3), <code><a href="/docs/linux/man/3-centre_dialog/">centre_dialog</a></code>(3), <code><a href="/docs/linux/man/3-set_dialog_color/">set_dialog_color</a></code>(3), <code><a href="/docs/linux/man/3-find_dialog_focus/">find_dialog_focus</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
