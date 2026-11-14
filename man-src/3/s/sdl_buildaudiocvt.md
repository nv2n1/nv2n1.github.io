---
title: "sdl_buildaudiocvt(3)"
name: "sdl_buildaudiocvt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_buildaudiocvt/"
description: "SDL_BuildAudioCVT – Initializes a SDL_AudioCVT structure for conversion"
---

<p>SDL_BuildAudioCVT &#8211; Initializes a SDL_AudioCVT structure for conversion</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_BuildAudioCVT</code>(<code>SDL_AudioCVT *cvt, Uint16 src_format, Uint8 src_channels, int src_rate, Uint16 dst_format, Uint8 dst_channels, int dst_rate</code>);</p>
<h2>Description</h2>
<p>Before an <i></i><code>SDL_AudioCVT</code> structure can be used to convert audio data it must be initialized with source and destination information. </p>
<p> <code>src_format</code> and <code>dst_format</code> are the source and destination format of the conversion. (For information on audio formats see <i></i><code> SDL_AudioSpec</code>). <code>src_channels</code> and <code>dst_channels</code> are the number of channels in the source and destination formats. Finally, <code>src_rate</code> and <code>dst_rate</code> are the frequency or samples-per-second of the source and destination formats. Once again, see <i></i><code>SDL_AudioSpec</code>.</p>
<h2>Return Values</h2>
<p>Returns <code>-1</code> if the filter could not be built or 1 if it could.</p>
<h2>Examples</h2>
<p>See <i></i><code>SDL_ConvertAudio</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_ConvertAudio</code>, <i></i><code>SDL_AudioCVT</code></p>
