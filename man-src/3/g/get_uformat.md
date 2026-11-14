---
title: "get_uformat(3)"
name: "get_uformat"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_uformat/"
description: "get_uformat – Finds out what text encoding format is currently selected. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_uformat &#8211; Finds out what text encoding format is currently selected. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_uformat(void);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds out what text encoding format is currently selected. This function is probably useful only if you are writing an Allegro addon dealing with text strings and you use a different codepath for each possible format. Example: </p>
<pre><code>
switch (get_uformat()) {
case U_ASCII:
    do_something();
    break;
case U_UTF8:
    do_something_else();
    break;
    ...
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the currently selected text encoding format. See the documentation of set_uformat() for a list of encoding formats. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3) </p>
<h2>Index</h2>
