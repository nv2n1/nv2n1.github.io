---
title: "expackf(3)"
name: "expackf"
section: "3"
letter: "e"
url: "/docs/linux/man/3-expackf/"
description: "expackf – Using custom PACKFILE vtables. Allegro game programming library."
---

<h2>NAME</h2>
<p> expackf &#8211; Using custom PACKFILE vtables. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example expackf</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates the use of the packfile functions, with some simple tests. </p>
<p> The first test uses the standard packfile functions to transfer a bitmap file into a block of memory, then reads the bitmap out of the block of memory, using a custom packfile vtable. </p>
<p> The second test reads in a bitmap with another custom packfile vtable, which uses libc&#8217;s file stream functions. </p>
<p> The third test demonstrates seeking with a custom vtable. </p>
<p> The fourth test reads two bitmaps, and dumps them back into a single file, using a custom vtable again. </p>
<p> Tools</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-assert/">ASSERT</a></code>(3), <code><a href="/docs/linux/man/3-bitmap/">BITMAP</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-packfile/">PACKFILE</a></code>(3), <code><a href="/docs/linux/man/3-packfile_vtable/">PACKFILE_VTABLE</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-alert/">alert</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-file_size_ex/">file_size_ex</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-load_bmp_pf/">load_bmp_pf</a></code>(3), <code><a href="/docs/linux/man/3-load_pcx/">load_pcx</a></code>(3), <code><a href="/docs/linux/man/3-load_pcx_pf/">load_pcx_pf</a></code>(3), <code><a href="/docs/linux/man/3-load_tga_pf/">load_tga_pf</a></code>(3), <code><a href="/docs/linux/man/3-pack_fclose/">pack_fclose</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3), <code><a href="/docs/linux/man/3-pack_fread/">pack_fread</a></code>(3), <code><a href="/docs/linux/man/3-pack_fseek/">pack_fseek</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-save_bmp_pf/">save_bmp_pf</a></code>(3), <code><a href="/docs/linux/man/3-save_tga_pf/">save_tga_pf</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-text_height/">text_height</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_centre_ex/">textprintf_centre_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3) </p>
<h2>Index</h2>
