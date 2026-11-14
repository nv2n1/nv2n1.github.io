---
title: "next_fli_frame(3)"
name: "next_fli_frame"
section: "3"
letter: "n"
url: "/docs/linux/man/3-next_fli_frame/"
description: "next_fli_frame – Reads the next frame of the current animation file. Allegro game programming library."
---

<p>next_fli_frame &#8211; Reads the next frame of the current animation file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int next_fli_frame(int loop);</code></pre>
<h2>Description</h2>
<p>Reads the next frame of the current animation file. If `loop&#8217; is not zero, the player will cycle when it reaches the end of the file, otherwise it will return FLI_EOF. The frame is read into the global variables fli_bitmap and fli_palette. Example: </p>
<pre><code>while (next_fli_frame(0) == FLI_OK) {
    /* Do stuff, like play audio stream
       or check keys to skip animation. */
    /* Rest some time until next frame... */
}</code></pre>
<h2>Return Value</h2>
<p>Returns FLI_OK on success, FLI_ERROR or FLI_NOT_OPEN on error, and FLI_EOF on reaching the end of the file. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-open_fli/">open_fli</a></code>(3), <code><a href="/docs/linux/man/3-fli_bitmap/">fli_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-fli_palette/">fli_palette</a></code>(3), <code><a href="/docs/linux/man/3-fli_timer/">fli_timer</a></code>(3), <code><a href="/docs/linux/man/3-fli_frame/">fli_frame</a></code>(3) </p>
