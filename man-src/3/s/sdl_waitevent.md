---
title: "sdl_waitevent(3)"
name: "sdl_waitevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_waitevent/"
---

SDL_WaitEvent - Waits indefinitely for the next available event.
<h2>Synopsis</h2><b>#include &quot;SDL.h&quot; 

 int SDL_WaitEvent</b>(<b>SDL_Event *event</b>);
<h2>Description</h2>Waits indefinitely for the next available event, returning <b>1</b>, or <b>0</b> if there was an error while waiting for events. 

 If <b>event</b> is not <b>NULL</b>, the next event is removed from the queue and stored in that area.
<h2>See Also</h2><i></i><b>SDL_Event</b>, <i></i><b>SDL_PollEvent</b>
