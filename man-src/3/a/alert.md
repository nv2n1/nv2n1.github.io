---
title: "alert(3)"
name: "alert"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alert/"
description: "alert – Displays a popup alert box. Allegro game programming library."
---

<h2>NAME</h2>
<p> alert &#8211; Displays a popup alert box. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int alert(const char *s1, *s2, *s3, const char *b1, *b2, int c1, c2);</code></p>
<h2>DESCRIPTION</h2>
<p> Displays a popup alert box, containing three lines of text (s1-s3), and with either one or two buttons. The text for these buttons is passed in `b1&#8242; and `b2&#8242; (`b2&#8242; may be NULL), and the keyboard shortcuts in `c1&#8242; and `c2&#8242; as ASCII value. Example: </p>
<pre><code>
if (!exists(CONFIG_FILE))
    alert(CONFIG_FILE, "not found.", "Using defaults.",
          "&amp;Continue", NULL, 'c', 0);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns 1 or 2 depending on which button was clicked. If the alert is dismissed by pressing ESC when ESC is not one of the keyboard shortcuts, it treats it as a click on the second button (this is consistent with the common &quot;Ok&quot;, &quot;Cancel&quot; alert). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-alert3/">alert3</a></code>(3), <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3) </p>
<h2>Index</h2>
