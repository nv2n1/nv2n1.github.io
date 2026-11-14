---
title: "release_voice(3)"
name: "release_voice"
section: "3"
letter: "r"
url: "/docs/linux/man/3-release_voice/"
description: "release_voice – Releases a sound card voice. Allegro game programming library."
---

<p>release_voice &#8211; Releases a sound card voice. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void release_voice(int voice);</code></pre>
<h2>Description</h2>
<p>Releases a sound card voice, indicating that you are no longer interested in manipulating it. The sound will continue to play, and any resources that it is using will automatically be freed when it finishes. This is essentially the same as deallocate_voice(), but it waits for the sound to stop playing before taking effect. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-allocate_voice/">allocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-deallocate_voice/">deallocate_voice</a></code>(3) </p>
