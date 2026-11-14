---
title: "sdl_flip(3)"
name: "sdl_flip"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_flip/"
description: "SDL_Flip – Swaps screen buffers"
---

<p>SDL_Flip &#8211; Swaps screen buffers</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_Flip</code>(<code>SDL_Surface *screen</code>);</p>
<h2>Description</h2>
<p>On hardware that supports double-buffering, this function sets up a flip and returns. The hardware will wait for vertical retrace, and then swap video buffers before the next video surface blit or lock will return. On hardware that doesn&#8217;t support double-buffering, this is equivalent to calling <i>SDL_UpdateRect</i><code>(screen, 0, 0, 0, 0)</code> </p>
<p> The <code>SDL_DOUBLEBUF</code> flag must have been passed to <i>SDL_SetVideoMode</i>, when setting the video mode for this function to perform hardware flipping.</p>
<h2>Return Value</h2>
<p>This function returns <code>0</code> if successful, or <code>-1</code> if there was an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_UpdateRect</code>, <i></i><code>SDL_Surface</code></p>
