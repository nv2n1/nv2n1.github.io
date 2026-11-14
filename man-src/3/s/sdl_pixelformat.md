---
title: "sdl_pixelformat(3)"
name: "sdl_pixelformat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_pixelformat/"
description: "SDL_PixelFormat – Stores surface format information"
---

<p>SDL_PixelFormat &#8211; Stores surface format information</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct SDL_PixelFormat {
 SDL_Palette *palette;
 Uint8 BitsPerPixel;
 Uint8 BytesPerPixel;
 Uint8 Rloss, Gloss, Bloss, Aloss;
 Uint8 Rshift, Gshift, Bshift, Ashift;
 Uint32 Rmask, Gmask, Bmask, Amask;
 Uint32 colorkey;
 Uint8 alpha;
} SDL_PixelFormat;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>palette</code></p>
<dd>Pointer to the <i>palette</i>, or <code>NULL</code> if the <code>BitsPerPixel</code>&gt;8</p>
<dt><code>BitsPerPixel</code></p>
<dd>The number of bits used to represent each pixel in a surface. Usually 8, 16, 24 or 32.</p>
<dt><code>BytesPerPixel</code></p>
<dd>The number of bytes used to represent each pixel in a surface. Usually one to four.</p>
<dt><code>[RGBA]mask</code></p>
<dd>Binary mask used to retrieve individual color values</p>
<dt><code>[RGBA]loss</code></p>
<dd>Precision loss of each color component (2^[RGBA]loss)</p>
<dt><code>[RGBA]shift</code></p>
<dd>Binary left shift of each color component in the pixel value</p>
<dt><code>colorkey</code></p>
<dd>Pixel value of transparent pixels</p>
<dt><code>alpha</code></p>
<dd>Overall surface alpha value</dl>
<h2>Description</h2>
<p>A <code>SDL_PixelFormat</code> describes the format of the pixel data stored at the <code>pixels</code> field of a <i></i><code>SDL_Surface</code>. Every surface stores a <code>SDL_PixelFormat</code> in the <code>format</code> field. </p>
<p> If you wish to do pixel level modifications on a surface, then understanding how SDL stores its color information is essential. </p>
<p> 8-bit pixel formats are the easiest to understand. Since its an 8-bit format, we have 8 <code>BitsPerPixel</code> and 1 <code>BytesPerPixel</code>. Since <code>BytesPerPixel</code> is 1, all pixels are represented by a Uint8 which contains an index into <code>palette</code>-&gt;<code>colors</code>. So, to determine the color of a pixel in a 8-bit surface: we read the color index from <code>surface</code>-&gt;<code>pixels</code> and we use that index to read the <i></i><code>SDL_Color</code> structure from <code>surface</code>-&gt;<code>format</code>-&gt;<code>palette</code>-&gt;<code>colors</code>. Like so: </p>
<pre><tt>SDL_Surface *surface;
SDL_PixelFormat *fmt;
SDL_Color *color;
Uint8 index;
.
.
/* Create surface */
.
.
fmt=surface-&gt;format;
/* Check the bitdepth of the surface */
if(fmt-&gt;BitsPerPixel!=8){
 fprintf(stderr, &quot;Not an 8-bit surface.
&quot;);
 return(-1);
}
/* Lock the surface */
SDL_LockSurface(surface);
/* Get the topleft pixel */
index=*(Uint8 *)surface-&gt;pixels;
color=fmt-&gt;palette-&gt;colors[index];
/* Unlock the surface */
SDL_UnlockSurface(surface);
printf(&quot;Pixel Color-&gt; Red: %d, Green: %d, Blue: %d. Index: %d
&quot;,
 color-&gt;r, color-&gt;g, color-&gt;b, index);
.
.</tt></pre>
<p>Pixel formats above 8-bit are an entirely different experience. They are considered to be &quot;TrueColor&quot; formats and the color information is stored in the pixels themselves, not in a palette. The mask, shift and loss fields tell us how the color information is encoded. The mask fields allow us to isolate each color component, the shift fields tell us the number of bits to the right of each component in the pixel value and the loss fields tell us the number of bits lost from each component when packing 8-bit color component in a pixel. </p>
<pre><tt>/* Extracting color components from a 32-bit color value */
SDL_PixelFormat *fmt;
SDL_Surface *surface;
Uint32 temp, pixel;
Uint8 red, green, blue, alpha;
.
.
.
fmt=surface-&gt;format;
SDL_LockSurface(surface);
pixel=*((Uint32*)surface-&gt;pixels);
SDL_UnlockSurface(surface);
/* Get Red component */
temp=pixel&amp;fmt-&gt;Rmask; /* Isolate red component */
temp=temp&gt;&gt;fmt-&gt;Rshift;/* Shift it down to 8-bit */
temp=temp&lt;&lt;fmt-&gt;Rloss; /* Expand to a full 8-bit number */
red=(Uint8)temp;
/* Get Green component */
temp=pixel&amp;fmt-&gt;Gmask; /* Isolate green component */
temp=temp&gt;&gt;fmt-&gt;Gshift;/* Shift it down to 8-bit */
temp=temp&lt;&lt;fmt-&gt;Gloss; /* Expand to a full 8-bit number */
green=(Uint8)temp;
/* Get Blue component */
temp=pixel&amp;fmt-&gt;Bmask; /* Isolate blue component */
temp=temp&gt;&gt;fmt-&gt;Bshift;/* Shift it down to 8-bit */
temp=temp&lt;&lt;fmt-&gt;Bloss; /* Expand to a full 8-bit number */
blue=(Uint8)temp;
/* Get Alpha component */
temp=pixel&amp;fmt-&gt;Amask; /* Isolate alpha component */
temp=temp&gt;&gt;fmt-&gt;Ashift;/* Shift it down to 8-bit */
temp=temp&lt;&lt;fmt-&gt;Aloss; /* Expand to a full 8-bit number */
alpha=(Uint8)temp;
printf(&quot;Pixel Color -&gt; R: %d, G: %d, B: %d, A: %d
&quot;, red, green, blue, alpha);
.
.
.</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_Surface</code>, <i></i><code>SDL_MapRGB</code></p>
