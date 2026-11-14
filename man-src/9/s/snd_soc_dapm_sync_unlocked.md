---
title: "snd_soc_dapm_sync_unlocked(9)"
name: "snd_soc_dapm_sync_unlocked"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_sync_unlocked/"
---

snd_soc_dapm_sync_unlocked - scan and power dapm paths

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_sync_unlocked(struct snd_soc_dapm_context *dapm);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>

<h2>Description</h2>

Walks all dapm audio paths and powers widgets according to their stream or path usage. 

 Requires external locking. 

 Returns 0 for success.

<h2>Copyright</h2>


