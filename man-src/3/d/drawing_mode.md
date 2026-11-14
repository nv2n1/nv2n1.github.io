---
title: "drawing_mode(3)"
name: "drawing_mode"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drawing_mode/"
description: "drawing_mode – Sets the graphics drawing mode. Allegro game programming library."
---

<h2>NAME</h2>
<p> drawing_mode &#8211; Sets the graphics drawing mode. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void drawing_mode(int mode, BITMAP *pattern, int x_anchor, int y_anchor);</code></p>
<h2>DESCRIPTION</h2>
<p> Sets the graphics drawing mode. This only affects the geometric routines like putpixel, lines, rectangles, circles, polygons, floodfill, etc, not the text output, blitting, or sprite drawing functions. The mode should be one of the following constants: </p>
<pre>
   DRAW_MODE_SOLID               - the default, solid color
                                   drawing
   DRAW_MODE_XOR                 - exclusive-or drawing
   DRAW_MODE_COPY_PATTERN        - multicolored pattern fill
   DRAW_MODE_SOLID_PATTERN       - single color pattern fill
   DRAW_MODE_MASKED_PATTERN      - masked pattern fill
   DRAW_MODE_TRANS               - translucent color blending
   
</pre>
<p> In DRAW_MODE_SOLID, pixels of the bitmap being drawn onto are simply replaced by those produced by the drawing function. </p>
<p> In DRAW_MODE_XOR, pixels are written to the bitmap with an exclusive-or operation rather than a simple copy, so drawing the same shape twice will erase it. Because it involves reading as well as writing the bitmap memory, xor drawing is a lot slower than the normal replace mode. </p>
<p> With the patterned modes, you provide a pattern bitmap which is tiled across the surface of the shape. Allegro stores a pointer to this bitmap rather than copying it, so you must not destroy the bitmap while it is still selected as the pattern. The width and height of the pattern must be powers of two, but they can be different, eg. a 64&#215;16 pattern is fine, but a 17&#215;3 one is not. The pattern is tiled in a grid starting at point (x_anchor, y_anchor). Normally you should just pass zero for these values, which lets you draw several adjacent shapes and have the patterns meet up exactly along the shared edges. Zero alignment may look peculiar if you are moving a patterned shape around the screen, however, because the shape will move but the pattern alignment will not, so in some situations you may wish to alter the anchor position. </p>
<p> When you select DRAW_MODE_COPY_PATTERN, pixels are simply copied from the pattern bitmap onto the destination bitmap. This allows the use of multicolored patterns, and means that the color you pass to the drawing routine is ignored. This is the fastest of the patterned modes. </p>
<p> In DRAW_MODE_SOLID_PATTERN, each pixel in the pattern bitmap is compared with the mask color, which is zero in 256-color modes or bright pink for truecolor data (maximum red and blue, zero green). If the pattern pixel is solid, a pixel of the color you passed to the drawing routine is written to the destination bitmap, otherwise a zero is written. The pattern is thus treated as a monochrome bitmask, which lets you use the same pattern to draw different shapes in different colors, but prevents the use of multicolored patterns. </p>
<p> DRAW_MODE_MASKED_PATTERN is almost the same as DRAW_MODE_SOLID_PATTERN, but the masked pixels are skipped rather than being written as zeros, so the background shows through the gaps. </p>
<p> In DRAW_MODE_TRANS, the global color_map table or truecolor blender functions are used to overlay pixels on top of the existing image. This must only be used after you have set up the color mapping table (for 256 color modes) or blender functions (for truecolor modes). Because it involves reading as well as writing the bitmap memory, translucent drawing is very slow if you draw directly to video RAM, so wherever possible you should use a memory bitmap instead. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-xor_mode/">xor_mode</a></code>(3), <code><a href="/docs/linux/man/3-solid_mode/">solid_mode</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
<h2>Index</h2>
