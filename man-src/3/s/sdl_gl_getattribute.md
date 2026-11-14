---
title: "sdl_gl_getattribute(3)"
name: "sdl_gl_getattribute"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_gl_getattribute/"
description: "SDL_GL_GetAttribute – Get the value of a special SDL/OpenGL attribute"
---

<p>SDL_GL_GetAttribute &#8211; Get the value of a special SDL/OpenGL attribute</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_GL_GetAttribute</code>(<code>SDLGLattr attr, int *value</code>);</p>
<h2>Description</h2>
<p>Places the value of the SDL/OpenGL <i>attribute</i> <code>attr</code> into <code>value</code>. This is useful after a call to <i></i><code>SDL_SetVideoMode</code> to check whether your attributes have been <i>set</i> as you expected.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on success, or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GL_SetAttribute</code>, <i>GL Attributes</i></p>
