---
title: "snd_pcm_sgbuf_ops_page(9)"
name: "snd_pcm_sgbuf_ops_page"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_sgbuf_ops_page/"
description: "snd_pcm_sgbuf_ops_page – get the page struct at the given offset"
---

<p>snd_pcm_sgbuf_ops_page &#8211; get the page struct at the given offset</p>
<h2>Synopsis</h2>
<pre><code>struct page *snd_pcm_sgbuf_ops_page(struct snd_pcm_substream *substream, unsigned long offset);</code></pre>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>the pcm substream instance</dl>
<p> <i>offset</i></p>
<dl>
<dd>the buffer offset</dl>
<h2>Description</h2>
<p>Used as the page callback of PCM ops.</p>
<h2>Return</h2>
<p>The page struct at the given buffer offset. <code>NULL</code> on failure.</p>
<h2>Copyright</h2>
