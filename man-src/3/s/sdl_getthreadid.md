---
title: "sdl_getthreadid(3)"
name: "sdl_getthreadid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getthreadid/"
description: "SDL_GetThreadID – Get the SDL thread ID of a SDL_Thread"
---

<p>SDL_GetThreadID &#8211; Get the SDL thread ID of a SDL_Thread</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> Uint32 SDL_GetThreadID</code>(<code>SDL_Thread *thread</code>);</p>
<h2>Description</h2>
<p>Returns the ID of a <code>SDL_Thread</code> created by <i>SDL_CreateThread</i>.</p>
<h2>See Also</h2>
<p><i>SDL_CreateThread</i></p>
