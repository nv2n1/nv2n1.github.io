---
title: "sdl_pauseaudio(3)"
name: "sdl_pauseaudio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_pauseaudio/"
description: "SDL_PauseAudio – Pauses and unpauses the audio callback processing"
---

<p>SDL_PauseAudio &#8211; Pauses and unpauses the audio callback processing</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_PauseAudio</code>(<code>int pause_on</code>);</p>
<h2>Description</h2>
<p>This function pauses and unpauses the audio callback processing. It should be called with <code>pause_on</code>=0 after opening the audio device to start playing sound. This is so you can safely initialize data for your callback function after opening the audio device. Silence will be written to the audio device during the pause.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetAudioStatus</code>, <i></i><code>SDL_OpenAudio</code></p>
