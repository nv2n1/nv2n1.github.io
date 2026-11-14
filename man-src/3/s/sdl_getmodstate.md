---
title: "sdl_getmodstate(3)"
name: "sdl_getmodstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getmodstate/"
description: "SDL_GetModState – Get the state of modifier keys."
---

<p>SDL_GetModState &#8211; Get the state of modifier keys.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDLMod SDL_GetModState</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>Returns the current state of the modifier keys (CTRL, ALT, etc.).</p>
<h2>Return Value</h2>
<p>The return value can be an OR&#8217;d combination of the SDLMod enum. </p>
<dl COMPACT>
<dd><code>SDLMod</code> </p>
<pre><tt>typedef enum {
 KMOD_NONE = 0x0000,
 KMOD_LSHIFT= 0x0001,
 KMOD_RSHIFT= 0x0002,
 KMOD_LCTRL = 0x0040,
 KMOD_RCTRL = 0x0080,
 KMOD_LALT = 0x0100,
 KMOD_RALT = 0x0200,
 KMOD_LMETA = 0x0400,
 KMOD_RMETA = 0x0800,
 KMOD_NUM = 0x1000,
 KMOD_CAPS = 0x2000,
 KMOD_MODE = 0x4000,
} SDLMod;</tt></pre>
</dl>
<p>&nbsp;<wbr>SDL also defines the following symbols for convenience:&nbsp;<wbr> </p>
<dl COMPACT>
<dd>
<pre><tt>#define KMOD_CTRL (KMOD_LCTRL|KMOD_RCTRL)
#define KMOD_SHIFT (KMOD_LSHIFT|KMOD_RSHIFT)
#define KMOD_ALT (KMOD_LALT|KMOD_RALT)
#define KMOD_META (KMOD_LMETA|KMOD_RMETA)</tt></pre>
</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_GetKeyState</code></p>
