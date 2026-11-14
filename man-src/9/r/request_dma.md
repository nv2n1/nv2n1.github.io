---
title: "request_dma(9)"
name: "request_dma"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_dma/"
---

request_dma - request and reserve a system DMA channel

<h2>Synopsis</h2>

<pre><code>int request_dma(unsigned int dmanr, const char *device_id);</code></pre>

<h2>Arguments</h2>

<i>dmanr</i>
<dl><dd><dd>DMA channel number</dl>
 

 <i>device_id</i>
<dl><dd>reserving device ID string, used in /proc/dma</dl>

<h2>Copyright</h2>


