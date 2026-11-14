---
title: "snd_pcm_notify(9)"
name: "snd_pcm_notify"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_notify/"
---

snd_pcm_notify - Add/remove the notify list

<h2>Synopsis</h2>

<pre><code>int snd_pcm_notify(struct snd_pcm_notify *notify, int nfree);</code></pre>

<h2>Arguments</h2>

<i>notify</i>
<dl><dd><dd>PCM notify list</dl>
 

 <i>nfree</i>
<dl><dd>0 = register, 1 = unregister</dl>

<h2>Description</h2>

This adds the given notifier to the global list so that the callback is called for each registered PCM devices. This exists only for PCM OSS emulation, so far.

<h2>Copyright</h2>


