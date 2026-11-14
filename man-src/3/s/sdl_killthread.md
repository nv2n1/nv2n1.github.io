---
title: "sdl_killthread(3)"
name: "sdl_killthread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_killthread/"
description: "SDL_KillThread – Gracelessly terminates the thread."
---

<p>SDL_KillThread &#8211; Gracelessly terminates the thread.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> void SDL_KillThread</code>(<code>SDL_Thread *thread</code>);</p>
<h2>Description</h2>
<p><code>SDL_KillThread</code> gracelessly terminates the thread associated with <code>thread</code>. If possible, you should use some other form of IPC to signal the thread to quit.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateThread</code>, <i></i><code>SDL_WaitThread</code></p>
