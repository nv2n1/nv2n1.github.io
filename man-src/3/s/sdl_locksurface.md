---
title: "sdl_locksurface(3)"
name: "sdl_locksurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_locksurface/"
description: "SDL_LockSurface – Lock a surface for directly access."
---

<p>SDL_LockSurface &#8211; Lock a surface for directly access.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_LockSurface</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p><code>SDL_LockSurface</code> sets up a surface for directly accessing the pixels. Between calls to <code>SDL_LockSurface</code> and <code>SDL_UnlockSurface</code>, you can write to and read from <code>surface-&gt;pixels</code>, using the pixel format stored in <code>surface-&gt;format</code>. Once you are done accessing the surface, you should use <code>SDL_UnlockSurface</code> to release it. </p>
<p> Not all surfaces require locking. If <code>SDL_MUSTLOCK</code>(<code>surface</code>) evaluates to <code>0</code>, then you can read and write to the surface at any time, and the pixel format of the surface will not change. </p>
<p> No operating system or library calls should be made between lock/unlock pairs, as critical system locks may be held during this time. </p>
<p> It should be noted, that since SDL 1.1.8 surface locks are recursive. This means that you can lock a surface multiple times, but each lock must have a match unlock. </p>
<pre><tt> .
 .
 SDL_LockSurface( surface );
 .
 /* Surface is locked */
 /* Direct pixel access on surface here */
 .
 SDL_LockSurface( surface );
 .
 /* More direct pixel access on surface */
 .
 SDL_UnlockSurface( surface );
 /* Surface is still locked */
 /* Note: Is versions &lt; 1.1.8, the surface would have been */
 /* no longer locked at this stage */
 .
 SDL_UnlockSurface( surface );
 /* Surface is now unlocked */
 .
 .</tt></pre>
<h2>Return Value</h2>
<p><code>SDL_LockSurface</code> returns <code>0</code>, or <code>-1</code> if the surface couldn&#8217;t be locked.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_UnlockSurface</code></p>
