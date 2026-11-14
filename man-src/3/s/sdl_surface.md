---
title: "sdl_surface(3)"
name: "sdl_surface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_surface/"
description: "SDL_Surface – Graphical Surface Structure"
---

<p>SDL_Surface &#8211; Graphical Surface Structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct SDL_Surface {
 Uint32 flags; /* Read-only */
 SDL_PixelFormat *format; /* Read-only */
 int w, h; /* Read-only */
 Uint16 pitch; /* Read-only */
 void *pixels; /* Read-write */
 /* clipping information */
 SDL_Rect clip_rect; /* Read-only */
 /* Reference count -- used when freeing surface */
 int refcount; /* Read-mostly */
 /* This structure also contains private fields not shown here */
} SDL_Surface;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>Surface flags</p>
<dt><code>format</code></p>
<dd>Pixel <i>format</i></p>
<dt><code>w, h</code></p>
<dd>Width and height of the surface</p>
<dt><code>pitch</code></p>
<dd>Length of a surface scanline in bytes</p>
<dt><code>pixels</code></p>
<dd>Pointer to the actual pixel data</p>
<dt><code>clip_rect</code></p>
<dd>surface clip <i>rectangle</i></dl>
<h2>Description</h2>
<p><code>SDL_Surface</code>&#8216;s represent areas of &quot;graphical&quot; memory, memory that can be drawn to. The video framebuffer is returned as a <code>SDL_Surface</code> by <i></i><code>SDL_SetVideoMode</code> and <i></i><code>SDL_GetVideoSurface</code>. Most of the fields should be pretty obvious. <code>w</code> and <code>h</code> are the width and height of the surface in pixels. <code>pixels</code> is a pointer to the actual pixel data, the surface should be <i>locked</i> before accessing this field. The <code>clip_rect</code> field is the clipping rectangle as set by <i></i><code>SDL_SetClipRect</code>. </p>
<p> The following are supported in the <code>flags</code> field.</p>
<dl COMPACT>
<dt><code>SDL_SWSURFACE</code></p>
<dd>Surface is stored in system memory</p>
<dt><code>SDL_HWSURFACE</code></p>
<dd>Surface is stored in video memory</p>
<dt><code>SDL_ASYNCBLIT</code></p>
<dd>Surface uses asynchronous blits if possible</p>
<dt><code>SDL_ANYFORMAT</code></p>
<dd>Allows any pixel-format (Display surface)</p>
<dt><code>SDL_HWPALETTE</code></p>
<dd>Surface has exclusive palette</p>
<dt><code>SDL_DOUBLEBUF</code></p>
<dd>Surface is double buffered (Display surface)</p>
<dt><code>SDL_FULLSCREEN</code></p>
<dd>Surface is full screen (Display Surface)</p>
<dt><code>SDL_OPENGL</code></p>
<dd>Surface has an OpenGL context (Display Surface)</p>
<dt><code>SDL_OPENGLBLIT</code></p>
<dd>Surface supports OpenGL blitting (Display Surface)</p>
<dt><code>SDL_RESIZABLE</code></p>
<dd>Surface is resizable (Display Surface)</p>
<dt><code>SDL_HWACCEL</code></p>
<dd>Surface blit uses hardware acceleration</p>
<dt><code>SDL_SRCCOLORKEY</code></p>
<dd>Surface use colorkey blitting</p>
<dt><code>SDL_RLEACCEL</code></p>
<dd>Colorkey blitting is accelerated with RLE</p>
<dt><code>SDL_SRCALPHA</code></p>
<dd>Surface blit uses alpha blending</p>
<dt><code>SDL_PREALLOC</code></p>
<dd>Surface uses preallocated memory</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_PixelFormat</code></p>
