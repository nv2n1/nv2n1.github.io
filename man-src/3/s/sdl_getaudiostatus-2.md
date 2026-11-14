---
title: "sdl_getaudiostatus-2(3)"
name: "sdl_getaudiostatus-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getaudiostatus-2/"
description: "SDL_GetAudioStatus – Get the current audio state"
---

<p>SDL_GetAudioStatus &#8211; Get the current audio state</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_audiostatusSDL_GetAudioStatus</code>(<code>void</code>);</p>
<h2>Description</h2>
<pre><tt>typedef enum{
 SDL_AUDIO_STOPPED,
 SDL_AUDIO_PAUSED,
 SDL_AUDIO_PLAYING
} SDL_audiostatus;</tt></pre>
<p>Returns either <code>SDL_AUDIO_STOPPED</code>, <code>SDL_AUDIO_PAUSED</code> or <code>SDL_AUDIO_PLAYING</code> depending on the current audio state.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_PauseAudio</code></p>
