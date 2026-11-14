---
title: "sdl_videoinfo(3)"
name: "sdl_videoinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_videoinfo/"
description: "SDL_VideoInfo – Video Target information"
---

<p>SDL_VideoInfo &#8211; Video Target information</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint32 hw_available:1;
 Uint32 wm_available:1;
 Uint32 blit_hw:1;
 Uint32 blit_hw_CC:1;
 Uint32 blit_hw_A:1;
 Uint32 blit_sw:1;
 Uint32 blit_sw_CC:1;
 Uint32 blit_sw_A:1;
 Uint32 blit_fill;
 Uint32 video_mem;
 SDL_PixelFormat *vfmt;
} SDL_VideoInfo;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>hw_available</code></p>
<dd>Is it possible to create hardware surfaces?</p>
<dt><code>wm_available</code></p>
<dd>Is there a window manager available</p>
<dt><code>blit_hw</code></p>
<dd>Are hardware to hardware blits accelerated?</p>
<dt><code>blit_hw_CC</code></p>
<dd>Are hardware to hardware colorkey blits accelerated?</p>
<dt><code>blit_hw_A</code></p>
<dd>Are hardware to hardware alpha blits accelerated?</p>
<dt><code>blit_sw</code></p>
<dd>Are software to hardware blits accelerated?</p>
<dt><code>blit_sw_CC</code></p>
<dd>Are software to hardware colorkey blits accelerated?</p>
<dt><code>blit_sw_A</code></p>
<dd>Are software to hardware alpha blits accelerated?</p>
<dt><code>blit_fill</code></p>
<dd>Are color fills accelerated?</p>
<dt><code>video_mem</code></p>
<dd>Total amount of video memory in Kilobytes</p>
<dt><code>vfmt</code></p>
<dd><i>Pixel format</i> of the video device</dl>
<h2>Description</h2>
<p>This (read-only) structure is returned by <i></i><code>SDL_GetVideoInfo</code>. It contains information on either the &#8216;best&#8217; available mode (if called before <i></i><code>SDL_SetVideoMode</code>) or the current video mode.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_PixelFormat</code>, <i></i><code>SDL_GetVideoInfo</code></p>
