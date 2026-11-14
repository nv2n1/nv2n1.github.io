---
title: "sdl_lockaudio(3)"
name: "sdl_lockaudio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_lockaudio/"
description: "SDL_LockAudio – Lock out the callback function"
---

<p>SDL_LockAudio &#8211; Lock out the callback function</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_LockAudio</code>(<code>void</code>)</p>
<h2>Description</h2>
<p>The lock manipulated by these functions protects the callback function. During a LockAudio period, you can be guaranteed that the callback function is not running. Do not call these from the callback function or you will cause deadlock.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_OpenAudio</code></p>
