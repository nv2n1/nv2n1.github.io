---
title: "sdl_quitsubsystem(3)"
name: "sdl_quitsubsystem"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_quitsubsystem/"
description: "SDL_QuitSubSystem – Shut down a subsystem"
---

<p>SDL_QuitSubSystem &#8211; Shut down a subsystem</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_QuitSubSystem</code>(<code>Uint32 flags</code>);</p>
<h2>Description</h2>
<p><code>SDL_QuitSubSystem</code> allows you to shut down a subsystem that has been previously initialized by <i></i><code>SDL_Init</code> or <i></i><code>SDL_InitSubSystem</code>. The <code>flags</code> tells <code>SDL_QuitSubSystem</code> which subsystems to shut down, it uses the same values that are passed to <i></i><code>SDL_Init</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Quit</code>, <i></i><code>SDL_Init</code>, <i></i><code>SDL_InitSubSystem</code></p>
