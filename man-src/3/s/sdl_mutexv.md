---
title: "sdl_mutexv(3)"
name: "sdl_mutexv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_mutexv/"
---

SDL_mutexV - Unlock a mutex
<h2>Synopsis</h2><b>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; 

 int SDL_mutexV</b>(<b>SDL_mutex *mutex</b>);
<h2>Description</h2>Unlocks the <b>mutex</b>, which was previously created with <i></i><b>SDL_CreateMutex</b>. Returns <b>0</b> on success, or <b>-1</b> on an error. 

 SDL also defines a macro <b>#define SDL_UnlockMutex(m) SDL_mutexV(m)</b>.
<h2>See Also</h2><i></i><b>SDL_CreateMutex</b>, <i></i><b>SDL_mutexP</b>
