---
title: "sdl_glattr(3)"
name: "sdl_glattr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_glattr/"
description: "SDL_GLattr – SDL GL Attributes"
---

<p>SDL_GLattr &#8211; SDL GL Attributes</p>
<h2>Attributes</h2>
<dl COMPACT>
<dt><code>SDL_GL_RED_SIZE</code></p>
<dd>Size of the framebuffer red component, in bits</p>
<dt><code>SDL_GL_GREEN_SIZE</code></p>
<dd>Size of the framebuffer green component, in bits</p>
<dt><code>SDL_GL_BLUE_SIZE</code></p>
<dd>Size of the framebuffer blue component, in bits</p>
<dt><code>SDL_GL_ALPHA_SIZE</code></p>
<dd>Size of the framebuffer alpha component, in bits</p>
<dt><code>SDL_GL_DOUBLEBUFFER</code></p>
<dd>0 or 1, enable or disable double buffering</p>
<dt><code>SDL_GL_BUFFER_SIZE</code></p>
<dd>Size of the framebuffer, in bits</p>
<dt><code>SDL_GL_DEPTH_SIZE</code></p>
<dd>Size of the depth buffer, in bits</p>
<dt><code>SDL_GL_STENCIL_SIZE</code></p>
<dd>Size of the stencil buffer, in bits</p>
<dt><code>SDL_GL_ACCUM_RED_SIZE</code></p>
<dd>Size of the accumulation buffer red component, in bits</p>
<dt><code>SDL_GL_ACCUM_GREEN_SIZE</code></p>
<dd>Size of the accumulation buffer green component, in bits</p>
<dt><code>SDL_GL_ACCUM_BLUE_SIZE</code></p>
<dd>Size of the accumulation buffer blue component, in bits</p>
<dt><code>SDL_GL_ACCUM_ALPHA_SIZE</code></p>
<dd>Size of the accumulation buffer alpha component, in bits</dl>
<h2>Description</h2>
<p>While you can set most OpenGL attributes normally, the attributes list above must be known <i>before</i> SDL sets the video mode. These attributes a set and read with <i></i><code>SDL_GL_SetAttribute</code> and <i></i><code>SDL_GL_GetAttribute</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GL_SetAttribute</code>, <i></i><code>SDL_GL_GetAttribute</code></p>
