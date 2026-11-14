---
title: "audiostream(3)"
name: "audiostream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audiostream/"
description: "AUDIOSTREAM – Stores an audiostream. Allegro game programming library."
---

<p>AUDIOSTREAM &#8211; Stores an audiostream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct AUDIOSTREAM</code></p>
<h2>Description</h2>
<pre> int voice; - the hardware voice used for the sample</pre>
<p>A structure holding an audiostream, which is a convenience wrapper around a SAMPLE structure to double buffer sounds too big to fit into memory, or do clever things like generating the sound wave real time. </p>
<p> While you shouldn&#8217;t modify directly the value of the voice, you can use all of the voice functions in chapter &quot;Digital sample routines&quot; to modify the properties of the sound, like the frequency. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-play_audio_stream/">play_audio_stream</a></code>(3), <code><a href="/docs/linux/man/3-exstream/">exstream</a></code>(3)</p>
