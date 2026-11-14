---
title: "sdl_mutexp(3)"
name: "sdl_mutexp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_mutexp/"
---

SDL_mutexP - Lock a mutex
<h2>Synopsis</h2><b>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; 

 int SDL_mutexP</b>(<b>SDL_mutex *mutex</b>);
<h2>Description</h2>Locks the <b>mutex</b>, which was previously created with <i></i><b>SDL_CreateMutex</b>. If the mutex is already locked then <b>SDL_mutexP</b> will not return until it is <i>unlocked</i>. Returns <b>0</b> on success, or <b>-1</b> on an error. 

 SDL also defines a macro <b>#define SDL_LockMutex(m) SDL_mutexP(m)</b>.
<h2>See Also</h2><i></i><b>SDL_CreateMutex</b>, <i></i><b>SDL_mutexV</b>
