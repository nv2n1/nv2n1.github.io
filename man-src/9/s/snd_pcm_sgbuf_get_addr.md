---
title: "snd_pcm_sgbuf_get_addr(9)"
name: "snd_pcm_sgbuf_get_addr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_sgbuf_get_addr/"
description: "snd_pcm_sgbuf_get_addr – Get the DMA address at the corresponding offset"
---

<p>snd_pcm_sgbuf_get_addr &#8211; Get the DMA address at the corresponding offset</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dma_addr_t snd_pcm_sgbuf_get_addr(struct snd_pcm_substream&nbsp;<wbr>*&nbsp;<wbr></code><i>substream</i><code>, unsigned int&nbsp;<wbr></code><i>ofs</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>substream</i></p>
<dl>
<dd>
<dd>PCM substream</dl>
<p> <i>ofs</i></p>
<dl>
<dd>byte offset</dl>
<h2>Copyright</h2>
