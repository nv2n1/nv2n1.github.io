---
title: "ex3buf(3)"
name: "ex3buf"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ex3buf/"
description: "ex3buf – Mode-X triple buffering and retrace interrupt simulation. Allegro game programming library."
---

<h2>NAME</h2>
<p> ex3buf &#8211; Mode-X triple buffering and retrace interrupt simulation. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example ex3buf</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates the use of triple buffering. Several triangles are displayed rotating and bouncing on the screen until you press a key. Note that on some platforms you can&#8217;t get real hardware triple buffering. The Allegro code remains the same, but most likely the graphic driver will emulate it. Unfortunately, in these cases you can&#8217;t expect the animation to be completely smooth and flicker free. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-acquire_bitmap/">acquire_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-desktop_palette/">desktop_palette</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-enable_triple_buffer/">enable_triple_buffer</a></code>(3), <code><a href="/docs/linux/man/3-fixcos/">fixcos</a></code>(3), <code><a href="/docs/linux/man/3-fixed/">fixed</a></code>(3), <code><a href="/docs/linux/man/3-fixmul/">fixmul</a></code>(3), <code><a href="/docs/linux/man/3-fixsin/">fixsin</a></code>(3), <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-itofix/">itofix</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-poll_scroll/">poll_scroll</a></code>(3), <code><a href="/docs/linux/man/3-release_bitmap/">release_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-request_video_bitmap/">request_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-triangle/">triangle</a></code>(3), <code><a href="/docs/linux/man/3-ustrzcpy/">ustrzcpy</a></code>(3) </p>
<h2>Index</h2>
