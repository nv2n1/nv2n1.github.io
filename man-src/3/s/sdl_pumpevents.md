---
title: "sdl_pumpevents(3)"
name: "sdl_pumpevents"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_pumpevents/"
description: "SDL_PumpEvents – Pumps the event loop, gathering events from the input devices."
---

<p>SDL_PumpEvents &#8211; Pumps the event loop, gathering events from the input devices.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_PumpEvents</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>Pumps the event loop, gathering events from the input devices. </p>
<p> <code>SDL_PumpEvents</code> gathers all the pending input information from devices and places it on the event queue. Without calls to <code>SDL_PumpEvents</code> no events would ever be placed on the queue. Often calls the need for <code>SDL_PumpEvents</code> is hidden from the user since <i></i><code>SDL_PollEvent</code> and <i></i><code>SDL_WaitEvent</code> implicitly call <code>SDL_PumpEvents</code>. However, if you are not polling or waiting for events (e.g. your filtering them), then you must call <code>SDL_PumpEvents</code> to force an event queue update. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> You can only call this function in the thread that set the video mode.</dl>
<p> </code></p>
<h2>See Also</h2>
<p><i></i><code>SDL_PollEvent</code></p>
