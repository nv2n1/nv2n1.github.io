---
title: "gfx_capabilities(3)"
name: "gfx_capabilities"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gfx_capabilities/"
description: "gfx_capabilities – Bitfield describing video hardware capabilities. Allegro game programming library."
---

<h2>NAME</h2>
<p> gfx_capabilities &#8211; Bitfield describing video hardware capabilities. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int gfx_capabilities;</code></p>
<h2>DESCRIPTION</h2>
<p> Bitfield describing the capabilities of the current graphics driver and video hardware. This may contain combination any of the flags: </p>
<p> <code>GFX_CAN_SCROLL:</code> Indicates that the scroll_screen() function may be used with this driver. </p>
<p> <code>GFX_CAN_TRIPLE_BUFFER:</code> Indicates that the request_scroll() and poll_scroll() functions may be used with this driver. If this flag is not set, it is possible that the enable_triple_buffer() function may be able to activate it. </p>
<p> <code>GFX_HW_CURSOR:</code> Indicates that a hardware mouse cursor is in use. When this flag is set, it is safe to draw onto the screen without hiding the mouse pointer first. Note that not every cursor graphic can be implemented in hardware: in particular VBE/AF only supports 2-color images up to 32&#215;32 in size, where the second color is an exact inverse of the first. This means that Allegro may need to switch between hardware and software cursors at any point during the execution of your program, so you should not assume that this flag will remain constant for long periods of time. It only tells you whether a hardware cursor is in use at the current time, and may change whenever you hide/redisplay the pointer. </p>
<p> <code>GFX_SYSTEM_CURSOR</code> Indicates that the mouse cursor is the default system cursor, not Allegro&#8217;s custom cursor. </p>
<p> <code>GFX_HW_HLINE:</code> Indicates that the normal opaque version of the hline() function is implemented using a hardware accelerator. This will improve the performance not only of hline() itself, but also of many other functions that use it as a workhorse, for example circlefill(), triangle(), and floodfill(). </p>
<p> <code>GFX_HW_HLINE_XOR:</code> Indicates that the XOR version of the hline() function, and any other functions that use it as a workhorse, are implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_HLINE_SOLID_PATTERN:</code> Indicates that the solid and masked pattern modes of the hline() function, and any other functions that use it as a workhorse, are implemented using a hardware accelerator (see note below). </p>
<p> <code>GFX_HW_HLINE_COPY_PATTERN:</code> Indicates that the copy pattern mode of the hline() function, and any other functions that use it as a workhorse, are implemented using a hardware accelerator (see note below). </p>
<p> <code>GFX_HW_FILL:</code> Indicates that the opaque version of the rectfill() function, the clear_bitmap() routine, and clear_to_color(), are implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_FILL_XOR:</code> Indicates that the XOR version of the rectfill() function is implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_FILL_SOLID_PATTERN:</code> Indicates that the solid and masked pattern modes of the rectfill() function are implemented using a hardware accelerator (see note below). </p>
<p> <code>GFX_HW_FILL_COPY_PATTERN:</code> Indicates that the copy pattern mode of the rectfill() function is implemented using a hardware accelerator (see note below). </p>
<p> <code>GFX_HW_LINE:</code> Indicates that the opaque mode line() and vline() functions are implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_LINE_XOR:</code> Indicates that the XOR version of the line() and vline() functions are implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_TRIANGLE:</code> Indicates that the opaque mode triangle() function is implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_TRIANGLE_XOR:</code> Indicates that the XOR version of the triangle() function is implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_GLYPH:</code> Indicates that monochrome character expansion (for text drawing) is implemented using a hardware accelerator. </p>
<p> <code>GFX_HW_VRAM_BLIT:</code> Indicates that blitting from one part of the screen to another is implemented using a hardware accelerator. If this flag is set, blitting within the video memory will almost certainly be the fastest possible way to display an image, so it may be worth storing some of your more frequently used graphics in an offscreen portion of the video memory. </p>
<p> <code>GFX_HW_VRAM_BLIT_MASKED:</code> Indicates that the masked_blit() routine is capable of a hardware accelerated copy from one part of video memory to another, and that draw_sprite() will use a hardware copy when given a sub-bitmap of the screen or a video memory bitmap as the source image. If this flag is set, copying within the video memory will almost certainly be the fastest possible way to display an image, so it may be worth storing some of your more frequently used sprites in an offscreen portion of the video memory. </p>
<p> Warning: if this flag is not set, masked_blit() and draw_sprite() will not work correctly when used with a video memory source image! You must only try to use these functions to copy within the video memory if they are supported in hardware. </p>
<p> <code>GFX_HW_MEM_BLIT:</code> Indicates that blitting from a memory bitmap onto the screen is being accelerated in hardware. </p>
<p> <code>GFX_HW_MEM_BLIT_MASKED:</code> Indicates that the masked_blit() and draw_sprite() functions are being accelerated in hardware when the source image is a memory bitmap and the destination is the physical screen. </p>
<p> <code>GFX_HW_SYS_TO_VRAM_BLIT:</code> Indicates that blitting from a system bitmap onto the screen is being accelerated in hardware. Note that some acceleration may be present even if this flag is not set, because system bitmaps can benefit from normal memory to screen blitting as well. This flag will only be set if system bitmaps have further acceleration above and beyond what is provided by GFX_HW_MEM_BLIT. </p>
<p> <code>GFX_HW_SYS_TO_VRAM_BLIT_MASKED:</code> Indicates that the masked_blit() and draw_sprite() functions are being accelerated in hardware when the source image is a system bitmap and the destination is the physical screen. Note that some acceleration may be present even if this flag is not set, because system bitmaps can benefit from normal memory to screen blitting as well. This flag will only be set if system bitmaps have further acceleration above and beyond what is provided by GFX_HW_MEM_BLIT_MASKED. </p>
<p> <code>GFX_HW_VRAM_STRETCH_BLIT:</code> Indicates that stretched blitting of video bitmaps onto the screen is implemented using hardware acceleration. </p>
<p> <code>GFX_HW_SYS_STRETCH_BLIT:</code> Indicates that stretched blitting of system bitmaps onto the screen is implemented using hardware acceleration. </p>
<p> <code>GFX_HW_VRAM_STRETCH_BLIT_MASKED:</code> Indicates that masked stretched blitting (including stretch_sprite) of video bitmaps onto the screen is implemented using hardware acceleration. NOTE: some display drivers may show artifacts when this function is used. If the image does not look correct try updating your video drivers. </p>
<p> <code>GFX_HW_SYS_STRETCH_BLIT_MASKED:</code> Indicates that masked stretched blitting (including stretch_sprite) of system bitmaps onto the screen is implemented using hardware acceleration. NOTE: some display drivers may show artefact&#8217;s when this function is used. If the image does not look correct try updating your video drivers. </p>
<p> Note: even if the capabilities information says that patterned drawing is supported by the hardware, it will not be possible for every size of pattern. VBE/AF only supports patterns up to 8&#215;8 in size, so Allegro will fall back on the original non-accelerated drawing routines whenever you use a pattern larger than this. </p>
<p> Note2: these hardware acceleration features will only take effect when you are drawing directly onto the screen bitmap, a video memory bitmap, or a sub-bitmap thereof. Accelerated hardware is most useful in a page flipping or triple buffering setup, and is unlikely to make any difference to the classic &quot;draw onto a memory bitmap, then blit to the screen&quot; system. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-screen/">screen</a></code>(3), <code><a href="/docs/linux/man/3-create_video_bitmap/">create_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-scroll_screen/">scroll_screen</a></code>(3), <code><a href="/docs/linux/man/3-request_scroll/">request_scroll</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-enable_triple_buffer/">enable_triple_buffer</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exaccel/">exaccel</a></code>(3), <code><a href="/docs/linux/man/3-exsyscur/">exsyscur</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
