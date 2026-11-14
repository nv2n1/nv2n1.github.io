---
title: "snd_pcm_format_size(9)"
name: "snd_pcm_format_size"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_pcm_format_size/"
description: "snd_pcm_format_size – return the byte size of samples on the given format"
---

<p>snd_pcm_format_size &#8211; return the byte size of samples on the given format</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t snd_pcm_format_size(snd_pcm_format_t&nbsp;<wbr></code><i>format</i><code>, size_t&nbsp;<wbr></code><i>samples</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>format</i></p>
<dl>
<dd>
<dd>the format to check</dl>
<p> <i>samples</i></p>
<dl>
<dd>sampling rate</dl>
<h2>Return</h2>
<p>The byte size of the given samples for the format, or a negative error code if unknown format.</p>
<h2>Copyright</h2>
