---
title: "sdl_audiocvt(3)"
name: "sdl_audiocvt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_audiocvt/"
description: "SDL_AudioCVT – Audio Conversion Structure"
---

<p>SDL_AudioCVT &#8211; Audio Conversion Structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 int needed;
 Uint16 src_format;
 Uint16 dest_format;
 double rate_incr;
 Uint8 *buf;
 int len;
 int len_cvt;
 int len_mult;
 double len_ratio;
 void (*filters[10])(struct SDL_AudioCVT *cvt, Uint16 format);
 int filter_index;
} SDL_AudioCVT;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>needed</code></p>
<dd>Set to one if the conversion is possible</p>
<dt><code>src_format</code></p>
<dd>Audio format of the source</p>
<dt><code>dest_format</code></p>
<dd>Audio format of the destination</p>
<dt><code>rate_incr</code></p>
<dd>Rate conversion increment</p>
<dt><code>buf</code></p>
<dd>Audio buffer</p>
<dt><code>len</code></p>
<dd>Length of the original audio buffer in bytes</p>
<dt><code>len_cvt</code></p>
<dd>Length of converted audio buffer in bytes (calculated)</p>
<dt><code>len_mult</code></p>
<dd><code>buf</code> must be <code>len</code>*<code>len_mult</code> bytes in size(calculated)</p>
<dt><code>len_ratio</code></p>
<dd>Final audio size is <code>len</code>*<code>len_ratio</code></p>
<dt><code>filters[10](..)</code></p>
<dd>Pointers to functions needed for this conversion</p>
<dt><code>filter_index</code></p>
<dd>Current conversion function</dl>
<h2>Description</h2>
<p>The <code>SDL_AudioCVT</code> is used to convert audio data between different formats. A <code>SDL_AudioCVT</code> structure is created with the <i></i><code>SDL_BuildAudioCVT</code> function, while the actual conversion is done by the <i></i><code>SDL_ConvertAudio</code> function. </p>
<p> Many of the fields in the <code>SDL_AudioCVT</code> structure should be considered private and their function will not be discussed here.</p>
<dl COMPACT>
<dt><code>Uint8 *</code><code>buf</code></p>
<dd>
<dt><code>int</code> <code>len</code></p>
<dd>
<dt><code>int</code> <code>len_mult</code></p>
<dd>
<dt><code>double</code> <code>len_ratio</code></p>
<dd></dl>
<h2>See Also</h2>
<p><i></i><code>SDL_BuildAudioCVT</code>, <i></i><code>SDL_ConvertAudio</code>, <i></i><code>SDL_AudioSpec</code></p>
