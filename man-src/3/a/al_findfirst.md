---
title: "al_findfirst(3)"
name: "al_findfirst"
section: "3"
letter: "a"
url: "/docs/linux/man/3-al_findfirst/"
description: "al_findfirst – Low-level function for searching files. Allegro game programming library."
---

<h2>NAME</h2>
<p> al_findfirst &#8211; Low-level function for searching files. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int al_findfirst(const char *pattern, struct al_ffblk *info, int attrib);</code></p>
<h2>DESCRIPTION</h2>
<p> Low-level function for searching files. This function finds the first file which matches the given wildcard specification and file attributes (see above). The information about the file (if any) will be put in the al_ffblk structure which you have to provide. The al_ffblk structure looks like: </p>
<pre><code>
struct al_ffblk {
    int attrib;
    - actual attributes of the file found
        time_t time;
    - modification time of file char name[512];
    - name of file
};
</code></pre>
<p> There is some other stuff in the structure as well, but it is there for internal use only. Example: </p>
<pre><code>
struct al_ffblk info;

if (al_findfirst("*.pcx", &amp;info, FA_ALL) != 0) {
    /* Tell user there are no PCX files. */
    return;
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> The function returns non-zero if no match is found or if an error occurred and, in the latter case, sets `errno&#8217; accordingly. It returns zero if a match is found, allocating some memory for internal use in the structure. Therefore you have to close your search when you are finished to avoid memory leaks in your program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-al_findnext/">al_findnext</a></code>(3), <code><a href="/docs/linux/man/3-al_findclose/">al_findclose</a></code>(3), <code><a href="/docs/linux/man/3-al_ffblk_get_size/">al_ffblk_get_size</a></code>(3) </p>
<h2>Index</h2>
