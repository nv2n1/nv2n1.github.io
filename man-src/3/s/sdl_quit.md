---
title: "sdl_quit(3)"
name: "sdl_quit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_quit/"
description: "SDL_Quit – Shut down SDL"
---

<p>SDL_Quit &#8211; Shut down SDL</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_Quit</code>(<code>void</code>);</p>
<h2>Description</h2>
<p><code>SDL_Quit</code> shuts down all SDL subsystems and frees the resources allocated to them. This should always be called before you exit. For the sake of simplicity you can set <code>SDL_Quit</code> as your <code>atexit</code> call, like: </p>
<pre><tt>SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO);
atexit(SDL_Quit);
.
.</tt></pre>
<dl COMPACT>
<dd><code>Note: </p>
<p> While using atexit</code> maybe be fine for small programs, more advanced users should shut down SDL in their own cleanup code. Plus, using <code>atexit</code> in a library is a sure way to crash dynamically loaded code</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_QuitSubsystem</code>, <i></i><code>SDL_Init</code></p>
