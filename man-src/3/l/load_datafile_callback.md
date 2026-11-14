---
title: "load_datafile_callback(3)"
name: "load_datafile_callback"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_datafile_callback/"
description: "load_datafile_callback – Loads a datafile into memory, calling a hook per object. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_datafile_callback &#8211; Loads a datafile into memory, calling a hook per object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE *load_datafile_callback(const char *filename,</code> <code>void (*callback)(DATAFILE *d));</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a datafile into memory, calling the specified hook function once for each object in the file, passing it a pointer to the object just read. You can use this to implement very simple loading screens where every time the hook is called, the screen is updated to let the user know your program is still loading from disk: </p>
<pre><code>
void load_callback(DATAFILE *dat_obj)
{
    static const char indicator[] = "-\|/-.oOXOo.";
    static int current = 0;

    /* Show a different character every time. */
    textprintf_ex(screen, font, 0, 0, makecol(0, 0, 0),
                  makecol(255, 255, 255), "%c Loading %c",
                  indicator[current], indicator[current]);
    /* Increase index and check if we need to reset it. */
    current++;
    if (!indicator[current])
        current = 0;
}
... dat = load_datafile_callback("data.dat", load_callback);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the DATAFILE or NULL on error. Remember to free this DATAFILE later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-unload_datafile/">unload_datafile</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3), <code><a href="/docs/linux/man/3-fixup_datafile/">fixup_datafile</a></code>(3), <code><a href="/docs/linux/man/3-packfile_password/">packfile_password</a></code>(3), <code><a href="/docs/linux/man/3-find_datafile_object/">find_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-register_datafile_object/">register_datafile_object</a></code>(3) </p>
<h2>Index</h2>
