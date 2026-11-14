---
title: "sdl_joybuttonevent(3)"
name: "sdl_joybuttonevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joybuttonevent/"
description: "SDL_JoyButtonEvent – Joystick button event structure"
---

<p>SDL_JoyButtonEvent &#8211; Joystick button event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 which;
 Uint8 button;
 Uint8 state;
} SDL_JoyButtonEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_JOYBUTTONDOWN</code> or <code>SDL_JOYBUTTONUP</code></p>
<dt><code>which</code></p>
<dd>Joystick device index</p>
<dt><code>button</code></p>
<dd>Joystick button index</p>
<dt><code>state</code></p>
<dd><code>SDL_PRESSED</code> or <code>SDL_RELEASED</code></dl>
<h2>Description</h2>
<p><code>SDL_JoyButtonEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_JOYBUTTONDOWN</code> or <code>SDL_JOYBUTTONUP</code> is reported. </p>
<p> A <code>SDL_JOYBUTTONDOWN</code> or <code>SDL_JOYBUTTONUP</code> event occurs when ever a user presses or releases a button on a joystick. The field <code>which</code> is the index of the joystick that reported the event and <code>button</code> is the index of the button (for a more detailed explaination see the <i>Joystick section</i>). <code>state</code> is the current state or the button which is either <code>SDL_PRESSED</code> or <code>SDL_RELEASED</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i>Joystick Functions</i>, <i></i><code>SDL_JoystickEventState</code>, <i></i><code>SDL_JoystickGetButton</code></p>
