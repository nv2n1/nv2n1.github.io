---
title: "sdl_setvideomode(3)"
name: "sdl_setvideomode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setvideomode/"
description: "SDL_SetVideoMode – Set up a video mode with the specified width, height and bits-per-pixel."
---

<p>SDL_SetVideoMode &#8211; Set up a video mode with the specified width, height and bits-per-pixel.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_SetVideoMode</code>(<code>int width, int height, int bpp, Uint32 flags</code>);</p>
<h2>Description</h2>
<p>Set up a video mode with the specified width, height and bits-per-pixel. </p>
<p> If <code>bpp</code> is 0, it is treated as the current display bits per pixel. </p>
<p> The <code>flags</code> parameter is the same as the <code>flags</code> field of the <i></i><code>SDL_Surface</code> structure. OR&#8217;d combinations of the following values are valid.</p>
<dl COMPACT>
<dt><code>SDL_SWSURFACE</code></p>
<dd>Create the video surface in system memory</p>
<dt><code>SDL_HWSURFACE</code></p>
<dd>Create the video surface in video memory</p>
<dt><code>SDL_ASYNCBLIT</code></p>
<dd>Enables the use of asynchronous updates of the display surface. This will usually slow down blitting on single CPU machines, but may provide a speed increase on SMP systems.</p>
<dt><code>SDL_ANYFORMAT</code></p>
<dd>Normally, if a video surface of the requested bits-per-pixel (<code>bpp</code>) is not available, SDL will emulate one with a shadow surface. Passing <code>SDL_ANYFORMAT</code> prevents this and causes SDL to use the video surface, regardless of its pixel depth.</p>
<dt><code>SDL_HWPALETTE</code></p>
<dd>Give SDL exclusive palette access. Without this flag you may not always get the the colors you request with <i></i><code>SDL_SetColors</code> or <i></i><code>SDL_SetPalette</code>.</p>
<dt><code>SDL_DOUBLEBUF</code></p>
<dd>Enable hardware double buffering; only valid with SDL_HWSURFACE. Calling <i></i><code>SDL_Flip</code> will flip the buffers and update the screen. All drawing will take place on the surface that is not displayed at the moment. If double buffering could not be enabled then <code>SDL_Flip</code> will just perform a <i></i><code>SDL_UpdateRect</code> on the entire screen.</p>
<dt><code>SDL_FULLSCREEN</code></p>
<dd>SDL will attempt to use a fullscreen mode. If a hardware resolution change is not possible (for whatever reason), the next higher resolution will be used and the display window centered on a black background.</p>
<dt><code>SDL_OPENGL</code></p>
<dd>Create an OpenGL rendering context. You should have previously set OpenGL video attributes with <i></i><code>SDL_GL_SetAttribute</code>.</p>
<dt><code>SDL_OPENGLBLIT</code></p>
<dd>Create an OpenGL rendering context, like above, but allow normal blitting operations. The screen (2D) surface may have an alpha channel, and <i></i><code>SDL_UpdateRects</code> must be used for updating changes to the screen surface.</p>
<dt><code>SDL_RESIZABLE</code></p>
<dd>Create a resizable window. When the window is resized by the user a <i></i><code>SDL_VIDEORESIZE</code> event is generated and <code>SDL_SetVideoMode</code> can be called again with the new size.</p>
<dt><code>SDL_NOFRAME</code></p>
<dd>If possible, <code>SDL_NOFRAME</code> causes SDL to create a window with no title bar or frame decoration. Fullscreen modes automatically have this flag set.</dl>
<dl COMPACT>
<dd><code>Note: </p>
<p> Whatever flags</code> <code>SDL_SetVideoMode</code> could satisfy are set in the <code>flags</code> member of the returned surface.</dl>
<dl COMPACT>
<dd><code>Note: </p>
<p> The bpp</code> parameter is the number of bits per pixel, so a <code>bpp</code> of 24 uses the packed representation of 3 bytes/pixel. For the more common 4 bytes/pixel mode, use a <code>bpp</code> of 32. Somewhat oddly, both 15 and 16 will request a 2 bytes/pixel mode, but different pixel formats.</dl>
<h2>Return Value</h2>
<p>The framebuffer surface, or <code>NULL</code> if it fails. The surface returned is freed by SDL_Quit() and should nt be freed by the caller.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_LockSurface</code>, <i></i><code>SDL_SetColors</code>, <i></i><code>SDL_Flip</code>, <i></i><code>SDL_Surface</code></p>
