---
title: "sdl_showcursor(3)"
name: "sdl_showcursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_showcursor/"
description: "SDL_ShowCursor – Toggle whether or not the cursor is shown on the screen."
---

<p>SDL_ShowCursor &#8211; Toggle whether or not the cursor is shown on the screen.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_ShowCursor</code>(<code>int toggle</code>);</p>
<h2>Description</h2>
<p>Toggle whether or not the cursor is shown on the screen. Passing <code>SDL_ENABLE</code> displays the cursor and passing <code>SDL_DISABLE</code> hides it. The current state of the mouse cursor can be queried by passing <code>SDL_QUERY</code>, either <code>SDL_DISABLE</code> or <code>SDL_ENABLE</code> will be returned. </p>
<p> The cursor starts off displayed, but can be turned off.</p>
<h2>Return Value</h2>
<p>Returns the current state of the cursor.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateCursor</code>, <i></i><code>SDL_SetCursor</code></p>
