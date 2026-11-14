---
title: "get_gfx_mode_list(3)"
name: "get_gfx_mode_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_gfx_mode_list/"
description: "get_gfx_mode_list – Obtains a list of available video modes. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_gfx_mode_list &#8211; Obtains a list of available video modes. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>GFX_MODE_LIST *get_gfx_mode_list(int card);</code></p>
<h2>DESCRIPTION</h2>
<p> Attempts to create a list of all the supported video modes for a certain graphics driver, made up from the GFX_MODE_LIST structure, which has the following definition: </p>
<pre><code>
typedef struct GFX_MODE_LIST {
    int num_modes;
    GFX_MODE *mode;
} GFX_MODE_LIST;
</code></pre>
<p> The mode entry points to the actual list of video modes. </p>
<pre><code>
typedef struct GFX_MODE {
    int width, height, bpp;
} GFX_MODE;
</code></pre>
<p> This list of video modes is terminated with an { 0, 0, 0 } entry. </p>
<p> Note that the card parameter must refer to a _real_ driver. This function fails if you pass GFX_SAFE, GFX_AUTODETECT, or any other &quot;magic&quot; driver.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a list structure of the type GFX_MODE_LIST or NULL if the request could not be satisfied. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-destroy_gfx_mode_list/">destroy_gfx_mode_list</a></code>(3), <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
