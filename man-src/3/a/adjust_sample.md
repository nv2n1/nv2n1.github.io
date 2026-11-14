---
title: "adjust_sample(3)"
name: "adjust_sample"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adjust_sample/"
description: "adjust_sample – Alters the parameters of a sample while it is playing. Allegro game programming library."
---

<h2>NAME</h2>
<p> adjust_sample &#8211; Alters the parameters of a sample while it is playing. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void adjust_sample(const SAMPLE *spl, int vol, int pan, int freq, int loop);</code></p>
<h2>DESCRIPTION</h2>
<p> Alters the parameters of a sample while it is playing (useful for manipulating looped sounds). You can alter the volume, pan, and frequency, and can also clear the loop flag, which will stop the sample when it next reaches the end of its loop. The values of the parameters are just like those of play_sample(). If there are several copies of the same sample playing, this will adjust the first one it comes across. If the sample is not playing it has no effect. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_sample/">play_sample</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3) </p>
<h2>Index</h2>
