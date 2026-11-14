---
title: "for_each_file_ex(3)"
name: "for_each_file_ex"
section: "3"
letter: "f"
url: "/docs/linux/man/3-for_each_file_ex/"
description: "for_each_file_ex – Executes callback() for each file matching a wildcard. Allegro game programming library."
---

<h2>NAME</h2>
<p> for_each_file_ex &#8211; Executes callback() for each file matching a wildcard. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int for_each_file_ex(const char *name, int in_attrib, int out_attrib,</code> <code>int (*callback)(const char *filename, int attrib,</code> <code>void *param), void *param);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds all the files on disk which match the given wildcard specification and file attributes, and executes callback() once for each. Basically, this is a convenient wrapper around al_findfirst(), al_findnext() and al_findclose(). `in_attrib&#8217; is a bitmask specifying the attributes the files must carry, `out_attrib&#8217; is a bitmask specifying the attributes the files must not carry; attributes which are not specified in either bitmasks are not taken into account for deciding whether callback() is invoked or not. </p>
<p> The callback function will be passed three arguments: the first is a string which contains the completed filename (exactly the same string you passed to for_each_file_ex() but with meta characters), the second is the actual attributes of the file, and the third is a void pointer which is simply a copy of `param&#8217; (you can use this for whatever you like). The callback must return zero to let the enumeration proceed, or any non-zero value to stop it. If an error occurs, the error code will be stored in `errno&#8217; but the enumeration won&#8217;t stop. Example: </p>
<pre><code>
int show_name(const char *filename, int attrib, void *param)
{
    allegro_message("Caught `%s', attribs %d
",
                    filename, attrib);
    return 0;
}
... count = for_each_file_ex("data/level*", FA_DIREC,
                             0, show_name, 0);
allegro_message("%d game directories
", count);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the number of successful calls made to callback(), that is, the number of times callback() was called and returned 0. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-al_findfirst/">al_findfirst</a></code>(3), <code><a href="/docs/linux/man/3-al_findnext/">al_findnext</a></code>(3), <code><a href="/docs/linux/man/3-al_findclose/">al_findclose</a></code>(3) </p>
<h2>Index</h2>
