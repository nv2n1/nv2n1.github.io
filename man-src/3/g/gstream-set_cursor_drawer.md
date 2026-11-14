---
title: "gstream-set_cursor_drawer(3)"
name: "gstream-set_cursor_drawer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_cursor_drawer/"
description: "set_cursor_drawer"
---

<h2>NAME</h2>
<p> set_cursor_drawer</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_cursor_drawer(void (*cd)(BITMAP *, int, int, int, int, int, bool));</code></p>
<h2>DESCRIPTION</h2>
<p> This will set the function for drawing the cursor, which is useful if you want to customize it with your own favourite cursor (perhaps a BITMAP). Before you can actually use the cursor for inputting, you also have to call set_cursor_dimensions with the width and height of your cursor, in both insert and overwrite mode. </p>
<p> The parameters of the drawer function are: destination bitmap (the BITMAP you draw on); x-coordinate; y-coordinate; the width (if you passed gbuf::DYNAMIC_CURSOR_SIZE it is the width of the character under the cursor, else it is the width you specified); the height (ditto); the colour of the font (watch out for a -1!); whether in insert mode (true if so). </p>
<p> A simple example of a standard console cursor: </p>
<pre><code>
void cd_cons(BITMAP *bmp, int x, int y, int w, int h, int c, bool ins)
{
    int colour;

    // determine colour (defaults to black if no colour specified)
    if (c == -1)
        colour = makecol_depth(bitmap_color_depth(bmp), 0, 0, 0);
    else
        colour = c;

    if (ins) // if it is the insert cursor
        rectfill(bmp, x, y + h - 2, x + w - 1, y + h - 1, colour);
    else // else overwrite cursor
        rectfill(bmp, x, y, x + w - 1, y + h - 1, colour);
}
</code></pre>
<p> You don&#8217;t have to think about flashing the cursor or other pecularities &#8211; the gstream will take care of that, all you have to do is to construct a function that draws something on the specified BITMAP, at the specified position, not exceeding the specified width and height. You are of course free to ignore the color and the insert parameter, just make sure that you don&#8217;t draw outside the given rectangle, or else the gstream can&#8217;t recover the background and the result will be artifacts. </p>
<p> A typedef, &#8216;cursor_drawer&#8217;, in &#8216;gbuf&#8217; makes it easy to declare pointers to this type of functions: </p>
<pre><code>
gbuf::cursor_drawer tmp_cd;

//...

tmp_cd = gs1.get_cursor_drawer();
gs1.set_cursor_drawer(gs2.get_cursor_drawer());
gs2.set_cursor_drawer(tmp_cd);
</code></pre>
<p> The default cursor drawer is &#8216;cd_winconsole&#8217;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-set_cursor_dimensions/">gstream-set_cursor_dimensions</a></code>(3), <code><a href="/docs/linux/man/3-gstream-get_cursor_drawer/">gstream-get_cursor_drawer</a></code>(3), <code><a href="/docs/linux/man/3-gstream-cd_winconsole/">gstream-cd_winconsole</a></code>(3) </p>
<h2>Index</h2>
