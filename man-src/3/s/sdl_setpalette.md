---
title: "sdl_setpalette(3)"
name: "sdl_setpalette"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setpalette/"
description: "SDL_SetPalette – Sets the colors in the palette of an 8-bit surface."
---

<p>SDL_SetPalette &#8211; Sets the colors in the palette of an 8-bit surface.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetPalette</code>(<code>SDL_Surface *surface, int flags, SDL_Color *colors, int firstcolor, int ncolors</code>);</p>
<h2>Description</h2>
<p>Sets a portion of the palette for the given 8-bit surface. </p>
<p> Palettized (8-bit) screen surfaces with the <code>SDL_HWPALETTE</code> flag have two palettes, a logical palette that is used for mapping blits to/from the surface and a physical palette (that determines how the hardware will map the colors to the display). <i>SDL_BlitSurface</i> always uses the logical palette when blitting surfaces (if it has to convert between surface pixel formats). Because of this, it is often useful to modify only one or the other palette to achieve various special color effects (e.g., screen fading, color flashes, screen dimming). </p>
<p> This function can modify either the logical or physical palette by specifing <code>SDL_LOGPAL</code> or <code>SDL_PHYSPAL</code>the in the <code>flags</code> parameter. </p>
<p> When <code>surface</code> is the surface associated with the current display, the display colormap will be updated with the requested colors. If <code>SDL_HWPALETTE</code> was set in <i>SDL_SetVideoMode</i> flags, <code>SDL_SetPalette</code> will always return <code>1</code>, and the palette is guaranteed to be set the way you desire, even if the window colormap has to be warped or run under emulation. </p>
<p> The color components of a <i></i><code>SDL_Color</code> structure are 8-bits in size, giving you a total of 256^3=16777216 colors.</p>
<h2>Return Value</h2>
<p>If <code>surface</code> is not a palettized surface, this function does nothing, returning <code>0</code>. If all of the colors were set as passed to <code>SDL_SetPalette</code>, it will return <code>1</code>. If not all the color entries were set exactly as given, it will return <code>0</code>, and you should look at the surface palette to determine the actual color palette.</p>
<h2>Example</h2>
<pre><tt> /* Create a display surface with a grayscale palette */
 SDL_Surface *screen;
 SDL_Color colors[256];
 int i;
 .
 .
 .
 /* Fill colors with color information */
 for(i=0;i&lt;256;i++){
 colors[i].r=i;
 colors[i].g=i;
 colors[i].b=i;
 }
 /* Create display */
 screen=SDL_SetVideoMode(640, 480, 8, SDL_HWPALETTE);
 if(!screen){
 printf(&quot;Couldn't set video mode: %s
&quot;, SDL_GetError());
 exit(-1);
 }
 /* Set palette */
 SDL_SetPalette(screen, SDL_LOGPAL|SDL_PHYSPAL, colors, 0, 256);
 .
 .
 .
 .</tt></pre>
<h2>See Also</h2>
<p><i>SDL_SetColors</i>, <i>SDL_SetVideoMode</i>, <i>SDL_Surface</i>, <i>SDL_Color</i></p>
