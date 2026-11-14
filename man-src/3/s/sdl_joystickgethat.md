---
title: "sdl_joystickgethat(3)"
name: "sdl_joystickgethat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickgethat/"
description: "SDL_JoystickGetHat – Get the current state of a joystick hat"
---

<p>SDL_JoystickGetHat &#8211; Get the current state of a joystick hat</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_JoystickGetHat</code>(<code>SDL_Joystick *joystick, int hat</code>);</p>
<h2>Description</h2>
<p>SDL_JoystickGetHat returns the current state of the given <code>hat</code> on the given <code>joystick</code>.</p>
<h2>Return Value</h2>
<p>The current state is returned as a Uint8 which is defined as an OR&#8217;d combination of one or more of the following</p>
<dl COMPACT>
<dd><code>SDL_HAT_CENTERED</code></p>
<dd><code>SDL_HAT_UP</code></p>
<dd><code>SDL_HAT_RIGHT</code></p>
<dd><code>SDL_HAT_DOWN</code></p>
<dd><code>SDL_HAT_LEFT</code></p>
<dd><code>SDL_HAT_RIGHTUP</code></p>
<dd><code>SDL_HAT_RIGHTDOWN</code></p>
<dd><code>SDL_HAT_LEFTUP</code></p>
<dd><code>SDL_HAT_LEFTDOWN</code></dl>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickNumHats</code></p>
