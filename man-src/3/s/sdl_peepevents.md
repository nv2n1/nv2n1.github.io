---
title: "sdl_peepevents(3)"
name: "sdl_peepevents"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_peepevents/"
description: "SDL_PeepEvents – Checks the event queue for messages and optionally returns them."
---

<p>SDL_PeepEvents &#8211; Checks the event queue for messages and optionally returns them.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_PeepEvents</code>(<code>SDL_Event *events, int numevents, SDL_eventaction action, Uint32 mask</code>);</p>
<h2>Description</h2>
<p>Checks the event queue for messages and optionally returns them. </p>
<p> If <code>action</code> is <code>SDL_ADDEVENT</code>, up to <code>numevents</code> events will be added to the back of the event queue. </p>
<p> If <code>action</code> is <code>SDL_PEEKEVENT</code>, up to <code>numevents</code> events at the front of the event queue, matching <i></i><code>mask</code>, will be returned and will not be removed from the queue. </p>
<p> If <code>action</code> is <code>SDL_GETEVENT</code>, up to <code>numevents</code> events at the front of the event queue, matching <i></i><code>mask</code>, will be returned and will be removed from the queue. </p>
<p> This function is thread-safe.</p>
<h2>Return Value</h2>
<p>This function returns the number of events actually stored, or <code>-1</code> if there was an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_PollEvent</code>, <i></i><code>SDL_PushEvent</code></p>
