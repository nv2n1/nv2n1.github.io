---
title: "load_voc_pf(3)"
name: "load_voc_pf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_voc_pf/"
description: "load_voc_pf – Packfile version of load_voc. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_voc_pf &#8211; Packfile version of load_voc. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>SAMPLE *load_voc_pf(PACKFILE *f);</code></p>
<h2>DESCRIPTION</h2>
<p> A version of load_voc() which reads from a packfile. Example: </p>
<pre><code>
PACKFILE *packfile;
SAMPLE *sample;

packfile = pack_fopen("sound.wav", F_READ);
if (!packfile)
    abort_on_error("Couldn't open sound.wav");

sample = load_wav_pf(packfile);
if (!sample)
    abort_on_error("Error loading sound.wav");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the SAMPLE or NULL on error. Remember to free this sample later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_voc/">load_voc</a></code>(3) </p>
<h2>Index</h2>
