---
title: "sdl_joystickopened(3)"
name: "sdl_joystickopened"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickopened/"
description: "SDL_JoystickOpened – Determine if a joystick has been opened"
---

<p>SDL_JoystickOpened &#8211; Determine if a joystick has been opened</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_JoystickOpened</code>(<code>int index</code>);</p>
<h2>Description</h2>
<p>Determines whether a joystick has already been opened within the application. <code>index</code> refers to the N&#8217;th joystick on the system.</p>
<h2>Return Value</h2>
<p>Returns <code>1</code> if the joystick has been opened, or <code>0</code> if it has not.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickOpen</code>, <i></i><code>SDL_JoystickClose</code></p>
