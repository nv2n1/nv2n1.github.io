---
title: "sdl_setcursor(3)"
name: "sdl_setcursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setcursor/"
description: "SDL_SetCursor – Set the currently active mouse cursor."
---

<p>SDL_SetCursor &#8211; Set the currently active mouse cursor.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_SetCursor</code>(<code>SDL_Cursor *cursor</code>);</p>
<h2>Description</h2>
<p>Sets the currently active cursor to the specified one. If the cursor is currently visible, the change will be immediately represented on the display.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetCursor</code>, <i></i><code>SDL_CreateCursor</code>, <i></i><code>SDL_ShowCursor</code></p>
