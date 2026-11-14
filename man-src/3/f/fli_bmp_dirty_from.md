---
title: "fli_bmp_dirty_from(3)"
name: "fli_bmp_dirty_from"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fli_bmp_dirty_from/"
description: "fli_bmp_dirty_from, fli_bmp_dirty_to – Indicate which parts of the image have changed. Allegro game programming library."
---

<h2>NAME</h2>
<p> fli_bmp_dirty_from, fli_bmp_dirty_to &#8211; Indicate which parts of the image have changed. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int fli_bmp_dirty_from;</code> </p>
<p> <code>extern int fli_bmp_dirty_to;</code></p>
<h2>DESCRIPTION</h2>
<p> These variables are set by next_fli_frame() to indicate which part of the fli_bitmap has changed since the last call to reset_fli_variables(). If fli_bmp_dirty_from is greater than fli_bmp_dirty_to, the bitmap has not changed, otherwise lines fli_bmp_dirty_from to fli_bmp_dirty_to (inclusive) have altered. You can use these when copying the fli_bitmap onto the screen, to avoid moving data unnecessarily. Example: </p>
<pre><code>
if (fli_bmp_dirty_from &lt;= fli_bmp_dirty_to)
    blit(fli_bitmap, screen, 0, fli_bmp_dirty_from,
         0, fli_bmp_dirty_from, fli_bitmap-&gt;w,
         fli_bmp_dirty_to - fli_bmp_dirty_from + 1);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fli_bitmap/">fli_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-reset_fli_variables/">reset_fli_variables</a></code>(3) </p>
<h2>Index</h2>
