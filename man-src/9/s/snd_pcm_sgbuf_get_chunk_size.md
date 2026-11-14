---
title: "snd_pcm_sgbuf_get_chunk_size(9)"
name: "snd_pcm_sgbuf_get_chunk_size"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_sgbuf_get_chunk_size/"
---

snd_pcm_sgbuf_get_chunk_size - Compute the max size that fits within the contig. page from the given size

<h2>Synopsis</h2>

<pre><code>unsigned int snd_pcm_sgbuf_get_chunk_size(struct snd_pcm_substream *substream, unsigned int ofs, unsigned int size);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>PCM substream</dl>
 

 <i>ofs</i>
<dl><dd>byte offset</dl>
 

 <i>size</i>
<dl><dd>byte size to examine</dl>

<h2>Copyright</h2>


