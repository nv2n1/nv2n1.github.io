---
title: "snd_pcm_suspend_all(9)"
name: "snd_pcm_suspend_all"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_suspend_all/"
description: "snd_pcm_suspend_all – trigger SUSPEND to all substreams in the given pcm"
---

<p>snd_pcm_suspend_all &#8211; trigger SUSPEND to all substreams in the given pcm</p>
<h2>Synopsis</h2>
<pre><code>int snd_pcm_suspend_all(struct snd_pcm *pcm);</code></pre>
<h2>Arguments</h2>
<p><i>pcm</i></p>
<dl>
<dd>
<dd>the PCM instance</dl>
<h2>Description</h2>
<p>After this call, all streams are changed to SUSPENDED state.</p>
<h2>Return</h2>
<p>Zero if successful (or <i>pcm</i> is <code>NULL</code>), or a negative error code.</p>
<h2>Copyright</h2>
