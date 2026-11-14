---
title: "sdl_unlocksurface(3)"
name: "sdl_unlocksurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_unlocksurface/"
description: "SDL_UnlockSurface – Unlocks a previously locked surface."
---

<p>SDL_UnlockSurface &#8211; Unlocks a previously locked surface.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_UnlockSurface</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p>Surfaces that were previously locked using <code>SDL_LockSurface</code> must be unlocked with <code>SDL_UnlockSurface</code>. Surfaces should be unlocked as soon as possible. </p>
<p> It should be noted that since 1.1.8, surface locks are recursive. See <i></i><code>SDL_LockSurface</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_LockSurface</code></p>
