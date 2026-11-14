---
title: "sdl_joystickeventstate(3)"
name: "sdl_joystickeventstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickeventstate/"
description: "SDL_JoystickEventState – Enable/disable joystick event polling"
---

<p>SDL_JoystickEventState &#8211; Enable/disable joystick event polling</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_JoystickEventState</code>(<code>int state</code>);</p>
<h2>Description</h2>
<p>This function is used to enable or disable joystick event processing. With joystick event processing disabled you will have to update joystick states with <i></i><code>SDL_JoystickUpdate</code> and read the joystick information manually. <code>state</code> is either <code>SDL_QUERY</code>, <code>SDL_ENABLE</code> or <code>SDL_IGNORE</code>. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Joystick event handling is prefered</dl>
<p> </code></p>
<h2>Return Value</h2>
<p>If <code>state</code> is <code>SDL_QUERY</code> then the current state is returned, otherwise the new processing <code>state</code> is returned.</p>
<h2>See Also</h2>
<p><i>SDL Joystick Functions</i>, <i></i><code>SDL_JoystickUpdate</code>, <i></i><code>SDL_JoyAxisEvent</code>, <i></i><code>SDL_JoyBallEvent</code>, <i></i><code>SDL_JoyButtonEvent</code>, <i></i><code>SDL_JoyHatEvent</code></p>
