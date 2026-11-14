---
title: "gstream-set_tab(3)"
name: "gstream-set_tab"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_tab/"
description: "set_tab"
---

<h2>NAME</h2>
<p> set_tab</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_tab(int x, int color, FONT fnt);</code></p>
<h2>DESCRIPTION</h2>
<p> This is the basic function &#8211; it creates a tab stop at the specified x-coordinate with the specified colour and the specified font. But the function is overloaded so it is possible only to set a tab stop without changing the font or the font colour, or just changing the colour or just changing the font: set_tab(int x), set_tab(int x, int color) and set_tab(int x, FONT fnt) respectively. </p>
<p> A few examples are granted: </p>
<pre><code>
set_tab(130);
// set a tab stop at the x-position 130, don't change colour or font

set_tab(400);
// set a tab stop at 400, don't change colour or font

set_tab(80, 24);
// set a stop at 80 and let it change the colour to 24, no font change

set_tab(190, 57, my_arial_font);
// set tab stop at 190, change colour to 57 and font to 'my_arial_font'

set_tab(250, courier);
// set tab stop at 250, don't change colour, but change font to 'courier'
</code></pre>
<p> The first version of gstream didn&#8217;t have these overloaded functions, but used a more clumsy syntax (involving a constant) which is now deprecated. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-remove_tab/">gstream-remove_tab</a></code>(3), <code><a href="/docs/linux/man/3-gstream-remove_all_tabs/">gstream-remove_all_tabs</a></code>(3), <code><a href="/docs/linux/man/3-gstream-restore/">gstream-restore</a></code>(3) </p>
<h2>Index</h2>
