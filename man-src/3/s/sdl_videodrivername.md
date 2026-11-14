---
title: "sdl_videodrivername(3)"
name: "sdl_videodrivername"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_videodrivername/"
description: "SDL_VideoDriverName – Obtain the name of the video driver"
---

<p>SDL_VideoDriverName &#8211; Obtain the name of the video driver</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> char *SDL_VideoDriverName</code>(<code>char *namebuf, int maxlen</code>);</p>
<h2>Description</h2>
<p>The buffer pointed to by <code>namebuf</code> is filled up to a maximum of <code>maxlen</code> characters (include the NULL terminator) with the name of the initialised video driver. The driver name is a simple one word identifier like &quot;x11&quot; or &quot;windib&quot;.</p>
<h2>Return Value</h2>
<p>Returns <code>NULL</code> if video has not been initialised with <code>SDL_Init</code> or a pointer to <code>namebuf</code> otherwise.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Init</code> <i></i><code>SDL_InitSubSystem</code></p>
