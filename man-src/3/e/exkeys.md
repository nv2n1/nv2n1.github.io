---
title: "exkeys(3)"
name: "exkeys"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exkeys/"
description: "exkeys – How to get input from the keyboard in different ways. Allegro game programming library."
---

<h2>NAME</h2>
<p> exkeys &#8211; How to get input from the keyboard in different ways. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example exkeys</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates how to access the keyboard. The first part shows the basic use of readkey(). The second part shows how to extract the ASCII value. Next come the scan codes. The fourth test detects modifier keys like alt or shift. The fifth test requires some focus to be passed. The final step shows how to use the global key array to read simultaneous key presses. The last method to detect key presses are keyboard callbacks. This is demonstrated by by installing a keyboard callback, which marks all pressed keys by drawing to a grid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-end_of_function/">END_OF_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-lock_function/">LOCK_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-acquire_screen/">acquire_screen</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3), <code><a href="/docs/linux/man/3-desktop_palette/">desktop_palette</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-key_shifts/">key_shifts</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_lowlevel_callback/">keyboard_lowlevel_callback</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-rectfill/">rectfill</a></code>(3), <code><a href="/docs/linux/man/3-release_screen/">release_screen</a></code>(3), <code><a href="/docs/linux/man/3-rest/">rest</a></code>(3), <code><a href="/docs/linux/man/3-scancode_to_name/">scancode_to_name</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_centre_ex/">textprintf_centre_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-usprintf/">usprintf</a></code>(3), <code><a href="/docs/linux/man/3-ustrzncpy/">ustrzncpy</a></code>(3) </p>
<h2>Index</h2>
