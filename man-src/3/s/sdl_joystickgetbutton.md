---
title: "sdl_joystickgetbutton(3)"
name: "sdl_joystickgetbutton"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickgetbutton/"
description: "SDL_JoystickGetButton – Get the current state of a given button on a given joystick"
---

<p>SDL_JoystickGetButton &#8211; Get the current state of a given button on a given joystick</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_JoystickGetButton</code>(<code>SDL_Joystick *joystick, int button</code>);</p>
<h2>Description</h2>
<p>SDL_JoystickGetButton returns the current state of the given <code>button</code> on the given <code>joystick</code>.</p>
<h2>Return Value</h2>
<p><code>1</code> if the button is pressed. Otherwise, <code>0</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickNumButtons</code></p>
