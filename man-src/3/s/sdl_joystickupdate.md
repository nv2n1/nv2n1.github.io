---
title: "sdl_joystickupdate(3)"
name: "sdl_joystickupdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickupdate/"
description: "SDL_JoystickUpdate – Updates the state of all joysticks"
---

<p>SDL_JoystickUpdate &#8211; Updates the state of all joysticks</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_JoystickUpdate</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>Updates the state(position, buttons, etc.) of all open joysticks. If joystick events have been enabled with <i></i><code>SDL_JoystickEventState</code> then this is called automatically in the event loop.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickEventState</code></p>
