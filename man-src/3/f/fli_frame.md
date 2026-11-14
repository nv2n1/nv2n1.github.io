---
title: "fli_frame(3)"
name: "fli_frame"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fli_frame/"
description: "fli_frame – Stores the current frame number of the animation. Allegro game programming library."
---

<h2>NAME</h2>
<p> fli_frame &#8211; Stores the current frame number of the animation. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int fli_frame;</code></p>
<h2>DESCRIPTION</h2>
<p> Global variable containing the current frame number in the FLI file. This is useful for synchronising other events with the animation, for instance you could check it in a play_fli() callback function and use it to trigger a sample at a particular point. Example: </p>
<pre><code>
while (next_fli_frame(0) == FLI_OK) {
    if (fli_frame == 345)
        play_sample(trumpet_sound, 255, 128, 1000, 0);
    /* Rest some time until next frame... */
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_fli/">play_fli</a></code>(3), <code><a href="/docs/linux/man/3-play_memory_fli/">play_memory_fli</a></code>(3), <code><a href="/docs/linux/man/3-next_fli_frame/">next_fli_frame</a></code>(3) </p>
<h2>Index</h2>
