---
title: "allegro_message(3)"
name: "allegro_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-allegro_message/"
description: "allegro_message – Used mainly to show error messages to users. Allegro game programming library."
---

<h2>NAME</h2>
<p> allegro_message &#8211; Used mainly to show error messages to users. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void allegro_message(const char *text_format, &#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> Outputs a message, using a printf() format string. Usually you want to use this to report messages to the user in an OS independent way when some Allegro subsystem cannot be initialised. But you must not use this function if you are in a graphic mode, only before calling set_gfx_mode(), or after a set_gfx_mode(GFX_TEXT). Also, this function depends on a system driver being installed, which means that it won&#8217;t display the message at all on some platforms if Allegro has not been initialised correctly. </p>
<p> On platforms featuring a windowing system, it will bring up a blocking GUI message box. If there is no windowing system, it will try to print the string to a text console, attempting to work around codepage differences by reducing any accented characters to 7-bit ASCII approximations. Example: </p>
<pre><code>
if (allegro_init() != 0)
    exit(1);

if (init_my_data() != 0) {
    allegro_message("Sorry, missing game data!
");
    exit(2);
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-install_allegro/">install_allegro</a></code>(3), <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3) </p>
<h2>Index</h2>
