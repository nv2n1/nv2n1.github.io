---
title: "sdl_mixaudio(3)"
name: "sdl_mixaudio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_mixaudio/"
description: "SDL_MixAudio – Mix audio data"
---

<p>SDL_MixAudio &#8211; Mix audio data</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_MixAudio</code>(<code>Uint8 *dst, Uint8 *src, Uint32 len, int volume</code>);</p>
<h2>Description</h2>
<p>This function takes two audio buffers of <code>len</code> bytes each of the playing audio format and mixes them, performing addition, volume adjustment, and overflow clipping. The <code>volume</code> ranges from 0 to <code>SDL_MIX_MAXVOLUME</code> and should be set to the maximum value for full audio volume. Note this does not change hardware volume. This is provided for convenience &#8212; you can mix your own audio data. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Do not use this function for mixing together more than two streams of sample data. The output from repeated application of this function may be distorted by clipping, because there is no accumulator with greater range than the input (not to mention this being an inefficient way of doing it). Use mixing functions from SDL_mixer, OpenAL, or write your own mixer instead.</dl>
<p> </code></p>
<h2>See Also</h2>
<p><i></i><code>SDL_OpenAudio</code></p>
