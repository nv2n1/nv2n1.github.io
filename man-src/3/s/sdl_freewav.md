---
title: "sdl_freewav(3)"
name: "sdl_freewav"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_freewav/"
description: "SDL_FreeWAV – Frees previously opened WAV data"
---

<p>SDL_FreeWAV &#8211; Frees previously opened WAV data</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_FreeWAV</code>(<code>Uint8 *audio_buf</code>);</p>
<h2>Description</h2>
<p>After a WAVE file has been opened with <i></i><code>SDL_LoadWAV</code> its data can eventually be freed with <code>SDL_FreeWAV</code>. <code>audio_buf</code> is a pointer to the buffer created by <code>SDL_LoadWAV</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_LoadWAV</code></p>
