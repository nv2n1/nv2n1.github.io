---
title: "snd_pcm_lib_ioctl(9)"
name: "snd_pcm_lib_ioctl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_lib_ioctl/"
---

snd_pcm_lib_ioctl - a generic PCM ioctl callback

<h2>Synopsis</h2>

<pre><code>int snd_pcm_lib_ioctl(struct snd_pcm_substream *substream, unsigned int cmd, void *arg);</code></pre>

<h2>Arguments</h2>

<i>substream</i>
<dl><dd><dd>the pcm substream instance</dl>
 

 <i>cmd</i>
<dl><dd>ioctl command</dl>
 

 <i>arg</i>
<dl><dd>ioctl argument</dl>

<h2>Description</h2>

Processes the generic ioctl commands for PCM. Can be passed as the ioctl callback for PCM ops.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


