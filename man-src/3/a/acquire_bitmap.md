---
title: "acquire_bitmap(3)"
name: "acquire_bitmap"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acquire_bitmap/"
description: "acquire_bitmap – Locks the bitmap before drawing onto it. Allegro game programming library."
---

<h2>NAME</h2>
<p> acquire_bitmap &#8211; Locks the bitmap before drawing onto it. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void acquire_bitmap(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Acquires the specified video bitmap prior to drawing onto it. You never need to call the function explicitly as it is low level, and will only give you a speed up if you know what you are doing. Using it wrongly may cause slowdown, or even lock up your program. </p>
<p> Note: You do never need to use acquire_bitmap on a memory bitmap, i.e. a normal bitmap created with create_bitmap. It will simply do nothing in that case. </p>
<p> It still can be useful, because e.g. under the current DirectDraw driver of Allegro, most drawing functions need to lock a video bitmap before drawing to it. But doing this is very slow, so you will get much better performance if you acquire the screen just once at the start of your main redraw function, then call multiple drawing operations which need the bitmap locked, and only release it when done. </p>
<p> Multiple acquire calls may be nested, but you must make sure to match up the acquire_bitmap and release_bitmap calls. Be warned that DirectX and X11 programs activate a mutex lock whenever a surface is locked, which prevents them from getting any input messages, so you must be sure to release all your bitmaps before using any timer, keyboard, or other non-graphics routines! </p>
<p> Note that if you are using hardware accelerated VRAM-&gt;VRAM functions, you should not call acquire_bitmap(). Such functions need an unlocked target bitmap under DirectX, so there is now just the opposite case from before &#8211; if the bitmap is already locked with acquire_bitmap, the drawing operation has to unlock it. </p>
<p> Note: For backwards compatibility, the unlocking behavior of such functions is permanent. That is, if you call acquire_bitmap first, then call e.g. an accelerated blit, the DirectX bitmap will be unlocked internally (it won&#8217;t affect the nesting counter of acquire/release calls). </p>
<p> There is no clear cross-platform way in this Allegro version to know which drawing operations need a locked/unlocked state. For example a normal rectfill most probably is accelerated under DirectX, and therefore needs the screen unlocked, but an XOR rectfill, or one with blending activated, most probably is not, and therefore locks the screen. And while the DirectX driver will do automatic unlocking, there is no such thing under X11, where the function is used to synchronize X11 calls from different threads. Your best bet is to never use acquire_bitmap &#8211; changes are you are doing something in the wrong way if you think you need it. </p>
<p> Warning: This function can be very dangerous to use, since the whole program may get locked while the bitmap is locked. So the lock should only be held for a short time, and you should not call anything but drawing operations onto the locked video bitmap while a lock is in place. Especially don&#8217;t call things like show_mouse (or scare_mouse which calls that) or readkey, since it will most likely deadlock your entire program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-release_bitmap/">release_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-acquire_screen/">acquire_screen</a></code>(3), <code><a href="/docs/linux/man/3-release_screen/">release_screen</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exaccel/">exaccel</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
