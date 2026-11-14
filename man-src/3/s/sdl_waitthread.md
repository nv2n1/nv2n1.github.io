---
title: "sdl_waitthread(3)"
name: "sdl_waitthread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_waitthread/"
---

SDL_WaitThread - Wait for a thread to finish.
<h2>Synopsis</h2><b>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; 

 void SDL_WaitThread</b>(<b>SDL_Thread *thread, int *status</b>);
<h2>Description</h2>Wait for a thread to finish (timeouts are not supported).
<h2>Return Value</h2>The return code for the thread function is placed in the area pointed to by <b>status</b>, if <b>status</b> is not <b>NULL</b>.
<h2>See Also</h2><i></i><b>SDL_CreateThread</b>
