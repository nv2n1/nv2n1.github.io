---
title: "register_sample_file_type(3)"
name: "register_sample_file_type"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_sample_file_type/"
description: "register_sample_file_type – Registers custom loading/saving sample routines. Allegro game programming library."
---

<p>register_sample_file_type &#8211; Registers custom loading/saving sample routines. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_sample_file_type(const char *ext,

                               SAMPLE *(*load)(const char *filename),

                               int (*save)(const char *filename, SAMPLE *spl));</code></pre>
<h2>Description</h2>
<p>Informs the load_sample() function of a new sample file type, providing routines to read and write samples in this format (either function may be NULL). Example: </p>
<pre> SAMPLE *load_mp3(const char *filename)
 {
 ...
 }
 
 register_sample_file_type(&quot;mp3&quot;, load_mp3, NULL);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3), <code><a href="/docs/linux/man/3-save_sample/">save_sample</a></code>(3) </p>
