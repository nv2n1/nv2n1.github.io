---
title: "sdl_audiospec(3)"
name: "sdl_audiospec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_audiospec/"
description: "SDL_AudioSpec – Audio Specification Structure"
---

<p>SDL_AudioSpec &#8211; Audio Specification Structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 int freq;
 Uint16 format;
 Uint8 channels;
 Uint8 silence;
 Uint16 samples;
 Uint32 size;
 void (*callback)(void *userdata, Uint8 *stream, int len);
 void *userdata;
} SDL_AudioSpec;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>freq</code></dt>
<dd>Audio frequency in samples per second</dd>
<dt><code>format</code></dt>
<dd>Audio data format</dd>
<dt><code>channels</code></dt>
<dd>Number of channels: 1 mono, 2 stereo</dd>
<dt><code>silence</code></dt>
<dd>Audio buffer silence value (calculated)</dd>
<dt><code>samples</code></dt>
<dd>Audio buffer size in samples</dd>
<dt><code>size</code></dt>
<dd>Audio buffer size in bytes (calculated)</dd>
<dt><code>callback(..)</code></dt>
<dd>Callback function for filling the audio buffer</dd>
<dt><code>userdata</code></dt>
<dd>Pointer the user data which is passed to the callback function</dd></dl>
<h2>Description</h2>
<p>The <code>SDL_AudioSpec</code> structure is used to describe the format of some audio data. This structure is used by <i></i><code>SDL_OpenAudio</code> and <i></i><code>SDL_LoadWAV</code>. While all fields are used by <code>SDL_OpenAudio</code> only <code>freq</code>, <code>format</code>, <code>samples</code> and <code>channels</code> are used by <code>SDL_LoadWAV</code>. We will detail these common members here.</p>
<dl COMPACT>
<dt><code>freq</code></dt>
<dd>The number of samples sent to the sound device every second. Common values are 11025, 22050 and 44100. The higher the better.</dd>
<dt><code>format</code></dt>
<dd>Specifies the size and type of each sample element</dd>
<dt><code>AUDIO_U8</code></dt>
<dd>
</dd><dt><code>AUDIO_S8</code></dt>
<dd>
</dd><dt><code>AUDIO_U16</code> or <code>AUDIO_U16LSB</code></dt>
<dd>
</dd><dt><code>AUDIO_S16</code> or <code>AUDIO_S16LSB</code></dt>
<dd>
</dd><dt><code>AUDIO_U16MSB</code></dt>
<dd>
</dd><dt><code>AUDIO_S16MSB</code></dt>
<dd>
</dd><dt><code>AUDIO_U16SYS</code></dt>
<dd>
</dd><dt><code>AUDIO_S16SYS</code></dt>
<dd>
</dd><dt><code>channels</code></dt>
<dd>The number of seperate sound channels. 1 is mono (single channel), 2 is stereo (dual channel).</dd>
<dt><code>samples</code></dt>
<dd>When used with <i></i><code>SDL_OpenAudio</code> this refers to the size of the audio buffer in samples. A sample a chunk of audio data of the size specified in <code>format</code> mulitplied by the number of channels. When the <code>SDL_AudioSpec</code> is used with <i></i><code>SDL_LoadWAV</code> <code>samples</code> is set to 4096.</dd></dl>
<h2>See Also</h2>
<p><i></i><code>SDL_OpenAudio</code>, <i></i><code>SDL_LoadWAV</code></p>
