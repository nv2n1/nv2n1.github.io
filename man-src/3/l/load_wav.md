---
title: "load_wav(3)"
name: "load_wav"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_wav/"
description: "load_wav – Loads a sample from a RIFF WAV file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_wav &#8211; Loads a sample from a RIFF WAV file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>SAMPLE *load_wav(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a sample from a RIFF WAV file. Example: </p>
<pre><code>
SAMPLE *sample = load_wav("scream.wav");
if (!sample)
    abort_on_error("Couldn't scare user!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the SAMPLE or NULL on error. Remember to free this sample later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3), <code><a href="/docs/linux/man/3-register_sample_file_type/">register_sample_file_type</a></code>(3) </p>
<h2>Index</h2>
