---
title: "load_datafile_object(3)"
name: "load_datafile_object"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_datafile_object/"
description: "load_datafile_object – Loads a specific object from a datafile. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_datafile_object &#8211; Loads a specific object from a datafile. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE *load_datafile_object(const char *filename, </code> <code>const char *objectname);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a specific object from a datafile. This won&#8217;t work if you strip the object names from the file, and it will be very slow if you save the file with global compression. Example: </p>
<pre><code>
/* Load only the music from the datafile. */
music_object = load_datafile_object("datafile.dat",
                                    "MUSIC");
/* Play it and wait a moment for it. */
play_midi(music_object-&gt;dat);
...
    /* Destroy unneeded music. */
    unload_datafile_object(music_object);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a single DATAFILE element whose `dat&#8217; member points to the object, or NULL if there was an error or there was no object with the requested name. Remember to free this DATAFILE later to avoid memory leaks, but use the correct unloading function! </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-unload_datafile_object/">unload_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-find_datafile_object/">find_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-register_datafile_object/">register_datafile_object</a></code>(3) </p>
<h2>Index</h2>
