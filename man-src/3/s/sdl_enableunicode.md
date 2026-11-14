---
title: "sdl_enableunicode(3)"
name: "sdl_enableunicode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_enableunicode/"
description: "SDL_EnableUNICODE – Enable UNICODE translation"
---

<p>SDL_EnableUNICODE &#8211; Enable UNICODE translation</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_EnableUNICODE</code>(<code>int enable</code>);</p>
<h2>Description</h2>
<p>Enables/Disables Unicode keyboard translation. </p>
<p> To obtain the character codes corresponding to received keyboard events, Unicode translation must first be turned on using this function. The translation incurs a slight overhead for each keyboard event and is therefore disabled by default. For each subsequently received key down event, the <code>unicode</code> member of the <i></i><code>SDL_keysym</code> structure will then contain the corresponding character code, or zero for keysyms that do not correspond to any character code. </p>
<p> A value of 1 for <code>enable</code> enables Unicode translation; 0 disables it, and -1 leaves it unchanged (useful for querying the current translation mode). </p>
<p> Note that only key press events will be translated, not release events.</p>
<h2>Return Value</h2>
<p>Returns the previous translation mode (<code>0</code> or <code>1</code>).</p>
<h2>See Also</h2>
<p><i></i><code>SDL_keysym</code></p>
