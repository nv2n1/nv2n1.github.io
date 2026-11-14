---
title: "create_sample(3)"
name: "create_sample"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_sample/"
description: "create_sample – Constructs a new sample structure of the specified type. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_sample &#8211; Constructs a new sample structure of the specified type. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>SAMPLE *create_sample(int bits, int stereo, int freq, int len);</code></p>
<h2>DESCRIPTION</h2>
<p> Constructs a new sample structure of the specified type. Read chapter &quot;Structures and types defined by Allegro&quot; for an internal description of the SAMPLE structure. The `bits&#8217; parameter can be 8 or 16, `stereo&#8217; can be zero for mono samples and non-zero for stereo samples, `freq&#8217; is the frequency in hertz, and `len&#8217; is the number of samples you want to allocate for the full sound buffer.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the created sample, or NULL if the sample could not be created. Remember to free this sample later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3), <code><a href="/docs/linux/man/3-destroy_sample/">destroy_sample</a></code>(3) </p>
<h2>Index</h2>
