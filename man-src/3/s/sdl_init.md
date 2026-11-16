---
title: "sdl_init(3)"
name: "sdl_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_init/"
description: "SDL_Init – Initializes SDL"
---

<p>SDL_Init &#8211; Initializes SDL</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_Init</code>(<code>Uint32 flags</code>);</p>
<h2>Description</h2>
<p>Initializes SDL. This should be called before all other SDL functions. The <code>flags</code> parameter specifies what part(s) of SDL to initialize.</p>
<dl COMPACT>
<dt><code>SDL_INIT_TIMER</code></dt>
<dd>Initializes the <i>timer</i> subsystem.</dd>
<dt><code>SDL_INIT_AUDIO</code></dt>
<dd>Initializes the <i>audio</i> subsystem.</dd>
<dt><code>SDL_INIT_VIDEO</code></dt>
<dd>Initializes the <i>video</i> subsystem.</dd>
<dt><code>SDL_INIT_CDROM</code></dt>
<dd>Initializes the <i>cdrom</i> subsystem.</dd>
<dt><code>SDL_INIT_JOYSTICK</code></dt>
<dd>Initializes the <i>joystick</i> subsystem.</dd>
<dt><code>SDL_INIT_EVERYTHING</code></dt>
<dd>Initialize all of the above.</dd>
<dt><code>SDL_INIT_NOPARACHUTE</code></dt>
<dd>Prevents SDL from catching fatal signals.</dd>
<dt><code>SDL_INIT_EVENTTHREAD</code></dt>
<dd></dd></dl>
<h2>Return Value</h2>
<p>Returns <code>-1</code> on an error or <code>0</code> on success.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Quit</code>, <i></i><code>SDL_InitSubSystem</code></p>
