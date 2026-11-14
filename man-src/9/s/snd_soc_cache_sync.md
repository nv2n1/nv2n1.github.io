---
title: "snd_soc_cache_sync(9)"
name: "snd_soc_cache_sync"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_cache_sync/"
description: "snd_soc_cache_sync – Sync the register cache with the hardware"
---

<p>snd_soc_cache_sync &#8211; Sync the register cache with the hardware</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_cache_sync(struct snd_soc_codec *codec);</code></pre>
<h2>Arguments</h2>
<p><i>codec</i></p>
<dl>
<dd>
<dd>CODEC to sync</dl>
<h2>Note</h2>
<p>This function will call <code>regcache_sync</code></p>
<h2>Copyright</h2>
