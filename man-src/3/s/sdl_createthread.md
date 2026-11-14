---
title: "sdl_createthread(3)"
name: "sdl_createthread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createthread/"
description: "SDL_CreateThread – Creates a new thread of execution that shares its parent’s properties."
---

<p>SDL_CreateThread &#8211; Creates a new thread of execution that shares its parent&#8217;s properties.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> SDL_Thread *SDL_CreateThread</code>(<code>int (*fn)(void *), void *data</code>);</p>
<h2>Description</h2>
<p> <code>SDL_CreateThread</code> creates a new thread of execution that shares all of its parent&#8217;s global memory, signal handlers, file descriptors, etc, and runs the function <code>fn</code> passed the void pointer <code>data</code> The thread quits when this function returns.</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_KillThread</code></p>
