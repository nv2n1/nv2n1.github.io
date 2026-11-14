---
title: "sdl_loadwav(3)"
name: "sdl_loadwav"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_loadwav/"
description: "SDL_LoadWAV – Load a WAVE file"
---

<p>SDL_LoadWAV &#8211; Load a WAVE file</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_AudioSpec *SDL_LoadWAV</code>(<code>const char *file, SDL_AudioSpec *spec, Uint8 **audio_buf, Uint32 *audio_len</code>);</p>
<h2>Description</h2>
<p><code>SDL_LoadWAV</code> This function loads a WAVE <code>file</code> into memory. </p>
<p> If this function succeeds, it returns the given <i></i><code>SDL_AudioSpec</code>, filled with the audio data format of the wave data, and sets <code>audio_buf</code> to a <code>malloc</code>&#8216;d buffer containing the audio data, and sets <code>audio_len</code> to the length of that audio buffer, in bytes. You need to free the audio buffer with <i></i><code>SDL_FreeWAV</code> when you are done with it. </p>
<p> This function returns <code>NULL</code> and sets the SDL error message if the wave file cannot be opened, uses an unknown data format, or is corrupt. Currently raw, MS-ADPCM and IMA-ADPCM WAVE files are supported.</p>
<h2>Example</h2>
<pre><tt>SDL_AudioSpec wav_spec;
Uint32 wav_length;
Uint8 *wav_buffer;
/* Load the WAV */
if( SDL_LoadWAV(&quot;test.wav&quot;, &amp;wav_spec, &amp;wav_buffer, &amp;wav_length) == NULL ){
 fprintf(stderr, &quot;Could not open test.wav: %s
&quot;, SDL_GetError());
 exit(-1);
}
.
.
.
/* Do stuff with the WAV */
.
.
/* Free It */
SDL_FreeWAV(wav_buffer);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_AudioSpec</code>, <i></i><code>SDL_OpenAudio</code>, <i></i><code>SDL_FreeWAV</code></p>
