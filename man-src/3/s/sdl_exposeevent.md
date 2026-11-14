---
title: "sdl_exposeevent(3)"
name: "sdl_exposeevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_exposeevent/"
description: "SDL_ExposeEvent – Quit requested event"
---

<p>SDL_ExposeEvent &#8211; Quit requested event</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type
} SDL_ExposeEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_VIDEOEXPOSE</code></dl>
<h2>Description</h2>
<p><code>SDL_ExposeEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used whan an event of type <code>SDL_VIDEOEXPOSE</code> is reported. </p>
<p> A VIDEOEXPOSE event is triggered when the screen has been modified outside of the application, usually by the window manager and needs to be redrawn.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_SetEventFilter</code></p>
