---
title: "sdl_lockyuvoverlay(3)"
name: "sdl_lockyuvoverlay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_lockyuvoverlay/"
description: "SDL_LockYUVOverlay – Lock an overlay"
---

<p>SDL_LockYUVOverlay &#8211; Lock an overlay</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_LockYUVOverlay</code>(<code>SDL_Overlay *overlay</code>);</p>
<h2>Description</h2>
<p>Much the same as <i></i><code>SDL_LockSurface</code>, <code>SDL_LockYUVOverlay</code> locks the <i></i><code>overlay</code> for direct access to pixel data.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on success, or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_UnlockYUVOverlay</code>, <i></i><code>SDL_CreateYUVOverlay</code>, <i></i><code>SDL_Overlay</code></p>
