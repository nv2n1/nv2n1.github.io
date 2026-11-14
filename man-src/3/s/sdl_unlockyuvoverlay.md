---
title: "sdl_unlockyuvoverlay(3)"
name: "sdl_unlockyuvoverlay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_unlockyuvoverlay/"
description: "SDL_UnlockYUVOverlay – Unlock an overlay"
---

<p>SDL_UnlockYUVOverlay &#8211; Unlock an overlay</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_UnlockYUVOverlay</code>(<code>SDL_Overlay *overlay</code>);</p>
<h2>Description</h2>
<p>The opposite to <i></i><code>SDL_LockYUVOverlay</code>. Unlocks a previously locked overlay. An overlay must be unlocked before it can be displayed.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_UnlockYUVOverlay</code>, <i></i><code>SDL_CreateYUVOverlay</code>, <i></i><code>SDL_Overlay</code></p>
