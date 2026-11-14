---
title: "sdl_joyaxisevent(3)"
name: "sdl_joyaxisevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joyaxisevent/"
description: "SDL_JoyAxisEvent – Joystick axis motion event structure"
---

<p>SDL_JoyAxisEvent &#8211; Joystick axis motion event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 which;
 Uint8 axis;
 Sint16 value;
} SDL_JoyAxisEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_JOYAXISMOTION</code></p>
<dt><code>which</code></p>
<dd>Joystick device index</p>
<dt><code>axis</code></p>
<dd>Joystick axis index</p>
<dt><code>value</code></p>
<dd>Axis value (range: -32768 to 32767)</dl>
<h2>Description</h2>
<p><code>SDL_JoyAxisEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_JOYAXISMOTION</code> is reported. </p>
<p> A <code>SDL_JOYAXISMOTION</code> event occurs when ever a user moves an axis on the joystick. The field <code>which</code> is the index of the joystick that reported the event and <code>axis</code> is the index of the axis (for a more detailed explaination see the <i>Joystick section</i>). <code>value</code> is the current position of the axis.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i>Joystick Functions</i>, <i></i><code>SDL_JoystickEventState</code>, <i></i><code>SDL_JoystickGetAxis</code></p>
