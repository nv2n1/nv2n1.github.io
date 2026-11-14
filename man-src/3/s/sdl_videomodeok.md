---
title: "sdl_videomodeok(3)"
name: "sdl_videomodeok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_videomodeok/"
description: "SDL_VideoModeOK – Check to see if a particular video mode is supported."
---

<p>SDL_VideoModeOK &#8211; Check to see if a particular video mode is supported.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_VideoModeOK</code>(<code>int width, int height, int bpp, Uint32 flags</code>);</p>
<h2>Description</h2>
<p><code>SDL_VideoModeOK</code> returns <code>0</code> if the requested mode is not supported under any bit depth, or returns the bits-per-pixel of the closest available mode with the given width, height and requested <i>surface</i> flags (see <i></i><code>SDL_SetVideoMode</code>). </p>
<p> The bits-per-pixel value returned is only a suggested mode. You can usually request and bpp you want when <i>setting</i> the video mode and SDL will emulate that color depth with a shadow video surface. </p>
<p> The arguments to <code>SDL_VideoModeOK</code> are the same ones you would pass to <i>SDL_SetVideoMode</i></p>
<h2>Example</h2>
<pre><tt>SDL_Surface *screen;
Uint32 bpp;
.
.
.
printf(&quot;Checking mode 640x480 [at] 16bpp.
&quot;);
bpp=SDL_VideoModeOK(640, 480, 16, SDL_HWSURFACE);
if(!bpp){
 printf(&quot;Mode not available.
&quot;);
 exit(-1);
}
printf(&quot;SDL Recommends 640x480@%dbpp.
&quot;, bpp);
screen=SDL_SetVideoMode(640, 480, bpp, SDL_HWSURFACE);
.
.</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_GetVideoInfo</code></p>
