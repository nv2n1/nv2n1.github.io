---
title: "load_datafile(3)"
name: "load_datafile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_datafile/"
description: "load_datafile – Loads a datafile into memory. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_datafile &#8211; Loads a datafile into memory. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE *load_datafile(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a datafile into memory in one go. If the datafile has been encrypted, you must first call packfile_password() to set the appropriate key. If the datafile contains truecolor graphics, you must set the video mode or call set_color_conversion() before loading it. Example: </p>
<pre><code>
/* Load the resources for our game. */
DATAFILE *dat = load_datafile("game.dat");
if (!dat)
    abort_on_error("Couldn't load sound resources!");
/* Use resources. */
...
    /* Destroy them when we don't need them any more. */
    unload_datafile(dat);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the DATAFILE, or NULL on error. Remember to free this DATAFILE later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_datafile_callback/">load_datafile_callback</a></code>(3), <code><a href="/docs/linux/man/3-unload_datafile/">unload_datafile</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-fixup_datafile/">fixup_datafile</a></code>(3), <code><a href="/docs/linux/man/3-packfile_password/">packfile_password</a></code>(3), <code><a href="/docs/linux/man/3-find_datafile_object/">find_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-register_datafile_object/">register_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exdata/">exdata</a></code>(3), <code><a href="/docs/linux/man/3-exexedat/">exexedat</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3) </p>
<h2>Index</h2>
