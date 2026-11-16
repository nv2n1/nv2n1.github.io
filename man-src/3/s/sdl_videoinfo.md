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
<dt><code>hw_available</code></dt>
<dd>Is it possible to create hardware surfaces?</dd>
<dt><code>wm_available</code></dt>
<dd>Is there a window manager available</dd>
<dt><code>blit_hw</code></dt>
<dd>Are hardware to hardware blits accelerated?</dd>
<dt><code>blit_hw_CC</code></dt>
<dd>Are hardware to hardware colorkey blits accelerated?</dd>
<dt><code>blit_hw_A</code></dt>
<dd>Are hardware to hardware alpha blits accelerated?</dd>
<dt><code>blit_sw</code></dt>
<dd>Are software to hardware blits accelerated?</dd>
<dt><code>blit_sw_CC</code></dt>
<dd>Are software to hardware colorkey blits accelerated?</dd>
<dt><code>blit_sw_A</code></dt>
<dd>Are software to hardware alpha blits accelerated?</dd>
<dt><code>blit_fill</code></dt>
<dd>Are color fills accelerated?</dd>
<dt><code>video_mem</code></dt>
<dd>Total amount of video memory in Kilobytes</dd>
<dt><code>vfmt</code></dt>
<dd><i>Pixel format</i> of the video device</dd></dl>
<h2>Description</h2>
<p>This (read-only) structure is returned by <i></i><code>SDL_GetVideoInfo</code>. It contains information on either the &#8216;best&#8217; available mode (if called before <i></i><code>SDL_SetVideoMode</code>) or the current video mode.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_PixelFormat</code>, <i></i><code>SDL_GetVideoInfo</code></p>
