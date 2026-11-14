---
title: "axfer-list(1)"
name: "axfer-list"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axfer-list/"
description: "axfer-list – dump lists of available sound devices and nodes to transfer audio data frame."
---

<h2 class="name">NAME</h2>
<p> axfer-list &#8211; dump lists of available sound devices and nodes to transfer audio data frame.</p>
<h2>SYNOPSIS</h2>
<p> <code>axfer list</code> <i>direction target</i> </p>
<p> direction = <code>capture</code> | <code>playback</code> </p>
<p> target = <code>device</code> | <code>pcm</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>list</code> subcommand of <code>axfer</code> dumps lists of available nodes to transfer audio data frame. At present, the subcommand is helpful just for libasound backend of <code>transfer</code> subcommand. </p>
<h2>OPTIONS</h2>
<h3>Direction</h3>
<dl>
<dt><code>capture</code></p>
<dd> Operates for capture transmission. </p>
<dt><code>playback</code></p>
<dd> Operates for playback transmission. </p>
</dl>
<h3>Target</h3>
<dl>
<dt><code>device</code></p>
<dd> Dumps a list of all soundcards and digital audio devices available in <i>libasound</i> backend for <i>tranfer</i> subcommand. </p>
<dt><code>pcm</code></p>
<dd> Dumps a list of all PCM nodes available in alsa-lib configuration space in <i>libasound</i> backend for <i>transfer</i> subcommand. </p>
</dl>
<h2>COMPATIBILITY TO APLAY</h2>
<p> Options of <i>-l</i> , <i>&#8211;list-devices</i> are handled as <i>device</i> operation. Options of <i>-L</i> , <i>&#8211;list-pcms</i> are handled as <i>pcm</i> operation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-axfer/">axfer</a>(1),</code> <code><a href="/docs/linux/man/1-axfer-transfer/">axfer-transfer</a>(1),</code> <code><a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1),</code> <code><a href="/docs/linux/man/1-amixer/">amixer</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> Takashi Sakamoto &lt;o-takashi [at] sakamocchi.jp&gt; </p>
<h2>Index</h2>
