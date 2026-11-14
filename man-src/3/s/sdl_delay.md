---
title: "sdl_delay(3)"
name: "sdl_delay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_delay/"
description: "SDL_Delay – Wait a specified number of milliseconds before returning."
---

<p>SDL_Delay &#8211; Wait a specified number of milliseconds before returning.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> void SDL_Delay</code>(<code>Uint32 ms</code>);</p>
<h2>Description</h2>
<p> Wait a specified number of milliseconds before returning. <code>SDL_Delay</code> will wait at <i>least</i> the specified time, but possible longer due to OS scheduling. </p>
<dl COMPACT>
<dt>
<dd> <code>Note: </p>
<p> Count on a delay granularity of </code><i>at least</i> 10 ms. Some platforms have shorter clock ticks but this is the most common.</dl>
<h2>See Also</h2>
<p> <i></i><code>SDL_AddTimer</code></p>
