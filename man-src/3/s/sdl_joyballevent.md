---
title: "sdl_joyballevent(3)"
name: "sdl_joyballevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joyballevent/"
description: "SDL_JoyBallEvent – Joystick trackball motion event structure"
---

<p>SDL_JoyBallEvent &#8211; Joystick trackball motion event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 which;
 Uint8 ball;
 Sint16 xrel, yrel;
} SDL_JoyBallEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_JOYBALLMOTION</code></p>
<dt><code>which</code></p>
<dd>Joystick device index</p>
<dt><code>ball</code></p>
<dd>Joystick trackball index</p>
<dt><code>xrel</code>, <code>yrel</code></p>
<dd>The relative motion in the X/Y direction</dl>
<h2>Description</h2>
<p><code>SDL_JoyBallEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_JOYBALLMOTION</code> is reported. </p>
<p> A <code>SDL_JOYBALLMOTION</code> event occurs when a user moves a trackball on the joystick. The field <code>which</code> is the index of the joystick that reported the event and <code>ball</code> is the index of the trackball (for a more detailed explaination see the <i>Joystick section</i>). Trackballs only return relative motion, this is the change in position on the ball since it was last polled (last cycle of the event loop) and it is stored in <code>xrel</code> and <code>yrel</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i>Joystick Functions</i>, <i></i><code>SDL_JoystickEventState</code>, <i></i><code>SDL_JoystickGetBall</code></p>
