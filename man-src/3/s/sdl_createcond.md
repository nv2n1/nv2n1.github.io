---
title: "sdl_createcond(3)"
name: "sdl_createcond"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createcond/"
description: "SDL_CreateCond – Create a condition variable"
---

<p>SDL_CreateCond &#8211; Create a condition variable</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> SDL_cond *SDL_CreateCond</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>Creates a condition variable.</p>
<h2>Examples</h2>
<pre><tt>SDL_cond *cond;
cond=SDL_CreateCond();
.
.
/* Do stuff */
.
.
SDL_DestroyCond(cond);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_DestroyCond</code>, <i></i><code>SDL_CondWait</code>, <i></i><code>SDL_CondSignal</code></p>
