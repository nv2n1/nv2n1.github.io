---
title: "set_gfx_mode(3)"
name: "set_gfx_mode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_gfx_mode/"
description: "set_gfx_mode – Sets a graphic video mode. Allegro game programming library."
---

<p>set_gfx_mode &#8211; Sets a graphic video mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_gfx_mode(int card, int w, int h, int v_w, int v_h);</code></pre>
<h2>Description</h2>
<p>Switches into graphics mode. The card parameter should usually be one of the Allegro magic drivers (read introduction of chapter &quot;Graphics modes&quot;) or see the platform specific documentation for a list of the available drivers. The w and h parameters specify what screen resolution you want. The color depth of the graphic mode has to be specified before calling this function with set_color_depth(). </p>
<p> The v_w and v_h parameters specify the minimum virtual screen size, in case you need a large virtual screen for hardware scrolling or page flipping. You should set them to zero if you don&#8217;t care about the virtual screen size. </p>
<p> When you call set_gfx_mode(), the v_w and v_h parameters represent the minimum size of virtual screen that is acceptable for your program. The range of possible sizes is usually very restricted, and Allegro may end up creating a virtual screen much larger than the one you request. Allowed sizes are driver dependent and some drivers do not allow virtual screens that are larger than the visible screen at all: don&#8217;t assume that whatever you pass will always work. </p>
<p> In mode-X the virtual width can be any multiple of eight greater than or equal to the physical screen width, and the virtual height will be set accordingly (the VGA has 256k of vram, so the virtual height will be 256*1024/virtual_width). </p>
<p> Currently, using a big virtual screen for page flipping is considered bad practice. There are platforms which don&#8217;t support virtual screens bigger than the physical screen but can create different video pages to flip back and forth. This means that, if you want page flipping and aren&#8217;t going to use hardware scrolling, you should call set_gfx_mode() with (0,0) as the virtual screen size and later create the different video pages with create_video_bitmap(). Otherwise your program will be limited to the platforms supporting hardware scrolling. </p>
<p> After you select a graphics mode, the physical and virtual screen sizes can be checked with the macros SCREEN_W, SCREEN_H, VIRTUAL_W, and VIRTUAL_H.</p>
<h2>Return Value</h2>
<p>Returns zero on success. On failure returns a negative number and stores a description of the problem in allegro_error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-request_refresh_rate/">request_refresh_rate</a></code>(3), <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-get_desktop_resolution/">get_desktop_resolution</a></code>(3), <code><a href="/docs/linux/man/3-screen_w/">SCREEN_W</a></code>(3), <code><a href="/docs/linux/man/3-screen_h/">SCREEN_H</a></code>(3), <code><a href="/docs/linux/man/3-virtual_w/">VIRTUAL_W</a></code>(3), <code><a href="/docs/linux/man/3-virtual_h/">VIRTUAL_H</a></code>(3) </p>
