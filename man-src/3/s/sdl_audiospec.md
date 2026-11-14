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
<dt><code>freq</code></p>
<dd>Audio frequency in samples per second</p>
<dt><code>format</code></p>
<dd>Audio data format</p>
<dt><code>channels</code></p>
<dd>Number of channels: 1 mono, 2 stereo</p>
<dt><code>silence</code></p>
<dd>Audio buffer silence value (calculated)</p>
<dt><code>samples</code></p>
<dd>Audio buffer size in samples</p>
<dt><code>size</code></p>
<dd>Audio buffer size in bytes (calculated)</p>
<dt><code>callback(..)</code></p>
<dd>Callback function for filling the audio buffer</p>
<dt><code>userdata</code></p>
<dd>Pointer the user data which is passed to the callback function</dl>
<h2>Description</h2>
<p>The <code>SDL_AudioSpec</code> structure is used to describe the format of some audio data. This structure is used by <i></i><code>SDL_OpenAudio</code> and <i></i><code>SDL_LoadWAV</code>. While all fields are used by <code>SDL_OpenAudio</code> only <code>freq</code>, <code>format</code>, <code>samples</code> and <code>channels</code> are used by <code>SDL_LoadWAV</code>. We will detail these common members here.</p>
<dl COMPACT>
<dt><code>freq</code></p>
<dd>The number of samples sent to the sound device every second. Common values are 11025, 22050 and 44100. The higher the better.</p>
<dt><code>format</code></p>
<dd>Specifies the size and type of each sample element</p>
<dt><code>AUDIO_U8</code></p>
<dd>
<dt><code>AUDIO_S8</code></p>
<dd>
<dt><code>AUDIO_U16</code> or <code>AUDIO_U16LSB</code></p>
<dd>
<dt><code>AUDIO_S16</code> or <code>AUDIO_S16LSB</code></p>
<dd>
<dt><code>AUDIO_U16MSB</code></p>
<dd>
<dt><code>AUDIO_S16MSB</code></p>
<dd>
<dt><code>AUDIO_U16SYS</code></p>
<dd>
<dt><code>AUDIO_S16SYS</code></p>
<dd>
<dt><code>channels</code></p>
<dd>The number of seperate sound channels. 1 is mono (single channel), 2 is stereo (dual channel).</p>
<dt><code>samples</code></p>
<dd>When used with <i></i><code>SDL_OpenAudio</code> this refers to the size of the audio buffer in samples. A sample a chunk of audio data of the size specified in <code>format</code> mulitplied by the number of channels. When the <code>SDL_AudioSpec</code> is used with <i></i><code>SDL_LoadWAV</code> <code>samples</code> is set to 4096.</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_OpenAudio</code>, <i></i><code>SDL_LoadWAV</code></p>
