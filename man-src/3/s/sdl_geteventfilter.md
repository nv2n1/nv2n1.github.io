---
title: "sdl_geteventfilter(3)"
name: "sdl_geteventfilter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_geteventfilter/"
description: "SDL_GetEventFilter – Retrieves a pointer to he event filter"
---

<p>SDL_GetEventFilter &#8211; Retrieves a pointer to he event filter</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_EventFilter SDL_GetEventFilter</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>This function retrieces a pointer to the event filter that was previously set using <i></i><code>SDL_SetEventFilter</code>. An SDL_EventFilter function is defined as: </p>
<pre><tt>typedef int (*SDL_EventFilter)(const SDL_Event *event);</tt></pre>
<h2>Return Value</h2>
<p>Returns a pointer to the event filter or <code>NULL</code> if no filter has been set.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_SetEventFilter</code></p>
