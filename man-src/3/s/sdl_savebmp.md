---
title: "sdl_savebmp(3)"
name: "sdl_savebmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_savebmp/"
description: "SDL_SaveBMP – Save an SDL_Surface as a Windows BMP file."
---

<p>SDL_SaveBMP &#8211; Save an SDL_Surface as a Windows BMP file.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SaveBMP</code>(<code>SDL_Surface *surface, const char *file</code>);</p>
<h2>Description</h2>
<p> Saves the <code>SDL_Surface</code> <code>surface</code> as a Windows BMP file named <code>file</code>.</p>
<h2>Return Value</h2>
<p> Returns <code>0</code> if successful or <code>-1</code> if there was an error.</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_LoadBMP</code></p>
