---

title: "exrgbhsv(3)"
name: "exrgbhsv"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exrgbhsv/"
description: "exrgbhsv – RGB <-> HSV color space conversions. Allegro game programming library."
---

<p> exrgbhsv &#8211; RGB &lt;-&gt; HSV color space conversions. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example exrgbhsv</code></p>
<h2>DESCRIPTION</h2>
<p> This program shows how to convert colors between the different color-space representations. The central area of the screen will display the current color. On the top left corner of the screen, three sliders allow you to modify the red, green and blue value of the color. On the bottom right corner of the screen, three sliders allow you to modify the hue, saturation and value of the color. The color bars beneath the sliders show what the resulting color will look like when the slider is dragged to that position. </p>
<p> Additionally this example also shows how to &quot;inherit&quot; the behaviour of a GUI object and extend it, here used to create the sliders. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-dialog/">DIALOG</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code>PALETTE</code>(3), <code><a href="/docs/linux/man/3-rgb/">RGB</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">RGB_MAP</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code>allegro_init</code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code>clear_to_color</code>(3), <code><a href="/docs/linux/man/3-create_bitmap_ex/">create_bitmap_ex</a></code>(3), <code><a href="/docs/linux/man/3-create_rgb_table/">create_rgb_table</a></code>(3), <code>d_bitmap_proc</code>(3), <code>d_box_proc</code>(3), <code><a href="/docs/linux/man/3-d_slider_proc/">d_slider_proc</a></code>(3), <code><a href="/docs/linux/man/3-d_text_proc/">d_text_proc</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-do_dialog/">do_dialog</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-generate_332_palette/">generate_332_palette</a></code>(3), <code><a href="/docs/linux/man/3-get_color_depth/">get_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-hsv_to_rgb/">hsv_to_rgb</a></code>(3), <code>install_keyboard</code>(3), <code>install_mouse</code>(3), <code>install_timer</code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-makecol32/">makecol32</a></code>(3), <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3), <code><a href="/docs/linux/man/3-object_message/">object_message</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-rgb_to_hsv/">rgb_to_hsv</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_color/">set_color</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-vline/">vline</a></code>(3), <code><a href="/docs/linux/man/3-vsync/">vsync</a></code>(3) </p>
