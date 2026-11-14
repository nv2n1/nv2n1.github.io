---
title: "reallocate_voice(3)"
name: "reallocate_voice"
section: "3"
letter: "r"
url: "/docs/linux/man/3-reallocate_voice/"
description: "reallocate_voice – Switches the sample of an already-allocated voice. Allegro game programming library."
---

<p>reallocate_voice &#8211; Switches the sample of an already-allocated voice. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void reallocate_voice(int voice, const SAMPLE *spl);</code></pre>
<h2>Description</h2>
<p>Switches an already-allocated voice to use a different sample. Calling reallocate_voice(voice, sample) is equivalent to: </p>
<pre><code>deallocate_voice(voice);
voice = allocate_voice(sample);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-allocate_voice/">allocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-deallocate_voice/">deallocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3) </p>
