---
title: "sdl_joystickgetaxis(3)"
name: "sdl_joystickgetaxis"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickgetaxis/"
description: "SDL_JoystickGetAxis – Get the current state of an axis"
---

<p>SDL_JoystickGetAxis &#8211; Get the current state of an axis</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Sint16 SDL_JoystickGetAxis</code>(<code>SDL_Joystick *joystick, int axis</code>);</p>
<h2>Description</h2>
<p><code>SDL_JoystickGetAxis</code> returns the current state of the given <code>axis</code> on the given <code>joystick</code>. </p>
<p> On most modern joysticks the X axis is usually represented by <code>axis</code> 0 and the Y axis by <code>axis</code> 1. The value returned by <code>SDL_JoystickGetAxis</code> is a signed integer (-32768 to 32768) representing the current position of the <code>axis</code>, it maybe necessary to impose certain tolerances on these values to account for jitter. It is worth noting that some joysticks use axes 2 and 3 for extra buttons.</p>
<h2>Return Value</h2>
<p>Returns a 16-bit signed integer representing the current position of the <code>axis</code>.</p>
<h2>Examples</h2>
<pre><tt>Sint16 x_move, y_move;
SDL_Joystick *joy1;
.
.
x_move=SDL_JoystickGetAxis(joy1, 0);
y_move=SDL_JoystickGetAxis(joy1, 1);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickNumAxes</code></p>
