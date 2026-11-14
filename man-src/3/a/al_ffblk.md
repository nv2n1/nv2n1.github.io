---
title: "al_ffblk(3)"
name: "al_ffblk"
section: "3"
letter: "a"
url: "/docs/linux/man/3-al_ffblk/"
description: "al_ffblk – Cross platform structure storing file information. Allegro game programming library."
---

<h2>NAME</h2>
<p> al_ffblk &#8211; Cross platform structure storing file information. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>struct al_ffblk</code></p>
<h2>DESCRIPTION</h2>
<pre><code>
int attrib;
- actual attributes of the file found
    time_t time;
- modification time of file char name[512];
- name of file
</code></pre>
<p> Read the description of al_findfirst for a description on how to obtain/use this structure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-al_findfirst/">al_findfirst</a></code>(3), <code><a href="/docs/linux/man/3-al_ffblk_get_size/">al_ffblk_get_size</a></code>(3) </p>
<h2>Index</h2>
