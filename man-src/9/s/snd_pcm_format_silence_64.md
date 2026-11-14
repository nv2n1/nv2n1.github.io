---
title: "snd_pcm_format_silence_64(9)"
name: "snd_pcm_format_silence_64"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_silence_64/"
description: "snd_pcm_format_silence_64 – return the silent data in 8 bytes array"
---

<p>snd_pcm_format_silence_64 &#8211; return the silent data in 8 bytes array</p>
<h2>Synopsis</h2>
<pre><code>const unsigned char *snd_pcm_format_silence_64(snd_pcm_format_t format);</code></pre>
<h2>Arguments</h2>
<p><i>format</i></p>
<dl>
<dd>
<dd>the format to check</dl>
<h2>Return</h2>
<p>The format pattern to fill or <code>NULL</code> if error.</p>
<h2>Copyright</h2>
