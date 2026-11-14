---
title: "make_trans_font(3)"
name: "make_trans_font"
section: "3"
letter: "m"
url: "/docs/linux/man/3-make_trans_font/"
description: "make_trans_font – Makes a font use transparency. Allegro game programming library."
---

<h2>NAME</h2>
<p> make_trans_font &#8211; Makes a font use transparency. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void make_trans_font(FONT *f);</code></p>
<h2>DESCRIPTION</h2>
<p> This function converts a font to use transparency for drawing. That is, each glyph in the font will be drawn with draw_trans_sprite, so you can use the same blenders as with draw_trans_sprite to draw the font. One common use of this is to load a bitmap font with an alpha channel, and therefore get anti-aliased text output by using Allegro&#8217;s alpha blender. Here&#8217;s an example how to do that: </p>
<pre><code>
FONT *f = load_font("alphafont.tga", NULL, NULL);
make_trans_font(f);
set_alpha_blender();
textprintf_centre_ex(screen, f, 320, 240, -1, -1, "Anti-aliased Font!");
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-is_trans_font/">is_trans_font</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3) </p>
<h2>Index</h2>
