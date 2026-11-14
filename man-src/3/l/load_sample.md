---
title: "load_sample(3)"
name: "load_sample"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_sample/"
description: "load_sample – Loads a sample from a file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_sample &#8211; Loads a sample from a file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>SAMPLE *load_sample(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a sample from a file, supporting both mono and stereo WAV and mono VOC files, in 8 or 16-bit formats, as well as formats handled by functions registered using register_sample_file_type(). Example: </p>
<pre><code>
SAMPLE *sample = load_sample(user_input);
if (!sample)
    abort_on_error("Couldn't load sample!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the SAMPLE or NULL on error. Remember to free this sample later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-destroy_sample/">destroy_sample</a></code>(3), <code><a href="/docs/linux/man/3-load_voc/">load_voc</a></code>(3), <code><a href="/docs/linux/man/3-load_wav/">load_wav</a></code>(3), <code><a href="/docs/linux/man/3-play_sample/">play_sample</a></code>(3), <code><a href="/docs/linux/man/3-save_sample/">save_sample</a></code>(3), <code><a href="/docs/linux/man/3-register_sample_file_type/">register_sample_file_type</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3) </p>
<h2>Index</h2>
