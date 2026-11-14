---
title: "sdl_creatergbsurface(3)"
name: "sdl_creatergbsurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_creatergbsurface/"
description: "SDL_CreateRGBSurface – Create an empty SDL_Surface"
---

<p>SDL_CreateRGBSurface &#8211; Create an empty SDL_Surface</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_CreateRGBSurface</code>(<code>Uint32 flags, int width, int height, int depth, Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask</code>);</p>
<h2>Description</h2>
<p>Allocate an empty surface (must be called after <i>SDL_SetVideoMode</i>) </p>
<p> If <code>depth</code> is 8 bits an empty palette is allocated for the surface, otherwise a &#8216;packed-pixel&#8217; <i></i><code>SDL_PixelFormat</code> is created using the <code>[RGBA]mask</code>&#8216;s provided (see <i></i><code>SDL_PixelFormat</code>). The <code>flags</code> specifies the type of surface that should be created, it is an OR&#8217;d combination of the following possible values.</p>
<dl COMPACT>
<dt><code>SDL_SWSURFACE</code></p>
<dd>SDL will create the surface in system memory. This improves the performance of pixel level access, however you may not be able to take advantage of some types of hardware blitting.</p>
<dt><code>SDL_HWSURFACE</code></p>
<dd>SDL will attempt to create the surface in video memory. This will allow SDL to take advantage of Video-&gt;Video blits (which are often accelerated).</p>
<dt><code>SDL_SRCCOLORKEY</code></p>
<dd>This flag turns on colourkeying for blits from this surface. If <code>SDL_HWSURFACE</code> is also specified and colourkeyed blits are hardware-accelerated, then SDL will attempt to place the surface in video memory. Use <i></i><code>SDL_SetColorKey</code> to set or clear this flag after surface creation.</p>
<dt><code>SDL_SRCALPHA</code></p>
<dd>This flag turns on alpha-blending for blits from this surface. If <code>SDL_HWSURFACE</code> is also specified and alpha-blending blits are hardware-accelerated, then the surface will be placed in video memory if possible. Use <i></i><code>SDL_SetAlpha</code> to set or clear this flag after surface creation.</dl>
<dl COMPACT>
<dd><code>Note: </p>
<p> If an alpha-channel is specified (that is, if Amask</code> is nonzero), then the <code>SDL_SRCALPHA</code> flag is automatically set. You may remove this flag by calling <i></i><code>SDL_SetAlpha</code> after surface creation.</dl>
<h2>Return Value</h2>
<p>Returns the created surface, or <code>NULL</code> upon error.</p>
<h2>Example</h2>
<pre><tt> /* Create a 32-bit surface with the bytes of each pixel in R,G,B,A order,
 as expected by OpenGL for textures */
 SDL_Surface *surface;
 Uint32 rmask, gmask, bmask, amask;
 /* SDL interprets each pixel as a 32-bit number, so our masks must depend
 on the endianness (byte order) of the machine */
#if SDL_BYTEORDER == SDL_BIG_ENDIAN
 rmask = 0xff000000;
 gmask = 0x00ff0000;
 bmask = 0x0000ff00;
 amask = 0x000000ff;
#else
 rmask = 0x000000ff;
 gmask = 0x0000ff00;
 bmask = 0x00ff0000;
 amask = 0xff000000;
#endif
 surface = SDL_CreateRGBSurface(SDL_SWSURFACE, width, height, 32,
 rmask, gmask, bmask, amask);
 if(surface == NULL) {
 fprintf(stderr, &quot;CreateRGBSurface failed: %s
&quot;, SDL_GetError());
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 }</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateRGBSurfaceFrom</code>, <i></i><code>SDL_FreeSurface</code>, <i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_LockSurface</code>, <i></i><code>SDL_PixelFormat</code>, <i></i><code>SDL_Surface</code> <i></i><code>SDL_SetAlpha</code> <i></i><code>SDL_SetColorKey</code></p>
