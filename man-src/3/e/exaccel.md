---
title: "exaccel(3)"
name: "exaccel"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exaccel/"
description: "exaccel – Using offscreen video memory to store source graphics for VBE/AF. Allegro game programming library."
---

<h2>NAME</h2>
<p> exaccel &#8211; Using offscreen video memory to store source graphics for VBE/AF. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example exaccel</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates how to use an offscreen part of the video memory to store source graphics for a hardware accelerated graphics driver. The example loads the `mysha.pcx&#8217; file and then blits it several times on the screen. Depending on whether you have enough video memory and Allegro supports the hardware acceleration features of your card, your success running this example may be none at all, sluggish performance due to software emulation, or flicker free smooth hardware accelerated animation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-palette/">PALETTE</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-acquire_bitmap/">acquire_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-release_bitmap/">release_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-replace_filename/">replace_filename</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-show_video_bitmap/">show_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3) </p>
<h2>Index</h2>
