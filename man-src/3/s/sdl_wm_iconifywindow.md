---
title: "sdl_wm_iconifywindow(3)"
name: "sdl_wm_iconifywindow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_wm_iconifywindow/"
description: "SDL_WM_IconifyWindow – Iconify/Minimise the window"
---

<p>SDL_WM_IconifyWindow &#8211; Iconify/Minimise the window</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_WM_IconifyWindow</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>If the application is running in a window managed environment SDL attempts to iconify/minimise it. If <code>SDL_WM_IconifyWindow</code> is successful, the application will receive a <i></i><code>SDL_APPACTIVE</code> loss event.</p>
<h2>Return Value</h2>
<p>Returns non-zero on success or <code>0</code> if iconification is not support or was refused by the window manager.</p>
