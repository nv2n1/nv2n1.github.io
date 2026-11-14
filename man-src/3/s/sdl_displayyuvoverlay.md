---
title: "sdl_displayyuvoverlay(3)"
name: "sdl_displayyuvoverlay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_displayyuvoverlay/"
description: "SDL_DisplayYUVOverlay – Blit the overlay to the display"
---

<p>SDL_DisplayYUVOverlay &#8211; Blit the overlay to the display</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> int SDL_DisplayYUVOverlay</code>(<code>SDL_Overlay *overlay, SDL_Rect *dstrect</code>);</p>
<h2>Description</h2>
<p> Blit the <code>overlay</code> to the surface specified when it was <i>created</i>. The <i></i><code>SDL_Rect</code> structure, <code>dstrect</code>, specifies the position and size of the destination. If the <code>dstrect</code> is a larger or smaller than the overlay then the overlay will be scaled, this is optimized for 2x scaling.</p>
<h2>Return Values</h2>
<p> Returns 0 on success</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_Overlay</code>, <i></i><code>SDL_CreateYUVOverlay</code></p>
