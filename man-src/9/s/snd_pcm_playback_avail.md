---
title: "snd_pcm_playback_avail(9)"
name: "snd_pcm_playback_avail"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_playback_avail/"
description: "snd_pcm_playback_avail – Get the available (writable) space for playback"
---

<p>snd_pcm_playback_avail &#8211; Get the available (writable) space for playback</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>snd_pcm_uframes_t snd_pcm_playback_avail(struct snd_pcm_runtime&nbsp;<wbr>*&nbsp;<wbr></code><i>runtime</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>runtime</i></p>
<dl>
<dd>
<dd>PCM runtime instance</dl>
<h2>Description</h2>
<p>Result is between 0 &#8230; (boundary &#8211; 1)</p>
<h2>Copyright</h2>
