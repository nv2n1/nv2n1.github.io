---
title: "snd_pcm_mmap_data_open(9)"
name: "snd_pcm_mmap_data_open"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_mmap_data_open/"
---

snd_pcm_mmap_data_open - increase the mmap counter

<h2>Synopsis</h2>

<pre><code>void snd_pcm_mmap_data_open(struct vm_area_struct *area);</code></pre>

<h2>Arguments</h2>

<i>area</i>
<dl><dd><dd>VMA</dl>

<h2>Description</h2>

PCM mmap callback should handle this counter properly

<h2>Copyright</h2>


