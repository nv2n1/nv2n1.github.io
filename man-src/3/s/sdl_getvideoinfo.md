---
title: "sdl_getvideoinfo(3)"
name: "sdl_getvideoinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getvideoinfo/"
description: "SDL_GetVideoInfo – returns a pointer to information about the video hardware"
---

<p>SDL_GetVideoInfo &#8211; returns a pointer to information about the video hardware</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_VideoInfo *SDL_GetVideoInfo</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>This function returns a read-only pointer to <i>information</i> about the video hardware. If this is called before <i>SDL_SetVideoMode</i>, the <code>vfmt</code> member of the returned structure will contain the pixel format of the &quot;best&quot; video mode.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_VideoInfo</code></p>
