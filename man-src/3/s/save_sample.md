---
title: "save_sample(3)"
name: "save_sample"
section: "3"
letter: "s"
url: "/docs/linux/man/3-save_sample/"
description: "save_sample – Writes a sample into a file. Allegro game programming library."
---

<p>save_sample &#8211; Writes a sample into a file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int save_sample(const char *filename, SAMPLE *spl);</code></pre>
<h2>Description</h2>
<p>Writes a sample into a file. The output format is determined from the filename extension. At present Allegro does not natively support the writing of any sample formats, so you must register a custom saver routine with register_sample_file_type(). Example: </p>
<pre><code>if (save_sample(&quot;sound.wav&quot;, sample) != 0)
    abort_on_error(&quot;Couldn't save sample!&quot;);</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success, non-zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3), <code><a href="/docs/linux/man/3-register_sample_file_type/">register_sample_file_type</a></code>(3) </p>
