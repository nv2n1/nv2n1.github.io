---
title: "sdl_updaterects(3)"
name: "sdl_updaterects"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_updaterects/"
description: "SDL_UpdateRects – Makes sure the given list of rectangles is updated on the given screen."
---

<p>SDL_UpdateRects &#8211; Makes sure the given list of rectangles is updated on the given screen.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_UpdateRects</code>(<code>SDL_Surface *screen, int numrects, SDL_Rect *rects</code>);</p>
<h2>Description</h2>
<p>Makes sure the given list of rectangles is updated on the given screen. The rectangles must all be confined within the screen boundaries (no clipping is done). </p>
<p> This function should not be called while <code>screen</code> is <i>locked</i>. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> It is adviced to call this function only once per frame, since each call has some processing overhead. This is no restriction since you can pass any number of rectangles each time. </p>
<p> The rectangles are not automatically merged or checked for overlap. In general, the programmer can use his knowledge about his particular rectangles to merge them in an efficient way, to avoid overdraw.</dl>
<p> </code></p>
<h2>See Also</h2>
<p><i></i><code>SDL_UpdateRect</code>, <i></i><code>SDL_Rect</code>, <i></i><code>SDL_Surface</code>, <i></i><code>SDL_LockSurface</code></p>
