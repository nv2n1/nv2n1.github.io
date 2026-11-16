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
<dt><code>flags</code></dt>
<dd>Surface flags</dd>
<dt><code>format</code></dt>
<dd>Pixel <i>format</i></dd>
<dt><code>w, h</code></dt>
<dd>Width and height of the surface</dd>
<dt><code>pitch</code></dt>
<dd>Length of a surface scanline in bytes</dd>
<dt><code>pixels</code></dt>
<dd>Pointer to the actual pixel data</dd>
<dt><code>clip_rect</code></dt>
<dd>surface clip <i>rectangle</i></dd></dl>
<h2>Description</h2>
<p><code>SDL_Surface</code>&#8216;s represent areas of &quot;graphical&quot; memory, memory that can be drawn to. The video framebuffer is returned as a <code>SDL_Surface</code> by <i></i><code>SDL_SetVideoMode</code> and <i></i><code>SDL_GetVideoSurface</code>. Most of the fields should be pretty obvious. <code>w</code> and <code>h</code> are the width and height of the surface in pixels. <code>pixels</code> is a pointer to the actual pixel data, the surface should be <i>locked</i> before accessing this field. The <code>clip_rect</code> field is the clipping rectangle as set by <i></i><code>SDL_SetClipRect</code>. </p>
<p> The following are supported in the <code>flags</code> field.</p>
<dl COMPACT>
<dt><code>SDL_SWSURFACE</code></dt>
<dd>Surface is stored in system memory</dd>
<dt><code>SDL_HWSURFACE</code></dt>
<dd>Surface is stored in video memory</dd>
<dt><code>SDL_ASYNCBLIT</code></dt>
<dd>Surface uses asynchronous blits if possible</dd>
<dt><code>SDL_ANYFORMAT</code></dt>
<dd>Allows any pixel-format (Display surface)</dd>
<dt><code>SDL_HWPALETTE</code></dt>
<dd>Surface has exclusive palette</dd>
<dt><code>SDL_DOUBLEBUF</code></dt>
<dd>Surface is double buffered (Display surface)</dd>
<dt><code>SDL_FULLSCREEN</code></dt>
<dd>Surface is full screen (Display Surface)</dd>
<dt><code>SDL_OPENGL</code></dt>
<dd>Surface has an OpenGL context (Display Surface)</dd>
<dt><code>SDL_OPENGLBLIT</code></dt>
<dd>Surface supports OpenGL blitting (Display Surface)</dd>
<dt><code>SDL_RESIZABLE</code></dt>
<dd>Surface is resizable (Display Surface)</dd>
<dt><code>SDL_HWACCEL</code></dt>
<dd>Surface blit uses hardware acceleration</dd>
<dt><code>SDL_SRCCOLORKEY</code></dt>
<dd>Surface use colorkey blitting</dd>
<dt><code>SDL_RLEACCEL</code></dt>
<dd>Colorkey blitting is accelerated with RLE</dd>
<dt><code>SDL_SRCALPHA</code></dt>
<dd>Surface blit uses alpha blending</dd>
<dt><code>SDL_PREALLOC</code></dt>
<dd>Surface uses preallocated memory</dd></dl>
<h2>See Also</h2>
<p><i></i><code>SDL_PixelFormat</code></p>
