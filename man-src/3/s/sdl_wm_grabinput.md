---
title: "sdl_wm_grabinput(3)"
name: "sdl_wm_grabinput"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_wm_grabinput/"
description: "SDL_WM_GrabInput – Grabs mouse and keyboard input."
---

<p>SDL_WM_GrabInput &#8211; Grabs mouse and keyboard input.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_GrabMode SDL_WM_GrabInput</code>(<code>SDL_GrabMode mode</code>);</p>
<h2>Description</h2>
<p>Grabbing means that the mouse is confined to the application window, and nearly all keyboard input is passed directly to the application, and not interpreted by a window manager, if any. </p>
<p> When <code>mode</code> is <code>SDL_GRAB_QUERY</code> the grab mode is not changed, but the current grab mode is returned. </p>
<pre><tt>typedef enum {
 SDL_GRAB_QUERY,
 SDL_GRAB_OFF,
 SDL_GRAB_ON
} SDL_GrabMode;</tt></pre>
<p>&nbsp;<wbr></p>
<h2>Return Value</h2>
<p>The current/new <code>SDL_GrabMode</code>.</p>
