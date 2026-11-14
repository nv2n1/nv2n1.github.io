---
title: "snd_pcm_sgbuf_get_ptr(9)"
name: "snd_pcm_sgbuf_get_ptr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_sgbuf_get_ptr/"
---

snd_pcm_sgbuf_get_ptr - Get the virtual address at the corresponding offset

<h2>Synopsis</h2>

<pre><code>void *snd_pcm_sgbuf_get_ptr(struct snd_pcm_substream *substream, unsigned int ofs);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>ofs</i>
<dl><dd>byte offset</dl>

<h2>Copyright</h2>


