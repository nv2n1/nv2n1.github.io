---
title: "sdl_wm_seticon(3)"
name: "sdl_wm_seticon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_wm_seticon/"
description: "SDL_WM_SetIcon – Sets the icon for the display window."
---

<p>SDL_WM_SetIcon &#8211; Sets the icon for the display window.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_WM_SetIcon</code>(<code>SDL_Surface *icon, Uint8 *mask</code>);</p>
<h2>Description</h2>
<p>Sets the icon for the display window. Win32 icons must be 32&#215;32. </p>
<p> This function must be called before the first call to <i>SDL_SetVideoMode</i>. </p>
<p> It takes an <code>icon</code> surface, and a <code>mask</code> in MSB format. </p>
<p> If <code>mask</code> is <code>NULL</code>, the entire icon surface will be used as the icon.</p>
<h2>Example</h2>
<pre><tt>SDL_WM_SetIcon(SDL_LoadBMP(&quot;icon.bmp&quot;), NULL);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_WM_SetCaption</code></p>
