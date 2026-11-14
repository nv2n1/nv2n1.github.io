---
title: "sdl_pollevent(3)"
name: "sdl_pollevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_pollevent/"
description: "SDL_PollEvent – Polls for currently pending events."
---

<p>SDL_PollEvent &#8211; Polls for currently pending events.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_PollEvent</code>(<code>SDL_Event *event</code>);</p>
<h2>Description</h2>
<p>Polls for currently pending events, and returns <code>1</code> if there are any pending events, or <code>0</code> if there are none available. </p>
<p> If <code>event</code> is not <code>NULL</code>, the next event is removed from the queue and stored in that area.</p>
<h2>Examples</h2>
<pre><tt>SDL_Event event; /* Event structure */
.
.
.
/* Check for events */
while(SDL_PollEvent(&amp;event)){ /* Loop until there are no events left on the queue */
 switch(event.type){ /* Process the appropiate event type */
 case SDL_KEYDOWN: /* Handle a KEYDOWN event */ 
 printf(&quot;Oh! Key press
&quot;);
 break;
 case SDL_MOUSEMOTION:
 .
 .
 .
 default: /* Report an unhandled event */
 printf(&quot;I don't know what this event is!
&quot;);
 }
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_WaitEvent</code>, <i></i><code>SDL_PeepEvents</code></p>
