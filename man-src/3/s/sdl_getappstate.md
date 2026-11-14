---
title: "sdl_getappstate(3)"
name: "sdl_getappstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getappstate/"
description: "SDL_GetAppState – Get the state of the application"
---

<p><code>SDL_GetAppState</code> &#8211; Get the state of the application</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_GetAppState</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>This function returns the current state of the application. The value returned is a bitwise combination of:</p>
<dl COMPACT>
<dt><code>SDL_APPMOUSEFOCUS</code></p>
<dd>The application has mouse focus.</p>
<dt><code>SDL_APPINPUTFOCUS</code></p>
<dd>The application has keyboard focus</p>
<dt><code>SDL_APPACTIVE</code></p>
<dd>The application is visible</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_ActiveEvent</code></p>
