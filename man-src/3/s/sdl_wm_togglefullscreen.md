---
title: "sdl_wm_togglefullscreen(3)"
name: "sdl_wm_togglefullscreen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_wm_togglefullscreen/"
description: "SDL_WM_ToggleFullScreen – Toggles fullscreen mode"
---

<p>SDL_WM_ToggleFullScreen &#8211; Toggles fullscreen mode</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_WM_ToggleFullScreen</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p>Toggles the application between windowed and fullscreen mode, if supported. (X11 is the only target currently supported, BeOS support is experimental).</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on failure or <code>1</code> on success.</p>
