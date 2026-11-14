---
title: "voice_check(3)"
name: "voice_check"
section: "3"
letter: "v"
url: "/docs/linux/man/3-voice_check/"
description: "voice_check – Checks whether a voice is currently allocated. Allegro game programming library."
---

<p>voice_check &#8211; Checks whether a voice is currently allocated. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>SAMPLE *voice_check(int voice);</code></p>
<h2>Description</h2>
<p>Checks whether a voice is currently allocated.</p>
<h2>Return Value</h2>
<p>Returns a pointer to the sample that the voice is using, or NULL if the voice is inactive (ie. it has been deallocated, or the release_voice() function has been called and the sample has then finished playing). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-allocate_voice/">allocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-voice_start/">voice_start</a></code>(3), <code><a href="/docs/linux/man/3-voice_get_position/">voice_get_position</a></code>(3) </p>
