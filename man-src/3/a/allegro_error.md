---
title: "allegro_error(3)"
name: "allegro_error"
section: "3"
letter: "a"
url: "/docs/linux/man/3-allegro_error/"
description: "allegro_error – Stores the last Allegro error message."
---

<h2>NAME</h2>
<p> allegro_error &#8211; Stores the last Allegro error message.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern char allegro_error[ALLEGRO_ERROR_SIZE];</code></p>
<h2>DESCRIPTION</h2>
<p> Text string used by set_gfx_mode(), install_sound() and other functions to report error messages. If they fail and you want to tell the user why, this is the place to look for a description of the problem. Example: </p>
<pre><code>
void abort_on_error(const char *message)
{
    if (screen != NULL)
        set_gfx_mode(GFX_TEXT, 0, 0, 0, 0);

    allegro_message("%s.
Last Allegro error `%s'
",
                    message, allegro_error);
    exit(-1);
}
... if (some_allegro_function() == ERROR_CODE)
    abort_on_error("Error calling some function!");
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3) </p>
<h2>Index</h2>
