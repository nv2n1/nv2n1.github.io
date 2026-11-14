---
title: "sdl_pushevent(3)"
name: "sdl_pushevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_pushevent/"
description: "SDL_PushEvent – Pushes an event onto the event queue"
---

<p>SDL_PushEvent &#8211; Pushes an event onto the event queue</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_PushEvent</code>(<code>SDL_Event *event</code>);</p>
<h2>Description</h2>
<p>The event queue can actually be used as a two way communication channel. Not only can events be read from the queue, but the user can also push their own events onto it. <code>event</code> is a pointer to the event structure you wish to push onto the queue. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Pushing device input events onto the queue doesn&#8217;t modify the state of the device within SDL.</dl>
<p> </code></p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on success or <code>-1</code> if the event couldn&#8217;t be pushed.</p>
<h2>Examples</h2>
<p>See <i></i><code>SDL_Event</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_PollEvent</code>, <i></i><code>SDL_PeepEvents</code>, <i></i><code>SDL_Event</code></p>
