---
title: "sdl_gl_loadlibrary(3)"
name: "sdl_gl_loadlibrary"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_gl_loadlibrary/"
description: "SDL_GL_LoadLibrary – Specify an OpenGL library"
---

<p>SDL_GL_LoadLibrary &#8211; Specify an OpenGL library</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_GL_LoadLibrary</code>(<code>const char *path</code>);</p>
<h2>Description</h2>
<p>If you wish, you may load the OpenGL library at runtime, this must be done before <i></i><code>SDL_SetVideoMode</code> is called. The <code>path</code> of the GL library is passed to <code>SDL_GL_LoadLibrary</code> and it returns <code>0</code> on success, or <code>-1</code> on an error. You must then use <i></i><code>SDL_GL_GetProcAddress</code> to retrieve function pointers to GL functions.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GL_GetProcAddress</code></p>
