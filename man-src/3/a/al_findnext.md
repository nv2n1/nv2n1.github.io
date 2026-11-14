---
title: "al_findnext(3)"
name: "al_findnext"
section: "3"
letter: "a"
url: "/docs/linux/man/3-al_findnext/"
description: "al_findnext – Finds the next file in a search started by al_findfirst(). Allegro game programming library."
---

<h2>NAME</h2>
<p> al_findnext &#8211; Finds the next file in a search started by al_findfirst(). Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int al_findnext(struct al_ffblk *info);</code></p>
<h2>DESCRIPTION</h2>
<p> This finds the next file in a search started by al_findfirst(). Example: </p>
<pre><code>
if (al_findfirst("*.pcx", &amp;info, 0) != 0)
    return;

do {
    /* Do something useful here with info.name. */
} while (al_findnext(&amp;info) == 0);

al_findclose(&amp;info);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns zero if a match is found, non-zero if none is found or if an error occurred and, in the latter case, sets errno accordingly. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-al_findfirst/">al_findfirst</a></code>(3), <code><a href="/docs/linux/man/3-al_findclose/">al_findclose</a></code>(3) </p>
<h2>Index</h2>
