---
title: "exexedat(3)"
name: "exexedat"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exexedat/"
description: "exexedat – Appending datafiles onto your executable. Allegro game programming library."
---

<h2>NAME</h2>
<p> exexedat &#8211; Appending datafiles onto your executable. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Example exexedat</code></p>
<h2>DESCRIPTION</h2>
<p> This program demonstrates how to access the contents of an Allegro datafile (created by the grabber utility) linked to the executable by the exedat tool. It is basically the exdata example with minor modifications. </p>
<p> You may ask: how do you compile, append and exec your program? </p>
<p> Answer: like this&#8230; </p>
<p> 1) Compile your program like normal. Use the magic filenames with &#8216;#&#8217; to load your data where needed. </p>
<p> 2) Once you compressed your program, run &quot;exedat foo.exe data.dat&quot; </p>
<p> 3) Finally run your program. </p>
<p> Note that appending data to the end of binaries may not be portable across all platforms supported by Allegro. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-datafile/">DATAFILE</a></code>(3), <code><a href="/docs/linux/man/3-end_of_main/">END_OF_MAIN</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-line/">line</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_palette/">set_palette</a></code>(3), <code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-unload_datafile/">unload_datafile</a></code>(3) </p>
<h2>Index</h2>
