---
title: "sdl_eventstate(3)"
name: "sdl_eventstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_eventstate/"
description: "SDL_EventState – This function allows you to set the state of processing certain events."
---

<p>SDL_EventState &#8211; This function allows you to set the state of processing certain events.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_EventState</code>(<code>Uint8 type, int state</code>);</p>
<h2>Description</h2>
<p>This function allows you to set the state of processing certain event <code>type</code>&#8216;s. </p>
<p> If <code>state</code> is set to <code>SDL_IGNORE</code>, that event <code>type</code> will be automatically dropped from the event queue and will not be filtered. </p>
<p> If <code>state</code> is set to <code>SDL_ENABLE</code>, that event <code>type</code> will be processed normally. </p>
<p> If <code>state</code> is set to <code>SDL_QUERY</code>, <code>SDL_EventState</code> will return the current processing state of the specified event <code>type</code>. </p>
<p> A list of event <code>type</code>&#8216;s can be found in the <i></i><code>SDL_Event</code> section.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code></p>
