---
title: "sdl_setalpha(3)"
name: "sdl_setalpha"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setalpha/"
description: "SDL_SetAlpha – Adjust the alpha properties of a surface"
---

<p>SDL_SetAlpha &#8211; Adjust the alpha properties of a surface</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetAlpha</code>(<code>SDL_Surface *surface, Uint32 flag, Uint8 alpha</code>);</p>
<h2>Description</h2>
<dl COMPACT>
<dd><code>Note: </p>
<p> This function and the semantics of SDL alpha blending have changed since version 1.1.4. Up until version 1.1.5, an alpha value of 0 was considered opaque and a value of 255 was considered transparent. This has now been inverted: 0 (SDL_ALPHA_TRANSPARENT</code>) is now considered transparent and 255 (<code>SDL_ALPHA_OPAQUE</code>) is now considered opaque.</dl>
<p> <code>SDL_SetAlpha</code> is used for setting the per-surface alpha value and/or enabling and disabling alpha blending. </p>
<p> The<code>surface</code> parameter specifies which surface whose alpha attributes you wish to adjust. <code>flags</code> is used to specify whether alpha blending should be used (<code>SDL_SRCALPHA</code>) and whether the surface should use RLE acceleration for blitting (<code>SDL_RLEACCEL</code>). <code>flags</code> can be an OR&#8217;d combination of these two options, one of these options or 0. If <code>SDL_SRCALPHA</code> is not passed as a flag then all alpha information is ignored when blitting the surface. The <code>alpha</code> parameter is the per-surface alpha value; a surface need not have an alpha channel to use per-surface alpha and blitting can still be accelerated with <code>SDL_RLEACCEL</code>. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> The per-surface alpha value of 128 is considered a special case and is optimised, so it&#8217;s much faster than other per-surface values.</dl>
<p> Alpha effects surface blitting in the following ways:</p>
<dl COMPACT>
<dt>RGBA-&gt;RGB with SDL_SRCALPHA</code></p>
<dd>The source is alpha-blended with the destination, using the alpha channel. <code>SDL_SRCCOLORKEY</code> and the per-surface alpha are ignored.</p>
<dt>RGBA-&gt;RGB without <code>SDL_SRCALPHA</code></p>
<dd>The RGB data is copied from the source. The source alpha channel and the per-surface alpha value are ignored.</p>
<dt>RGB-&gt;RGBA with <code>SDL_SRCALPHA</code></p>
<dd>The source is alpha-blended with the destination using the per-surface alpha value. If <code>SDL_SRCCOLORKEY</code> is set, only the pixels not matching the colorkey value are copied. The alpha channel of the copied pixels is set to opaque.</p>
<dt>RGB-&gt;RGBA without <code>SDL_SRCALPHA</code></p>
<dd>The RGB data is copied from the source and the alpha value of the copied pixels is set to opaque. If <code>SDL_SRCCOLORKEY</code> is set, only the pixels not matching the colorkey value are copied.</p>
<dt>RGBA-&gt;RGBA with <code>SDL_SRCALPHA</code></p>
<dd>The source is alpha-blended with the destination using the source alpha channel. The alpha channel in the destination surface is left untouched. <code>SDL_SRCCOLORKEY</code> is ignored.</p>
<dt>RGBA-&gt;RGBA without <code>SDL_SRCALPHA</code></p>
<dd>The RGBA data is copied to the destination surface. If <code>SDL_SRCCOLORKEY</code> is set, only the pixels not matching the colorkey value are copied.</p>
<dt>RGB-&gt;RGB with <code>SDL_SRCALPHA</code></p>
<dd>The source is alpha-blended with the destination using the per-surface alpha value. If <code>SDL_SRCCOLORKEY</code> is set, only the pixels not matching the colorkey value are copied.</p>
<dt>RGB-&gt;RGB without <code>SDL_SRCALPHA</code></p>
<dd>The RGB data is copied from the source. If <code>SDL_SRCCOLORKEY</code> is set, only the pixels not matching the colorkey value are copied.</dl>
<dl COMPACT>
<dd><code>Note: </p>
<p>&nbsp;<wbr>Note that RGBA-&gt;RGBA blits&nbsp;<wbr>(with SDL_SRCALPHA set)&nbsp;<wbr>keep the alpha of the destination surface. This means that you cannot compose two arbitrary RGBA surfaces this way and get the result you would expect from&nbsp;<wbr>&quot;overlaying&quot;&nbsp;<wbr>them;&nbsp;<wbr>the destination alpha will work as a mask. </p>
<p> Also note that per-pixel and per-surface alpha cannot be combined; the per-pixel alpha is always used if available</dl>
<p> </code></p>
<h2>Return Value</h2>
<p>This function returns <code>0</code>, or <code>-1</code> if there was an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_MapRGBA</code>, <i></i><code>SDL_GetRGBA</code>, <i></i><code>SDL_DisplayFormatAlpha</code>, <i></i><code>SDL_BlitSurface</code></p>
