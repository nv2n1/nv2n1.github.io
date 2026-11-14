---
title: "excolmap(3)"
name: "excolmap"
section: "3"
letter: "e"
url: "/docs/linux/man/3-excolmap/"
description: "excolmap – Creating graphical effects with color mapping tables. Allegro game programming library."
---

<h2>NAME</h2>
<p> excolmap &#8211; Creating graphical effects with color mapping tables. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example excolmap</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates how to create custom graphic effects with the create_color_table function. Allegro drawing routines are affected by any color table you might have set up. In the first part of this example, a greyscale color table is set. The result is that a simple rectfill call, instead of drawing a rectangle with color zero, uses the already drawn pixels to determine the pixel to be drawn (read the comment of return_grey_color() for a precise description of the algorithm). In the second part of the test, the color table is changed to be an inverse table, meaning that any pixel drawn will be shown as its color values had been inverted. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">COLOR_MAP</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-palette/">PALETTE</a></code>(3), <code><a href="/docs/linux/man/3-rgb/">RGB</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">RGB_MAP</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-circlefill/">circlefill</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-create_rgb_table/">create_rgb_table</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-generate_332_palette/">generate_332_palette</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-rectfill/">rectfill</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textout_centre_ex/">textout_centre_ex</a></code>(3), <code><a href="/docs/linux/man/3-vsync/">vsync</a></code>(3) </p>
<h2>Index</h2>
