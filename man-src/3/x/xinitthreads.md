---
title: "xinitthreads(3)"
name: "xinitthreads"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xinitthreads/"
description: "XInitThreads, XLockDisplay, XUnlockDisplay – multi-threading support"
---

<p>XInitThreads, XLockDisplay, XUnlockDisplay &#8211; multi-threading support </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XInitThreads(void);</p>
<dd>void XLockDisplay(Display *<i>display</i>);</p>
<dd>void XUnlockDisplay(Display *<i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</dl>
<h2>Description</h2>
<p>The <code>XInitThreads</code> function initializes Xlib support for concurrent threads. This function must be the first Xlib function a multi-threaded program calls, and it must complete before any other Xlib call is made. This function returns a nonzero status if initialization was successful; otherwise, it returns zero. On systems that do not support threads, this function always returns zero. </p>
<p> It is only necessary to call this function if multiple threads might use Xlib concurrently. If all calls to Xlib functions are protected by some other access mechanism (for example, a mutual exclusion lock in a toolkit or through explicit client programming), Xlib thread initialization is not required. It is recommended that single-threaded programs not call this function. </p>
<p> The <code>XLockDisplay</code> function locks out all other threads from using the specified display. Other threads attempting to use the display will block until the display is unlocked by this thread. Nested calls to <code>XLockDisplay</code> work correctly; the display will not actually be unlocked until <code>XUnlockDisplay</code> has been called the same number of times as <code>XLockDisplay</code>. This function has no effect unless Xlib was successfully initialized for threads using <code>XInitThreads</code>. </p>
<p> The <code>XUnlockDisplay</code> function allows other threads to use the specified display again. Any threads that have blocked on the display are allowed to continue. Nested locking works correctly; if <code>XLockDisplay</code> has been called multiple times by a thread, then <code>XUnlockDisplay</code> must be called an equal number of times before the display is actually unlocked. This function has no effect unless Xlib was successfully initialized for threads using <code>XInitThreads</code>.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
