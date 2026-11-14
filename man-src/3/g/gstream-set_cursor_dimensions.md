---
title: "gstream-set_cursor_dimensions(3)"
name: "gstream-set_cursor_dimensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_cursor_dimensions/"
description: "set_cursor_dimensions"
---

<h2>NAME</h2>
<p> set_cursor_dimensions</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_cursor_dimensions(int iw, int ih, int ow, int oh);</code></p>
<h2>DESCRIPTION</h2>
<p> This will set the cursor dimensions to IW x IH when in insert mode and OW x OH when in overwrite mode. Although the standard cursors respond to this, it is mostly intended to be used with custom cursor drawers. </p>
<p> Before requesting any inputs with your custom cursor drawer, you should call this function with the appropriate values. To set the size of the character underneath the cursor dynamically, pass gbuf::DYNAMIC_CURSOR_SIZE: if the cursor is at the end of the line, it will get the width of a space &#8216; &#8216;, else it will get the size of the character under it. </p>
<p> Say that we have created a nice cursor drawer that for the insert cursor is one pixel wide and as tall as the characters (in other words: a vertical line), but for the overwrite cursor is a BITMAP with the dimensions 8&#215;10. Then the following would do: </p>
<pre>
   gs.set_cursor_dimensions(1, gbuf::DYNAMIC_CURSOR_SIZE, 8, 10);
   
</pre>
<p> It is important that you remember to call this function when you are using custom cursor drawers &#8211; else the inputter doesn&#8217;t know how much of the background below the cursor to save and recover. </p>
<p> The default dimensions are the dimensions that are suited for the default cursor. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-get_cursor_w/">gstream-get_cursor_w</a></code>(3), <code><a href="/docs/linux/man/3-gstream-get_cursor_h/">gstream-get_cursor_h</a></code>(3), <code><a href="/docs/linux/man/3-gstream-set_cursor_drawer/">gstream-set_cursor_drawer</a></code>(3) </p>
<h2>Index</h2>
