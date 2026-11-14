---
title: "play_fli(3)"
name: "play_fli"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_fli/"
description: "play_fli – Plays a FLI or FLC animation from disk. Allegro game programming library."
---

<p>play_fli &#8211; Plays a FLI or FLC animation from disk. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int play_fli(const char *filename, BITMAP *bmp, int loop, int (*callback)());</code></pre>
<h2>Description</h2>
<p>Plays an Autodesk Animator FLI or FLC animation file on the specified BITMAP, reading the data from disk as it is required. If `loop&#8217; is not zero, the player will cycle when it reaches the end of the file, otherwise it will play through the animation once and then return. Read the beginning of chapter &quot;FLIC routines&quot; for a description of the callback parameter. Example: </p>
<pre><code>/* Let users skip looped animations. */
int check_escape_key(void)
{
    if (key[KEY_ESC])
        return 1;
    else
        return 0;
}
... int ret = play_fli(&quot;animlogo.fli&quot;, screen, 1,
                       check_escape_key);
if (ret == FLI_ERROR)
    abort_on_error(&quot;Error playing intro!&quot;);</code></pre>
<h2>Return Value</h2>
<p>The FLI player returns FLI_OK if it reached the end of the file, FLI_ERROR if something went wrong, and the value returned by the callback function if that was what stopped it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-play_memory_fli/">play_memory_fli</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-fli_frame/">fli_frame</a></code>(3) </p>
