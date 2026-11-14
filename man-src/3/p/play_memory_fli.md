---
title: "play_memory_fli(3)"
name: "play_memory_fli"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_memory_fli/"
description: "play_memory_fli – Plays a FLI or FLC animation from memory. Allegro game programming library."
---

<p>play_memory_fli &#8211; Plays a FLI or FLC animation from memory. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int play_memory_fli(const void *fli_data, BITMAP *bmp, int loop,

                    int (*callback)());</code></pre>
<h2>Description</h2>
<p>Plays an Autodesk Animator FLI or FLC animation on the specified BITMAP, reading the data from a copy of the file which is held in memory. You can obtain the `fli_data&#8217; pointer by allocating a block of memory and reading an FLI file into it, or by importing an FLI into a grabber datafile. If `loop&#8217; is not zero, the player will cycle when it reaches the end of the file, otherwise it will play through the animation once and then return. Read the beginning of chapter &quot;FLIC routines&quot; for a description of the callback parameter. Playing animations from memory is obviously faster than cuing them directly from disk, and is particularly useful with short, looped FLI&#8217;s. Animations can easily get very large, though, so in most cases you will probably be better just using play_fli(). You can think of this function as a wrapper on top of open_memory_fli(), next_fli_frame() and close_fli(). Example: </p>
<pre><code>int ret = play_memory_fli(anim_data, screen, 0, NULL);
if (ret == FLI_ERROR)
    abort_on_error(&quot;Corrupted animation data?&quot;);</code></pre>
<h2>Return Value</h2>
<p>The FLI player returns FLI_OK if it reached the end of the file, FLI_ERROR if something went wrong, and the value returned by the callback function if that was what stopped it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-play_fli/">play_fli</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-fli_frame/">fli_frame</a></code>(3) </p>
