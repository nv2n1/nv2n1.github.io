---
title: "fli_timer(3)"
name: "fli_timer"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fli_timer/"
description: "fli_timer – Global variable for timing FLI playback. Allegro game programming library."
---

<h2>NAME</h2>
<p> fli_timer &#8211; Global variable for timing FLI playback. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern volatile int fli_timer;</code></p>
<h2>DESCRIPTION</h2>
<p> Global variable for timing FLI playback. When you open an FLI file, a timer interrupt is installed which increments this variable every time a new frame should be displayed. Calling next_fli_frame() decrements it, so you can test it and know that it is time to display a new frame if it is greater than zero. Example: </p>
<pre><code>
while (next_fli_frame(0) == FLI_OK) {
    /* Do stuff, like play audio stream
       or check keys to skip animation. */
    /* Rest some time until next frame... */
    while (fli_timer &lt;= 0)
        rest(0);
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-next_fli_frame/">next_fli_frame</a></code>(3) </p>
<h2>Index</h2>
