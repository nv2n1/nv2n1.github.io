---
title: "sdl_createcursor(3)"
name: "sdl_createcursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createcursor/"
description: "SDL_CreateCursor – Creates a new mouse cursor."
---

<p>SDL_CreateCursor &#8211; Creates a new mouse cursor.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Cursor *SDL_CreateCursor</code>(<code>Uint8 *data, Uint8 *mask, int w, int h, int hot_x, int hot_y</code>);</p>
<h2>Description</h2>
<p>Create a cursor using the specified <code>data</code> and <code>mask</code> (in MSB format). The cursor width must be a multiple of 8 bits. </p>
<p> The cursor is created in black and white according to the following:</p>
<dl COMPACT>
<dt><code>Data / Mask</code></p>
<dd><code>Resulting pixel on screen</code></p>
<dt>0 / 1</p>
<dd>White</p>
<dt>1 / 1</p>
<dd>Black</p>
<dt>0 / 0</p>
<dd>Transparent</p>
<dt>1 / 0</p>
<dd>Inverted color if possible, black if not.</dl>
<p> Cursors created with this function must be freed with <i>SDL_FreeCursor</i>.</p>
<h2>Example</h2>
<pre><tt>/* Stolen from the mailing list */
/* Creates a new mouse cursor from an XPM */
/* XPM */
static const char *arrow[] = {
 /* width height num_colors chars_per_pixel */
 &quot; 32 32 3 1&quot;,
 /* colors */
 &quot;X c #000000&quot;,
 &quot;. c #ffffff&quot;,
 &quot; c None&quot;,
 /* pixels */
 &quot;X &quot;,
 &quot;XX &quot;,
 &quot;X.X &quot;,
 &quot;X..X &quot;,
 &quot;X...X &quot;,
 &quot;X....X &quot;,
 &quot;X.....X &quot;,
 &quot;X......X &quot;,
 &quot;X.......X &quot;,
 &quot;X........X &quot;,
 &quot;X.....XXXXX &quot;,
 &quot;X..X..X &quot;,
 &quot;X.X X..X &quot;,
 &quot;XX X..X &quot;,
 &quot;X X..X &quot;,
 &quot; X..X &quot;,
 &quot; X..X &quot;,
 &quot; X..X &quot;,
 &quot; XX &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot; &quot;,
 &quot;0,0&quot;
};
static SDL_Cursor *init_system_cursor(const char *image[])
{
 int i, row, col;
 Uint8 data[4*32];
 Uint8 mask[4*32];
 int hot_x, hot_y;
 i = -1;
 for ( row=0; row&lt;32; ++row ) {
 for ( col=0; col&lt;32; ++col ) {
 if ( col % 8 ) {
 data[i] &lt;&lt;= 1;
 mask[i] &lt;&lt;= 1;
 } else {
 ++i;
 data[i] = mask[i] = 0;
 }
 switch (image[4+row][col]) {
 case 'X':
 data[i] |= 0x01;
 k[i] |= 0x01;
 break;
 case '.':
 mask[i] |= 0x01;
 break;
 case ' ':
 break;
 }
 }
 }
 sscanf(image[4+row], &quot;%d,%d&quot;, &amp;hot_x, &amp;hot_y);
 return SDL_CreateCursor(data, mask, 32, 32, hot_x, hot_y);
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_FreeCursor</code>, <i></i><code>SDL_SetCursor</code>, <i></i><code>SDL_ShowCursor</code></p>
