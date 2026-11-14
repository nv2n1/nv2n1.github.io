---
title: "fli_pal_dirty_from(3)"
name: "fli_pal_dirty_from"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fli_pal_dirty_from/"
description: "fli_pal_dirty_from, fli_pal_dirty_to – Indicate which parts of the palette have changed. Allegro game programming library."
---

<h2>NAME</h2>
<p> fli_pal_dirty_from, fli_pal_dirty_to &#8211; Indicate which parts of the palette have changed. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int fli_pal_dirty_from;</code> </p>
<p> <code>extern int fli_pal_dirty_to;</code></p>
<h2>DESCRIPTION</h2>
<p> These variables are set by next_fli_frame() to indicate which part of the fli_palette has changed since the last call to reset_fli_variables(). If fli_pal_dirty_from is greater than fli_pal_dirty_to, the palette has not changed, otherwise colors fli_pal_dirty_from to fli_pal_dirty_to (inclusive) have altered. You can use these when updating the hardware palette, to avoid unnecessary calls to set_palette(). Example: </p>
<pre><code>
if (fli_pal_dirty_from &lt;= fli_pal_dirty_to)
    set_palette_range(fli_palette, fli_pal_dirty_from,
                      fli_pal_dirty_to, 1);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fli_palette/">fli_palette</a></code>(3), <code><a href="/docs/linux/man/3-reset_fli_variables/">reset_fli_variables</a></code>(3) </p>
<h2>Index</h2>
